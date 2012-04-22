#-------------------------------------------------------------------------------
# rubygem1.9-hoe.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname hoe


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-hoe
Version:        2.8.0
Release:        1%{?dist}
Summary:        Rubygems helper for project Rakefiles

Group:          Development/Languages
License:        MIT
URL:            http://rubyforge.org/projects/seattlerb/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage and
maintain, and release your project and includes a dynamic plug-in system
allowing for easy extensibility. Hoe ships with plug-ins for all your usual
project tasks including rdoc generation, testing, packaging, and deployment.


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
  rm -rf .autotest .gemtest Manifest.txt Rakefile test
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/sow %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/History.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.txt
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/template
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/Hoe.pdf


#-------------------------------------------------------------------------------
%changelog
* Mon Jun 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.8.0-1%{?dist}
- Initial package creation
