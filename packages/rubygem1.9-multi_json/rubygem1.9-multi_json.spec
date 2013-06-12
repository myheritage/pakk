#-------------------------------------------------------------------------------
# rubygem1.9-multi_json.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname multi_json


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-multi_json
Version:        1.7.7
Release:        1%{?dist}
Summary:        A gem to provide swappable JSON backends

Group:          Development/Languages
License:        MIT
URL:            http://github.com/intridea/multi_json
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
A gem to provide easy switching between different JSON backends, including
Oj, Yajl, the JSON gem (with C-extensions), the pure-Ruby JSON gem, and
OkJson.


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
  rm -rf .??* Gemfile Rakefile spec *.gemspec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CONTRIBUTING.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sat Jun 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.7-1%{?dist}
- New upstream version

* Mon Jun 10 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.6-1%{?dist}
- New upstream version

* Sun Jun 2 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.5-1%{?dist}
- New upstream version

* Mon May 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.4-1%{?dist}
- New upstream version

* Fri May 10 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.3-1%{?dist}
- New upstream version

* Tue Mar 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.2-1%{?dist}
- New upstream version

* Fri Mar 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.1-1%{?dist}
- New upstream version

* Mon Mar 15 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.0-1%{?dist}
- New upstream version

* Fri Feb 15 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.6.1-1%{?dist}
- New upstream version

* Thu Feb 12 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.5.1-1%{?dist}
- New upstream version

* Thu Dec 13 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.5.0-1%{?dist}
- Initial package creation
