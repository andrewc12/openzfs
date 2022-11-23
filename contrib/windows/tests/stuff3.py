import os
import argparse

import subprocess

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-path', type=dir_path, required=True)
    return parser.parse_args()
def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")



def get_DeviceId():
    magic_number_process = subprocess.run(
        ["wmic", "diskdrive", "get", "DeviceId"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    #https://github.com/sir-ragna/dddddd
    #get DeviceId

    a=magic_number_process.stdout.decode(encoding='UTF-8',errors='strict').replace("\r\r\n", "\r\n")

    c = a.splitlines()

    d = [x.split() for x in c]

    e = [x[0] for x in d if len(x) > 0 and x[0] not in "DeviceID"]

    e.sort()

    #print(e)

    #print([x.encode(encoding='UTF-8') for x in e])

    #import csv

    #with open('csv_file.csv', 'w', encoding='UTF8') as f:
    #    writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_ALL)
    #
    #    for row in e:
    #        writer.writerow([row])

    return e

def allocate_file(name, size):
    with open(name, 'wb') as f:
        f.seek(size)
        f.write(b'0')

def get_driveletters():
    magic_number_process = subprocess.run(
        ["zfs.exe", "mount"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    #b'test01                          H:\\ \r\ntest02                          I:\\ \r\n'


    a=magic_number_process.stdout.decode(encoding='UTF-8',errors='strict')

    c = a.splitlines()

    d = [x.split() for x in c]

    return d

#      run: '& "C:\Program Files\OpenZFS On Windows\zfs.exe" mount'



def create_pool(name, file):
    magic_number_process = subprocess.run(
        ["zpool.exe", "create", "-f", name, file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )



def destroy_pool(name):
    magic_number_process = subprocess.run(
        ["zpool.exe", "destroy", "-f", name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def main():
    parsed_args = parse_arguments()

    print(get_DeviceId())

    print(get_driveletters())

    #allocate_file('C:/Users/andre/b.img', 1024*1024*1024)

    #create_pool("testb", "\\\\?\\C:\\Users\\andre\\b.img")

    #print(get_driveletters())

    #destroy_pool("testb")

    #print(get_driveletters())



    
if __name__ == "__main__":
    main()





