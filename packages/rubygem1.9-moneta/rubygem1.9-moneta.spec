#-------------------------------------------------------------------------------
# rubygem1.9-moneta.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname moneta


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-moneta
Version:        0.7.14
Release:        1%{?dist}
Summary:        Unified interface to key/value stores

Group:          Development/Languages
License:        MIT
URL:            http://www.yehudakatz.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
A unified interface to key/value stores.


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
  rm -rf .??* Gemfile Rakefile SPEC.md *.gemspec benchmarks script spec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Fri Feb 8 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.14-1%{?dist}
- New upstream version

* Tue Feb 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.12-1%{?dist}
- New upstream version

* Sun Jan 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.8-1%{?dist}
- New upstream version

* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.6-1%{?dist}
- New upstream version

* Mon Jan 7 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.5-1%{?dist}
- New upstream version

* Sat Jan 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.4-1%{?dist}
- New upstream version

* Sat Dec 29 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.7.2-1%{?dist}
- New upstream version

* Tue Dec 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.7.1-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.0-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Mon Jan 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.0-1%{?dist}
- Initial package creation
