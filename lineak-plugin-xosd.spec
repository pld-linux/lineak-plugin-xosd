%define		packagename	lineak-xosdplugin

Summary:	XOSD On-screen Display plugin for the lineakd daemon
Summary(pl.UTF-8):   Wtyczka XOSD On-screen Display dla demona lineakd
Name:		lineak-plugin-xosd
Version:	0.9
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{packagename}-%{version}.tar.gz
# Source0-md5:	295bba616b3b74264385b14b242947a4
URL:		http://lineak.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lineakd-devel >= %{version}
BuildRequires:	sed >= 4.0
BuildRequires:	xosd-devel
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

%description -l pl.UTF-8
To jest wtyczka do lineakd. Wtyczka ta pozwala na dowiązywanie akcji
do specjalnych klawiszy.

Ta wtyczka pozwala na wyświetlanie przy pomocy biblioteki xosd.
Wtyczka wymaga istnienia następującej opcji konfiguracyjnej w pliku
lineakd.conf:

 Display_plugin = xosd

Wtyczka rozumie również następujące dyrektywy konfiguracyjne:

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

# kill plugin dir existence test
sed -i -e 's/test ! -d \$pdir/false/' admin/lineak.m4.in
cat admin/{acinclude.m4.in,lineak.m4.in} > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-lineak-plugindir=%{_libdir}/lineakd/plugins

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lineakd/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lineakd/plugins/xosdplugin.so
%{_mandir}/man1/lineak_xosdplugin.1*
