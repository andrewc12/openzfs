
use_clang()

add_compile_options(/FI ${CMAKE_SOURCE_DIR}/include/libzfs.h)

um_add_executable(btree_test
	 btree_test.c

)
target_link_libraries(btree_test PRIVATE
	libspl
	libzfs
	libzpool
)
install(TARGETS btree_test RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")
install(FILES $<TARGET_PDB_FILE:btree_test>
	DESTINATION "${CMAKE_INSTALL_BINDIR}"
	OPTIONAL
)
