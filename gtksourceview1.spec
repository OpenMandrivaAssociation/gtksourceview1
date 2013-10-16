%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	gtksourceview
%define api	1.0
%define major	0
%define libname %mklibname %{oname}- %{api} %{major}
%define devname %mklibname -d %{oname}- %{api}

Summary:	Source code viewing library
Name:		gtksourceview1
Version:	1.8.5
Release:	15
License:	GPLv2+
Group:		Editors
Url:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gtksourceview/%{url_ver}/%{oname}-%{version}.tar.bz2
Patch0:		gtksourceview-1.8.5-fix-str-fmt.patch
Patch1:		gtksourceview-1.8.5_glib_h.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
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

%package -n %{devname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%find_lang %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README TODO
%{_datadir}/gtksourceview-%{api}

%files -n %{libname}
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/gtksourceview
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

