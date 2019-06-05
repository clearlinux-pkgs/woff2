#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : woff2
Version  : 1.0.2
Release  : 3
URL      : https://github.com/google/woff2/archive/v1.0.2.tar.gz
Source0  : https://github.com/google/woff2/archive/v1.0.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: woff2-lib
BuildRequires : cmake
BuildRequires : pkgconfig(libbrotlidec)

%description
compression related modules in this repository.
brotli/ contains reference code for the Brotli byte-level compression
algorithm. Note that it is licensed under the MIT license.

%package dev
Summary: dev components for the woff2 package.
Group: Development
Requires: woff2-lib
Provides: woff2-devel

%description dev
dev components for the woff2 package.


%package lib
Summary: lib components for the woff2 package.
Group: Libraries

%description lib
lib components for the woff2 package.


%prep
%setup -q -n woff2-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521668651
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1521668651
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/woff2/decode.h
/usr/include/woff2/encode.h
/usr/include/woff2/output.h
/usr/lib64/libwoff2common.so
/usr/lib64/libwoff2dec.so
/usr/lib64/libwoff2enc.so
/usr/lib64/pkgconfig/libwoff2common.pc
/usr/lib64/pkgconfig/libwoff2dec.pc
/usr/lib64/pkgconfig/libwoff2enc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwoff2common.so.1.0.2
/usr/lib64/libwoff2dec.so.1.0.2
/usr/lib64/libwoff2enc.so.1.0.2
