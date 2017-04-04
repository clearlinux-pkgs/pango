#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pango
Version  : 1.40.3
Release  : 34
URL      : https://download.gnome.org/sources/pango/1.40/pango-1.40.3.tar.xz
Source0  : https://download.gnome.org/sources/pango/1.40/pango-1.40.3.tar.xz
Summary  : Freetype 2.0 and fontconfig font support for Pango
Group    : Development/Tools
License  : LGPL-2.0
Requires: pango-bin
Requires: pango-data
Requires: pango-lib
Requires: pango-doc
BuildRequires : clear-font
BuildRequires : docbook-xml
BuildRequires : font-bitstream-type1
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : harfbuzz-dev32
BuildRequires : libX11-dev32
BuildRequires : libXrender-dev32
BuildRequires : libxcb-dev32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32cairo)
BuildRequires : pkgconfig(32fontconfig)
BuildRequires : pkgconfig(32freetype2)
BuildRequires : pkgconfig(32harfbuzz)
BuildRequires : pkgconfig(32xft)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(cairo-png)
BuildRequires : pkgconfig(cairo-xlib)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(xft)

%description
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. Pango can be used anywhere that text layout
is needed; however, most of the work on Pango so far has been done using
the GTK+ widget toolkit as a test platform. Pango forms the core of text
and font handling for GTK+-2.x.

%package bin
Summary: bin components for the pango package.
Group: Binaries
Requires: pango-data

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
Requires: pango-lib
Requires: pango-bin
Requires: pango-data
Provides: pango-devel

%description dev
dev components for the pango package.


%package dev32
Summary: dev32 components for the pango package.
Group: Default
Requires: pango-lib32
Requires: pango-bin
Requires: pango-data
Requires: pango-dev

%description dev32
dev32 components for the pango package.


%package doc
Summary: doc components for the pango package.
Group: Documentation

%description doc
doc components for the pango package.


%package lib
Summary: lib components for the pango package.
Group: Libraries
Requires: pango-data

%description lib
lib components for the pango package.


%package lib32
Summary: lib32 components for the pango package.
Group: Default
Requires: pango-data

%description lib32
lib32 components for the pango package.


