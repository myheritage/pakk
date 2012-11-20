#-----------------------------------------------------------------------------
# collectd5.spec
#
# files overlapping with EPEL's package:
# - %{_libdir}/libcollectdclient*
# - %{_libdir}/pkgconfig/libcollectdclient
# - %{_datadir}/perl5/vendor_perl/Collectd*
#-----------------------------------------------------------------------------

%global upstream_name collectd
%global plugindir     %{_libdir}/%{name}

%if 0%{?rhel} <= 5
%define _without_yajl 1
%endif


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           collectd5
Version:        5.2.0
Release:        1%{?dist}
Summary:        Statistics collection daemon for filling RRD files

Group:          System Environment/Daemons
License:        GPLv2
URL:            http://collectd.org
Source0:        http://collectd.org/files/%{upstream_name}-%{version}.tar.bz2
Source1:        %{name}-collection3.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Conflicts:      collectd > 5.0.0, collectd <= 5.1.0
Obsoletes:      collectd > 5.0.0, collectd <= 5.1.0

BuildRequires:  curl-devel
%if 0%{?rhel} >= 6
BuildRequires:  iptables-devel
%endif
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libpcap-devel
BuildRequires:  libxml2-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Embed)
%if 0%{?rhel} <= 5
BuildRequires:  python26-devel
%else
BuildRequires:  python-devel
%endif
%if %{!?_without_yajl:1}0
BuildRequires:  yajl-devel
%endif

Requires:       initscripts
Requires:       shadow-utils


%description
collectd is a small daemon written in C for performance.  It reads various
system  statistics  and updates  RRD files,  creating  them if necessary.
Since the daemon doesn't need to startup every time it wants to update the
files it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Header files and libraries for building collectd clients
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Header files and libraries for building collectd clients.


#-----------------------------------------------------------------------------
# -dbi package
#-----------------------------------------------------------------------------
%package dbi
Summary:        DBI module for collectd
Group:          System Environment/Daemons

BuildRequires:  libdbi-devel

Requires:       %{name} = %{version}

%description dbi
This plugin for collectd provides DBI support.


#-----------------------------------------------------------------------------
# -ipmi package
#-----------------------------------------------------------------------------
%package ipmi
Summary:        IPMI module for collectd
Group:          System Environment/Daemons

BuildRequires:  OpenIPMI-devel

Requires:       %{name} = %{version}

%description ipmi
This plugin for collectd provides IPMI support.


#-----------------------------------------------------------------------------
# -java package
#-----------------------------------------------------------------------------
%package java
Summary:        Java module for collectd
Group:          System Environment/Daemons
AutoReqProv:    no

BuildRequires:  java-devel

%description java
This plugin for collectd provides Java and JMX support.


#-----------------------------------------------------------------------------
# -libvirt package
#-----------------------------------------------------------------------------
%package libvirt
Summary:        Libvirt module for collectd
Group:          System Environment/Daemons

BuildRequires:  libvirt-devel

Requires:       %{name} = %{version}

%description libvirt
This plugin for collectd provides libvirt support.


#-----------------------------------------------------------------------------
# -memcachec package
#-----------------------------------------------------------------------------
%package memcachec
Summary:        Memcache module for collectd
Group:          System Environment/Daemons

BuildRequires:  libmemcached-devel

Requires:       %{name} = %{version}

%description memcachec
This plugin for collectd provides Memcache support.


#-----------------------------------------------------------------------------
# -mongodb package
#-----------------------------------------------------------------------------
%package mongodb
Summary:        MongoDB module for collectd
Group:          System Environment/Daemons

BuildRequires:  libmongoc-devel

Requires:       %{name} = %{version}

%description mongodb
This plugin for collectd provides MongoDB support.


#-----------------------------------------------------------------------------
# -mysql package
#-----------------------------------------------------------------------------
%package mysql
Summary:        MySQL module for collectd
Group:          System Environment/Daemons

BuildRequires:  mysql-devel

Requires:       %{name} = %{version}

%description mysql
This plugin for collectd provides MySQL support.


#-----------------------------------------------------------------------------
# -notify_email package
#-----------------------------------------------------------------------------
%package notify_email
Summary:        Email notification module for collectd
Group:          System Environment/Daemons

BuildRequires:  libesmtp-devel

Requires:       %{name} = %{version}

%description notify_email
This plugin for collectd provides email notification support.


#-----------------------------------------------------------------------------
# perl-Collectd5 package
#-----------------------------------------------------------------------------
%package -n perl-Collectd5
Summary:        Perl bindings for collectd
Group:          System Environment/Daemons

Requires:       %{name} = %{version}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description -n perl-Collectd5
This package contains Perl bindings and plugin for collectd.


