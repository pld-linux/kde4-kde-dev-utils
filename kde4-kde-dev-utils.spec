%define		orgname		kde-dev-utils
%define		_state		stable
%define		qtver		4.8.1

Summary:	An set of utils useful for building and maintaining KDE
Summary(pl.UTF-8):	Zestaw programów do kompilowania i utrzymywania KDE
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b43b6e422ba8b71ad382604a2982fa95
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	antlr
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	subversion-devel >= 0.37.0
BuildRequires:	utempter-devel
Suggests:	/usr/bin/perl
Obsoletes:	kde4-kdesdk-kpartloader
Obsoletes:	kde4-kdesdk-kstartperf
Obsoletes:	kde4-kdesdk-kuiviewer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains:
kpartloader - UML Modeller.
kstartperf - measures startup time for KDE applications.
kuiviewer - Qt Designer UI file Viewer.

%description -l pl.UTF-8
Pakiet zawiera:
kpartloader - modeler UML.
kstartperf - narzędzie służące do pomiaru czasu ładowania aplikacji KDE.
kuiviewer - przeglądarka plików UI generowanych przez Qt designera.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libktrace.so.4.*
%ghost %{_libdir}/libktrace.so.4
%attr(755,root,root) %{_bindir}/demangle
%attr(755,root,root) %{_bindir}/kminspector
%attr(755,root,root) %{_bindir}/kmmatch
%attr(755,root,root) %{_bindir}/kmtrace
%attr(755,root,root) %{_bindir}/kpartloader
%attr(755,root,root) %{_bindir}/kstartperf
%attr(755,root,root) %{_bindir}/kuiviewer
%attr(755,root,root) %{_libdir}/kde4/kstartperf.so
%attr(755,root,root) %{_libdir}/kde4/kuiviewerpart.so
%attr(755,root,root) %{_libdir}/kde4/quithumbnail.so
%{_mandir}/man1/demangle.1*
%{_includedir}/kprofilemethod.h
%{_desktopdir}/kde4/kuiviewer.desktop
%{_datadir}/apps/kmtrace
%{_datadir}/apps/kpartloader
%{_datadir}/apps/kuiviewer
%{_datadir}/apps/kuiviewerpart
%{_iconsdir}/hicolor/*x*/apps/kuiviewer.png
%{_datadir}/kde4/services/designerthumbnail.desktop
%{_datadir}/kde4/services/kuiviewer_part.desktop
