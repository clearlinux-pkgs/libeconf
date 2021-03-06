#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libeconf
Version  : 0.3.4
Release  : 6
URL      : https://github.com/openSUSE/libeconf/archive/v0.3.4/libeconf-0.3.4.tar.gz
Source0  : https://github.com/openSUSE/libeconf/archive/v0.3.4/libeconf-0.3.4.tar.gz
Summary  : TODO
Group    : Development/Tools
License  : MIT
Requires: libeconf-lib = %{version}-%{release}
Requires: libeconf-license = %{version}-%{release}

%description
# libeconf
**libeconf** is a highly flexible and configureable library to parse and
manage key=value configuration files.
It reads configuration file snippets from different directories and builds
the final configuration file for the application from it.

%package dev
Summary: dev components for the libeconf package.
Group: Development
Requires: libeconf-lib = %{version}-%{release}
Provides: libeconf-devel = %{version}-%{release}
Requires: libeconf = %{version}-%{release}

%description dev
dev components for the libeconf package.


%package lib
Summary: lib components for the libeconf package.
Group: Libraries
Requires: libeconf-license = %{version}-%{release}

%description lib
lib components for the libeconf package.


%package license
Summary: license components for the libeconf package.
Group: Default

%description license
license components for the libeconf package.


%prep
%setup -q -n libeconf-0.3.4
cd %{_builddir}/libeconf-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580234506
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1580234506
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libeconf
cp %{_builddir}/libeconf-0.3.4/LICENSE %{buildroot}/usr/share/package-licenses/libeconf/fcc7730890cf59ca8a39456c72a6d63c599094d9
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libeconf.h
/usr/lib64/libeconf.so
/usr/lib64/pkgconfig/libeconf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libeconf.so.0
/usr/lib64/libeconf.so.0.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libeconf/fcc7730890cf59ca8a39456c72a6d63c599094d9