%prep
%setup -q -n pango-1.40.3
pushd ..
cp -a pango-1.40.3 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491326317
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static --enable-explicit-deps=yes  --with-included-modules=basic-fc --with-xft
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-explicit-deps=yes  --with-included-modules=basic-fc --with-xft   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1491326317
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Pango-1.0.typelib
/usr/lib32/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib32/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib32/girepository-1.0/PangoXft-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/pango-view

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Pango-1.0.typelib
/usr/lib64/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib64/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib64/girepository-1.0/PangoXft-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/pango-1.0/pango/pango-attributes.h
/usr/include/pango-1.0/pango/pango-bidi-type.h
/usr/include/pango-1.0/pango/pango-break.h
/usr/include/pango-1.0/pango/pango-context.h
/usr/include/pango-1.0/pango/pango-coverage.h
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
/usr/lib64/libpango-1.0.so
/usr/lib64/libpangocairo-1.0.so
/usr/lib64/libpangoft2-1.0.so
/usr/lib64/libpangoxft-1.0.so
/usr/lib64/pkgconfig/pango.pc
/usr/lib64/pkgconfig/pangocairo.pc
/usr/lib64/pkgconfig/pangoft2.pc
/usr/lib64/pkgconfig/pangoxft.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpango-1.0.so
/usr/lib32/libpangocairo-1.0.so
/usr/lib32/libpangoft2-1.0.so
/usr/lib32/libpangoxft-1.0.so
/usr/lib32/pkgconfig/32pango.pc
/usr/lib32/pkgconfig/32pangocairo.pc
/usr/lib32/pkgconfig/32pangoft2.pc
/usr/lib32/pkgconfig/32pangoxft.pc
/usr/lib32/pkgconfig/pango.pc
/usr/lib32/pkgconfig/pangocairo.pc
/usr/lib32/pkgconfig/pangoft2.pc
/usr/lib32/pkgconfig/pangoxft.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/pango/PangoEngineLang.html
/usr/share/gtk-doc/html/pango/PangoEngineShape.html
/usr/share/gtk-doc/html/pango/PangoFcDecoder.html
/usr/share/gtk-doc/html/pango/PangoFcFont.html
/usr/share/gtk-doc/html/pango/PangoFcFontMap.html
/usr/share/gtk-doc/html/pango/PangoMarkupFormat.html
/usr/share/gtk-doc/html/pango/PangoRenderer.html
/usr/share/gtk-doc/html/pango/annotation-glossary.html
/usr/share/gtk-doc/html/pango/api-index-1-10.html
/usr/share/gtk-doc/html/pango/api-index-1-12.html
/usr/share/gtk-doc/html/pango/api-index-1-14.html
/usr/share/gtk-doc/html/pango/api-index-1-16.html
/usr/share/gtk-doc/html/pango/api-index-1-18.html
/usr/share/gtk-doc/html/pango/api-index-1-2.html
/usr/share/gtk-doc/html/pango/api-index-1-20.html
/usr/share/gtk-doc/html/pango/api-index-1-22.html
/usr/share/gtk-doc/html/pango/api-index-1-24.html
/usr/share/gtk-doc/html/pango/api-index-1-26.html
/usr/share/gtk-doc/html/pango/api-index-1-30.html
/usr/share/gtk-doc/html/pango/api-index-1-31-0.html
/usr/share/gtk-doc/html/pango/api-index-1-32-4.html
/usr/share/gtk-doc/html/pango/api-index-1-32.html
/usr/share/gtk-doc/html/pango/api-index-1-34.html
/usr/share/gtk-doc/html/pango/api-index-1-38.html
/usr/share/gtk-doc/html/pango/api-index-1-4.html
/usr/share/gtk-doc/html/pango/api-index-1-40.html
/usr/share/gtk-doc/html/pango/api-index-1-6.html
/usr/share/gtk-doc/html/pango/api-index-1-8.html
/usr/share/gtk-doc/html/pango/api-index-deprecated.html
/usr/share/gtk-doc/html/pango/api-index-full.html
/usr/share/gtk-doc/html/pango/home.png
/usr/share/gtk-doc/html/pango/index.html
/usr/share/gtk-doc/html/pango/layout.gif
/usr/share/gtk-doc/html/pango/left-insensitive.png
/usr/share/gtk-doc/html/pango/left.png
/usr/share/gtk-doc/html/pango/lowlevel.html
/usr/share/gtk-doc/html/pango/pango-Bidirectional-Text.html
/usr/share/gtk-doc/html/pango/pango-Cairo-Rendering.html
/usr/share/gtk-doc/html/pango/pango-CoreText-Fonts.html
/usr/share/gtk-doc/html/pango/pango-Coverage-Maps.html
/usr/share/gtk-doc/html/pango/pango-Engines.html
/usr/share/gtk-doc/html/pango/pango-Fonts.html
/usr/share/gtk-doc/html/pango/pango-FreeType-Fonts-and-Rendering.html
/usr/share/gtk-doc/html/pango/pango-Glyph-Storage.html
/usr/share/gtk-doc/html/pango/pango-Layout-Objects.html
/usr/share/gtk-doc/html/pango/pango-Miscellaneous-Utilities.html
/usr/share/gtk-doc/html/pango/pango-Modules.html
/usr/share/gtk-doc/html/pango/pango-OpenType-Font-Handling.html
/usr/share/gtk-doc/html/pango/pango-Scripts-and-Languages.html
/usr/share/gtk-doc/html/pango/pango-Tab-Stops.html
/usr/share/gtk-doc/html/pango/pango-Text-Attributes.html
/usr/share/gtk-doc/html/pango/pango-Text-Processing.html
/usr/share/gtk-doc/html/pango/pango-Version-Checking.html
/usr/share/gtk-doc/html/pango/pango-Vertical-Text.html
/usr/share/gtk-doc/html/pango/pango-Win32-Fonts-and-Rendering.html
/usr/share/gtk-doc/html/pango/pango-Xft-Fonts-and-Rendering.html
/usr/share/gtk-doc/html/pango/pango-hierarchy.html
/usr/share/gtk-doc/html/pango/pango.devhelp2
/usr/share/gtk-doc/html/pango/pango.html
/usr/share/gtk-doc/html/pango/rendering.html
/usr/share/gtk-doc/html/pango/right-insensitive.png
/usr/share/gtk-doc/html/pango/right.png
/usr/share/gtk-doc/html/pango/rotated-text.png
/usr/share/gtk-doc/html/pango/style.css
/usr/share/gtk-doc/html/pango/up-insensitive.png
/usr/share/gtk-doc/html/pango/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpango-1.0.so.0
/usr/lib64/libpango-1.0.so.0.4000.3
/usr/lib64/libpangocairo-1.0.so.0
/usr/lib64/libpangocairo-1.0.so.0.4000.3
/usr/lib64/libpangoft2-1.0.so.0
/usr/lib64/libpangoft2-1.0.so.0.4000.3
/usr/lib64/libpangoxft-1.0.so.0
/usr/lib64/libpangoxft-1.0.so.0.4000.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpango-1.0.so.0
/usr/lib32/libpango-1.0.so.0.4000.3
/usr/lib32/libpangocairo-1.0.so.0
/usr/lib32/libpangocairo-1.0.so.0.4000.3
/usr/lib32/libpangoft2-1.0.so.0
/usr/lib32/libpangoft2-1.0.so.0.4000.3
/usr/lib32/libpangoxft-1.0.so.0
/usr/lib32/libpangoxft-1.0.so.0.4000.3
