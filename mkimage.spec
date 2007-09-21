Name: mkimage
Version: 0.0.2
Release: alt1

Summary: Simple image creator
License: GPL
Group: Development/Other

Packager: Alexey Gladkov <legion@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

%description
Simple image creator

%prep
%setup -q

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_datadir/%name
%doc example

%changelog
* Fri Sep 21 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt1
- New version (0.0.2).

* Thu Aug 30 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- First build for ALT Linux.
