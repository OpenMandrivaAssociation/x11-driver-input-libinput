%define _disable_ld_no_undefined 1

Summary:	X.org input driver based on libinput
Name:		x11-driver-input-libinput
Version:	1.0.0
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-libinput-%{version}.tar.bz2
Source1:	https://src.fedoraproject.org/rpms/xorg-x11-drv-libinput/raw/rawhide/f/71-libinput-overrides-wacom.conf
Patch0:		https://src.fedoraproject.org/rpms/xorg-x11-drv-libinput/raw/rawhide/f/0001-Add-a-DPIScaleFactor-option-as-temporary-solution-to.patch
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(libinput)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Requires:	xkeyboard-config
Recommends:	libinput-tools
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
cp %{SOURCE1} %{buildroot}%{_datadir}/X11/xorg.conf.d/

%files
%{_datadir}/X11/xorg.conf.d/*.conf
%{_libdir}/xorg/modules/input/libinput_drv.so
%{_mandir}/man4/libinput.4.*

%files devel
%{_libdir}/pkgconfig/xorg-libinput.pc
%{_includedir}/xorg/libinput-properties.h
