#-----------------------------------------------------------------------------
# weighttp.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           weighttp
Version:        0.3
Release:        1%{?dist}
Summary:        Lightweight and small benchmarking tool for webservers

Group:          Applications/System
License:        MIT
URL:            http://redmine.lighttpd.net/projects/weighttp/wiki
Source0:        http://git.lighttpd.net/weighttp.git/snapshot/master.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libev-devel
BuildRequires:  python

%description
Weighttp was designed to be very fast and easy to use and only supports a
tiny fraction of the HTTP protocol in order to be lean and simple.
Weighttp supports multithreading to make good use of modern CPUs with
multiple cores as well as asynchronous i/o for concurrent requests within a
single thread.


#-----------------------------------------------------------------------------
%prep
%setup -q -n master


#-----------------------------------------------------------------------------
%build
sed -i \
  -e "s|conf.env\['CCFLAGS'\] += \[|conf.env['CCFLAGS'] += ['-I/usr/include/libev',|g" \
  wscript
./waf configure
./waf build


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}

install -p -D -m 0755 build/default/%{name} %{buildroot}%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc COPYING README
%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%changelog
* Wed May 2 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.3-1%{?dist}
- Initial package creation
