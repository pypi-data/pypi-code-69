import inspect
import hashlib
import zlib

import six
import os

from rook.services.bdb_location_service import BdbLocationService
from rook.services.import_service import ImportService

from rook.exceptions import RookHashMismatchException, \
    RookCrcMismatchException, RookLineMoved

from rook.logger import logger
from rook.processor.error import Error
from rook.file_utils import FileUtils

class LocationFileLine(object):

    NAME = 'file_line'

    def __init__(self, arguments, processor_factory=None):
        self.filename = arguments.get('filename')
        # If we have a filename, make sure pyc is removed
        if self.filename:
            if isinstance(self.filename, six.string_types):
                # Some BDBs identify files by ID
                self.filename = self.filename.replace('.pyc', '.py')

        if self.filename is None:
            self.module_name = arguments['module_name'].lower()
        else:
            self.module_name = None

        self.lineno = arguments['lineno']

        self.file_hash = arguments.get('sha256')
        self.line_crc32 = arguments.get('line_crc32_2')
        self.line_unique = arguments.get('line_unique', False)

        self.file_utils = FileUtils()

        self.include_externals = arguments.get('includeExternals')
        if self.include_externals is None:
            # The only case it will be equal to '' is when its only filename (without folder, and without '/')
            if self.filename and isinstance(self.filename, six.string_types) and os.path.dirname(self.filename) == '':
                self.include_externals = False
            else:
                self.include_externals = True

    def add_aug(self, trigger_services, output, aug):
        logger.info("Adding aug")

        def callback(module):
            try:
                updatedLineNo = self._get_updated_line_number(aug, module)

                filepath = inspect.getsourcefile(module)
                if not filepath:
                    if module.__file__.endswith('.pyc'):
                        filepath = module.__file__.replace('.pyc', '.py')

                trigger_services.get_service(BdbLocationService.NAME).add_breakpoint_aug(module, updatedLineNo,
                                                                                         filepath, aug)
            except Exception as exc:
                message = "Exception when adding aug"
                logger.exception(message)
                aug.set_error(Error(exc=exc, message=message))

        def removed():
            aug.set_removed()

        aug.set_pending()
        trigger_services.get_service(ImportService.NAME).register_post_import_notification(
            aug, self.module_name, self.filename, self.file_hash, self.include_externals, self.lineno, callback, removed)

    def _get_updated_line_number(self, aug, module):
        filepath = inspect.getsourcefile(module)
        file_contents = self.file_utils.get_file_contents(aug, module, filepath)
        if file_contents is None:
            return self.lineno

        if self.line_crc32 is not None:
            return self._find_line_using_crc(aug, filepath, file_contents)

        if self.file_hash:
            self._verify_file_hash(filepath, file_contents)
            return self.lineno

        return self.lineno

    def _find_line_using_crc(self, aug, filepath, file_contents):
        lines = file_contents.splitlines()

        line_crc32 = None
        if len(lines) >= self.lineno:
            line_crc32 = format(zlib.crc32(lines[self.lineno - 1]) & 0xffffffff, 'x')
        if line_crc32 == self.line_crc32:
            return self.lineno

        if self.line_unique:
            crc32s = [format(zlib.crc32(line) & 0xffffffff, 'x') for line in lines]
            firstIndex = None
            secondFound = False

            for i in range(len(crc32s)):
                if crc32s[i] == self.line_crc32:
                    if firstIndex is None:
                        firstIndex = i
                    else:
                        secondFound = True
                        break

            if firstIndex and not secondFound:
                updatedLine = firstIndex + 1
                aug.send_warning(Error(exc=RookLineMoved(filepath, self.lineno, updatedLine)))
                return updatedLine

        blob_hash = self._get_git_blob_hash(filepath)
        raise RookCrcMismatchException(filepath, self.line_crc32, line_crc32, blob_hash)

    def _verify_file_hash(self, filepath, file_contents):
        hash = hashlib.sha256(file_contents).hexdigest()
        if hash != self.file_hash:
            blob_hash = self._get_git_blob_hash(filepath)
            raise RookHashMismatchException(filepath, self.file_hash, hash, blob_hash)

    def _get_git_blob_hash(self, file_path):
        return None
