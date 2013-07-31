#-------------------------------------------------------------------------------
# rubygem1.9-ohai.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname ohai


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-ohai
Version:        6.18.0
Release:        1%{?dist}
Summary:        Profiles your system and emits JSON

Group:          Development/Languages
License:        ASL 2.0
URL:            http://wiki.opscode.com/display/ohai
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       dmidecode
Requires:       ruby1.9
Requires:       rubygem1.9-ipaddress
Requires:       rubygem1.9-mixlib-cli
Requires:       rubygem1.9-mixlib-config
Requires:       rubygem1.9-mixlib-log
Requires:       rubygem1.9-mixlib-shellout
Requires:       rubygem1.9-systemu
Requires:       rubygem1.9-yajl

%description
Ohai profiles your system and emits JSON.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

Requires:       %{name} = %{version}

%description doc
Documentation for %{name} in rdoc and ri format.


#-------------------------------------------------------------------------------
%install
rm -rf %{buildroot}
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf Rakefile spec
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/docs


#-------------------------------------------------------------------------------
%changelog
* Wed Jul 31 2013 Eric-Olivier Lamey <pakk@96b.it> - 6.18.0-1%{?dist}
- New upstream version

* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 6.16.0-1%{?dist}
- New upstream version

* Thu May 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 6.14.0-1%{?dist}
- New upstream version

* Fri Mar 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.12-1%{?dist}
- New upstream version

* Tue Jan 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.10-2%{?dist}
- Updated dependecy on net-ssh (rpm needs ~>)

* Sun Oct 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.10-1%{?dist}
- New upstream version

* Thu Oct 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.8-1%{?dist}
- New upstream version

* Tue Oct 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.6-1%{?dist}
- New upstream version

* Sat Apr 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.4-1%{?dist}
- New upstream version

* Tue Apr 19 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.5.8-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Mon Jan 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.5.8-1%{?dist}
- Initial package creation
