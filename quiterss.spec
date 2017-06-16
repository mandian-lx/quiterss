%define	oname	QuiteRSS
%define lname %(echo %oname | tr [:upper:] [:lower:])

%bcond_with qt5

Summary:	RSS/Atom feed reader written on Qt
Name:		%{lname}
Version:	0.18.5
Release:	0
License:	GPLv3+
Group:		Networking/News
URL:		https://quiterss.org/
Source0:	https://quiterss.org/files/%{version}/%{oname}-%{version}-src.tar.gz

BuildRequires:	desktop-file-utils
%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Printsupport)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	qtsingleapplication-devel
%else
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(QtXml)
BuildRequires:	pkgconfig(QtSql)
BuildRequires:	qt5singleapplication-devel #FIXME
%endif
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(sqlite3)

%description
QuiteRSS is RSS/Atom feed reader written on Qt.

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/sound/notification.wav
%{_datadir}/%{name}/style/*.qss
%{_datadir}/%{name}/style/*.css

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}

# remove bundled
rm -rf 3rdparty/qtsingleapplication
rm -rf 3rdparty/sqlite

%build
%setup_compile_flags
%if %{with qt5}
%qmake_qt5  PREFIX=%{_prefix} SYSTEMQTSA=true
%else
%qmake_qt4  PREFIX=%{_prefix} SYSTEMQTSA=true
%endif
%make

%install
%make_install INSTALL_ROOT=%{buildroot}

# locales
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

