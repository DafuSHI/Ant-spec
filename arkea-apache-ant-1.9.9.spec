%define _prefix /opt

Name:			arkea-apache-ant
Version:		1.9.9
Release:		1
Summary:		Arkea Apache Ant
License:		Apache
Source:			arkea-apache-ant-1.9.9.zip
BuildArch:		noarch


%description
%{summary}
%
%prep
%setup -q

%build
#Since no install make, here we don't write anything

%install
ls
mkdir -p %{buildroot}%{_prefix}
cp -r apache-ant-%{version} %{buildroot}%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,users,-)
%{_prefix}/apache-ant-1.9.9

