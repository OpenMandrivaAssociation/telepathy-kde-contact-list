%define srcname ktp-contact-list 

Summary:        Telepathy contact list application
Name:           telepathy-kde-contact-list
Version:	0.5.1
Release:        1
Url:            https://projects.kde.org/projects/extragear/network/telepathy/ktp-contact-list
Source0:        ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:        GPLv2+
Group:          Networking/Instant messaging
BuildRequires:  telepathy-kde-common-internals-devel >= %{version}

Requires:       telepathy-kde-text-ui
Requires:       telepathy-kde-accounts-kcm
Requires:       telepathy-kde-auth-handler
Requires:       telepathy-kde-filetransfer-handler
Requires:       telepathy-kde-integration-module
Requires:       telepathy-kde-approver
Requires:       telepathy-mission-control

#Needed for Jabber
Requires: telepathy-gabble
# needed by MSN
Suggests: telepathy-butterfly
# various protocol provided by libpurple
Suggests: telepathy-haze
# needed for local XMPP
Suggests: telepathy-salut
# needed for irc
Suggests: telepathy-idle
# needed for voip
Suggests: gstreamer0.10-farsight2

Suggests:       telepathy-kde-contact-applet

# Added on 2011/11/27 
Obsoletes:      telepathy-contact-list < 0.2.0-0

%description
Telepathy contact list application.

%files -f ktp-contactlist.lang
%{_kde_bindir}/ktp-contactlist
%{_kde_datadir}/applications/kde4/ktp-contactlist.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang ktp-contactlist

