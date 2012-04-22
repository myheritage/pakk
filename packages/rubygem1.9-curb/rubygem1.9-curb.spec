#-------------------------------------------------------------------------------
# rubygem1.9-curb.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname curb


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-curb
Version:        0.8.0
Release:        1%{?dist}
Summary:        Libcurl bindings for Ruby

Group:          Development/Languages
License:        Ruby
URL:            http://curb.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  curl-devel
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for
the libcurl(3), a fully-featured client-side URL transfer library.


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
  rm -rf .require_paths Rakefile doc.rb ext tasks tests
  strip lib/*.so
popd

pushd %{buildroot}%{ruby_sitelib}
  sed -i -e 's|%{buildroot}||g' \
    doc/%{gemname}-%{version}/rdoc/ext/Makefile.html
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.8.0-1%{?dist}
- New upstream version

* Mon Jan 9 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.7.17-1%{?dist}
- New upstream version

* Mon Mar 21 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.15-1%{?dist}
- New upstream version

* Fri Mar 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.14-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.10-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.10-1%{?dist}
- New upstream version

* Wed Dec 22 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.7.9-1%{?dist}
- New upstream version

* Fri Nov 26 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.7.8-1%{?dist}
- Initial package creation
