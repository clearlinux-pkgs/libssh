#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7EE0FC4DCC014E3D (asn@samba.org)
#
Name     : libssh
Version  : 0.9.5
Release  : 22
URL      : https://www.libssh.org/files/0.9/libssh-0.9.5.tar.xz
Source0  : https://www.libssh.org/files/0.9/libssh-0.9.5.tar.xz
Source1  : https://www.libssh.org/files/0.9/libssh-0.9.5.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1 MIT
Requires: libssh-lib = %{version}-%{release}
Requires: libssh-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : krb5-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : python3
BuildRequires : zlib-dev

%description
_   _   _                          _
(_) (_) (_)                        (_)
(_)  _  (_) _         _  _   _  _  (_) _
(_) (_) (_)(_) _     (_)(_) (_)(_) (_)(_) _
(_) (_) (_)   (_)  _ (_)  _ (_)    (_)   (_)
(_) (_) (_)(_)(_) (_)(_) (_)(_)    (_)   (_).org

%package dev
Summary: dev components for the libssh package.
Group: Development
Requires: libssh-lib = %{version}-%{release}
Provides: libssh-devel = %{version}-%{release}
Requires: libssh = %{version}-%{release}

%description dev
dev components for the libssh package.


%package lib
Summary: lib components for the libssh package.
Group: Libraries
Requires: libssh-license = %{version}-%{release}

%description lib
lib components for the libssh package.


%package license
Summary: license components for the libssh package.
Group: Default

%description license
license components for the libssh package.


%prep
%setup -q -n libssh-0.9.5
cd %{_builddir}/libssh-0.9.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601053480
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1601053480
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libssh
cp %{_builddir}/libssh-0.9.5/COPYING %{buildroot}/usr/share/package-licenses/libssh/daf9314932a8dd8b2617371575b6ad49aa51e813
cp %{_builddir}/libssh-0.9.5/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libssh/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/libssh-0.9.5/doc/that_style/LICENSE %{buildroot}/usr/share/package-licenses/libssh/86b52f0f7e15225010495c0b221b79ef0dc1a90d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libssh/callbacks.h
/usr/include/libssh/legacy.h
/usr/include/libssh/libssh.h
/usr/include/libssh/libssh_version.h
/usr/include/libssh/libsshpp.hpp
/usr/include/libssh/server.h
/usr/include/libssh/sftp.h
/usr/include/libssh/ssh2.h
/usr/lib64/cmake/libssh/libssh-config-relwithdebinfo.cmake
/usr/lib64/cmake/libssh/libssh-config-version.cmake
/usr/lib64/cmake/libssh/libssh-config.cmake
/usr/lib64/libssh.so
/usr/lib64/pkgconfig/libssh.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libssh.so.4
/usr/lib64/libssh.so.4.8.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libssh/86b52f0f7e15225010495c0b221b79ef0dc1a90d
/usr/share/package-licenses/libssh/daf9314932a8dd8b2617371575b6ad49aa51e813
/usr/share/package-licenses/libssh/ff3ed70db4739b3c6747c7f624fe2bad70802987