#-----------------------------------------------------------------------------
# -ping package
#-----------------------------------------------------------------------------
%package ping
Summary:        Ping module for collectd
Group:          System Environment/Daemons

BuildRequires:  liboping-devel

Requires:       %{name} = %{version}

%description ping
This plugin for collectd provides network latency statistics.


#-----------------------------------------------------------------------------
# -postgresql package
#-----------------------------------------------------------------------------
%package postgresql
Summary:        PostgreSQL module for collectd
Group:          System Environment/Daemons

BuildRequires:  postgresql-devel

Requires:       %{name} = %{version}

%description postgresql
PostgreSQL querying plugin. This plugins provides data of issued commands,
called handlers and database traffic.


#-----------------------------------------------------------------------------
# -redis package
#-----------------------------------------------------------------------------
%package redis
Summary:        Redis module for collectd
Group:          System Environment/Daemons

BuildRequires:  credis-devel

Requires:       %{name} = %{version}

%description redis
This plugin for collectd provides redis support.


#-----------------------------------------------------------------------------
# -rrdtool package
#-----------------------------------------------------------------------------
%package rrdtool
Summary:        RRDTool module for collectd
Group:          System Environment/Daemons

BuildRequires:  rrdtool-devel

Requires:       %{name} = %{version}
Requires:       rrdtool

%description rrdtool
This plugin for collectd provides rrdtool support.


#-----------------------------------------------------------------------------
# -sensors package
#-----------------------------------------------------------------------------
%package sensors
Summary:        Libsensors module for collectd
Group:          System Environment/Daemons

BuildRequires:  lm_sensors-devel

Requires:       %{name} = %{version}
Requires:       lm_sensors

%description sensors
This plugin for collectd provides querying of sensors supported by
lm_sensors.


#-----------------------------------------------------------------------------
# -snmp package
#-----------------------------------------------------------------------------
%package snmp
Summary:        SNMP module for collectd
Group:          System Environment/Daemons

BuildRequires:  net-snmp-devel

Requires:       %{name} = %{version}
Requires:       net-snmp

%description snmp
This plugin for collectd provides querying of net-snmp.


#-----------------------------------------------------------------------------
# -varnish package
#-----------------------------------------------------------------------------
%package varnish
Summary:        Varnish module for collectd
Group:          System Environment/Daemons

BuildRequires:  varnish-libs-devel

Requires:       %{name} = %{version}

%description varnish
This plugin for collectd provides varnish support.


#-----------------------------------------------------------------------------
# -web package
#-----------------------------------------------------------------------------
%package web
Summary:        Contrib web interface to viewing rrd files
Group:          System Environment/Daemons

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

Requires:       %{name} = %{version}
Requires:       %{name}-rrdtool = %{version}
Requires:       perl(Config::General)
Requires:       perl(Regexp::Common)
Requires:       perl(HTML::Entities)
Requires:       perl(RRDs)

%description web
This package will allow for a simple web interface to view rrd files created
by collectd.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{upstream_name}-%{version}

sed -i \
  -e 's|OpenIPMIpthread|OpenIPMI|g' \
  -e "s|PACKAGE_NAME='%{upstream_name}'|PACKAGE_NAME='%{name}'|g" \
  configure

sed -i -e 's|-Werror||g' Makefile.in */Makefile.in
sed -i -e 's|(sysconfdir)/%{upstream_name}.conf|(sysconfdir)/${PACKAGE_NAME}.conf|g' \
  src/Makefile.in
sed -i -e 's|/@PACKAGE@|/@PACKAGE_NAME@|g' \
  bindings/java/Makefile.in \
  src/Makefile.in \
  src/libcollectdclient/Makefile.in


#-----------------------------------------------------------------------------
%build
export CFLAGS="%{optflags} -DLT_LAZY_OR_NOW='RTLD_LAZY|RTLD_GLOBAL'"
%configure \
  --program-transform-name='s|%{upstream_name}|%{name}|g' \
%if 0%{?rhel} >= 6
  --with-libiptc \
%endif
  --with-perl-bindings=INSTALLDIRS=vendor \
  --with-python=/usr/bin/python2.6 \
  --disable-static \
  --disable-ascent \
  --disable-apple_sensors \
  --disable-gmond \
  --disable-lpar \
  --disable-modbus \
  --disable-netapp \
  --disable-netlink \
  --disable-notify_desktop \
  --disable-nut \
  --disable-onewire \
  --disable-oracle \
  --disable-pinba \
  --disable-routeros \
  --disable-rrdcached \
  --disable-tape \
  --disable-tokyotyrant \
  --disable-xmms \
  --disable-zfs_arc \
  --enable-apache \
  --enable-apcups \
  --enable-battery \
  --enable-bind \
  --enable-conntrack \
  --enable-contextswitch \
  --enable-cpu \
  --enable-cpufreq \
  --enable-csv \
  --enable-curl \
