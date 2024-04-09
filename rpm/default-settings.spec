%define specrelease 1%{?dist}
%if 0%{?openeuler}
%define specrelease 1
%endif

Name:           deepin-default-settings
Version:        2021.04.13.1
Release:        %{specrelease}
Summary:        default settings for deepin destkop environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/default-settings
Source0:        default-settings-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  dde-desktop
BuildRequires:  deepin-wallpapers

%description
default settings for deepin destkop environment.

%package        -n deepin-default-settings-tuning
Summary:        default settings for deepin destkop environment
%description    -n deepin-default-settings-tuning
This package includes files to override cups default page and fcitx icon.

%prep
%autosetup -n %{name}-%{version}

%build
echo "build OK"

%install
%make_install

mkdir -p  %{buildroot}/usr/share/deepin-default-settings/google-chrome/
mkdir -p  %{buildroot}/usr/share/deepin-default-settings/fcitx/
mkdir -p  %{buildroot}/etc/

install -Dm644 tuning/google-chrome/*.tar %{buildroot}/usr/share/deepin-default-settings/google-chrome/
install -Dm644 tuning/fcitx/*.png  %{buildroot}/usr/share/deepin-default-settings/fcitx/
cp -r skel  %{buildroot}/etc/

install -d %{buildroot}%{_sysconfdir}/skel/{Desktop,Documents,Downloads,Pictures/Wallpapers,Music,Videos,.Public,.Templates}
install -d %{buildroot}%{_sysconfdir}/skel/.local/share/Trash
install -Dm644 %{_datadir}/applications/dde-computer.desktop %{buildroot}%{_sysconfdir}/skel/Desktop/dde-computer.desktop
install -Dm755 %{_datadir}/applications/dde-trash.desktop %{buildroot}%{_sysconfdir}/skel/Desktop/dde-trash.desktop
for file in `ls /usr/share/wallpapers/deepin/`
do
    ln -svf /usr/share/wallpapers/deepin/$file %{buildroot}%{_sysconfdir}/skel/Pictures/Wallpapers/$file
done

%post
## when root first login, init
if [ ! -f /root/Desktop/dde-computer.desktop ] && [ ! -f /root/Desktop/dde-trash.desktop ] ; then
    install -Dm644 /etc/skel/.config/user-dirs.dirs /root/.config/user-dirs.dirs || true
    install -d /root/{Desktop,Documents,Downloads,Pictures/Wallpapers,Music,Videos,.Public,.Templates} || true
    install -Dm644 /etc/skel/.config/autostart/dde-first-run.desktop /root/.config/autostart/dde-first-run.desktop || true
	install -m644 /etc/skel/Pictures/Wallpapers/*.jpg /root/Pictures/Wallpapers/ || true
	install -m644 /etc/skel/Music/bensound-sunny.mp3   /root//Music/ || true
fi

%post -n deepin-default-settings-tuning

for i in 16 22 24 32 48 128 ;do
    [ -f /usr/share/icons/hicolor/${i}x${i}/apps/fcitx.png ] && rm -f /usr/share/icons/hicolor/${i}x${i}/apps/fcitx.png
done
[ -f /usr/share/icons/hicolor/scalable/apps/fcitx.svg ] && rm -f /usr/share/icons/hicolor/scalable/apps/fcitx.svg
install -Dm644 /usr/share/deepin-default-settings/fcitx/fcitx.png /usr/share/icons/hicolor/16x16/apps/fcitx.png || true

[ -f /usr/share/icons/hicolor/16x16/status/fcitx-kbd.png ] && rm -f /usr/share/icons/hicolor/16x16/status/fcitx-kbd.png
install -Dm644 /usr/share/deepin-default-settings/fcitx/fcitx.png /usr/share/icons/hicolor/16x16/status/fcitx-kbd.png || true

rm -f /etc/apt/sources.list.d/google-chrome*.list
if [ -f /etc/opt/chrome/policies/recommended/defalut-plugins-settings.json ];then
    rm -f /etc/opt/chrome/policies/recommended/defalut-plugins-settings.json
fi

%files
%license LICENSE
## conflicts with file from package systemd
%exclude %{_sysconfdir}/X11/xinit/xinitrc.d/50-systemd-user.sh
## conflicts with file from package shared-mime-info
%exclude %{_datadir}/applications/mimeapps.list
%{_sysconfdir}/X11/xorg.conf.d/*.conf
%{_sysconfdir}/binfmt.d/wine.conf
%{_sysconfdir}/fonts/conf.d/*.conf
%{_sysconfdir}/lscolor-256color
%{_sysconfdir}/modprobe.d/8821ce.conf
%{_sysconfdir}/modprobe.d/iwlwifi.conf
%{_sysconfdir}/skel/*
%{_sysconfdir}/skel/.config/SogouPY/sogouEnv.ini
%{_sysconfdir}/skel/.config/Trolltech.conf
%{_sysconfdir}/skel/.config/autostart/dde-first-run.desktop
%{_sysconfdir}/skel/.config/deepin/qt-theme.ini
%{_sysconfdir}/skel/.config/user-dirs.dirs
%{_sysconfdir}/skel/.icons/default/index.theme
%{_sysconfdir}/skel/Music/bensound-sunny.mp3
%{_sysconfdir}/sudoers.d/01_always_set_sudoers_home
/lib/udev/rules.d/99-deepin.rules
%{_libexecdir}/dde-first-run
#服务器不需要桌面版调优参数
%exclude %{_sysctldir}/deepin.conf
%{_datadir}/applications/deepin/dde-mimetype.list
%{_datadir}/fontconfig/conf.avail/*.conf
%{_datadir}/mime/packages/deepin-workaround.xml
%{_datadir}/mime/wine-ini.xml
%{_datadir}/music/bensound-sunny.mp3

%files  -n deepin-default-settings-tuning
%{_datadir}/deepin-default-settings/google-chrome/*.tar
%{_datadir}/deepin-default-settings/fcitx/*.png

%changelog
* Tue Apr 21 2021 uoser <uoser@uniontech.com> - 2021.04.13.1-1
- update to 2021.04.13.1
