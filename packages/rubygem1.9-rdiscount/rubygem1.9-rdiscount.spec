#-------------------------------------------------------------------------------
# rubygem1.9-rdiscount.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname rdiscount


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-rdiscount
Version:        2.1.7
Release:        1%{?dist}
Summary:        Fast Implementation of Gruber's Markdown in C

Group:          Development/Languages
License:        BSD
URL:            http://github.com/rtomayko/rdiscount
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Discount is an implementation of John Gruber's Markdown markup language in C.
It implements all of the language described in the markdown syntax document
and passes the Markdown 1.0 test suite.


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
  rm -rf BUILDING Rakefile ext test rdiscount.gemspec
  strip lib/*.so
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man{1,7}
cp %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/*.1 \
  %{buildroot}%{_mandir}/man1 && gzip %{buildroot}%{_mandir}/man1/*
cp %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/*.7 \
  %{buildroot}%{_mandir}/man7 && gzip %{buildroot}%{_mandir}/man7/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.markdown
%{_bindir}/*
%{_mandir}/man1/*.gz
%{_mandir}/man7/*.gz
%{ruby_sitelib}/bin/rdiscount
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/man


#-------------------------------------------------------------------------------
%changelog
* Sat Oct 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.1.7-1%{?dist}
- New upstream version

* Sun Jun 2 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.1.6-1%{?dist}
- New upstream version

* Fri May 10 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.7.3-1%{?dist}
- New upstream version

* Tue Apr 9 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.7.2-1%{?dist}
- New upstream version

* Mon Mar 4 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.7.1-1%{?dist}
- New upstream version

* Tue Feb 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.0.7-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.6.8-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.6.8-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.6.5-1%{?dist}
- Initial package creation
