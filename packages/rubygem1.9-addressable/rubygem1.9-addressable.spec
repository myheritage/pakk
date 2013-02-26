#-------------------------------------------------------------------------------
# rubygem1.9-addressable.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname addressable


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-addressable
Version:        2.3.3
Release:        1%{?dist}
Summary:        URI Implementation

Group:          Development/Languages
License:        MIT
URL:            http://addressable.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to the relevant RFCs and
adds support for IRIs and URI templates.


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
  rm -rf Gemfile* Rakefile spec tasks website
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/data
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.3.3-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.3.2-1%{?dist}
- New upstream version

* Sun Jul 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.3.1-1%{?dist}
- New upstream version

* Thu May 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.8-1%{?dist}
- New upstream version

* Thu Feb 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.7-1%{?dist}
- New upstream version

* Sat May 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.6-1%{?dist}
- New upstream version

* Sun Apr 10 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.5-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.4-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.4-1%{?dist}
- New upstream version

* Wed Oct 13 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.2.2-1%{?dist}
- New upstream version

* Sat Oct 9 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.2.1-1%{?dist}
- Initial package creation
