#-------------------------------------------------------------------------------
# rubygem1.9-dm-sqlite-adapter.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname dm-sqlite-adapter


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-dm-sqlite-adapter
Version:        1.2.0
Release:        1%{?dist}
Summary:        Sqlite3 Adapter for DataMapper

Group:          Development/Languages
License:        MIT
URL:            http://github.com/datamapper/dm-sqlite-adapter
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-dm-do-adapter >= 1.2.0
Requires:       rubygem1.9-do_sqlite3 >= 0.10.6

%description
Sqlite3 Adapter for DataMapper.


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

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .gitignore Rakefile dm-sqlite-adapter.gemspec spec tasks
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Gemfile
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sun Oct 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- New upstream version

* Sat Mar 19 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.2-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.0.2-1%{?dist}
- Initial package creation
