#-------------------------------------------------------------------------------
# rubygem1.9-rbtrace.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname rbtrace


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-rbtrace
Version:        0.4.1
Release:        1%{?dist}
Summary:        Like strace but for ruby code

Group:          Development/Languages
License:        Ruby
URL:            http://github.com/tmm1/rbtrace
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-ffi >= 1.0.6
Requires:       rubygem1.9-msgpack >= 0.4.3
Requires:       rubygem1.9-trollop >= 1.16.2

%description
rbtrace shows you method calls happening inside another ruby process in real
time.


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


%install
rm -rf %{buildroot}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CFLAGS="%{optflags}"
%ifarch i386
export CONFIGURE_ARGS="--with-cflags='%{optflags} -march=i686'"
export CFLAGS="%{optflags} -march=i686"
%endif
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .gitignore Gemfile* ext server.rb test.sh %{gemname}.gemspec
  strip lib/*.so
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/rbtrace %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/tracers
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Mar 11 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.4.1-1%{?dist}
- New upstream version

* Mon Mar 4 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.3.19-1%{?dist}
- New upstream version

* Fri Jan 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.3.18-1%{?dist}
- New upstream version

* Sat Mar 19 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.13-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.12-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.12-1%{?dist}
- New upstream version

* Tue Mar 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.11-1%{?dist}
- New upstream version

* Mon Feb 28 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.10-1%{?dist}
- New upstream version

* Wed Feb 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.8-1%{?dist}
- Initial package creation
