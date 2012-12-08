%define oname gtksourceview
%define api 1.0
%define major 0
%define libname %mklibname %{oname}- %{api} %{major}
%define develname %mklibname -d %{oname}- %{api}

Summary:	Source code viewing library
Name:		gtksourceview1
Version:	1.8.5
Release:	11
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{oname}-%{version}.tar.bz2
Patch0:		gtksourceview-1.8.5-fix-str-fmt.patch
Patch1:		gtksourceview-1.8.5_glib_h.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	intltool

Obsoletes:	gtksourceview < 1.90

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Provides:	gtksourceview1.0 = %{version}-%{release}

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{develname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d gtksourceview- 1.0 0} < 1.8.5-11

%description -n %{develname}
GtkSourceView development files.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
export CPPFLAGS=-D_GNU_SOURCE=1
%configure2_5x
%make

%install
%makeinstall_std

%{find_lang} %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README TODO
%{_datadir}/gtksourceview-%{api}

%files -n %{libname}
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/gtksourceview
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*



%changelog
* Sat Dec 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.8.5-10
+ Revision: 744937
- and more to p1
- more to p1
- added patch1 for glib20 2.31.x
- converted p0 to p1 level
- employed apply_patchs
- rebuild
- clean up spec

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 1.8.5-9
+ Revision: 700352
- rebuild

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.5-8
+ Revision: 664958
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.5-7mdv2011.0
+ Revision: 605512
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.5-6mdv2010.1
+ Revision: 521142
- rebuilt for 2010.1

* Wed May 20 2009 Funda Wang <fwang@mandriva.org> 1.8.5-5mdv2010.0
+ Revision: 377913
- fix str fmt

* Mon Jul 28 2008 Götz Waschk <waschk@mandriva.org> 1.8.5-5mdv2009.0
+ Revision: 251183
- fix build
- update license
- update build deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.5-4mdv2008.1
+ Revision: 178743
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 30 2007 Götz Waschk <waschk@mandriva.org> 1.8.5-2mdv2008.0
+ Revision: 75311
- new devel name
- clean up provides and obsoletes

* Thu Jul 12 2007 Götz Waschk <waschk@mandriva.org> 1.8.5-1mdv2008.0
+ Revision: 51521
- rename package to gtksourceview1
- import latest version of gtksourceview 1.x

