%define		packagename	lineak_xosdplugin

Summary:	This is the XOSD Onscreen Display plugin for the lineakd daemon.
Summary(pl):	To jest XOSD Onscreen Display plugin dla demona lineakd.
Name:		lineak-plugin-xosd
Version:	0.8.4
Release:	0.9
License:	GPL
Url:		http://lineak.sourceforge.net
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{packagename}-%{version}.tar.gz
//Patch0:%{name}-DESTDIR.patch
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lineakd >= %{version}
Requires:	lineakd >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of plugins for lineakd. The plugins allow binding
actions to special keys. This plugin allows display using the xosd
library. It requires that you have the following configuration option
in your lineakd.conf file:

 Display_plugin = xosd

It also understands the following configuration directives.

 Display_font = 
 Display_color = 
 Display_pos = 
 Display_align =
 Display_timeout =
 Display_hoffset = 
 Display_voffset = 
 Display_soffset =

%description -l pl
To jest zbiór wtyczek do lineakd. Wtyczki te pozwalają na
dowiązywanie akcji do specjalnych klaiwszy. Ta wtyczka pozwala na
wyświetlanie przy pomocy biblioteki xosd. Wtyczka wymaga istnienia
następującej opcji konfiguracyjnej w Twoim pliku lineakd.conf:

 Display_plugin = xosd

Wtyczka rozumie również następujące dyrektywy konfiguracyjne.

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
#%patch0 -p1

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
%{_libdir}/lineakd/plugins/*
%{_sysconfdir}/*
%{_mandir}/*/*
