#-----------------------------------------------------------------------------
# libmongoc.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           libmongoc
Version:        0.7.1
Release:        1%{?dist}
Summary:        10gen-supported MongoDB C driver

Group:          System Environment/Libraries
License:        ASL 2.0
URL:            https://github.com/mongodb/mongo-c-driver
Source0:        https://github.com/mongodb/mongo-c-driver/tarball/v%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  scons

%description
This is then 10gen-supported MongoDB C driver. There are two goals for this
driver. The first is to provide a strict, default compilation option for
ultimate portability, no dependencies, and generic embeddability.
The second is to support more advanced, platform-specific features, like
socket timeout, by providing an interface for platform-specific modules.
Until the 1.0 release, this driver should be considered alpha. Keep in mind
that the API will be in flux until then.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Development libraries and headers for developing %{name} applications
Group:          Development/Libraries

Requires:       %{name} = %{version}

%description devel
Development libraries and headers for developing %{name} applications.


#-----------------------------------------------------------------------------
# -static package
#-----------------------------------------------------------------------------
%package static
Summary:        Static library for %{name}
Group:          Development/Libraries

%description static
Library for static linking for %{name}.


#-----------------------------------------------------------------------------
%prep
%setup -q -n mongo-c-driver-%{version}


#-----------------------------------------------------------------------------
%build

scons


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install \
  INSTALL_INCLUDE_PATH=%{buildroot}%{_includedir} \
  INSTALL_LIBRARY_PATH=%{buildroot}%{_libdir}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc APACHE-2.0.txt HISTORY.md README.md
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%doc docs
%{_includedir}/*.h
%{_libdir}/*.so

%files static
%defattr(-, root, root, -)
%{_libdir}/*.a


#-----------------------------------------------------------------------------
%changelog
* Mon May 6 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.7.1-1%{?dist}
- New upstream version

* Sun Nov 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6-1%{?dist}
- New upstream version

* Fri Apr 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.5-1%{?dist}
- Initial package creation
