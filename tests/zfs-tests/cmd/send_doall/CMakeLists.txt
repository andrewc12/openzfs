
use_clang()

um_add_executable(send_doall
	 send_doall.c
	 err.c
	 err.h
)
target_link_libraries(send_doall PRIVATE
	libnvpair
	libuutil
	libzfs
	libzfs_core
	libzpool
)
install(TARGETS send_doall RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:send_doall>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
