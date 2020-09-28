Name:           deepin-default-settings
Version:        2020.09.11-1
Release:        1
Summary:        deepin-default-settings
License:        GPLv3
URL:            %{gourl}
Source0:        deepin-default-settings_%{version}.orig.tar.xz

%description
deepin-default-settings

%prep
%autosetup

%install
%make_install

%files
/etc/
/usr/share
/usr/bin/dde-first-run
/usr/lib/sysctl.d/deepin.conf
/lib/udev/rules.d/99-deepin.rules
/usr/share/fontconfig/conf.avail/