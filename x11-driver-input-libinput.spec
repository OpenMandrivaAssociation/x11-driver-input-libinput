%define _disable_ld_no_undefined 1

Summary:	X.org input driver based on libinput
Name:		x11-driver-input-libinput
Version:	0.4.0
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	ftp://ftp.x.org/pub/individual/driver/xf86-input-libinput-%{version}.tar.bz2
Source1:	99-libinput.conf
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(libinput)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Conflicts:	x11-server < 1.4

%description
This is an X driver based on libinput. It is a thin wrapper 
around libinput, so while it does provide all features that 
libinput supports it does little beyond.

%package devel
Summary:	Development files for %{name}
Group:		Development/X11

%description devel
Development files for %{name}.

%prep
%setup -qn xf86-input-libinput-%{version}

%build
%configure
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# Add scrolling support for TrackPoint and similar devices
mkdir -p %{buildroot}%{_datadir}/X11/xorg.conf.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/X11/xorg.conf.d/

%files
%{_datadir}/X11/xorg.conf.d/99-libinput.conf

%files devel
