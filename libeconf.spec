#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libeconf
Version  : 0.4.7
Release  : 10
URL      : https://github.com/openSUSE/libeconf/archive/v0.4.7/libeconf-0.4.7.tar.gz
Source0  : https://github.com/openSUSE/libeconf/archive/v0.4.7/libeconf-0.4.7.tar.gz
Summary  : @PROJECT_DESCRIPTION@
Group    : Development/Tools
License  : MIT
Requires: libeconf-bin = %{version}-%{release}
Requires: libeconf-lib = %{version}-%{release}
Requires: libeconf-license = %{version}-%{release}
Requires: libeconf-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : doxygen

%description
# libeconf
**libeconf** is a highly flexible and configurable library to parse and
manage key=value configuration files.
It reads configuration file snippets from different directories and builds
the final configuration file for the application from it.

%package bin
Summary: bin components for the libeconf package.
Group: Binaries
Requires: libeconf-license = %{version}-%{release}

%description bin
bin components for the libeconf package.


%package dev
Summary: dev components for the libeconf package.
Group: Development
Requires: libeconf-lib = %{version}-%{release}
Requires: libeconf-bin = %{version}-%{release}
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


%package man
Summary: man components for the libeconf package.
Group: Default

%description man
man components for the libeconf package.


%prep
%setup -q -n libeconf-0.4.7
cd %{_builddir}/libeconf-0.4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666125761
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libeconf
cp %{_builddir}/libeconf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libeconf/fcc7730890cf59ca8a39456c72a6d63c599094d9
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/econftool

%files dev
%defattr(-,root,root,-)
/usr/include/libeconf.h
/usr/include/libeconf_ext.h
/usr/lib64/libeconf.so
/usr/lib64/pkgconfig/libeconf.pc
/usr/share/man/man3/libeconf.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libeconf.so.0
/usr/lib64/libeconf.so.0.4.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libeconf/fcc7730890cf59ca8a39456c72a6d63c599094d9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/econftool.8
