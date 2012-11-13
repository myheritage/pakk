#-------------------------------------------------------------------------------
# rubygem1.9-chef.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname   chef
%global username  %{gemname}
%global groupname %{gemname}


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-chef
Version:        10.16.2
Release:        2%{?dist}
Summary:        Configuration management tool (rubygem)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}-client.rb
Source2:        %{name}-solo.rb
Source3:        %{name}-client.init
Source4:        %{name}-client.sysconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       chef-common = %{version}
Requires:       initscripts
Requires:       ruby1.9
Requires:       rubygem1.9-bunny < 0.8.0
Requires:       rubygem1.9-erubis
Requires:       rubygem1.9-highline >= 1.6.9
Requires:       rubygem1.9-json <= 1.6.1
Requires:       rubygem1.9-net-ssh = 2.2.2
Requires:       rubygem1.9-net-ssh-multi >= 1.1
Requires:       rubygem1.9-mixlib-authentication >= 1.3.0
Requires:       rubygem1.9-mixlib-cli >= 1.1.0
Requires:       rubygem1.9-mixlib-config >= 1.1.2
Requires:       rubygem1.9-mixlib-log >= 1.3.0
Requires:       rubygem1.9-mixlib-shellout
Requires:       rubygem1.9-moneta
Requires:       rubygem1.9-ohai >= 0.6.0
Requires:       rubygem1.9-rest-client < 1.7.0
Requires:       rubygem1.9-treetop >= 1.4.9
Requires:       rubygem1.9-uuidtools
Requires:       rubygem1.9-yajl >= 1.1.0
Requires:       shadow-utils

%description
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.

This package contains the rubygem code. If you need to run chef-client
as a daemon, please install the "chef-client" package.


#-----------------------------------------------------------------------------
# chef-common package
#-----------------------------------------------------------------------------
%package -n chef-common
Summary:        Common package for Chef
Group:          Development/Languages

%description -n chef-common
Common files and directories for the client and server components of Chef.


#-----------------------------------------------------------------------------
# chef-client package
#-----------------------------------------------------------------------------
%package -n chef-client
Summary:        Configuration management tool
Group:          System Environment/Daemons

Requires:       %{name} = %{version}
Requires:       rubygem1.9-shadow

%description -n chef-client
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


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

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/chef-client \
  %{ruby_sitelib}/bin/chef-solo \
  %{ruby_sitelib}/bin/knife \
  %{ruby_sitelib}/bin/shef \
   %{buildroot}%{_bindir}/

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf Rakefile spec tasks
  sed -i -e 's|ruby -c|ruby1.9 -c|g' lib/chef/cookbook/syntax_check.rb
popd

mkdir -p %{buildroot}%{_sysconfdir}/chef
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/chef/client.rb
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/chef/solo.rb

mkdir -p %{buildroot}%{_initrddir}
install -p -m 0755 %{SOURCE3} %{buildroot}%{_initrddir}/chef-client
mkdir -p %{buildroot}%{_sysconfdir}/{sysconfig,logrotate.d}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/chef-client
install -p -m 0644 \
  %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/distro/redhat/etc/logrotate.d/chef-client \
  %{buildroot}%{_sysconfdir}/logrotate.d
sed -i -e 's|12|4|g' %{buildroot}%{_sysconfdir}/logrotate.d/chef-client

mkdir -p %{buildroot}%{_localstatedir}/{cache,lib,log,run}/chef
mkdir -p %{buildroot}%{_localstatedir}/{cache,lib}/chef/client

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 \
  %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/distro/common/man/man1/*.1 \
  %{buildroot}%{_mandir}/man1 \
  && gzip %{buildroot}%{_mandir}/man1/*
mkdir -p %{buildroot}%{_mandir}/man8
install -p -m 0644 \
  %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/distro/common/man/man8/chef-client.8 \
  %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/distro/common/man/man8/chef-solo.8 \
  %{buildroot}%{_mandir}/man8 \
  && gzip %{buildroot}%{_mandir}/man8/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%pre -n chef-common
if [ $1 == 1 ]; then
  /usr/bin/getent group %{groupname} > /dev/null || \
    /usr/sbin/groupadd -r %{groupname}
  /usr/bin/getent passwd %{username} > /dev/null || \
    /usr/sbin/useradd -g %{groupname} -c %{gemname} -s /sbin/nologin \
    -r -M -d %{_localstatedir}/lib/%{gemname} %{username}
fi

%post -n chef-client
if [ $1 == 1 ]; then
  /sbin/chkconfig --add chef-client
fi

%preun -n chef-client
if [ $1 = 0 ]; then
  /sbin/service chef-client stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del chef-client
fi

%postun -n chef-client
if [ $1 == 2 ]; then
  /sbin/service chef-client try-restart || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%{_bindir}/*
%{_mandir}/man1/*.gz
%{_mandir}/man8/*.gz
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n chef-common
%attr(0750, %{username}, %{groupname}) %dir %{_sysconfdir}/chef
%attr(0750, %{username}, %{groupname}) %dir %{_localstatedir}/cache/chef
%attr(0750, %{username}, %{groupname}) %dir %{_localstatedir}/lib/chef
%attr(-, %{username}, %{groupname}) %dir %{_localstatedir}/log/chef
%attr(-, %{username}, %{groupname}) %dir %{_localstatedir}/run/chef

%files -n chef-client
%config(noreplace) %{_sysconfdir}/chef/client.rb
%config(noreplace) %{_sysconfdir}/chef/solo.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-client
%config(noreplace) %{_sysconfdir}/sysconfig/chef-client
%{_initrddir}/chef-client
%attr(0750, root, root) %dir %{_localstatedir}/cache/chef/client
%attr(0750, root, root) %dir %{_localstatedir}/lib/chef/client

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/distro


#-------------------------------------------------------------------------------
%changelog
* Tue Nov 13 2012 Eric-Olivier Lamey <pakk@96b.it> - 10.16.2-2%{?dist}
- Fixed bunny dependency

* Tue Oct 30 2012 Eric-Olivier Lamey <pakk@96b.it> - 10.16.2-1%{?dist}
- New upstream version

* Sat May 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.10-1%{?dist}
- New upstream version

* Tue Jan 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- New upstream version

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.16-1%{?dist}
- New upstream version

* Sun Mar 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.14-2%{?dist}
- New rubygem1.9-shadow dependency

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.14-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Feb 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-1%{?dist}
- Initial package creation
