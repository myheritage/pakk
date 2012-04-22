#-----------------------------------------------------------------------------
# credis.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           credis
Version:        0.2.3
Release:        1%{?dist}
Summary:        C client library for Redis

Group:          System Environment/Libraries
License:        BSD
URL:            http://code.google.com/p/credis/
Source0:        http://credis.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Credis is a client library in plain C for communicating with Redis servers.
Credis aims to be fast and minimalistic with respect to memory usage. It
supports connections to multiple Redis servers. 


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Development libraries and headers for developing with %{name}
Group:          Development/Libraries

Requires:       %{name} = %{version}

%description devel
Development libraries and headers for developing with %{name}.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build

MAJOR=$(echo %{version} | cut -d. -f1)

sed -i \
  -e "s|-soname,|-soname,libcredis.so.${MAJOR}|g" \
  -e 's|$(SHAREDLIB_LINK_OPTIONS)$@|$(SHAREDLIB_LINK_OPTIONS)|g' \
  Makefile
%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}

MAJOR=$(echo %{version} | cut -d. -f1)
MINOR=$(echo %{version} | cut -d. -f2)
PATCH=$(echo %{version} | cut -d. -f3)
strip libcredis.so
install -D -p -m 0644 libcredis.so %{buildroot}%{_libdir}/libcredis.so.${MAJOR}.${MINOR}.${PATCH}
(
  cd %{buildroot}%{_libdir}
  ln -sf libcredis.so.${MAJOR}.${MINOR}.${PATCH} libcredis.so.${MAJOR}
  ln -sf libcredis.so.${MAJOR}.${MINOR}.${PATCH} libcredis.so
)
install -D -p -m 0644 %{name}.h %{buildroot}%{_includedir}/%{name}.h


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%doc credis-test.c
%{_includedir}/*.h
%{_libdir}/*.so


#-----------------------------------------------------------------------------
%changelog
* Thu Mar 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.2.3-1%{?dist}
- Initial package creation
