#-------------------------------------------------------------------------------
# rubygem1.9-ronn.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname ronn


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-ronn
Version:        0.7.3
Release:        2%{?dist}
Summary:        Builds manuals

Group:          Development/Languages
License:        MIT
URL:            http://rtomayko.github.com/ronn
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-hpricot >= 0.8.2
Requires:       rubygem1.9-mustache >= 0.7.0
Requires:       rubygem1.9-rdiscount >= 1.5.8

%description
Ronn builds manuals. It converts simple, human readable textfiles to roff for
terminal display, and also to HTML for the web.

The source format includes all of Markdown but has a more rigid structure and
syntax extensions for features commonly found in manpages (definition lists,
link notation, etc.). The ronn-format(7) manual page defines the format in
detail.


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
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf INSTALLING Rakefile %{gemname}.gemspec test

  # let's make rpmlint happy
  chmod 644 lib/ronn.rb
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man{1,7}
install -p -m 0644 %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/*.1 \
  %{buildroot}%{_mandir}/man1/ && gzip %{buildroot}%{_mandir}/man1/*
install -p -m 0644 %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/*.7 \
  %{buildroot}%{_mandir}/man7/ && gzip %{buildroot}%{_mandir}/man7/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/AUTHORS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%{_bindir}/*
%{_mandir}/man1/*.gz
%{_mandir}/man7/*.gz
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/config.ru
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/man


#-------------------------------------------------------------------------------
%changelog
* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.3-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.3-1%{?dist}
- Initial package creation
