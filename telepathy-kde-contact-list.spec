%define rel 1

Summary:	Telepathy contact list application
Name:		telepathy-kde-contact-list
Version:	0.2.0
Release:	%mkrel %{rel}
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-contact-list
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel

Requires:       telepathy-kde-text-ui
Requires:       telepathy-kde-accounts-kcm
Requires:       telepathy-kde-auth-handler
Requires:       telepathy-kde-filetransfer-handler
Requires:       telepathy-kde-integration-module
Requires:       telepathy-kde-approver
Requires:       telepathy-mission-control

Suggests:       telepathy-kde-contact-applet

# Added on 2011/11/27 
Provides:       telepathy-contact-list = %version-%release
Obsoletes:      telepathy-contact-list < 0.2.0-0

%description
Telepathy contact list application.

%files -f telepathy-kde-contactlist.lang
%{_kde_bindir}/telepathy-kde-contactlist
%{_kde_datadir}/apps/ktelepathy/ktelepathy.notifyrc
%{_kde_datadir}/applications/kde4/telepathy-kde-contactlist.desktop
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang telepathy-kde-contactlist


