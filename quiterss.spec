%define	oname		QuiteRSS
#define	oversion	0.13.0.2610
%define	qtsingleapp	%{_prefix}/lib/qt4/include/QtSolutions/

Name:		quiterss
Summary:	RSS/Atom feed reader written on Qt
Version:	0.17.0
Release:	1
License:	GPLv3+
Group:		Networking/News
URL:		https://code.google.com/p/quite-rss/
Source0:	http://quiterss.org/files/0.17.0/QuiteRSS-0.17.0-src.tar.bz2
Patch1:		QuiteRSS-0.17.0-fix-install-prefix.patch
BuildRequires:	qt4-devel >= 4.7.0
BuildRequires:	qtsingleapplication-devel
BuildRequires:	sqlite3-devel
BuildRequires:	pkgconfig(phonon)

%description
QuiteRSS is RSS/Atom feed reader written on Qt.

%prep
%setup -qn %{oname}-%{version}-src
#patch0 -p1
%patch1 -p1
find . -type f -executable -exec chmod a-x {} \;

%build
export CFLAGS="%{optflags}"
%qmake_qt4 SYSTEMQTSA=%{qtsingleapp}
%make

%install
make install INSTALL_ROOT=%{buildroot}

%if %{mdvver} >= 201200
%find_lang %{name} --with-qt
%else
cat > %{name}.lang << EOF
%lang(cs_cz) /usr/share/quiterss/lang/quiterss_cs_cz.qm
%lang(de) /usr/share/quiterss/lang/quiterss_de.qm
%lang(en) /usr/share/quiterss/lang/quiterss_en.qm
%lang(es) /usr/share/quiterss/lang/quiterss_es.qm
%lang(fa) /usr/share/quiterss/lang/quiterss_fa.qm
%lang(fr) /usr/share/quiterss/lang/quiterss_fr.qm
%lang(hu) /usr/share/quiterss/lang/quiterss_hu.qm
%lang(it) /usr/share/quiterss/lang/quiterss_it.qm
%lang(ja) /usr/share/quiterss/lang/quiterss_ja.qm
%lang(ko) /usr/share/quiterss/lang/quiterss_ko.qm
%lang(lt) /usr/share/quiterss/lang/quiterss_lt.qm
%lang(nl) /usr/share/quiterss/lang/quiterss_nl.qm
%lang(pl) /usr/share/quiterss/lang/quiterss_pl.qm
%lang(pt_br) /usr/share/quiterss/lang/quiterss_pt_br.qm
%lang(ru) /usr/share/quiterss/lang/quiterss_ru.qm
%lang(sr) /usr/share/quiterss/lang/quiterss_sr.qm
%lang(sv) /usr/share/quiterss/lang/quiterss_sv.qm
%lang(uk) /usr/share/quiterss/lang/quiterss_uk.qm
%lang(zh_cn) /usr/share/quiterss/lang/quiterss_zh_cn.qm
EOF
%endif


%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/sound/notification.wav
%{_datadir}/%{name}/style/*.qss
%{_datadir}/%{name}/style/*.css
