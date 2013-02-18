#-------------------------------------------------------------------------------
# rubygem1.9-haml.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname haml


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-haml
Version:        3.1.8
Release:        1%{?dist}
Summary:        Elegant, structured XHTML/XML templating engine

Group:          Development/Languages
License:        MIT
URL:            http://haml-lang.com/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or XML
that's designed to express the structure of XHTML or XML documents in a
non-repetitive, elegant, easy way, using indentation rather than closing tags
and allowing Ruby to be embedded with ease. It was originally envisioned as
a plugin for Ruby on Rails, but it can function as a stand-alone templating
engine.


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
  chmod 755 vendor/sass/bin/* vendor/sass/lib/sass/*.rb
  rm -rf .yardopts Rakefile test vendor/sass/test vendor/sass/vendor/fssm/spec
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} \
  %{ruby_sitelib}/bin/html2haml \
  %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CONTRIBUTING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/REVISION
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION_NAME
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/rails
%{ruby_sitelib}/gems/%{gemname}-%{version}/vendor
%{ruby_sitelib}/gems/%{gemname}-%{version}/init.rb
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/extra


#-------------------------------------------------------------------------------
%changelog
* Mon Feb 18 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.1.8-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.1.7-1%{?dist}
- New upstream version

* Sat May 19 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.1.6-1%{?dist}
- New upstream version

* Wed May 9 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.1.5-1%{?dist}
- New upstream version

* Sun Jan 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.1.4-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.0.25-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.0.25-1%{?dist}
- Initial package creation
