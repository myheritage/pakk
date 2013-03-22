#-------------------------------------------------------------------------------
# rubygem1.9-activesupport.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname activesupport


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-activesupport
Version:        3.2.13
Release:        1%{?dist}
Summary:        Support libraries and Ruby core extensions from Rails

Group:          Development/Languages
License:        MIT
URL:            http://www.rubyonrails.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-i18n >= 0.6
Requires:       rubygem1.9-multi_json >= 1.0

%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.


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
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Fri Mar 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.13-1%{?dist}
- New upstream version

* Tue Feb 12 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.12-1%{?dist}
- New upstream version

* Wed Jan 9 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.11-1%{?dist}
- New upstream version

* Sun Jan 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.10-1%{?dist}
- New upstream version

* Thu Dec 13 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.2.9-1%{?dist}
- Initial package creation
