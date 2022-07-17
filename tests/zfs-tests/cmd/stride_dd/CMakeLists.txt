
use_clang()

um_add_executable(stride_dd
	 stride_dd.c
)
target_link_libraries(stride_dd PRIVATE
	libspl
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS stride_dd RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:stride_dd>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
