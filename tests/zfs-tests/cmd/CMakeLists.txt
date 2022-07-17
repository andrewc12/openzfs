
include_directories(PRIVATE "${CMAKE_SOURCE_DIR}/lib/libspl/include/os/windows/" "${CMAKE_SOURCE_DIR}/lib/libspl/include" "${CMAKE_SOURCE_DIR}/include"
	"${CMAKE_SOURCE_DIR}/lib/os/windows/libpthread" "${OPENSSL_INCLUDE_DIR}")

add_definitions(-D_CRT_SECURE_NO_WARNINGS)

add_subdirectory(badsend)
add_subdirectory(btree_test)
add_subdirectory(file_check)
#[[add_subdirectory(file_trunc)]]
#[[add_subdirectory(file_write)
C:\Users\andre\Documents\GitHub\openzfs\out\build\x64-Debug\file_write.c.obj : error LNK2019: unresolved external symbol lseek64 referenced in function main]]
add_subdirectory(get_diff)
#[[add_subdirectory(largest_file)
C:\Users\andre\Documents\GitHub\openzfs\tests\zfs-tests\cmd\largest_file\largest_file.c(77,16): error : use of undeclared identifier 'SIGXFSZ']]
#[[add_subdirectory(mkbusy)]]
#[[add_subdirectory(mkfile)]]
add_subdirectory(send_doall)
add_subdirectory(stride_dd)
#[[add_subdirectory(rename_dir)]]
#[[add_subdirectory(rm_lnkcnt_zero_file)]]
add_subdirectory(threadsappend)
#[[add_subdirectory(user_ns_exec)]]
#[[add_subdirectory(xattrtest)]]
#[[add_subdirectory(mmap_exec)]]
#[[add_subdirectory(mmap_libaio)]]
#[[add_subdirectory(mmap_seek)]]
#[[add_subdirectory(mmapwrite)]]
add_subdirectory(nvlist_to_lua)
#[[add_subdirectory(randfree_file)]]
#[[add_subdirectory(randwritecomp)]]
#[[add_subdirectory(readmmap)]]