%if %{!?_without_yajl:1}0
  --enable-curl_json  \
%endif
  --enable-curl_xml \
  --enable-dbi  \
  --enable-df \
  --enable-disk \
  --enable-dns \
  --enable-email \
  --enable-entropy \
%if 0%{?rhel} >= 6
  --enable-ethstat \
%endif
  --enable-exec \
  --enable-filecount \
  --enable-fscache \
  --enable-hddtemp \
  --enable-interface \
%if 0%{?rhel} >= 6
  --enable-iptables \
  --enable-ipvs \
%else
  --disable-iptables \
  --disable-ipvs \
%endif
  --enable-irq \
  --enable-ipmi \
  --with-java=/usr/lib/jvm/java/ \
  --enable-java \
  --enable-libvirt \
  --enable-load \
  --enable-logfile \
  --enable-madwifi \
  --enable-match_empty_counter \
  --enable-match_hashed \
  --enable-match_regex \
  --enable-match_timediff \
  --enable-match_value \
  --enable-mbmon \
  --enable-md \
  --enable-memcachec \
  --enable-memcached \
  --enable-memory \
  --enable-multimeter \
  --enable-mysql \
  --enable-network \
  --enable-nfs \
  --enable-nginx \
  --enable-notify_email \
  --enable-ntpd \
  --enable-numa \
  --enable-olsrd \
  --enable-openvpn \
  --enable-perl \
  --enable-ping \
  --enable-postgresql \
  --enable-powerdns \
  --enable-processes \
  --enable-protocols \
  --enable-python \
  --enable-redis \
  --enable-rrdtool \
  --enable-sensors \
  --enable-serial \
  --enable-snmp \
  --enable-swap \
  --enable-syslog \
  --enable-table \
  --enable-tail \
  --enable-target_notification \
  --enable-target_replace \
  --enable-target_scale \
  --enable-target_set \
  --enable-tcpconns \
  --enable-teamspeak2 \
  --enable-ted \
  --enable-thermal \
  --enable-unixsock \
  --enable-uptime \
  --enable-users \
  --enable-uuid \
  --enable-varnish \
  --enable-vmem \
  --enable-vserver \
  --enable-wireless \
  --enable-write_graphite \
  --enable-write_http \
  --enable-write_mongodb \
  --enable-write_redis

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
rm -rf contrib/SpamAssassin
make install DESTDIR=%{buildroot}

chmod 644 %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i \
  -e 's|^#BaseDir.*|BaseDir     "/var/lib/%{name}"|g' \
  -e 's|^#PIDFile.*|PIDFile     "/var/run/%{name}.pid"|g' \
  %{buildroot}%{_sysconfdir}/%{name}.conf
echo -e "jmx_memory\t\tvalue:GAUGE:0:U" >> %{buildroot}/%{_datadir}/%{name}/types.db

install -Dp -m0755 contrib/fedora/init.d-collectd %{buildroot}%{_initrddir}/%{name}
sed -i -e 's|%{upstream_name}|%{name}|g' %{buildroot}%{_initrddir}/%{name}

install -d -m0755 %{buildroot}%{plugindir}/python
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/
install -d -m0755 %{buildroot}%{_datadir}/%{name}/collection3/

