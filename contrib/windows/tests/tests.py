import os
import argparse

import subprocess

from pathlib import Path, PurePosixPath, PureWindowsPath, WindowsPath


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

def delete_file(name):
    if os.path.exists(name):
        os.remove(name)
    else:
        print("The file does not exist")


def get_driveletters():
    magic_number_process = subprocess.run(
        ["C:\\Program Files\\OpenZFS On Windows\\zfs.exe", "mount"],
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
        ["C:\\Program Files\\OpenZFS On Windows\\zpool.exe", "create", "-f", name, file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )



def destroy_pool(name):
    magic_number_process = subprocess.run(
        ["C:\\Program Files\\OpenZFS On Windows\\zpool.exe", "destroy", "-f", name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def zpool(*args):
    magic_number_process = subprocess.run(
        ["C:\\Program Files\\OpenZFS On Windows\\zpool.exe", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return magic_number_process


def zfs(*args):
    magic_number_process = subprocess.run(
        ["C:\\Program Files\\OpenZFS On Windows\\zfs.exe", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return magic_number_process


def run(args):
    d = {"zfs": "C:\\Program Files\\OpenZFS On Windows\\zfs.exe", "zpool": "C:\\Program Files\\OpenZFS On Windows\\zpool.exe"}
    l = list(args)
    cmd = d[l[0]]
    result = subprocess.run(
        [cmd, *l[1:]],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return result



def tounc(name):
    q = "\\\\?\\" + str(name)
    return q


def main():
    parsed_args = parse_arguments()

    print("Path:", parsed_args.path)

    p = PureWindowsPath(parsed_args.path)

    print("Path object:", p)

    print("Physical devices", get_DeviceId())

    if p.is_absolute():

        f1 = PureWindowsPath(p, "test01.dat")
        allocate_file(f1, 1024*1024*1024)
        f2 = PureWindowsPath(p, "test02.dat")
        allocate_file(f2, 1024*1024*1024)
        f3 = PureWindowsPath(p, "test03.dat")
        allocate_file(f3, 1024*1024*1024)




        print("=" * 20)


        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test01", tounc(f1)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test01"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)




        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test02", tounc(f1), tounc(f2)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test02"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)






        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test03", tounc(f1), tounc(f2), tounc(f3)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test03"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)




        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test04", "mirror", tounc(f1), tounc(f2)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test04"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)






        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test05", "mirror", tounc(f1), tounc(f2), tounc(f3)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test05"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)







        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test06", "raidz", tounc(f1), tounc(f2), tounc(f3)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test06"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)








        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "test07", "raidz1", tounc(f1), tounc(f2), tounc(f3)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())
        print( run(["zpool", "destroy", "-f", "test07"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)














        print("snapshot no hang:")


        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "testsn01", tounc(f1)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())

        f = PureWindowsPath(get_driveletters()[0][1], "test01.file")
        allocate_file(f, 1024)

        cmd = ["zfs", "snapshot", "testsn01@friday"]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")


        f = PureWindowsPath(get_driveletters()[0][1], "test02.file")
        allocate_file(f, 1024)

        print( run(["zpool", "export", "-a"]) )

        print( run(["zpool", "destroy", "-f", "testsn01"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)







        print("snapshot hang:")


        print("Drive letters before pool create:", get_driveletters())
        cmd = ["zpool", "create", "-f", "testsn02", tounc(f1)]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")
        print("Drive letters after pool create:", get_driveletters())

        f = PureWindowsPath(get_driveletters()[0][1], "test01.file")
        allocate_file(f, 1024)

        cmd = ["zfs", "snapshot", "testsn02@friday"]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")


        f = PureWindowsPath(get_driveletters()[0][1], "test02.file")
        allocate_file(f, 1024)

        cmd = ["zfs", "mount", "testsn02@friday"]
        print(" ".join(cmd))
        ret = run(cmd)
        print(ret)
        if ret.returncode != 0:
            print("FAIL")


        print( run(["zpool", "export", "-a"]) )

        print( run(["zpool", "destroy", "-f", "testsn02"]) )
        print("Drive letters after pool destroy:", get_driveletters())
        print("=" * 20)











        delete_file(f1)
        delete_file(f2)
        delete_file(f3)




















if __name__ == "__main__":
    main()





