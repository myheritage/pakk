#-------------------------------------------------------------------------------
# rubygem1.9-oj.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname oj


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-oj
Version:        2.0.13
Release:        1%{?dist}
Summary:        A fast JSON parser and serializer

Group:          Development/Languages
License:        MIT
URL:            http://www.ohler.com/oj
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Optimized JSON (Oj), as the name implies was written to provide speed
optimized JSON handling. It was designed as a faster alternative to Yajl and
other the common Ruby JSON parsers. So far is has achieved that at about 2
times faster than Yajl for parsing and 3 or more times faster writing JSON.


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
  rm -rf ext test
  strip lib/*.so
popd

pushd %{buildroot}%{ruby_sitelib}
  rm -rf doc/%{gemname}-%{version}/rdoc/ext
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sun May 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.13-1%{?dist}
- New upstream version

* Mon Apr 29 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.12-1%{?dist}
- New upstream version

* Mon Mar 11 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.10-1%{?dist}
- New upstream version

* Tue Mar 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.9-1%{?dist}
- New upstream version

* Mon Mar 4 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.8-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.7-1%{?dist}
- New upstream version

* Mon Feb 18 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.5-1%{?dist}
- New upstream version

* Tue Feb 12 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.4-1%{?dist}
- New upstream version

* Tue Feb 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.3-1%{?dist}
- New upstream version

* Sun Jan 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.2-1%{?dist}
- New upstream version

* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.1-1%{?dist}
- New upstream version

* Wed Dec 19 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.0.0-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.7-1%{?dist}
- New upstream version

* Thu Nov 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.4-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.3-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.3.4-1%{?dist}
- New upstream version

* Wed Jul 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- New upstream version

* Sun Jul 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.13-1%{?dist}
- New upstream version

* Sat Jun 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.11-1%{?dist}
- New upstream version

* Tue May 29 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.9-1%{?dist}
- New upstream version

* Thu May 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.8-1%{?dist}
- New upstream version

* Sun Apr 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.7-1%{?dist}
- New upstream version

* Wed Apr 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.5-1%{?dist}
- Initial package creation
