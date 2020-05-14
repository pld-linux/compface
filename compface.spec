# TODO
# - devel collides with faces-devel
Summary:	Image from/to X-Face conversion utilities
Summary(pl.UTF-8):	Narzędzia do konwersji obrazu z/do formatu X-Face
Name:		compface
Version:	1.5.2
Release:	3
Epoch:		1
License:	MIT
Group:		Applications/Graphics
Source0:	http://ftp.xemacs.org/pub/xemacs/aux/%{name}-%{version}.tar.gz
# Source0-md5:	62f4f79c0861ad292ba3cf77b4c48319
URL:		http://freshmeat.sourceforge.net/projects/compface
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Conflicts:	faces
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compface provides utilities to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%description -l pl.UTF-8
Compface to para narzędzi służących do konwersji z i do formatu
X-Face. Format ten służy do przechowywania bitmap o wymiarach 48x48
pikseli, które można przekazywać w nagłówkach listów elektronicznych
czy postach na grupy dyskusyjne.

%package devel
Summary:	Image from/to X-Face conversion libraries
Summary(pl.UTF-8):	Biblioteki do konwersji obrazu z/do formatu X-Face
Group:		Development/Libraries
Conflicts:	faces-devel

%description devel
Compface provides a library to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%description devel -l pl.UTF-8
Biblioteka służąca do konwersji z i do formatu X-Face. Format ten
służy do przechowywania bitmap o wymiarach 48x48 pikseli, które można
przekazywać w nagłówkach listów elektronicznych czy postach na grupy
dyskusyjne.

%prep
%setup -q

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
cp -p compface.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p compface.3 $RPM_BUILD_ROOT%{_mandir}/man3
cp -p libcompface.a $RPM_BUILD_ROOT%{_libdir}
cp -p compface.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/compface
%attr(755,root,root) %{_bindir}/uncompface
%{_mandir}/man1/compface.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcompface.a
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*
