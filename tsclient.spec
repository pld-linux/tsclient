Summary:	Terminal Server Client - a frontend for rdesktop for the GNOME2 platform
Summary(pl.UTF-8):	Terminal Server Client - frontend dla rdesktop dla platformy GNOME2
Name:		tsclient
Version:	0.150
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/tsclient/%{name}-%{version}.tar.gz
# Source0-md5:	1dc95fbdbcf4344d05114e1f43bf32ea
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnomepro.com/tsclient/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnome-panel-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.27
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libSM-devel
Requires:	rdesktop >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal Server Client is a frontend for rdesktop for the GNOME2
platform.

%description -l pl.UTF-8
Terminal Server Client to frontend dla programu rdesktop dla platformy
GNOME2.

%prep
%setup -q
%patch0 -p0

mv -f po/{nl_NL,nl}.po
mv -f po/{pl_PL,pl}.po
mv -f po/{pt_PT,pt}.po

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
