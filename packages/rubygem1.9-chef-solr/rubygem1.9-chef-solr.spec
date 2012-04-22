#-------------------------------------------------------------------------------
# rubygem1.9-chef-solr.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname chef-solr


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-chef-solr
Version:        0.10.8
Release:        1%{?dist}
Summary:        Manages search indexes of Chef node attributes using Solr (rubygem)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}-solr.rb
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
Source5:        %{name}.man
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       chef-common = %{version}
Requires:       java
Requires:       ruby1.9
Requires:       rubygem1.9-chef = %{version}

%description
The Chef Solr search engine runs as a Jetty server, and an indexer talks to
the AMQP message queue.

This package contains the rubygem code. If you need to run chef-solr
as a daemon, please install the "chef-solr" package.


#-----------------------------------------------------------------------------
# chef-solr package
#-----------------------------------------------------------------------------
%package -n chef-solr
Summary:        Manages search indexes of Chef node attributes using Solr
Group:          System Environment/Daemons

Requires:       %{name} = %{version}

%description -n chef-solr
The Chef Solr search engine runs as a Jetty server, and an indexer talks to
the AMQP message queue.

The Chef indexer listens to a message queue via AMQP for changes to search
indexes. It then either creates or deletes entries in the index according
to the information it is passed.

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
  rm -rf Rakefile spec
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} \
  %{ruby_sitelib}/bin/%{gemname}-installer \
  %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/chef
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/chef/solr.rb

install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{gemname}

install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gemname}
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{gemname}

install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man8/%{gemname}.8
gzip %{buildroot}%{_mandir}/man8/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -n chef-solr
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{gemname}
fi

%preun -n chef-solr
if [ $1 = 0 ]; then
  /sbin/service %{gemname} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{gemname}
fi

%postun -n chef-solr
if [ $1 == 2 ]; then
   /sbin/service %{gemname}-indexer stop > /dev/null 2>&1 || :
   /sbin/chkconfig --del %{gemname}-indexer
   /sbin/service %{gemname} stop > /dev/null 2>&1 || :
  %{_bindir}/chef-solr-installer
  /sbin/service %{gemname} start > /dev/null 2>&1 || :
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
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/solr
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n chef-solr
%config(noreplace) %{_sysconfdir}/chef/solr.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-solr
%config(noreplace) %{_sysconfdir}/sysconfig/chef-solr
%{_initrddir}/chef-solr

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Jan 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- New upstream version
- The indexer doesn't exists anymore, and has been replaced by the expander

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.16-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.14-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Feb 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-1%{?dist}
- Initial package creation
