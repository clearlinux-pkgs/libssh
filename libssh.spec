#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7EE0FC4DCC014E3D (asn@samba.org)
#
Name     : libssh
Version  : 0.8.5
Release  : 8
URL      : https://www.libssh.org/files/0.8/libssh-0.8.5.tar.xz
Source0  : https://www.libssh.org/files/0.8/libssh-0.8.5.tar.xz
Source99 : https://www.libssh.org/files/0.8/libssh-0.8.5.tar.xz.asc
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
%setup -q -n libssh-0.8.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541000680
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541000680
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libssh
cp COPYING %{buildroot}/usr/share/package-licenses/libssh/COPYING
cp cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libssh/cmake_Modules_COPYING-CMAKE-SCRIPTS
cp doc/that_style/LICENSE %{buildroot}/usr/share/package-licenses/libssh/doc_that_style_LICENSE
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
/usr/include/libssh/libsshpp.hpp
/usr/include/libssh/server.h
/usr/include/libssh/sftp.h
/usr/include/libssh/ssh2.h
/usr/lib64/cmake/libssh/libssh-config-version.cmake
/usr/lib64/cmake/libssh/libssh-config.cmake
/usr/lib64/libssh.so
/usr/lib64/pkgconfig/libssh.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libssh.so.4
/usr/lib64/libssh.so.4.7.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libssh/COPYING
/usr/share/package-licenses/libssh/cmake_Modules_COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/libssh/doc_that_style_LICENSE
