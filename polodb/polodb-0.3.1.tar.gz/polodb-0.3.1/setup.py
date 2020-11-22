
import tempfile
import os
import urllib.request
import hashlib
from os import path
from distutils.core import setup, Extension

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
BUF_SIZE = 65536
LIB_VERSION = '0.3.1'

def get_download_url():
       return 'https://www.polodb.org/resources/' + LIB_VERSION + '/lib/darwin/x64/libpolodb_clib.a'

def gen_checksum_for(path):
       h = hashlib.sha256()
       with open(path, 'rb') as f:
              while True:
                     data = f.read(BUF_SIZE)
                     if not data:
                            break
                     h.update(data)

       return h.hexdigest()


def get_checksum_url(download_url):
       return download_url + '.SHA256'

def download_file(url, path):
       print('download file path: ' + url)
       headers = {'User-Agent':user_agent,} 
       request = urllib.request.Request(url, None, headers) #The assembled request
       g = urllib.request.urlopen(request)
       with open(path, 'b+w') as f:
              f.write(g.read())

def get_text_from_url(url):
       headers = {'User-Agent':user_agent,} 
       request = urllib.request.Request(url, None, headers) #The assembled request
       g = urllib.request.urlopen(request)
       with urllib.request.urlopen(request) as g:
              return g.read().decode('utf-8')

def download_lib():
       temp_root = tempfile.gettempdir()
       lib_root = path.join(temp_root, "polodb_lib", LIB_VERSION)
       os.makedirs(lib_root, exist_ok=True)
       file_path = path.join(lib_root, 'libpolodb_clib.a')

       lib_url = get_download_url()
       sha256_url = get_checksum_url(lib_url)

       if not path.exists(file_path):
              print('download lib to: ' + file_path)
              download_file(lib_url, file_path)

       remote_checksum_text = get_text_from_url(sha256_url)

       local_checksum_text = gen_checksum_for(file_path)
       return file_path

lib_path = download_lib()

module1 = Extension('polodb',
                    sources = ['polodb_ext.c'],
                    extra_objects=[lib_path])

setup (name = 'polodb',
       version = '0.3.1',
       description = 'PoloDB for Python',
       author = 'Vincent Chan',
       author_email = 'okcdz@diverse.space',
       license = 'MIT',
       ext_modules = [module1])
