#-------------------------------------------------------------------------------
# rubygem1.9-shadow.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname    ruby-shadow


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-shadow
Version:        2.3.1
Release:        1%{?dist}
Summary:        Access to shadow passwords on Linux and Solaris

Group:          Development/Languages
License:        Ruby
URL:            https://github.com/apalmblad/ruby-shadow
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
This is the module which used when you access linux shadow password files.  
Recent versions work on both Linux and Solaris.


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
  rm -rf extconf.rb MANIFEST Makefile mkmf.log pwd shadow shadow.* *.gemspec
  strip lib/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/HISTORY
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.euc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Dec 3 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.3.1-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.2.0-1%{?dist}
- New upstream version

* Sun Apr 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.1.4-1%{?dist}
- New upstream version

* Sat Mar 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.1.git134f2d-1%{?dist}
- Initial package creation
