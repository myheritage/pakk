#-------------------------------------------------------------------------------
# rubygem1.9-mixlib-cli.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname mixlib-cli


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-mixlib-cli
Version:        1.4.0
Release:        1%{?dist}
Summary:        Simple mixin for CLI interfaces, including option parsing

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
A simple mixin for CLI interfaces, including option parsing.


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
  rm -rf .gitignore Rakefile features spec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/NOTICE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sat Dec 28 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.4.0-1%{?dist}
- New upstream version

* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- New upstream version

* Fri Sep 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Mon Jan 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- Initial package creation
