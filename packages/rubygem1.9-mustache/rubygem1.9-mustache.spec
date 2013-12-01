#-------------------------------------------------------------------------------
# rubygem1.9-mustache.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname mustache


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-mustache
Version:        0.99.5
Release:        1%{?dist}
Summary:        Framework-agnostic way to render logic-free views

Group:          Development/Languages
License:        MIT
URL:            http://github.com/defunkt/mustache
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Inspired by ctemplate, Mustache is a framework-agnostic way to render
logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language.

Think of Mustache as a replacement for your views. Instead of views
consisting of ERB or HAML with random helpers and arbitrary logic,
your views are broken into two parts: a Ruby class and an HTML
template.


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
  rm -rf Rakefile test
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man{1,5}
install -p -m 0644 %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/*.1 \
  %{buildroot}%{_mandir}/man1/ && gzip %{buildroot}%{_mandir}/man1/*
install -p -m 0644 %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/*.5 \
  %{buildroot}%{_mandir}/man5/ && gzip %{buildroot}%{_mandir}/man5/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
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
* Tue Dec 3 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.99.5-1%{?dist}
- New upstream version

* Sun May 29 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.99.4-1%{?dist}
- New upstream version

* Sun Mar 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.99.3-1%{?dist}
- New upstream version

* Mon Mar 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.99.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.98.0-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Fri Feb 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.98.0-1%{?dist}
- New upstream version

* Wed Feb 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.12.1-1%{?dist}
- New upstream version

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.12.0-1%{?dist}
- Initial package creation
