Summary:	Terminal Server Client - a frontend for rdesktop for the GNOME2 platform
Summary(pl):	Terminal Server Client - frontend dla rdesktop dla platformy GNOME2
Name:		tsclient
Version:	0.124
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnomepro.com/tsclient/%{name}-%{version}.tar.gz
# Source0-md5:	0c03dc2fa332e9acf32945182114a320
URL:		http://www.gnomepro.com/tsclient/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
Requires:	rdesktop >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal Server Client is a frontend for rdesktop for the GNOME2
platform.

%description -l pl
Terminal Server Client to frontend dla programu rdesktop dla platformy
GNOME2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_iconsdir}/gnome/48x48/mimetypes
install gnome-mime-application-x-rdp.png $RPM_BUILD_ROOT%{_iconsdir}/gnome/48x48/mimetypes

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
%{_iconsdir}/gnome/48x48/mimetypes/*
%{_pixmapsdir}/tsclient
%{_pixmapsdir}/tsclient.png
