__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# Imported modules;
from zipfile import ZipFile
import os
from pathlib import Path
import shutil
import glob


def clean_cache():
    dir = "files\\cache"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(os.path.join("files", "cache"))


def cache_zip(x, y):
    with ZipFile(x, "r") as zip:
        zip.extractall(y)


def cached_files():
    ab_path = []
    file_list = glob.glob(r"C:\Users\julia\Winc_oktober\files\cache\*.txt")
    for x in file_list:
        ab_path.append(os.path.abspath(x))
    return(ab_path)

# isolleer wachtwoord met .split() of .strip()


def find_password(cached_files_function):
    keyword = "password:"
    for x in cached_files_function:
        f = open(x)
        for zin in f:
            if keyword in zin:
                return zin.replace(keyword, " ").strip()


if __name__ == "__main__":
    clean_cache()
    cache_zip(r"files\data.zip", r"C:\Users\julia\Winc_oktober\files\cache")
    cached_files()
    print(find_password(cached_files()))
