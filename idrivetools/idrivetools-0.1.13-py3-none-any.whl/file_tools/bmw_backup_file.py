from .bmw_file import BMWFile


class BMWBackupFile(BMWFile):
    def __init__(self, filename):
        """
        Handle the BMW backup file
        """
        super().__init__(filename)

    def save(self, destination, encrypt=True):
        """
        Create a copy of the file if we're decrypting
        Otherwise, calculate all the values
        """
        with open(self._filename, "rb") as source_file:
            with open(destination, "wb") as destination_file:
                destination_file.write(source_file.read())
