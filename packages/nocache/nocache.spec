#-----------------------------------------------------------------------------
# nocache.spec
#-----------------------------------------------------------------------------

%global gitrev 404fa61

#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           nocache
Version:        0.%{gitrev}
Release:        1%{?dist}
Summary:        Minimize filesystem caching effects

Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/Feh/nocache
Source0:        %{name}.zip
Source1:        %{name}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The nocache tool tries to minimize the effect an application has on the Linux
file system cache. This is done by intercepting the open and close system
calls and calling posix_fadvise with the POSIX_FADV_DONTNEED parameter.
Because the library remembers which pages (ie., 4K-blocks of the file) were
already in file system cache when the file was opened, these will not be
marked as "don't need", because other applications might need that, although
they are not actively used (think: hot standby).


#-----------------------------------------------------------------------------
%prep
%setup -q -n Feh-%{name}-%{gitrev}


#-----------------------------------------------------------------------------
%build

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}

install -p -D -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
mv cachestats cachedel %{buildroot}%{_bindir}

install -p -D -m 0644 %{name}.so %{buildroot}%{_libdir}/%{name}.so
strip %{buildroot}%{_libdir}/%{name}.so


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc COPYING README
%{_bindir}/*
%{_libdir}/*.so


#-----------------------------------------------------------------------------
%changelog
* Sat Jun 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.404fa61-1%{?dist}
- Initial package creation
