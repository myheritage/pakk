#-------------------------------------------------------------------------------
# rubygem1.9-yajl.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname yajl-ruby


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-yajl
Version:        1.1.0
Release:        1%{?dist}
Summary:        Ruby C bindings to the excellent Yajl JSON stream-based parser library

Group:          Development/Languages
License:        MIT
URL:            http://github.com/brianmario/yajl-ruby
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
* JSON parsing and encoding directly to and from an IO stream (file, socket,
  etc) or String. Compressed stream parsing and encoding supported for Bzip2,
  Gzip and Deflate.
* Parse and encode *multiple* JSON objects to and from streams or strings
  continuously.
* JSON gem compatibility API - allows yajl-ruby to be used as a drop-in
  replacement for the JSON gem
* Basic HTTP client (only GET requests supported for now) which parses JSON
  directly off the response body *as it's being received*


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
  chmod -x benchmark/subjects/unicode.json
  rm -rf .??* Rakefile Gemfile* benchmark ext spec tasks yajl-ruby.gemspec
  strip lib/yajl/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1.0-1%{?dist}
- New upstream version

* Wed Sep 21 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.0-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.3-1%{?dist}
- New upstream version

* Sun Mar 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.1-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Feb 12 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.1-1%{?dist}
- New upstream version

* Thu Feb 3 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.0-1%{?dist}
- New upstream version

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.9-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.7.8-1%{?dist}
- Initial package creation
