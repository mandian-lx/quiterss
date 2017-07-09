%define	oname QuiteRSS
%define lname %(echo %oname | tr [:upper:] [:lower:])

Summary:	RSS/Atom feed reader written on Qt
Name:		%{lname}
Version:	0.18.5
Release:	0
License:	GPLv3+
Group:		Networking/News
URL:		https://quiterss.org/
Source0:	https://quiterss.org/files/%{version}/%{oname}-%{version}-src.tar.gz
Patch0:		%{name}-0.18.5-translations.patch

BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	qtsingleapplication-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(sqlite3)

%description
QuiteRSS is RSS/Atom feed reader written on Qt.

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README.md
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
%apply_patches

# remove bundled
rm -rf 3rdparty/qtsingleapplication
rm -rf 3rdparty/sqlite

%build
%qmake_qt5 PREFIX=%{_prefix} SYSTEMQTSA=1
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

# locales
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

