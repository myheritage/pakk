#-------------------------------------------------------------------------------
# rubygem1.9-amq-protocol.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname amq-protocol


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-amq-protocol
Version:        1.5.0
Release:        1%{?dist}
Summary:        AMQP 0.9.1 serialization library for Ruby

Group:          Development/Languages
License:        Ruby
URL:            https://github.com/ruby-amqp/amq-protocol
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
amq-protocol is an AMQP 0.9.1 serialization library for Ruby. It is not an
AMQP client: amq-protocol only handles serialization and deserialization.
If you want to write your own AMQP client, this gem can help you with that.


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
  rm -rf .??* Gemfile Rakefile *.gemspec *.json *.py{,c,o,template} *.rb bin codegen spec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/PROFILING.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Fri May 10 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.5.0-1%{?dist}
- New upstream version

* Thu May 2 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.4.0-1%{?dist}
- New upstream version

* Thu Apr 11 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- New upstream version

* Fri Feb 15 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- New upstream version

* Sun Jan 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.1.0-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.1-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.5-1%{?dist}
- New upstream version

* Sun Jul 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.4-1%{?dist}
- New upstream version

* Wed Jun 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.3-1%{?dist}
- New upstream version

* Wed Jan 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.0-1%{?dist}
- New upstream version

* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.4-1%{?dist}
- New upstream version

* Thu Oct 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.3-1%{?dist}
- New upstream version

* Sun Sep 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.0-1%{?dist}
- Initial package creation
