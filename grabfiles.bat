mkdir zfsout

copy out\build\x64-Debug\module\os\windows\driver\* zfsout

copy out\build\x64-Debug\cmd\os\windows\kstat\kstat.exe zfsout\kstat.exe
copy out\build\x64-Debug\cmd\os\windows\zfsinstaller\zfsinstaller.exe zfsout\zfsinstaller.exe
copy out\build\x64-Debug\cmd\zdb\zdb.exe zfsout\zdb.exe
copy out\build\x64-Debug\cmd\zfs\zfs.exe zfsout\zfs.exe
copy out\build\x64-Debug\cmd\zpool\zpool.exe zfsout\zpool.exe
copy out\build\x64-Debug\cmd\zstream\zstreamdump.exe zfsout\zstreamdump.exe




