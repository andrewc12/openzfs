
use_clang()

um_add_executable(badsend
	 badsend.c
)
target_link_libraries(badsend PRIVATE
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS badsend RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:badsend>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
