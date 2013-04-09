#-------------------------------------------------------------------------------
# rubygem1.9-pg.spec
# dists: el6
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname pg


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-pg
Version:        0.15.1
Release:        1%{?dist}
Summary:        Ruby interface to PostgreSQL RDBMS

Group:          Development/Languages
License:        Ruby
URL:            http://bitbucket.org/ged/ruby-pg/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  postgresql-devel
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
This is the extension library to access a PostgreSQL database from Ruby. This
library works with PostgreSQL 7.4 and later.


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
  rm -rf .??* Rakefile* Manifest* ext misc rake sample spec
  sed -i -e '1,2d' lib/pg.rb
  sed -i -e '/rake-compiler/d' ../../specifications/*
  strip lib/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/BSDL
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Contributors.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/History.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/POSTGRES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.ja.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README-OS_X.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README-Windows.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Apr 9 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.15.1-1%{?dist}
- New upstream version

* Wed Mar 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.15.0-1%{?dist}
- New upstream version

* Sun Sep 9 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.14.1-1%{?dist}
- New upstream version

* Wed Jun 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.14.0-1%{?dist}
- New upstream version

* Fri Apr 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.13.2-1%{?dist}
- New upstream version

* Thu Feb 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.13.1-1%{?dist}
- New upstream version

* Sun Feb 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.13.0-1%{?dist}
- New upstream version

* Fri Jan 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.12.2-1%{?dist}
- New upstream version

* Sun Dec 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.12.0-1%{?dist}
- New upstream version

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.11.0-1%{?dist}
- New upstream version

* Fri Apr 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.1-3%{?dist}
- Builds against postgresql-devel instead of postgresql84-devel

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.1-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.1-1%{?dist}
- New upstream version

* Thu Dec 2 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.10.0-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.9.0-1%{?dist}
- Initial package creation
