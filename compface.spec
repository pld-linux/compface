Summary:	Image from/to X-Face conversion utilities
Summary(pl):	Narzêdzia do konwersji obrazu z/do formatu X-Face
Name:		compface
Version:	1.4
Release:	2
Epoch:		1
License:	MIT
Group:		Applications/Graphics
Source0:	http://metalab.unc.edu/pub/Linux/apps/graphics/convert/%{name}-%{version}.tar.gz
# Source0-md5:	c45b54f67cc5d3580a18e4113219bc26
Patch0:		%{name}-errno.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compface provides utilities to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%description -l pl
Compface to para narzêdzi s³u¿±cych do konwersji z i do formatu
X-Face. Format ten s³u¿y do przechowywania bitmap o wymiarach 48x48
pikseli, które mo¿na przekazywaæ w nag³ówkach listów elektronicznych
czy postach na grupy dyskusyjne.

%package devel
Summary:	Image from/to X-Face conversion libraries
Summary(pl):	Biblioteki do konwersji obrazu z/do formatu X-Face
Group:		Development/Libraries

%description devel
Compface provides a library to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%description devel -l pl
Biblioteka s³u¿±ca do konwersji z i do formatu X-Face. Format ten
s³u¿y do przechowywania bitmap o wymiarach 48x48 pikseli, które mo¿na
przekazywaæ w nag³ówkach listów elektronicznych czy postach na grupy
dyskusyjne.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,man3},%{_libdir},%{_includedir}}

install compface $RPM_BUILD_ROOT%{_bindir}
install uncompface $RPM_BUILD_ROOT%{_bindir}
install compface.1 $RPM_BUILD_ROOT%{_mandir}/man1
install compface.3 $RPM_BUILD_ROOT%{_mandir}/man3
install libcompface.a $RPM_BUILD_ROOT%{_libdir}
install compface.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/compface.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcompface.a
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*
