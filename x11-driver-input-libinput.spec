%define _disable_ld_no_undefined 1

Summary:	X.org input driver based on libinput
Name:		x11-driver-input-libinput
Version:	0.28.2
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-libinput-%{version}.tar.bz2
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

%package devel
Summary:	Xorg X11 libinput input driver development package
Requires:	pkgconfig
Requires:	%{name} = %{EVRD}

%description devel
Xorg X11 libinput input driver development files.

%prep
%autosetup -n xf86-input-libinput-%{version} -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_datadir}/X11/xorg.conf.d/*-libinput.conf
%{_libdir}/xorg/modules/input/libinput_drv.so
%{_mandir}/man4/libinput.4.xz

%files devel
%{_libdir}/pkgconfig/xorg-libinput.pc
%{_includedir}/xorg/libinput-properties.h
