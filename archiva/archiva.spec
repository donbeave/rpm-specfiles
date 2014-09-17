%undefine _missing_build_ids_terminate_build

%global _use_internal_dependency_generator 0

%define __os_install_post    \
    /usr/lib/rpm/redhat/brp-compress \
    %{!?__debug_package:/usr/lib/rpm/redhat/brp-strip %{__strip}} \
    /usr/lib/rpm/redhat/brp-strip-static-archive %{__strip} \
    /usr/lib/rpm/redhat/brp-strip-comment-note %{__strip} %{__objdump} \
%{nil}

%define archiva_home %{_sysconfdir}/archiva
%define archiva_user archiva
%define archiva_group archiva

Summary:        The Build Artifact Repository Manager
Name:           archiva
Version:        2.1.1
Release:        1%{?dist}.polusharie
Vendor:         Apache Software Foundation
URL:            http://archiva.apache.org

%if 0%{?rhel}  == 7
Group:          Development/Build Tools
Requires:	java-1.7.0-openjdk
%endif

Source0:        apache-archiva-%{version}-bin.tar.gz
Source1:        archiva.cassandra.properties
Source2:        archiva.xml
Source3:        archiva.jetty.xml
Source4:        archiva.shared.xml
Source5:        archiva.wrapper.conf
Source6:        archiva.context.xml
Source7:        archiva.init
Source8:        archiva.log4j2.xml

License:        Apache Software License

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Apache Archiva™ is an extensible repository management software that helps taking care of your own personal or enterprise-wide build artifact repository. It is the perfect companion for build tools such as Maven, Continuum, and ANT.

%prep
%setup -q -n apache-archiva-%{version}


%build
%{__rm} -f %{_builddir}/apache-archiva-%{version}/bin/wrapper-macosx*
%{__rm} -f %{_builddir}/apache-archiva-%{version}/bin/wrapper-solaris*
%{__rm} -f %{_builddir}/apache-archiva-%{version}/bin/wrapper-windows*
%{__rm} -f %{_builddir}/apache-archiva-%{version}/lib/libwrapper-macosx*
%{__rm} -f %{_builddir}/apache-archiva-%{version}/lib/libwrapper-solaris*
%{__rm} -f %{_builddir}/apache-archiva-%{version}/lib/wrapper-windows*

%ifarch x86_64
%{__rm} -f %{_builddir}/apache-archiva-%{version}/bin/wrapper-linux-x86-32
%else
%{__rm} -f %{_builddir}/apache-archiva-%{version}/bin/wrapper-linux-x86-64
%endif

%ifarch x86_64
%{__rm} -f %{_builddir}/apache-archiva-%{version}/lib/libwrapper-linux-x86-32.so
%else
%{__rm} -f %{_builddir}/apache-archiva-%{version}/lib/libwrapper-linux-x86-64.so
%endif

%{__rm} -f %{_builddir}/apache-archiva-%{version}/apps/archiva/WEB-INF/classes/log4j2.xml


%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/archiva/bin
%{__install} -m755 %{_builddir}/apache-archiva-%{version}/bin/wrapper* $RPM_BUILD_ROOT/%{_datadir}/archiva/bin/wrapper

%{__install} -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/archiva/lib
%{__install} -m755 %{_builddir}/apache-archiva-%{version}/lib/*.so $RPM_BUILD_ROOT/%{_datadir}/archiva/lib
%{__install} -m644 %{_builddir}/apache-archiva-%{version}/lib/*.jar $RPM_BUILD_ROOT/%{_datadir}/archiva/lib

%{__install} -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/archiva/webapps/
cp -R %{_builddir}/apache-archiva-%{version}/apps/archiva $RPM_BUILD_ROOT/%{_datadir}/archiva/webapps/
# remove executable bit recursively from files (not directories)
%{__chmod} -R -x+X $RPM_BUILD_ROOT/%{_datadir}/archiva/webapps

%{__install} -m644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/archiva/webapps/archiva/WEB-INF/classes/log4j2.xml

%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/log/archiva

%{__install} -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/archiva
%{__install} -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/archiva/cassandra.properties
%{__install} -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/archiva/archiva.xml
%{__install} -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/archiva/jetty.xml
%{__install} -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/archiva/shared.xml
%{__install} -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/archiva/wrapper.conf

%{__install} -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/archiva/contexts
%{__install} -m644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/archiva/contexts/archiva.xml

%{__install} -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
%{__install} -m755 %{SOURCE7} $RPM_BUILD_ROOT%{_initrddir}/archiva


%clean
rm -rf %{buildroot}


%files
%{_sysconfdir}/archiva/cassandra.properties
%{_sysconfdir}/archiva/archiva.xml
%{_sysconfdir}/archiva/jetty.xml
%{_sysconfdir}/archiva/shared.xml
%{_sysconfdir}/archiva/wrapper.conf
%{_sysconfdir}/archiva/contexts/archiva.xml
%{_initrddir}/archiva
%{_datadir}/archiva/bin/wrapper
%{_datadir}/archiva/lib/*.jar
%{_datadir}/archiva/lib/*.so
%{_datadir}/archiva/webapps/archiva


%pre
# Add the "archiva" user
getent group %{archiva_group} >/dev/null || groupadd -r %{archiva_group}
getent passwd %{archiva_user} >/dev/null || \
    useradd -r -g %{archiva_group} -s /sbin/nologin \
    -d %{archiva_home} -c "archiva user"  %{archiva_user}
exit 0


%post
# Register the nginx service
/sbin/chkconfig --add archiva

%{__mkdir} -p %{_localstatedir}/log/archiva
%{__chown} %{archiva_user}:%{archiva_group} %{_localstatedir}/log/archiva

%{__mkdir} -p %{_localstatedir}/lib/archiva/{temp,conf}
%{__chown} -R %{archiva_user}:%{archiva_group} %{_localstatedir}/lib/archiva

%{__mkdir} -p %{_localstatedir}/run/archiva
%{__chown} %{archiva_user}:%{archiva_group} %{_localstatedir}/run/archiva


%preun
if [ $1 -eq 0 ]; then
/sbin/service archiva stop > /dev/null 2>&1
/sbin/chkconfig --del archiva
fi