%if 0%{?rhel} >= 6
install -d -m0755 %{buildroot}%{perl_vendorlib}
mv %{buildroot}/usr/lib/perl5/* %{buildroot}%{perl_vendorlib}/
rm -rf %{buildroot}%{_libdir}/perl5
mv %{buildroot}/usr/man/man3 %{buildroot}%{_mandir}/
rm -rf %{buildroot}/usr/man
%endif

find %{buildroot} -name .packlist -exec rm {} \;
find %{buildroot} -name perllocal.pod -exec rm {} \;
rm -f %{buildroot}%{_libdir}/{%{name}/,}*.la
rm %{buildroot}%{_datadir}/%{name}/postgresql_default.conf

mkdir apache-config
install -Dp -m0644 %{SOURCE1} apache-config
cp -ad contrib/collection3/* %{buildroot}%{_datadir}/%{name}/collection3/
chmod +x %{buildroot}%{_datadir}/%{name}/collection3/bin/*.cgi
rm -f %{buildroot}%{_datadir}/%{name}/collection3/{bin,etc,lib,share}/.htaccess

mkdir perl-examples
find contrib -name '*.p[lm]' -exec mv {} perl-examples/ \;


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%post
/sbin/ldconfig
/sbin/chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
  /sbin/service %{name} stop >/dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi

%postun
/sbin/ldconfig
if [ $1 -ge 1 ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi


%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING INSTALL README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_initrddir}/%{name}
%{_sbindir}/*
%{_bindir}/*
%dir %{_localstatedir}/lib/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/python
%{_libdir}/%{name}/*.so
%exclude %{plugindir}/dbi.so
%exclude %{plugindir}/ipmi.so
%exclude %{plugindir}/java.so
%exclude %{plugindir}/libvirt.so
%exclude %{plugindir}/memcachec.so
%exclude %{plugindir}/mysql.so
%exclude %{plugindir}/notify_email.so
%exclude %{plugindir}/perl.so
%exclude %{plugindir}/ping.so
%exclude %{plugindir}/postgresql.so
%exclude %{plugindir}/redis.so
%exclude %{plugindir}/rrdtool.so
%exclude %{plugindir}/sensors.so
%exclude %{plugindir}/snmp.so
%exclude %{plugindir}/varnish.so
%exclude %{plugindir}/write_mongodb.so
%exclude %{plugindir}/write_redis.so
%{_datadir}/%{name}/types.db
%{_libdir}/*.so.*
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}ctl.1*
%doc %{_mandir}/man1/%{name}-nagios.1*
%doc %{_mandir}/man1/%{name}mon.1*
%doc %{_mandir}/man5/%{name}.conf.5*
%doc %{_mandir}/man5/%{name}-email.5*
%doc %{_mandir}/man5/%{name}-exec.5*
%doc %{_mandir}/man5/%{name}-python.5*
%doc %{_mandir}/man5/%{name}-threshold.5*
%doc %{_mandir}/man5/%{name}-unixsock.5*
%doc %{_mandir}/man5/types.db.5*

%files dbi
%defattr(-, root, root, -)
%{plugindir}/dbi.so

%files devel
%defattr(-, root, root, -)
%{_includedir}/%{name}
%{_libdir}/libcollectdclient.so
%{_libdir}/pkgconfig/*.pc

%files ipmi
%defattr(-, root, root, -)
%{plugindir}/ipmi.so

%files java
%defattr(-, root, root, -)
%{plugindir}/java.so
%{_datadir}/%{name}/java
%doc %{_mandir}/man5/%{name}-java.5*

%files libvirt
%defattr(-, root, root, -)
%{plugindir}/libvirt.so

%files memcachec
%defattr(-, root, root, -)
%{plugindir}/memcachec.so

%files mongodb
%defattr(-, root, root, -)
%{plugindir}/write_mongodb.so

%files mysql
%defattr(-, root, root, -)
%{plugindir}/mysql.so

%files notify_email
%defattr(-, root, root, -)
%{plugindir}/notify_email.so

%files -n perl-Collectd5
%defattr(-, root, root, -)
%doc perl-examples
%{plugindir}/perl.so
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd/
%doc %{_mandir}/man5/%{name}-perl.5*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm*

%files ping
%defattr(-, root, root, -)
%{plugindir}/ping.so

%files postgresql
%defattr(-, root, root, -)
%{plugindir}/postgresql.so
%doc src/postgresql_default.conf

%files redis
%defattr(-, root, root, -)
%{plugindir}/redis.so
%{plugindir}/write_redis.so

%files rrdtool
%defattr(-, root, root, -)
%{plugindir}/rrdtool.so

%files sensors
%defattr(-, root, root, -)
%{plugindir}/sensors.so

%files snmp
%defattr(-, root, root, -)
%{plugindir}/snmp.so
%doc %{_mandir}/man5/%{name}-snmp.5*

%files varnish
%defattr(-, root, root, -)
%{plugindir}/varnish.so

%files web
%defattr(-, root, root, -)
%doc apache-config
%{_datadir}/%{name}/collection3/


#-----------------------------------------------------------------------------
%changelog
* Sun Nov 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 5.2.0-1%{?dist}
- New upstream version

* Thu Nov 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 5.1.0-3%{?dist}
- Fixed JVM dependency

* Mon Apr 30 2012 Eric-Olivier Lamey <pakk@96b.it> - 5.1.0-2%{?dist}
- Renamed package to collectd5

* Fri Apr 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 5.1.0-1%{?dist}
- New upstream version
- Enabled ethstat, graphite and mongodb plugins
- Disabled iptables and ipvs on rhel < 6

* Tue Mar 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 5.0.3-1%{?dist}
- New upstream version
- Enabled redis plugins
- Enabled Python 2.6 instead of 2.4

* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 5.0.2-1%{?dist}
- New upstream version

* Mon Nov 28 2011 Eric-Olivier Lamey <pakk@96b.it> - 5.0.1-1%{?dist}
- New upstream version

* Sat Oct 8 2011 Eric-Olivier Lamey <pakk@96b.it> - 5.0.0-2%{?dist}
- Don't depend on apache, people might want to use a different web server

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 5.0.0-1%{?dist}
- Initial package creation (more than heavily inspired by Fedora's spec)
