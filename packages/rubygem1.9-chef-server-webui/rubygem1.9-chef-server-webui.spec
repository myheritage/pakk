#-------------------------------------------------------------------------------
# rubygem1.9-chef-server-webui.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname chef-server-webui


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-chef-server-webui
Version:        10.18.2
Release:        1%{?dist}
Summary:        Merb app slice providing a web interface for Chef (rubygem)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}-webui.rb
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
Source5:        %{name}.man
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       chef-common = %{version}
Requires:       ruby1.9
Requires:       rubygem1.9-coderay
Requires:       rubygem1.9-extlib < 0.10.0
Requires:       rubygem1.9-haml
Requires:       rubygem1.9-merb-core >= 1.1.0
Requires:       rubygem1.9-merb-assets >= 1.1.0
Requires:       rubygem1.9-merb-helpers >= 1.1.0
Requires:       rubygem1.9-merb-haml >= 1.1.0
Requires:       rubygem1.9-merb-param-protection >= 1.1.0
Requires:       rubygem1.9-openid
Requires:       rubygem1.9-thin

%description
The Chef Server WebUI is a Merb application that accesses the Chef Server API
directly to provide an easy to use interface for managing Chef clients and
Chef server data.

This package contains the rubygem code. If you need to run chef-server-webui
as a daemon, please install the "chef-server-webui" package.


#-----------------------------------------------------------------------------
# chef-server-webui package
#-----------------------------------------------------------------------------
%package -n chef-server-webui
Summary:        Merb app slice providing a web interface for Chef
Group:          System Environment/Daemons

Requires:       %{name} = %{version}

%description -n chef-server-webui
The Chef Server WebUI is a Merb application that accesses the Chef Server API
directly to provide an easy to use interface for managing Chef clients and
Chef server data.


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
  rm -rf Rakefile
  echo 'File.umask Chef::Config[:umask]' >> config/init.rb
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/chef
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/chef/webui.rb

install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{gemname}

install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gemname}
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{gemname}

install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man8/%{gemname}.8 \
  && gzip %{buildroot}%{_mandir}/man8/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -n chef-server-webui
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{gemname}
fi

%preun -n chef-server-webui
if [ $1 = 0 ]; then
  /sbin/service %{gemname} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{gemname}
fi

%postun -n chef-server-webui
if [ $1 == 2 ]; then
  /sbin/service %{gemname} try-restart || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%{_bindir}/*
%{_mandir}/man8/*.gz
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/app
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/config
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/public
%{ruby_sitelib}/gems/%{gemname}-%{version}/*.ru
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n chef-server-webui
%config(noreplace) %{_sysconfdir}/chef/webui.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-server-webui
%config(noreplace) %{_sysconfdir}/sysconfig/chef-server-webui
%{_initrddir}/chef-server-webui

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Mon Jan 28 2013 Eric-Olivier Lamey <pakk@96b.it> - 10.18.2-1%{?dist}
- New upstream version

* Tue Oct 30 2012 Eric-Olivier Lamey <pakk@96b.it> - 10.16.2-1%{?dist}
- New upstream version

* Sat May 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.10-1%{?dist}
- New upstream version

* Tue Jan 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- New upstream version

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.16-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.14-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Feb 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-1%{?dist}
- Initial package creation
