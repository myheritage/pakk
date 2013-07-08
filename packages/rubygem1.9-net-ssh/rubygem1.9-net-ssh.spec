#-------------------------------------------------------------------------------
# rubygem1.9-net-ssh.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname net-ssh


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-net-ssh
Version:        2.6.8
Release:        1%{?dist}
Summary:        Pure-Ruby implementation of the SSH2 client protocol

Group:          Development/Languages
License:        MIT
URL:            http://github.com/net-ssh/net-ssh
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Net::SSH is a pure-Ruby implementation of the SSH2 client protocol. It allows
you to write programs that invoke and interact with processes on remote
servers, via SSH2.


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
  rm -rf *.gemspec *.pem Manifest Rakefile Rudyfile setup.rb test

  sed -i -e 's|/usr/bin/ruby|/usr/bin/ruby1.9|g' support/*
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGES.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/THANKS.txt
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/support
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Jul 8 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.6.8-1%{?dist}
- New upstream version

* Tue Apr 23 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.6.7-1%{?dist}
- New upstream version

* Mon Mar 4 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.6.6-1%{?dist}
- New upstream version

* Fri Feb 8 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.6.5-1%{?dist}
- New upstream version

* Sun Jan 13 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.6.3-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.6.2-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.6.1-1%{?dist}
- New upstream version

* Thu Sep 20 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.6.0-1%{?dist}
- New upstream version

* Sat Jun 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.5.2-1%{?dist}
- New upstream version

* Wed Jan 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.3.0-1%{?dist}
- New upstream version

* Fri Jan 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.2-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.1-1%{?dist}
- New upstream version

* Thu Apr 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.4-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.3-1%{?dist}
- Initial package creation
