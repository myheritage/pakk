#-------------------------------------------------------------------------------
# rubygem1.9-msgpack.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname msgpack


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-msgpack
Version:        0.4.8
Release:        1%{?dist}
Summary:        Binary-based efficient data interchange format

Group:          Development/Languages
License:        ASL 2.0
URL:            http://msgpack.sourceforge.net/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
MessagePack, a binary-based efficient data interchange format.


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
  rm -rf ext msgpack test
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
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Dec 17 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.4.8-1%{?dist}
- New upstream version

* Sun May 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.4.7-1%{?dist}
- New upstream version

* Wed Aug 10 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.4.6-1%{?dist}
- New upstream version

* Mon May 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.4.5-1%{?dist}
- New upstream version

* Tue Mar 8 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.4.4-1%{?dist}
- Initial package creation
