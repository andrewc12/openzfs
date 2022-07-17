
use_clang()

um_add_executable(file_check
	 file_check.c
)
target_link_libraries(file_check PRIVATE
	libspl
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS file_check RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:file_check>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
