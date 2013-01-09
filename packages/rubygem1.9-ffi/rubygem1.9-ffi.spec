#-------------------------------------------------------------------------------
# rubygem1.9-ffi.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname ffi


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-ffi
Version:        1.3.0
Release:        1%{?dist}
Summary:        Ruby extension for programmatically loading dynamic libraries

Group:          Development/Languages
License:        LGPL
URL:            http://wiki.github.com/ffi/ffi
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libffi-devel
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here: http://wiki.github.com/ffi/ffi/why-use-ffi.


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
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .??* *.gemspec Rakefile ext gen libtest spec tasks
  strip lib/*.so
popd

pushd %{buildroot}%{ruby_sitelib}
  find doc/%{gemname}-%{version} -name Makefile.html -exec \
    sed -i -e 's|%{buildroot}||g' {} \;
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/History.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING.LESSER
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Wed Jan 9 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.5-1%{?dist}
- New upstream version

* Wed Jul 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.1.0-1%{?dist}
- New upstream version

* Mon Nov 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.11-1%{?dist}
- New upstream version

* Thu Oct 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.10-1%{?dist}
- New upstream version

* Sun May 22 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.9-1%{?dist}
- New upstream version

* Sun May 15 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.8-1%{?dist}
- New upstream version

* Sat Mar 19 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.7-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.6-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Wed Feb 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.6-1%{?dist}
- Initial package creation
