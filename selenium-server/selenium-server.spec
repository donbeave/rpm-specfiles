%global             daemon selenium

Summary:            Selenium Server (formerly the Selenium RC Server)
Name:               selenium-server
Version:            2.29.0
Release:            1.polusharie
License:            ASL 2.0
Group:              Development/Tools
URL:                http://www.seleniumhq.org
Requires:           firefox,xvfbdm
BuildArch:          noarch
Buildroot:          %{_tmppath}/%{name}-buildroot
Packager:           Zhokhov Alexey <donbeave@gmail.com>

%description
The Selenium Server is needed in order to run either Selenium RC style scripts or Remote Selenium Webdriver ones. The 2.x server is a drop-in replacement for the old Selenium RC server and is designed to be backwards compatible with your existing infrastructure.

%prep
%build
%install
if [ ! -f selenium-server-standalone-%{version}.jar ];
then
    wget http://selenium.googlecode.com/files/selenium-server-standalone-%{version}.jar
fi
%{__mkdir_p} %{buildroot}/%{_datadir}/selenium/lib
install -p -D -m 644 selenium-server-standalone-%{version}.jar %{buildroot}/%{_datadir}/selenium/lib

wget https://raw.github.com/donbeave/rpm-specfiles/master/selenium-server/etc/init.d/selenium --no-check-certificate
install -p -D -m 755 selenium %{buildroot}%{_initddir}/%{daemon}

%{__mkdir_p} %{buildroot}/%{_localstatedir}/log/selenium

cd %{buildroot}/%{_datadir}/selenium/lib
%{__ln_s} selenium-server-standalone-%{version}.jar selenium-server-standalone.jar

%files
%defattr(-,root,root)
%{_initddir}/%{daemon}
%{_datadir}/selenium/lib
%{_localstatedir}/log/selenium

%changelog
* Sat Feb 02 2012 Zhokhov Alexey <donbeave@gmail.com> - 2.29.0-1
- Initial version.
