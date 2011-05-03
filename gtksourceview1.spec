%define api_version	1.0
%define lib_major 0
%define libname	%mklibname %{oname}- %{api_version} %{lib_major}
%define libnamedev %mklibname -d %{oname}- %{api_version}
%define oname gtksourceview

Summary:	Source code viewing library
Name:		gtksourceview1
Version: 1.8.5
Release:	%mkrel 8
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{oname}-%{version}.tar.bz2
Patch0:		gtksourceview-1.8.5-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	libgtk+2-devel >= 2.3.0
BuildRequires:  libgnome-vfs2-devel >= 2.2.0
BuildRequires:  libgnomeprintui-devel >= 2.7.0
BuildRequires:  intltool
Conflicts:		gtksourceview-sharp <= 0.5-3mdk
Obsoletes: gtksourceview < 1.90

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Provides: gtksourceview1.0 = %version

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libnamedev}
Summary:        Libraries and include files for GtkSourceView
Group:          Development/GNOME and GTK+
Requires:       %{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{oname}-%{api_version}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{oname}- %{api_version} %{lib_major}

%description -n %{libnamedev}
GtkSourceView development files 


%prep
%setup -q -n %oname-%version
%patch0 -p0

%build
export CPPFLAGS=-D_GNU_SOURCE=1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{oname}-%{api_version}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{oname}-%{api_version}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_datadir}/gtksourceview-%{api_version}

%files -n %{libname} 
%defattr(-,root,root)
%{_libdir}/libgtksourceview-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/gtksourceview
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*


