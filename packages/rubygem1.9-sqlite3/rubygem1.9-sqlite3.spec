#-------------------------------------------------------------------------------
# rubygem1.9-sqlite3.spec
# dists: el6
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname sqlite3


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-sqlite3
Version:        1.3.5
Release:        1%{?dist}
Summary:        SQLite3 interface for Ruby

Group:          Development/Languages
License:        MIT
URL:            https://github.com/luislavena/sqlite3-ruby
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  sqlite-devel >= 3.6.16
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
This module allows Ruby programs to interface with the SQLite3 database
engine (www.sqlite.org).


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem1.9 install --local \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .??* Manifest.txt Rakefile ext setup.rb tasks test
  strip lib/sqlite3/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/API_CHANGES.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog.cvs
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/faq


#-------------------------------------------------------------------------------
%changelog
* Thu Apr 5 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.3.5-1%{?dist}
- Initial package creation
