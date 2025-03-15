Name:		brightnessctl
Version:	0.5.1
Release:	1
Summary:	A program to read and control device brightness
Group:		Extra
License:	MIT
URL:		https://github.com/Hummer12007/brightnessctl
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(libsystemd)

%description
%{summary}


%prep
%autosetup
%build
export ENABLE_SYSTEMD=1
%set_build_flags
%make_build
%install
%make_install INSTALL_UDEV_RULES=0 ENABLE_SYSTEMD=1 PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
