
use_clang()

um_add_executable(threadsappend
	 threadsappend.c
)
target_link_libraries(threadsappend PRIVATE
	libspl
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS threadsappend RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:threadsappend>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
