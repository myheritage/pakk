#-------------------------------------------------------------------------------
# rubygem1.9-amqp.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname amqp


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-amqp
Version:        0.9.10
Release:        1%{?dist}
Summary:        Implementation of the AMQP protocol in Ruby/EventMachine

Group:          Development/Languages
License:        Ruby
URL:            https://github.com/ruby-amqp/amqp
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-amq-client >= 0.9.12
Requires:       rubygem1.9-amq-protocol >= 1.2.0
Requires:       rubygem1.9-eventmachine

%description
This gem is a widely used, feature-rich asynchronous Ruby AMQP client built
on top of EventMachine.


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
  rm -rf .??* Gemfile Rakefile *.gemspec bin gemfiles spec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/docs
%{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Mon Mar 11 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.9.10-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.9.9-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.8-1%{?dist}
- New upstream version

* Wed Jun 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.6-1%{?dist}
- New upstream version

* Thu Feb 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.4-1%{?dist}
- New upstream version

* Sun Feb 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.3-1%{?dist}
- New upstream version

* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.2-1%{?dist}
- New upstream version

* Wed Jan 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.0-1%{?dist}
- New upstream version

* Wed Dec 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.4-1%{?dist}
- New upstream version

* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.3-1%{?dist}
- New upstream version

* Thu Oct 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.1-1%{?dist}
- New upstream version

* Wed Aug 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.5-1%{?dist}
- New upstream version

* Mon Jul 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.4-1%{?dist}
- New upstream version

* Mon Apr 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.1-1%{?dist}
- Initial package creation
