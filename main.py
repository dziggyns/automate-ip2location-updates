import wget
import os
import zipfile
import glob
import shutil

url = 'https://www.ip2location.com/download?token=[TOKEN]'
ROOT_DIR = os.path.abspath(os.curdir)


def update_ip4():
    url_4 = url+'&file=DB1BIN'
    wget.download(url_4, ROOT_DIR)
    zip_4 = zipfile.ZipFile('DB1-IP-COUNTRY.BIN.ZIP')
    zip_4_info = zip_4.infolist()
    for zipinfo in zip_4_info:
        if zipinfo.filename == 'IP-COUNTRY.BIN':
            zipinfo.filename = rename_zip_4(zipinfo.filename)
            zip_4.extract(zipinfo)


def update_ip6():
    url_6 = url+'&file=DB1BINIPV6'
    wget.download(url_6, ROOT_DIR)
    zip_6 = zipfile.ZipFile('DB1-IPV6-COUNTRY.BIN.ZIP')
    zip_6_info = zip_6.infolist()
    for zipinfo in zip_6_info:
        if zipinfo.filename == 'IPV6-COUNTRY.BIN':
            zipinfo.filename = rename_zip_6(zipinfo.filename)
            zip_6.extract(zipinfo)


def rename_zip_4(file):
    return 'countries.bin'


def rename_zip_6(file):
    return 'countries6.bin'


def cleanup():
    files = glob.glob('./*.ZIP')
    for f in files:
        try:
            os.remove(f)
        finally:
            pass


def movefilesup():
    filePath = os.getcwd()
    file_1 = os.path.join(filePath, 'countries.bin')
    file_2 = os.path.join(filePath, 'countries6.bin')
    os.chdir("..")
    folderPath = os.getcwd()
    shutil.copy(file_1, folderPath)
    shutil.copy(file_2, folderPath)


def main():
    update_ip4()
    update_ip6()
    cleanup()
    movefilesup()


if __name__ == '__main__':
    main()
