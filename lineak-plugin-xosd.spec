%define		packagename	lineak_xosdplugin

Summary:	XOSD On-screen Display plugin for the lineakd daemon
Summary(pl):	Wtyczka XOSD On-screen Display dla demona lineakd
Name:		lineak-plugin-xosd
Version:	0.8.4
Release:	0.9
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{packagename}-%{version}.tar.gz
# Source0-md5:	36f519b21e7c7257bd9af6543f7fd9fc
Url:		http://lineak.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xosd-devel
BuildRequires:	lineakd-devel >= %{version}
Requires:	lineakd >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a plugin for lineakd. The plugin allows binding actions to special
keys.

This plugin allows display using the xosd library. It requires that you
have the following configuration option in your lineakd.conf file:

 Display_plugin = xosd

It also understands the following configuration directives:

 Display_font =
 Display_color =
 Display_pos =
 Display_align =
 Display_timeout =
 Display_hoffset =
 Display_voffset =
 Display_soffset =

%description -l pl
To jest wtyczka do lineakd. Wtyczka ta pozwala na dowi±zywanie akcji
do specjalnych klawiszy.

Ta wtyczka pozwala na wy¶wietlanie przy pomocy biblioteki xosd.
Wtyczka wymaga istnienia nastêpuj±cej opcji konfiguracyjnej w pliku
lineakd.conf:

 Display_plugin = xosd

Wtyczka rozumie równie¿ nastêpuj±ce dyrektywy konfiguracyjne:

 Display_font =
 Display_color =
 Display_pos =
 Display_align =
 Display_timeout =
 Display_hoffset =
 Display_voffset =
 Display_soffset =

%prep
%setup -q -n %{packagename}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lineakd/plugins/*.so
%{_mandir}/*/*
