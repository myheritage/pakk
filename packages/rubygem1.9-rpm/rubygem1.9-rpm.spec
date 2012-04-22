#-------------------------------------------------------------------------------
# rubygem1.9-rpm.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname ruby-rpm


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-rpm
Version:        1.3.1
Release:        1%{?dist}
Summary:        RPM bindings for ruby

Group:          Development/Languages
License:        GPLv2
URL:            http://www.gitorious.org/ruby-rpm
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  db4-devel
BuildRequires:  rpm-devel
BuildRequires:  ruby1.9-devel

Requires:       db4
Requires:       ruby1.9

%description
Ruby/RPM is an interface to access RPM database for Ruby.


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
# this is a bit convoluted but we need to patch a file in the gem before
# building it.
mkdir -p %{buildroot}
pushd %{buildroot}
  gem1.9 unpack %{SOURCE0}
  pushd %{gemname}-%{version}
    gem1.9 spec --ruby %{SOURCE0} > %{gemname}.gemspec
    sed -i -e 's/-Werror//g' ext/rpm/extconf.rb
    gem1.9 build %{gemname}.gemspec
    gem1.9 install --local \
      --install-dir %{buildroot}%{ruby_sitelib} \
      %{gemname}-%{version}.gem
    rm -rf %{buildroot}%{ruby_sitelib}/cache
  popd
  rm -rf %{gemname}-%{version}
popd

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf ext
  strip lib/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sun Jan 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.3.1-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- Initial package creation
