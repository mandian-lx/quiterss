%define oname	QuiteRSS

Name:		quiterss
Summary:	RSS/Atom feed reader written on Qt
Version:	0.9.1
Release:	1
License:	GPLv3+
Group:		Networking/News
URL:		https://code.google.com/p/quite-rss/
Source0:	https://quite-rss.googlecode.com/files/%{oname}-%{version}-src.tar.gz
Patch0:		QuiteRSS-0.9.1-3rdparty.patch
BuildRequires:	qt4-devel
BuildRequires:	qtsingleapplication-devel
BuildRequires:	sqlite3-devel

%description
QuiteRSS is RSS/Atom feed reader written on Qt.

%prep
%setup -q -n %{oname}-%{version}-src
%patch0 -p1
find . -type f -executable -exec chmod a-x {} \;

%build
%qmake_qt4
%make

%install
make install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/sound/notification.wav
