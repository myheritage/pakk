#-----------------------------------------------------------------------------
# collectd-librato.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           collectd-librato
Version:        0.0.8
Release:        1%{?dist}
Summary:        collectd plugin that publishes collectd values to Librato Metrics

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/librato/collectd-librato
Source0:        https://github.com/librato/%{name}/tarball/v%{version}.tar.gz
Source1:        %{name}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       collectd5

%description
collectd-librato is a collectd plugin that publishes collectd values to
Librato Metrics using the Librato Metrics API. Librato Metrics is a hosted,
time-series data service.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/collectd.d/librato.conf
sed -i -e 's|{libdir}|%{_libdir}|g' %{buildroot}%{_sysconfdir}/collectd.d/librato.conf
install -p -D -m 0644 lib/collectd-librato.py \
  %{buildroot}%{_libdir}/collectd/python/collectd-librato.py


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc LICENSE README.md
%config(noreplace) %{_sysconfdir}/collectd.d/librato.conf
%{_libdir}/collectd/python/collectd-librato.py*


#-----------------------------------------------------------------------------
%changelog
* Sun Aug 11 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.0.8-1%{?dist}
- New upstream version

* Tue May 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.0.5-2%{?dist}
- collectd in now collectd5

* Wed Mar 28 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.0.5-1%{?dist}
- Initial package creation
