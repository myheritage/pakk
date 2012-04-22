#-----------------------------------------------------------------------------
# grok.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           grok
Version:        1.20110630.1
Release:        1%{?dist}
Summary:        Powerful pattern-matching/reacting tool

Group:          System Environment/Libraries
License:        BSD
URL:            http://code.google.com/p/semicomplete/wiki/Grok
Source0:        http://semicomplete.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         %{name}-build.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gperf
BuildRequires:  libevent-devel >= 1.3
BuildRequires:  pcre8-devel
BuildRequires:  tokyocabinet-devel >= 1.4.9

%description
Grok is simple software that allows you to easily parse logs and other files.
With grok, you can turn unstructured log and event data into structured data.

The grok program is a great tool for parsing log data and program output.
You can match any number of complex patterns on any number of inputs
(processes and files) and have custom reactions.

The grok library is a great choice when you need the pattern matching
features of grok in your own tools. There are currently C and Ruby APIs.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Development libraries and headers for developing grok applications
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Development libraries and headers for developing grok applications.


#-----------------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1
sed -i -e 's|\$(PREFIX)/lib|%{_libdir}|g' Makefile

#-----------------------------------------------------------------------------
%build

%if 0%{?rhel} <= 6
export PCRE_CONFIG=pcre8-config
%endif
%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

strip %{buildroot}{%{_bindir},%{_libdir}}/* 
chmod 644 %{buildroot}%{_datadir}/%{name}/patterns/base
MAJOR=$(./version.sh --major)
pushd %{buildroot}%{_libdir}
  mv libgrok.so libgrok.so.${MAJOR}
  ln -s libgrok.so.${MAJOR} libgrok.so
popd


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc CHANGELIST LICENSE
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}*
%{_libdir}/*.so


#-----------------------------------------------------------------------------
%changelog
* Mon Aug 15 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.20110630.1-1%{?dist}
- Initial package creation
