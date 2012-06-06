#-----------------------------------------------------------------------------
# python-whisper.spec
# dists: el6
#-----------------------------------------------------------------------------

%global upstream_name whisper


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           python-%{upstream_name}
Version:        0.9.10
Release:        1%{?dist}
Summary:        Fixed size round-robin style database

Group:          Applications/Databases
License:        ASL 2.0
URL:            https://launchpad.net/graphite
Source0:        http://launchpad.net/graphite/0.9/%{version}/+download/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python

%description
Fixed size round-robin style database.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{upstream_name}-%{version}


#-----------------------------------------------------------------------------
%build
%{__python} setup.py build


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

chmod 755 %{buildroot}%{python_sitelib}/whisper.py


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%{_bindir}/*
%{python_sitelib}/*


#-----------------------------------------------------------------------------
%changelog
* Sat Jun 2 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.10-1%{?dist}
- New upstream version

* Sun Apr 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.9-1%{?dist}
- Initial package creation
