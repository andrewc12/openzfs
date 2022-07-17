
use_clang()

um_add_executable(get_diff
	 get_diff.c
)
target_link_libraries(get_diff PRIVATE
	libspl
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS get_diff RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:get_diff>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
