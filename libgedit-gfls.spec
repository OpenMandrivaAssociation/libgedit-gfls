%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:           libgedit-gfls
Version:        0.1.0
Release:        1
Summary:        Text editor product line
Group:		      System/Libraries
License:        LGPLv3
URL:            https://github.com/gedit-technology/libgedit-gfls/
Source0:        https://github.com/gedit-technology/libgedit-gfls/releases/download/%{version}/libgedit-gfls-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
A module dedicated to file loading and saving.

%prep
%autosetup -n libgedit-tepl-%{version} -p1

%build
%meson  -Dgtk_doc=true
%meson_build

%install
%meson_install

%files
