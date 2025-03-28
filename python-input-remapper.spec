%global debug_package %{nil}

Name:		input-remapper
Version:	2.1.1
Release:	2
URL:		https://github.com/sezanzeb/input-remapper
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	An easy to use tool to change the behaviour of your input devices.

License:	GPL-3.0
Group:		Accessability

BuildSystem: python
BuildRequires:	python
BuildRequires:	gettext
BuildRequires:  python-pynput

%description
An easy to use tool for Linux to change the behaviour of your input devices.
Supports X11, Wayland, combinations, programmable macros, joysticks, wheels,
triggers, keys, mouse-movements and more. Maps any input to any other input.

%prep
%autosetup -p1

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%doc README.md
%license LICENSE
%{_datadir}/dbus-1/system.d/inputremapper.Control.conf
%{_sysconfdir}/xdg/autostart/%{name}-autoload.desktop
%{_bindir}/%{name}*
%{_unitdir}/%{name}.service
%{_udevrulesdir}/99-%{name}.rules
%{py_sitedir}/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%exclude %dir %{_datadir}/%{name}/lang
%lang(fr) %{_datadir}/%{name}/lang/fr
%lang(fr) %{_datadir}/%{name}/lang/fr_FR
%lang(it) %{_datadir}/%{name}/lang/it
%lang(it) %{_datadir}/%{name}/lang/it_IT
%lang(pt) %{_datadir}/%{name}/lang/pt
%lang(pt) %{_datadir}/%{name}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/lang/ru
%lang(ru) %{_datadir}/%{name}/lang/ru_RU
%lang(sk) %{_datadir}/%{name}/lang/sk
%lang(sk) %{_datadir}/%{name}/lang/sk_SK
%lang(uk) %{_datadir}/%{name}/lang/uk
%lang(uk) %{_datadir}/%{name}/lang/uk_UA
%lang(zh) %{_datadir}/%{name}/lang/zh
%lang(zh) %{_datadir}/%{name}/lang/zh_CN
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/polkit-1/actions/%{name}.policy
%{_metainfodir}/*.metainfo.xml
%{_datadir}/%{name}/99*
%{_datadir}/%{name}/%{name}-autoload.desktop
%{_datadir}/%{name}/%{name}-gtk.desktop
%{_datadir}/%{name}/%{name}-large.png
%{_datadir}/%{name}/inputremapper.Control.conf
%{_datadir}/%{name}/io.github.sezanzeb.input_remapper.metainfo.xml
%{_datadir}/%{name}/style.css
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/%{name}/%{name}.policy
%{_datadir}/%{name}/%{name}.service
%{_datadir}/%{name}/%{name}.svg
