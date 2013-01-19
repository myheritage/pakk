#-------------------------------------------------------------------------------
# rubygem1.9-rack.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname rack


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-rack
Version:        1.4.4
Release:        1%{?dist}
Summary:        A modular Ruby webserver interface

Group:          Development/Languages
License:        MIT
URL:            http://rack.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
A modular Ruby webserver interface.


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
  chmod 755 bin/*
  rm -rf Rakefile rack.gemspec test
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/rackup %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/KNOWN-ISSUES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/SPEC
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/contrib
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/example


#-------------------------------------------------------------------------------
%changelog
* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.4.4-1%{?dist}
- New upstream version

* Mon Jan 7 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.4.3-1%{?dist}
- New upstream version

* Mon Jan 7 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.4.2-1%{?dist}
- New upstream version

* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.1-1%{?dist}
- New upstream version

* Sat Dec 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.0-1%{?dist}
- New upstream version

* Thu Oct 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.5-1%{?dist}
- New upstream version

* Sun Oct 2 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.4-1%{?dist}
- New upstream version

* Wed Sep 21 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.3-1%{?dist}
- New upstream version

* Sat Aug 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.2-1%{?dist}
- New upstream version

* Sat Jul 16 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.1-1%{?dist}
- New upstream version

* Sat Jun 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- New upstream version

* Wed May 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.3-1%{?dist}
- New upstream version

* Sun Mar 13 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.1-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.2.1-1%{?dist}
- Initial package creation
