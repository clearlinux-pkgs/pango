#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pango
Version  : 1.49.1
Release  : 86
URL      : https://download.gnome.org/sources/pango/1.49/pango-1.49.1.tar.xz
Source0  : https://download.gnome.org/sources/pango/1.49/pango-1.49.1.tar.xz
Summary  : GObject-Introspection based documentation generator
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-3.0 CC0-1.0 GPL-3.0 LGPL-2.0 MIT OFL-1.1
Requires: pango-bin = %{version}-%{release}
Requires: pango-data = %{version}-%{release}
Requires: pango-filemap = %{version}-%{release}
Requires: pango-lib = %{version}-%{release}
Requires: pango-license = %{version}-%{release}
Requires: pango-man = %{version}-%{release}
BuildRequires : buildreq-distutils3
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
Requires: pango-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the pango package.
Group: Default

%description filemap
filemap components for the pango package.


%package lib
Summary: lib components for the pango package.
Group: Libraries
Requires: pango-data = %{version}-%{release}
Requires: pango-license = %{version}-%{release}
Requires: pango-filemap = %{version}-%{release}

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
%setup -q -n pango-1.49.1
cd %{_builddir}/pango-1.49.1
pushd ..
cp -a pango-1.49.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633818464
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk_doc=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk_doc=false  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/pango
cp %{_builddir}/pango-1.49.1/COPYING %{buildroot}/usr/share/package-licenses/pango/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
cp %{_builddir}/pango-1.49.1/subprojects/gi-docgen/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/pango/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/pango-1.49.1/subprojects/gi-docgen/LICENSES/CC-BY-SA-3.0.txt %{buildroot}/usr/share/package-licenses/pango/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51
cp %{_builddir}/pango-1.49.1/subprojects/gi-docgen/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pango/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/pango-1.49.1/subprojects/gi-docgen/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/pango/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/pango-1.49.1/subprojects/gi-docgen/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/pango/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
cp %{_builddir}/pango-1.49.1/subprojects/gi-docgen/LICENSES/OFL-1.1.txt %{buildroot}/usr/share/package-licenses/pango/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pango-list
/usr/bin/pango-segmentation
/usr/bin/pango-view
/usr/share/clear/optimized-elf/bin*

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
/usr/include/pango-1.0/pango/pango-color.h
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
/usr/include/pango-1.0/pango/pango-markup.h
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pango

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpango-1.0.so.0
/usr/lib64/libpango-1.0.so.0.4901.0
/usr/lib64/libpangocairo-1.0.so.0
/usr/lib64/libpangocairo-1.0.so.0.4901.0
/usr/lib64/libpangoft2-1.0.so.0
/usr/lib64/libpangoft2-1.0.so.0.4901.0
/usr/lib64/libpangoxft-1.0.so.0
/usr/lib64/libpangoxft-1.0.so.0.4901.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pango/220906dfcc3d3b7f4e18cf8a22454c628ca0ea2e
/usr/share/package-licenses/pango/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pango/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/pango/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pango/8b8a351a8476e37a2c4d398eb1e6c8403f487ea4
/usr/share/package-licenses/pango/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
/usr/share/package-licenses/pango/fb41626a3005c2b6e14b8b3f5d9d0b19b5faaa51

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pango-view.1
