#-------------------------------------------------------------------------------
# rubygem1.9-mysql2.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname mysql2


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-mysql2
Version:        0.3.11
Release:        1%{?dist}
Summary:        A simple, fast Mysql library for Ruby, binding to libmysql

Group:          Development/Languages
License:        MIT
URL:            http://github.com/brianmario/mysql2
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  mysql-devel
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
The Mysql2 gem is meant to serve the extremely common use-case of connecting,
querying and iterating on results. Some database libraries out there serve as
direct 1:1 mappings of the already complex C API's available.
This one is not.


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
  rm -rf .??* Gemfile Rakefile ext mysql2.gemspec spec tasks
  strip lib/mysql2/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/benchmark
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Wed Dec 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.11-1%{?dist}
- New upstream version

* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.10-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.7-1%{?dist}
- New upstream version

* Sat Jun 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.6-1%{?dist}
- New upstream version

* Sat Apr 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.2-1%{?dist}
- New upstream version

* Tue Mar 29 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.7-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.6-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Nov 2 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.2.6-1%{?dist}
- Initial package creation
