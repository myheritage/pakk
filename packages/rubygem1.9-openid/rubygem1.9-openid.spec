#-------------------------------------------------------------------------------
# rubygem1.9-openid.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname ruby-openid


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-openid
Version:        2.4.0
Release:        1%{?dist}
Summary:        Library for consuming and serving OpenID identities

Group:          Development/Languages
License:        Ruby
URL:            http://github.com/openid/ruby-openid
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
A library for consuming and serving OpenID identities.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

Requires:       %{name} = %{version}

%description doc
Documentation for %{name} in rdoc and ri format.


#-------------------------------------------------------------------------------
%install
rm -rf %{buildroot}
gem1.9 install --local \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf INSTALL.md UPGRADE.md admin test
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/NOTICE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Tue Jan 28 2014 Eric-Olivier Lamey <pakk@96b.it> - 2.4.0-1%{?dist}
- New upstream version

* Fri Feb 15 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.2.3-1%{?dist}
- New upstream version

* Wed Oct 24 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.2-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.1-1%{?dist}
- New upstream version

* Sun Jul 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.8-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.8-1%{?dist}
- Initial package creation
