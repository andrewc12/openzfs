
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

add_subdirectory(stride_dd)
