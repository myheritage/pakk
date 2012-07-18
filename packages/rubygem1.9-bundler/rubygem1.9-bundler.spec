#-------------------------------------------------------------------------------
# rubygem1.9-bundler.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname bundler


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-bundler
Version:        1.1.5
Release:        1%{?dist}
Summary:        The best way to manage your application's dependencies

Group:          Development/Languages
License:        MIT
URL:            http://gembundler.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel
BuildRequires:  rubygem1.9-ronn

Requires:       ruby1.9

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

Requires:       %{name} = %{version}

%description doc
Documentation for %{name} in rdoc and ri format.


#-------------------------------------------------------------------------------
%install
rm -rf %{buildroot}
gem1.9 install --local \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .gitignore .travis.yml Rakefile %{gemname}.gemspec spec

  # let's make rpmlint happy
  find lib/bundler/vendor/ -name '*.rb' -exec chmod 644 {} \;
  chmod 755 lib/bundler/templates/newgem/bin/newgem.tt
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/bundle %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man{1,5}
pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man
  ronn -r *.ronn
  install -p -m 0644 *.1 %{buildroot}%{_mandir}/man1/ && gzip %{buildroot}%{_mandir}/man1/*
  install -p -m 0644 *.5 %{buildroot}%{_mandir}/man5/ && gzip %{buildroot}%{_mandir}/man5/*
  rm -f *.1 *.5
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ISSUES.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/UPGRADING.md
%{_bindir}/*
%{_mandir}/man1/*.gz
%{_mandir}/man5/*.gz
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/man


#-------------------------------------------------------------------------------
%changelog
* Wed Jul 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.5-1%{?dist}
- New upstream version

* Tue May 29 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.4-1%{?dist}
- New upstream version

* Sat Mar 24 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.3-1%{?dist}
- New upstream version

* Wed Mar 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.2-1%{?dist}
- New upstream version

* Sun Mar 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.1-1%{?dist}
- New upstream version

* Thu Mar 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.0-1%{?dist}
- New upstream version

* Sun Feb 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.22-1%{?dist}
- New upstream version

* Sat Oct 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.21-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.18-1%{?dist}
- New upstream version

* Wed Aug 10 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.17-1%{?dist}
- New upstream version

* Sat Jun 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.15-1%{?dist}
- New upstream version

* Sun May 29 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.14-1%{?dist}
- New upstream version

* Wed May 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.13-1%{?dist}
- New upstream version

* Sat Apr 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.12-1%{?dist}
- New upstream version

* Sat Apr 2 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.11-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.10-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.10-1%{?dist}
- Initial package creation
