%define _disable_ld_no_undefined 1

Summary:	X.org input driver based on libinput
Name:		x11-driver-input-libinput
Version:	0.24.0
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	ftp://ftp.x.org/pub/individual/driver/xf86-input-libinput-%{version}.tar.bz2
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(libinput)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Conflicts:	x11-server < 1.4

%description
This is an X driver based on libinput. It is a thin wrapper 
around libinput, so while it does provide all features that 
libinput supports it does little beyond.

%prep
%setup -qn xf86-input-libinput-%{version}

%build
%configure
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

rm -rf %{buildroot}%{_includedir}/xorg/libinput-properties.h
rm -rf %{buildroot}%{_libdir}/pkgconfig/xorg-libinput.pc

%files
%{_datadir}/X11/xorg.conf.d/*-libinput.conf
%{_libdir}/xorg/modules/input/libinput_drv.so
%{_mandir}/man4/libinput.4.xz
