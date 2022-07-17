
use_clang()

um_add_executable(draid
	 draid.c
)
target_link_libraries(draid PRIVATE
	libspl
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS draid RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:draid>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
