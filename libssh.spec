#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x7EE0FC4DCC014E3D (asn@samba.org)
#
Name     : libssh
Version  : 0.10.5
Release  : 34
URL      : https://www.libssh.org/files/0.10/libssh-0.10.5.tar.xz
Source0  : https://www.libssh.org/files/0.10/libssh-0.10.5.tar.xz
Source1  : https://www.libssh.org/files/0.10/libssh-0.10.5.tar.xz.asc
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n libssh-0.10.5
cd %{_builddir}/libssh-0.10.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685636420
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685636420
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libssh
cp %{_builddir}/libssh-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libssh/daf9314932a8dd8b2617371575b6ad49aa51e813 || :
cp %{_builddir}/libssh-%{version}/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libssh/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/libssh-%{version}/doc/that_style/LICENSE %{buildroot}/usr/share/package-licenses/libssh/86b52f0f7e15225010495c0b221b79ef0dc1a90d || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/libssh.so.4.9.5
/usr/lib64/libssh.so.4
/usr/lib64/libssh.so.4.9.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libssh/86b52f0f7e15225010495c0b221b79ef0dc1a90d
/usr/share/package-licenses/libssh/daf9314932a8dd8b2617371575b6ad49aa51e813
/usr/share/package-licenses/libssh/ff3ed70db4739b3c6747c7f624fe2bad70802987
