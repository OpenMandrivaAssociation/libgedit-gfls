%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define major 0

%define libname %mklibname gedit-gfls
%define girname	%mklibname gedit-gfls-gir
%define devname %mklibname -d gedit-gfls


Name:           libgedit-gfls
Version:        0.2.1
Release:        1
Summary:        A module dedicated to file loading and saving.
Group:		      System/Libraries
License:        LGPLv3
URL:            https://github.com/gedit-technology/libgedit-gfls/
#Source0:        https://github.com/gedit-technology/libgedit-gfls/releases/download/%{version}/libgedit-gfls-%{version}.tar.xz
Source0:        https://gitlab.gnome.org/World/gedit/libgedit-gfls/-/archive/%{version}/libgedit-gfls-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
A module dedicated to file loading and saving.

%package -n %{libname}
Summary: Libraries for %{name}
Requires: %{girname} = %{EVRD}

%description    -n %{libname}
The %{name} package contains libraries for %{name}

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{girname}
GObject Introspection interface description for %{name}

%package -n %{devname}
Summary:  Development files for %{name}
Requires: %{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson  -Dgtk_doc=true
%meson_build

%install
%meson_install

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libgedit-gfls-1/
%{_libdir}/pkgconfig/libgedit-gfls-1.pc
%{_libdir}/libgedit-gfls-1.so
%{_datadir}/gir-1.0/Gfls-1.gir
%{_includedir}/libgedit-gfls-1/

%files -n %{girname}
%{_libdir}/girepository-1.0/Gfls-1.typelib

%files -n %{libname}
%{_libdir}/libgedit-gfls-1.so.%{major}
