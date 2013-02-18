#-------------------------------------------------------------------------------
# rubygem1.9-libxml.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname libxml-ruby


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-libxml
Version:        2.6.0
Release:        1%{?dist}
Summary:        Ruby language bindings for GNOME's Libxml2

Group:          Development/Languages
License:        MIT
URL:            http://libxml.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libxml2-devel
BuildRequires:  ruby1.9-devel
BuildRequires:  zlib-devel

Requires:       ruby1.9

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME
Libxml2 XML toolkit. It is free software, released under the MIT License.
Libxml-ruby's primary advantage over REXML is performance - if speed
is your need, these are good libraries to consider.


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
  rm -rf .require_paths MANIFEST Rakefile ext libxml-ruby.gemspec setup.rb script test
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
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Feb 18 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.6.0-1%{?dist}
- New upstream version

* Sun Jan 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.5.0-1%{?dist}
- New upstream version

* Sun Dec 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.4.0-1%{?dist}
- New upstream version

* Mon Jul 2 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.3.3-1%{?dist}
- New upstream version

* Tue Mar 20 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.3.2-1%{?dist}
- New upstream version

* Wed Aug 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.2-1%{?dist}
- New upstream version

* Sun Aug 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.1-1%{?dist}
- New upstream version

* Wed Aug 10 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.0-1%{?dist}
- New upstream version

* Sat Aug 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.2-1%{?dist}
- New upstream version

* Sun Jun 26 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.0.9-1%{?dist}
- New upstream version

* Wed May 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.0.6-1%{?dist}
- New upstream version

* Sat May 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.0.5-1%{?dist}
- New upstream version

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.0.2-1%{?dist}
- New upstream version

* Sun Apr 17 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.0.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1.4-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.1.4-1%{?dist}
- Initial package creation
