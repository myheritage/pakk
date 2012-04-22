#-----------------------------------------------------------------------------
# pcre8.spec
#-----------------------------------------------------------------------------

%global realname pcre


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           pcre8
Version:        8.21
Release:        1%{?dist}
Summary:        Perl-compatible regular expression library

Group:          System Environment/Libraries
License:        BSD
URL:            http://www.pcre.org/
Source0:        ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{realname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Perl-compatible regular expression library.
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Development libraries and headers for developing pcre applications
Group:          Development/Libraries

Requires:       %{name} = %{version}

%description devel
Development libraries and headers for developing pcre applications.


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
%setup -q -n %{realname}-%{version}


#-----------------------------------------------------------------------------
%build

./configure \
  --prefix=%{_prefix} \
  --includedir=%{_includedir}/%{name} \
  --libdir=%{_libdir}/%{name} \
  --program-transform-name='s/pcre/pcre8/g' \
  --enable-utf8 \
  --enable-unicode-properties
sed -i -e 's|-version-info 0|-version-info 1|g' Makefile
%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

iconv --from=latin1 --to=UTF-8 ChangeLog > ChangeLog.new && \
  mv ChangeLog.new ChangeLog
rm -rf  %{buildroot}%{_docdir} %{buildroot}%{_libdir}/%{name}/*.la

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%{_bindir}/pcre8grep
%{_bindir}/pcre8test
%{_libdir}/%{name}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, -)
%doc HACKING doc/*.txt doc/html
%{_bindir}/pcre8-config
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/pkgconfig
%{_mandir}/man3/*

%files static
%defattr(-, root, root, -)
%{_libdir}/%{name}/*.a


#-----------------------------------------------------------------------------
%changelog
* Mon Jan 2 2012 Eric-Olivier Lamey <pakk@96b.it> - 8.21-1%{?dist}
- Initial package creation
