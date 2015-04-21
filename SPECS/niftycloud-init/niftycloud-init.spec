Summary:	NIFTY Cloud Init
Name:		niftycloud-init
Version:	1.0.0
Release:	1
License:	Apache License
Group:		System Environment/Base
URL:		http://cloud.nifty.com/
Source0:	niftycloud-init-1.0.0.tar.gz
Source1:	niftycloud-init.service
Patch0:		niftycloud-init-fixes-for-photon.patch
Vendor:		NIFTY Corp.
Distribution:	Photon
Provides:	niftycloud-init
BuildArch:	noarch
Requires:       open-vm-tools
BuildRequires:  systemd

%description
The package for NIFTY Cloud init scripts

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/systemd/system
mkdir -p %{buildroot}/usr/share/niftycloud
install -p -m644 %{SOURCE1} %{buildroot}/lib/systemd/system/niftycloud-init.service
install -p -m755 garp %{buildroot}/usr/share/niftycloud/garp
install -p -m755 niftycloud_init %{buildroot}/usr/share/niftycloud/niftycloud_init

%clean
rm -rf %{buildroot}

%post
%systemd_post niftycloud-init.service

%preun
%systemd_preun niftycloud-init.service

%postun
%systemd_postun niftycloud-init.service

%files
%defattr(-,root,root)
/usr/share/niftycloud/garp
/usr/share/niftycloud/niftycloud_init
/lib/systemd/system/niftycloud-init.service
