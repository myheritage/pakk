#-----------------------------------------------------------------------------
# observium.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           observium
Version:        0.11.5.2261
Release:        1%{?dist}
Summary:        Autodiscovering PHP/MySQL/SNMP based network monitoring

Group:          System Environment/Daemons
License:        GPLv3
URL:            http://www.observium.org/wiki/Main_Page
Source0:        %{name}-%{version}.tar.gz
Source1:        http://download.pear.php.net/package/PEAR-1.9.4.tgz
Source2:        http://download.pear.php.net/package/Net_IPv4-1.3.4.tgz
Source3:        http://download.pear.php.net/package/Net_IPv6-1.2.1.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       ImageMagick
Requires:       OpenIPMI-tools
Requires:       dejavu-lgc-fonts
Requires:       fping
Requires:       graphviz
Requires:       httpd
Requires:       jwhois
Requires:       mysql-server
Requires:       net-snmp
Requires:       net-snmp-utils
Requires:       nmap
Requires:       php
Requires:       php53-mysql
Requires:       php53-gd
Requires:       php53-snmp
Requires:       rrdtool
Requires:       shadow-utils

%description
Observium is an autodiscovering PHP/MySQL/SNMP based network monitoring which
includes support for a wide range of network hardware and operating systems
including Cisco, Linux, FreeBSD, Juniper, Foundry, HP and many more.
Observium has grown out of a lack of easy to configure and easy use NMSes.
It is intended to provide a more navigable interface to the health and
performance of your network. Its design goals include collecting as much
historical data about devices as possible, being completely autodiscovered
with little or no manual intervention, and having a very intuitive interface.
Observium is not intended to replace a Nagios-type up/down monitoring system,
but rather to complement it with an easy to manage, intuitive representation
of historical and current performance statistics, configuration visualisation
and syslog capture.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{name}


#-----------------------------------------------------------------------------
%build


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/%{name}
mv attic contrib html includes mibs scripts upgrade-scripts *.php *.sh %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphs,rrd}

# config.php
# /var/log/observium
# /var/lib/observium/rrd

# replace .htaccess with apache conf file
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%pre
if [ $1 == 1 ]; then
  /usr/bin/getent group %{name} > /dev/null || \
    /usr/sbin/groupadd -r %{name}
  /usr/sbin/useradd -g %{name} -c %{name} -s /sbin/nologin -r -M \
    -d %{_datadir}/%{name} %{name} 2> /dev/null || :
fi


%files
%defattr(-, root, root, -)
%doc CHANGELOG COPYING INSTALL README database* *.conf.example
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_datadir}/%{name}/attic
%{_datadir}/%{name}/contrib
%{_datadir}/%{name}/html
%{_datadir}/%{name}/includes
%{_datadir}/%{name}/mibs
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/upgrade-scripts
%{_datadir}/%{name}/*.php
%{_datadir}/%{name}/*.sh
%dir(0755, apache, apache) %{_datadir}/%{name}/graphs
%dir(0755, %{name}, %{name}) %{_datadir}/%{name}/rrd


#-----------------------------------------------------------------------------
%changelog
* Wed Sep 13 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.11.5.2261-1%{?dist}
- Initial package creation
