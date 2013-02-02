Summary:            Selenium Server (formerly the Selenium RC Server)
Name:               selenium-server
Version:            2.29.0
Release:            1
License:            ASL 2.0
Group:              Development/Tools
URL:                http://www.seleniumhq.org
Requires:           firefox,xorg-x11-server-Xvfb
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
mkdir -p %{buildroot}/%{_datadir}/selenium/lib
mv selenium-server-standalone-%{version}.jar %{buildroot}/%{_datadir}/selenium/lib
cd %{buildroot}/%{_datadir}/selenium/lib
ln -s selenium-server-standalone-%{version}.jar selenium-server-standalone.jar

%files
%defattr(-,root,root)
%{_datadir}/selenium/lib

%changelog
* Sat Feb 02 2012 Zhokhov Alexey <donbeave@gmail.com> - 2.29.0-1
- Initial version.
