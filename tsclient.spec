Summary:	Terminal Server Client - a frontend for rdesktop for the GNOME2 platform
Summary(pl):	Terminal Server Client - frontend dla rdesktop dla platformy GNOME2
Name:		tsclient
Version:	0.148
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnomepro.com/tsclient/%{name}-%{version}.tar.gz
# Source0-md5:	06a6ff59b7c8ca26d4ea37340ed77423
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnomepro.com/tsclient/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	gnome-panel-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 1:2.6.0
BuildRequires:	intltool >= 0.27
BuildRequires:	pkgconfig
Requires:	rdesktop >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal Server Client is a frontend for rdesktop for the GNOME2
platform.

%description -l pl
Terminal Server Client to frontend dla programu rdesktop dla platformy
GNOME2.

%prep
%setup -q
%patch0 -p1

mv -f po/{nl_NL,nl}.po
mv -f po/{nl_NL,nl}.gmo
mv -f po/{pl_PL,pl}.po
mv -f po/{pl_PL,pl}.gmo
mv -f po/{pt_PT,pt}.po
mv -f po/{pt_PT,pt}.gmo
mv -f po/{se,sv}.po
mv -f po/{se,sv}.gmo

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_bindir}/tsclient
%attr(755,root,root) %{_libdir}/tsclient-applet
%{_libdir}/bonobo/servers/GNOME_TSClientApplet.server
%{_datadir}/application-registry/tsclient.*
%{_datadir}/mime-info/tsclient.*
%{_desktopdir}/tsclient.desktop
%{_pixmapsdir}/tsclient
%{_pixmapsdir}/tsclient.png
%{_mandir}/man1/*
