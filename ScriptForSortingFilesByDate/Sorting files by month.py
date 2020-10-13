import os
import time
import shutil
import zipfile


def unzip_file():
    """if the file is archived"""
    zip_file_name = 'file.zip'
    if zipfile.is_zipfile(zip_file_name):
        z_file = zipfile.ZipFile(zip_file_name, mode='r')
        for filename in z_file.namelist():
            if not z_file.extract(filename):
                z_file.extract(filename)
        z_file.close()


def sort_files():
    """
    In order to sort the files by year just change

    date_last_modified[1] to date_last_modified[0]

    or sort the files by day

    date_last_modified[1] to date_last_modified[3]

    """

    path = 'C:/.../.../.../...'
    norm_path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(norm_path):
        for files in filenames:
            super_path = os.path.join(dirpath, files)
            time_last_modified = os.path.getmtime(super_path)
            date_last_modified = time.gmtime(time_last_modified)
            if not os.path.exists('sorted files'):
                os.mkdir('sorted files')
            for i in range(1, 12 + 1):
                if date_last_modified[1] == i:
                    if not os.path.exists(f'sorted files/files created {i} months ago'):
                        os.mkdir(f'sorted files/files created {i} months ago')
                    shutil.copy(super_path, f'sorted files/files created {i} months ago')


unzip_file()
sort_files()
