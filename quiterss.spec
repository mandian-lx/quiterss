%define oname	QuiteRSS

Name:		quiterss
Summary:	RSS/Atom feed reader written on Qt
Version:	0.12.5
Release:	%mkrel 1
License:	GPLv3+
Group:		Networking/News
URL:		https://code.google.com/p/quite-rss/
Source0:	https://quite-rss.googlecode.com/files/%{oname}-%{version}-src.tar.bz2
Patch0:		QuiteRSS-0.12.4-not-use-3rdparty.patch
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


%changelog
* Fri May 10 2013 Giovanni Mariani <mc2374@mclink.it> 0.12.5-1
- New release 0.12.5
- Fixed file list

* Sat Mar 30 2013 Giovanni Mariani <mc2374@mclink.it> 0.12.4-1
- New release 0.12.4
- Remade P0 (there are a couples of files hardcoding the sqlite3.h
  header path)
- Updated the translations list
- Fixed file list
- Added some docs

* Thu Jun 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.1-1
+ Revision: 807381
- update to 0.9.1

* Thu Apr 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.8.6-1
+ Revision: 792009
- imported package quiterss

