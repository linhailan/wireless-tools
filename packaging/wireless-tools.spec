Name:           wireless-tools
Version:        29
Release:        0
License:        GPL-2.0+
Summary:        CLI configuration utility for wireless devices
Url:            https://hewlettpackard.github.io/wireless-tools/wireless_tools.29.tar.gz
Group:          Network & Connectivity/test
Source0:        %{name}-%{version}.tar.gz

%description
Wireless tools for Linux is a collection of user-space utilities written for
Linux kernel-based operating systems to support and facilitate the
configuration of device drivers of wireless network interface controllers and
some related aspects of networking using the Linux Wireless Extension.

%prep
%setup -q

%build
make

%install
make install PREFIX=%{buildroot}/usr

%post

%preun

%postun

%files
%manifest wireless-tools.manifest
%attr(500,root,root) %{_sbindir}/*
%attr(500,root,root) %{_libdir}/*
%attr(500,root,root) %{_includedir}/*
%attr(400,root,root) /usr/man/*
%license COPYING
