
use_clang()

um_add_executable(nvlist_to_lua
	 nvlist_to_lua.c
)
target_link_libraries(nvlist_to_lua PRIVATE
	libspl
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS nvlist_to_lua RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:nvlist_to_lua>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
