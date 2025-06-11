%define _disable_ld_no_undefined 1
%if %{cross_compiling}
%global optflags %{optflags} -I%{_prefix}/%{_target_platform}/include/xorg
%endif

Summary:	X.org input driver based on libinput
Name:		x11-driver-input-libinput
Version:	1.5.0
Release:	2
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-libinput-%{version}.tar.xz
Source1:	https://src.fedoraproject.org/rpms/xorg-x11-drv-libinput/raw/rawhide/f/71-libinput-overrides-wacom.conf
#Patch0:		https://src.fedoraproject.org/rpms/xorg-x11-drv-libinput/raw/rawhide/f/0001-Add-a-DPIScaleFactor-option-as-temporary-solution-to.patch
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(libinput)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Requires:	xkeyboard-config
Recommends:	libinput-tools
Conflicts:	x11-server < 1.4
# Version numbers below are the last versions of those drivers in Cooker
# before switching to libinput for everything.
Obsoletes:	x11-driver-input-evdev <= 2.10.6-5
Obsoletes:	x11-driver-input-evtouch <= 0.8.8-24
Obsoletes:	x11-driver-input-fpit <= 1.4.0-20
Obsoletes:	x11-driver-input-hyperpen <= 1.4.1-21
Obsoletes:	x11-driver-input-joystick <= 1.6.3-3
Obsoletes:	x11-driver-input-mouse <= 1.9.5-1
Obsoletes:	x11-driver-input-mutouch <= 1.3.0-21
Obsoletes:	x11-driver-input-penmount <= 1.5.0-27
Obsoletes:	x11-driver-input-synaptics <= 1.9.2-1
Obsoletes:	x11-driver-input-void <= 1.4.2-1

%description
This is an X driver based on libinput. It is a thin wrapper 
around libinput, so while it does provide all features that 
libinput supports it does little beyond.

%package devel
Summary:	Xorg X11 libinput input driver development package
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
%doc %{_mandir}/man4/libinput.4.*

%files devel
%{_libdir}/pkgconfig/xorg-libinput.pc
%{_includedir}/xorg/libinput-properties.h
