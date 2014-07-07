Summary:	A non-backtracking regex engine matching on data streams
Name:		sregex
Version:	0.0.1rc1
Release:	1.polusharie
License:	BSD
Group:		Libraries
Source0:	sregex-0.0.1rc1.tar.gz
# Source0-md5:	4ee5932468c308b7e7a3780f7550d713
URL:		https://github.com/openresty/sregex/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Packager:       Alexey Zhokhov <donbeave@gmail.com>

%description
This is a pure C library that is designed to have zero dependencies.

%package devel
Summary:	Header files for %{name} library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/%{_libdir}
rm $RPM_BUILD_ROOT/%{_includedir}/sregex/ddebug.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sregex-cli
%attr(755,root,root) %{_libdir}/libsregex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsregex.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsregex.so
%{_includedir}/sregex/sregex.h

%changelog
* Mon Jul 07 2014 Alexey Zhokhov <donbeave@gmail.com> - 0.0.1rc1-1.polusharie
- Initial version.
