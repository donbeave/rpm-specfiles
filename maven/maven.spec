Name:           maven
Version:        3.2.2
Release:        1.polusharie
Summary:        Apache Maven software project management and comprehension tool.
License:        Apache Software License
URL:            http://ant.apache.org/
Group:          Development/Build Tools
Source0:        apache-maven-%{version}-bin.tar.gz
Requires:       java-1.7.0-openjdk
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

%prep
%setup -q -n apache-maven-%{version}

%build

install -d -m 755 %{buildroot}/opt/%{name}
cp -R %{_builddir}/apache-maven-%{version}/* %{buildroot}/opt/%{name}/

# Make it the default, dawg.
install -d -m 755 %{buildroot}/etc/profile.d/
echo 'export MAVEN_HOME=/opt/%{name}' > %{buildroot}/etc/profile.d/%{name}.sh
echo 'export PATH=/opt/%{name}/bin:$PATH' >> %{buildroot}/etc/profile.d/%{name}.sh

%clean
rm -rf %{buildroot}

%post
echo
echo "You will need to exit your shell to have mvn in your default path."
echo "Or run the following"
echo '  export MAVEN_HOME=/opt/maven'
echo '  export PATH=/opt/maven/bin:$PATH'
echo

%files
/opt/%{name}/
/etc/profile.d/%{name}.sh

%changelog
* Sun Jun 30 2013 Nathan Milford <nathan@milford.io> - 3.0.5-1
- First go at it.
