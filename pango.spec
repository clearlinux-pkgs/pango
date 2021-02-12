#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pango
Version  : 1.48.2
Release  : 73
URL      : https://download.gnome.org/sources/pango/1.48/pango-1.48.2.tar.xz
Source0  : https://download.gnome.org/sources/pango/1.48/pango-1.48.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: pango-bin = %{version}-%{release}
Requires: pango-data = %{version}-%{release}
Requires: pango-lib = %{version}-%{release}
Requires: pango-license = %{version}-%{release}
Requires: pango-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : clear-font
BuildRequires : fontconfig-dev
BuildRequires : freetype-dev
BuildRequires : fribidi-dev
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev
BuildRequires : help2man
BuildRequires : xorg-fonts

%description
The Pango backends written for Win32 is pangowin32. Pangowin32 uses
the Win32 GDI font API. GTK+ 2.8 and later on Win32 however actually
uses the pangocairo backend (which then uses only small parts of
pangowin32). Much of the GDI font API calls are in cairo.

%package bin
Summary: bin components for the pango package.
Group: Binaries
Requires: pango-data = %{version}-%{release}
Requires: pango-license = %{version}-%{release}

%description bin
bin components for the pango package.


%package data
Summary: data components for the pango package.
Group: Data

%description data
data components for the pango package.


%package dev
Summary: dev components for the pango package.
Group: Development
Requires: pango-lib = %{version}-%{release}
Requires: pango-bin = %{version}-%{release}
Requires: pango-data = %{version}-%{release}
Provides: pango-devel = %{version}-%{release}
Requires: pango = %{version}-%{release}

%description dev
dev components for the pango package.


%package lib
Summary: lib components for the pango package.
Group: Libraries
Requires: pango-data = %{version}-%{release}
Requires: pango-license = %{version}-%{release}

%description lib
lib components for the pango package.


%package license
Summary: license components for the pango package.
Group: Default

%description license
license components for the pango package.


%package man
Summary: man components for the pango package.
Group: Default

%description man
man components for the pango package.


%prep
%setup -q -n pango-1.48.2
cd %{_builddir}/pango-1.48.2
pushd ..
cp -a pango-1.48.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613173772
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --libdir=lib64/haswell --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/pango
cp %{_builddir}/pango-1.48.2/COPYING %{buildroot}/usr/share/package-licenses/pango/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/girepository-1.0/Pango-1.0.typelib
/usr/lib64/haswell/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib64/haswell/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib64/haswell/girepository-1.0/PangoFc-1.0.typelib
/usr/lib64/haswell/girepository-1.0/PangoOT-1.0.typelib
/usr/lib64/haswell/girepository-1.0/PangoXft-1.0.typelib
/usr/lib64/haswell/pkgconfig/pango.pc
/usr/lib64/haswell/pkgconfig/pangocairo.pc
/usr/lib64/haswell/pkgconfig/pangofc.pc
/usr/lib64/haswell/pkgconfig/pangoft2.pc
/usr/lib64/haswell/pkgconfig/pangoot.pc
/usr/lib64/haswell/pkgconfig/pangoxft.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/pango-list
/usr/bin/pango-view

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Pango-1.0.typelib
/usr/lib64/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib64/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib64/girepository-1.0/PangoFc-1.0.typelib
/usr/lib64/girepository-1.0/PangoOT-1.0.typelib
/usr/lib64/girepository-1.0/PangoXft-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/pango-1.0/pango/pango-attributes.h
/usr/include/pango-1.0/pango/pango-bidi-type.h
/usr/include/pango-1.0/pango/pango-break.h
/usr/include/pango-1.0/pango/pango-context.h
/usr/include/pango-1.0/pango/pango-coverage.h
/usr/include/pango-1.0/pango/pango-direction.h
/usr/include/pango-1.0/pango/pango-engine.h
/usr/include/pango-1.0/pango/pango-enum-types.h
/usr/include/pango-1.0/pango/pango-features.h
/usr/include/pango-1.0/pango/pango-font.h
/usr/include/pango-1.0/pango/pango-fontmap.h
/usr/include/pango-1.0/pango/pango-fontset.h
/usr/include/pango-1.0/pango/pango-glyph-item.h
/usr/include/pango-1.0/pango/pango-glyph.h
/usr/include/pango-1.0/pango/pango-gravity.h
/usr/include/pango-1.0/pango/pango-item.h
/usr/include/pango-1.0/pango/pango-language.h
/usr/include/pango-1.0/pango/pango-layout.h
/usr/include/pango-1.0/pango/pango-matrix.h
/usr/include/pango-1.0/pango/pango-modules.h
/usr/include/pango-1.0/pango/pango-ot.h
/usr/include/pango-1.0/pango/pango-renderer.h
/usr/include/pango-1.0/pango/pango-script.h
/usr/include/pango-1.0/pango/pango-tabs.h
/usr/include/pango-1.0/pango/pango-types.h
/usr/include/pango-1.0/pango/pango-utils.h
/usr/include/pango-1.0/pango/pango-version-macros.h
/usr/include/pango-1.0/pango/pango.h
/usr/include/pango-1.0/pango/pangocairo.h
/usr/include/pango-1.0/pango/pangofc-decoder.h
/usr/include/pango-1.0/pango/pangofc-font.h
/usr/include/pango-1.0/pango/pangofc-fontmap.h
/usr/include/pango-1.0/pango/pangoft2.h
/usr/include/pango-1.0/pango/pangoxft-render.h
/usr/include/pango-1.0/pango/pangoxft.h
/usr/lib64/haswell/libpango-1.0.so
/usr/lib64/haswell/libpangocairo-1.0.so
/usr/lib64/haswell/libpangoft2-1.0.so
/usr/lib64/haswell/libpangoxft-1.0.so
/usr/lib64/libpango-1.0.so
/usr/lib64/libpangocairo-1.0.so
/usr/lib64/libpangoft2-1.0.so
/usr/lib64/libpangoxft-1.0.so
/usr/lib64/pkgconfig/pango.pc
/usr/lib64/pkgconfig/pangocairo.pc
/usr/lib64/pkgconfig/pangofc.pc
/usr/lib64/pkgconfig/pangoft2.pc
/usr/lib64/pkgconfig/pangoot.pc
/usr/lib64/pkgconfig/pangoxft.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libpango-1.0.so.0
/usr/lib64/haswell/libpango-1.0.so.0.4800.2
/usr/lib64/haswell/libpangocairo-1.0.so.0
/usr/lib64/haswell/libpangocairo-1.0.so.0.4800.2
/usr/lib64/haswell/libpangoft2-1.0.so.0
/usr/lib64/haswell/libpangoft2-1.0.so.0.4800.2
/usr/lib64/haswell/libpangoxft-1.0.so.0
/usr/lib64/haswell/libpangoxft-1.0.so.0.4800.2
/usr/lib64/libpango-1.0.so.0
/usr/lib64/libpango-1.0.so.0.4800.2
/usr/lib64/libpangocairo-1.0.so.0
/usr/lib64/libpangocairo-1.0.so.0.4800.2
/usr/lib64/libpangoft2-1.0.so.0
/usr/lib64/libpangoft2-1.0.so.0.4800.2
/usr/lib64/libpangoxft-1.0.so.0
/usr/lib64/libpangoxft-1.0.so.0.4800.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pango/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pango-view.1
