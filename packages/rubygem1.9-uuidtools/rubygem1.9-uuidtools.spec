#-------------------------------------------------------------------------------
# rubygem1.9-uuidtools.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname uuidtools


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-uuidtools
Version:        2.1.4
Release:        1%{?dist}
Summary:        Simple universally unique ID generation library

Group:          Development/Languages
License:        MIT
URL:            http://uuditools.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
UUIDTools was designed to be a simple library for generating any
of the various types of UUIDs.  It conforms to RFC 4122 whenever
possible.


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
  rm -rf Gemfile* Rakefile spec tasks website
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Apr 29 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.1.4-1%{?dist}
- New upstream version

* Wed Jul 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.1.3-2%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.2-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Thu Feb 3 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.2-1%{?dist}
- New upstream version

* Mon Jan 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.1-1%{?dist}
- Initial package creation
