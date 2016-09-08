#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pango
Version  : 1.40.2
Release  : 27
URL      : http://ftp.gnome.org/pub/GNOME/sources/pango/1.40/pango-1.40.2.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/pango/1.40/pango-1.40.2.tar.xz
Summary  : Freetype 2.0 and fontconfig font support for Pango
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: pango-bin
Requires: pango-lib
Requires: pango-data
Requires: pango-doc
BuildRequires : clear-font
BuildRequires : docbook-xml
BuildRequires : font-bitstream-type1
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
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


%prep
%setup -q -n pango-1.40.2

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export FCFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export FFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
%configure --disable-static --enable-explicit-deps=yes  --with-included-modules=basic-fc --with-xft
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pango-view

%files data
%defattr(-,root,root,-)
/usr/share/gir-1.0/Pango-1.0.gir
/usr/share/gir-1.0/PangoCairo-1.0.gir
/usr/share/gir-1.0/PangoFT2-1.0.gir
/usr/share/gir-1.0/PangoXft-1.0.gir

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
/usr/lib64/*.so
/usr/lib64/girepository-1.0/Pango-1.0.typelib
/usr/lib64/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib64/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib64/girepository-1.0/PangoXft-1.0.typelib
/usr/lib64/pkgconfig/*.pc

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
/usr/lib64/*.so.*
