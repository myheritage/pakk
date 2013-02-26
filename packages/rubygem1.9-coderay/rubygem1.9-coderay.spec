#-------------------------------------------------------------------------------
# rubygem1.9-coderay.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname coderay


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-coderay
Version:        1.0.9
Release:        1%{?dist}
Summary:        Fast syntax highlighting for selected languages

Group:          Development/Languages
License:        GPLv2+
URL:            http://coderay.rubychan.de
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Fast and easy syntax highlighting for selected languages, written in Ruby.


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
  rm -rf FOLDERS Rakefile test
  chmod 644 lib/coderay/token_kinds.rb
  sed -i -e '1d' lib/coderay/helpers/file_type.rb
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} \
  %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README_INDEX.rdoc
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.0.9-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.8-1%{?dist}
- New upstream version

* Wed Jun 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.7-1%{?dist}
- New upstream version

* Fri Apr 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.6-1%{?dist}
- New upstream version

* Sat Dec 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.5-1%{?dist}
- New upstream version

* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.4-1%{?dist}
- New upstream version

* Thu Oct 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.3-1%{?dist}
- New upstream version

* Thu Oct 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.1-1%{?dist}
- New upstream version

* Wed Sep 21 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.0-1%{?dist}
- New upstream version

* Sun May 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.8-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.7-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.7-1%{?dist}
- Initial package creation
