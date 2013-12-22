#-------------------------------------------------------------------------------
# rubygem1.9-i18n.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname i18n


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-i18n
Version:        0.6.9
Release:        1%{?dist}
Summary:        New wave Internationalization support for Ruby

Group:          Development/Languages
License:        MIT
URL:            http://github.com/svenfuchs/i18n
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
New wave Internationalization support for Ruby.


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
  rm -rf ci test
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.textile
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sun Dec 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.6.9-1%{?dist}
- New upstream version

* Thu Aug 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.6.5-1%{?dist}
- New upstream version

* Mon Mar 4 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.6.4-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.6.2-1%{?dist}
- New upstream version

* Thu Dec 13 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.1-1%{?dist}
- Initial package creation
