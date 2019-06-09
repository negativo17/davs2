Name:       davs2
Version:    1.6
Release:    1%{?dist}
Summary:    An open-source decoder of AVS2-P2/IEEE1857.4 video coding standard
URL:        https://github.com/pkuvcl/%{name}
License:    GPLv2

Source0:    https://github.com/pkuvcl/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/pkuvcl/davs2/commit/00ef2c8062a7f7d7265d933676fb5cc60f1ea659
Patch0:     %{name}-1.6-gcc8-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  yasm

%description
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the command line decoder.

%package libs
Summary:    AVS2-P2/IEEE1857.4 decoder library

%description libs
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library.

%package devel
Summary:    AVS2-P2/IEEE1857.4 decoder library development files
Requires:   %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library development files.

%prep
%autosetup -p1

%build
cd build/linux
%configure \
    --bit-depth='8' \
    --chroma-format='all' \
    --disable-static \
    --enable-pic \
    --enable-shared

# Remove hardcoded CFLAGS on generated file containing variables
sed -i \
    -e 's|CFLAGS=.*%{optflags}|CFLAGS=%{optflags}|g' \
    config.mak

%make_build

%install
cd build/linux
%make_install

%ldconfig_scriptlets libs

%files
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.16

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Jun 08 2019 Simone Caronni <negativo17@gmail.com> - 1.6-1
- First build.
