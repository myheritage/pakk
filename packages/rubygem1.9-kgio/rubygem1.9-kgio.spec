#-------------------------------------------------------------------------------
# rubygem1.9-kgio.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname kgio


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-kgio
Version:        2.9.0
Release:        1%{?dist}
Summary:        Kinder, gentler I/O for Ruby

Group:          Development/Languages
License:        LGPLv2
URL:            http://unicorn.bogomips.org/kgio/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
kgio provides non-blocking I/O methods for Ruby without raising
exceptions on EAGAIN and EINPROGRESS.  It is intended for use with the
Unicorn and Rainbows! Rack servers, but may be used by other
applications.


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
  rm -rf .document .gitignore .manifest .require_paths .wrongdoc.yml \
         GIT-VERSION-FILE GIT-VERSION-GEN GNUmakefile LATEST \
         Rakefile ext kgio.gemspec pkg.mk setup.rb \
         test
  strip lib/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/HACKING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ISSUES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/NEWS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/TODO
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Feb 4 2014 Eric-Olivier Lamey <pakk@96b.it> - 2.9.0-1%{?dist}
- New upstream version

* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.8.0-1%{?dist}
- New upstream version

* Sun Mar 24 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.7.4-1%{?dist}
- New upstream version

* Sun Mar 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.7.3-1%{?dist}
- New upstream version

* Tue Jan 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.7.2-1%{?dist}
- New upstream version

* Sat Dec 17 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.7.0-1%{?dist}
- New upstream version

* Sat Jul 16 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.6.0-1%{?dist}
- New upstream version

* Wed Jun 22 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.5.0-1%{?dist}
- New upstream version

* Sat Jun 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.4.2-1%{?dist}
- New upstream version

* Sun May 22 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.4.1-1%{?dist}
- New upstream version

* Sat May 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.4.0-1%{?dist}
- New upstream version

* Sat Mar 19 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.3.3-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.3.2-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Feb 15 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.3.2-1%{?dist}
- New upstream version

* Mon Feb 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.3.1-1%{?dist}
- New upstream version

* Wed Feb 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.3.0-1%{?dist}
- New upstream version

* Fri Feb 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.0-1%{?dist}
- New upstream version

* Mon Dec 27 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.1.1-1%{?dist}
- New upstream version

* Fri Nov 19 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.0.0-1%{?dist}
- New upstream version

* Thu Oct 28 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.3.1-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- Initial package creation
