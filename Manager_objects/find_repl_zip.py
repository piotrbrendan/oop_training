import sys
import shutil
import zipfile
from pathlib import Path


class ZipReplace:

    def __init__(self,filename, search_str, replace_str):
        self.filename = filename
        self.search_str = search_str
        self.replace_str = replace_str
        self.temp_directory = Path(f"unzipped-{filename}")

    def zip_find_replace(self):
        '''main method to perform whole process of unzipping, replacing and zipping back'''
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):

        self.temp_directory.mkdir()

        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(self.temp_directory)

    def find_replace(self):

        for filename in self.temp_directory.iterdir():
            with open(filename) as file:
                text = file.read()
            text = text.replace(self.search_str, self.replace_str)

    def zip_files(self):

        with zipfile.ZipFile(self.filename,'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)

        shutil.rmtree(self.temp_directory)


    if __name__ == 'main':
        #sys.argv unpacking is necessary
        ZipReplace(*sys.argv[1:4]).zip_find_replace()
