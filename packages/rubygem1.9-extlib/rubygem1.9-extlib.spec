#-------------------------------------------------------------------------------
# rubygem1.9-extlib.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname extlib


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-extlib
Version:        0.9.16
Release:        1%{?dist}
Summary:        Support library for DataMapper and Merb

Group:          Development/Languages
License:        MIT
URL:            http://github.com/datamapper/extlib
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Support library for DataMapper and Merb.


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
  chmod 644 Rakefile lib/extlib/logger.rb
  rm -rf .autotest .document .gitignore extlib.gemspec spec tasks
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Rakefile
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Wed Jan 9 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.9.16-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.15-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.9.15-1%{?dist}
- Initial package creation
