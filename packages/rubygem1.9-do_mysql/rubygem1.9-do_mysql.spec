#-------------------------------------------------------------------------------
# rubygem1.9-do_mysql.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname do_mysql


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-do_mysql
Version:        0.10.12
Release:        1%{?dist}
Summary:        DataObjects MySQL Driver

Group:          Development/Languages
License:        MIT
URL:            http://dataobjects.info
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  mysql-devel
BuildRequires:  ruby1.9-devel

Requires:       mysql
Requires:       ruby1.9
Requires:       rubygem1.9-data_objects = %{version}

%description
Implements the DataObjects API for MySQL.


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
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf Rakefile ext tasks spec
  strip lib/do_mysql/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog.markdown
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.markdown
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Jan 28 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.10.12-1%{?dist}
- New upstream version

* Sat Jan 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.10.11-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.10-1%{?dist}
- New upstream version

* Sun Feb 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- New upstream version

* Sun Oct 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.7-1%{?dist}
- New upstream version

* Wed May 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.6-1%{?dist}
- New upstream version

* Wed May 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.5-1%{?dist}
- New upstream version

* Sat Apr 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.4-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.3-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.3-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.10.2-1%{?dist}
- Initial package creation
