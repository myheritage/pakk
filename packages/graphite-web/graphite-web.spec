#-----------------------------------------------------------------------------
# graphite-web.spec
# dists: el6
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           graphite-web
Version:        0.9.9
Release:        1%{?dist}
Summary:        Enterprise scalable realtime graphing

Group:          Applications/System
License:        ASL 2.0
URL:            https://launchpad.net/graphite
Source0:        http://launchpad.net/graphite/0.9/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:         %{name}-paths.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python

Requires:       Django
Requires:       dejavu-sans-mono-fonts
Requires:       django-tagging
Requires:       initscripts
Requires:       pycairo
Requires:       python-carbon
Requires:       python-twisted >= 8.0
Requires:       python-whisper
Requires:       shadow-utils

%description
Backend data caching and persistence daemon for Graphite.


#-----------------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1


#-----------------------------------------------------------------------------
%build
rm -f setup.cfg
%{__python} setup.py build


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_prefix}/{conf,storage}

pushd %{buildroot}%{_bindir}
  sed -i \
    -e 's|\${GRAPHITE_ROOT}/storage|/var/lib/graphite-web|g' \
    -e 's|\${GRAPHITE_STORAGE_DIR}/whisper|/var/lib/carbon/whisper|g' \
    %{buildroot}%{_bindir}/build-index.sh
  mv build-index.sh graphite-build-index
  rm -f run-graphite-devel-server.py
popd

for file in dashboard.conf graphTemplates.conf; do
  install -D -p -m 0644 conf/${file}.example \
    %{buildroot}%{_sysconfdir}/%{name}/${file}
done

pushd %{buildroot}%{python_sitelib}/graphite
  mv local_settings.py{.example,}
  sed -i -e '1d' \
    manage.py \
    thirdparty/pytz/tzfile.py
popd

install -D -p -m 0755 conf/graphite.wsgi.example \
  %{buildroot}%{_datadir}/%{name}/%{name}.wsgi

mv %{buildroot}%{_prefix}/webapp %{buildroot}%{_datadir}/%{name}
pushd %{buildroot}%{_datadir}/%{name}
  chmod 644 graphite-web.wsgi
  find . -name \*.js -exec chmod 644 {} \;
popd

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%pre
if [ $1 == 1 ]; then
  /usr/sbin/useradd -c %{name} -s /bin/false -r -M -d %{_localstatedir}/lib/%{name} \
    %{name} 2> /dev/null || :
fi

%post
[ ! -f %{_localstatedir}/lib/%{name}/graphite.db ] && \
  python %{python_sitelib}/graphite/manage.py syncdb --noinput > /dev/null
chown %{name}:%{name} %{_localstatedir}/lib/%{name}/graphite.db


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc LICENSE README examples
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{python_sitelib}/*
%config(noreplace) %{python_sitelib}/graphite/local_settings.py
%{_datadir}/%{name}
%attr(-, %{name}, %{name}) %{_localstatedir}/lib/%{name}
%dir %attr(-, %{name}, %{name}) %{_localstatedir}/log/%{name}


#-----------------------------------------------------------------------------
%changelog
* Sun Apr 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.9-1%{?dist}
- Initial package creation
