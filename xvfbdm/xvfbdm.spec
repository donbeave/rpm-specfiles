%global             daemon xvfbdm

Summary:            A X Windows System virtual framebuffer X server.
Name:               xvfbdm
Version:            1.10
Release:            1.polusharie
License:            MIT and GPLv2
Group:              Development/Tools
URL:                http://www.x.org
Requires:           xorg-x11-server-Xvfb
Buildroot:          %{_tmppath}/%{name}-buildroot
Packager:           Zhokhov Alexey <donbeave@gmail.com>

%description
X virtual framebuffer is an X11 server that performs all graphical operations in memory, not showing any screen output.

%prep
%build
%install
wget https://raw.github.com/donbeave/rpm-specfiles/master/xvfbdm/etc/init.d/xvfbdm --no-check-certificate
install -p -D -m 755 xvfbdm %{buildroot}%{_initddir}/%{daemon}

%{__mkdir_p} %{buildroot}/%{_localstatedir}/log/xvfbdm

%files
%defattr(-,root,root)
%{_initddir}/%{daemon}
%{_localstatedir}/log/xvfbdm

%changelog
* Sat Feb 02 2012 Zhokhov Alexey <donbeave@gmail.com> - 1.10-1
- Initial version.
