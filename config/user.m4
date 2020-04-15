dnl #
dnl # Default ZFS user configuration
dnl #
AC_DEFUN([ZFS_AC_CONFIG_USER], [
	ZFS_AC_CONFIG_USER_GETTEXT
	ZFS_AC_CONFIG_USER_MOUNT_HELPER
	ZFS_AC_CONFIG_USER_SYSVINIT
	ZFS_AC_CONFIG_USER_DRACUT
	AM_COND_IF([BUILD_FREEBSD], [
		PKG_INSTALLDIR(['${prefix}/libdata/pkgconfig'])], [
		PKG_INSTALLDIR
	])
	ZFS_AC_CONFIG_USER_ZLIB
	AM_COND_IF([BUILD_LINUX], [
		ZFS_AC_CONFIG_USER_UDEV
		ZFS_AC_CONFIG_USER_SYSTEMD
		ZFS_AC_CONFIG_USER_LIBUDEV
		ZFS_AC_CONFIG_USER_LIBUUID
		ZFS_AC_CONFIG_USER_LIBBLKID
		ZFS_AC_CONFIG_USER_PAM
	])
	ZFS_AC_CONFIG_USER_LIBTIRPC
	ZFS_AC_CONFIG_USER_LIBCRYPTO
	ZFS_AC_CONFIG_USER_LIBAIO
	ZFS_AC_CONFIG_USER_LIBATOMIC
	ZFS_AC_CONFIG_USER_LIBFETCH
	ZFS_AC_CONFIG_USER_AIO_H
	AM_COND_IF([BUILD_MACOS], [
		ZFS_AC_MACOS_IMPURE_ENABLE], [
		ZFS_AC_CONFIG_USER_CLOCK_GETTIME
	])
	ZFS_AC_CONFIG_USER_RUNSTATEDIR
	ZFS_AC_CONFIG_USER_MAKEDEV_IN_SYSMACROS
	ZFS_AC_CONFIG_USER_MAKEDEV_IN_MKDEV
	ZFS_AC_CONFIG_USER_ZFSEXEC

	AC_CHECK_FUNCS([issetugid mlockall strlcat strlcpy])

	AC_SUBST(RM)
])
