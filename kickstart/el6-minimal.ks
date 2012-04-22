#-----------------------------------------------------------------------------
# http://pakk.96b.it/kickstart
# Minimal kickstart installation for RHEL 6
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# installation
#-----------------------------------------------------------------------------
install
text
cdrom
reboot

#-----------------------------------------------------------------------------
# system configuration
#-----------------------------------------------------------------------------
keyboard us
lang en_US.UTF-8
timezone --utc UTC
authconfig --enableshadow --passalgo=sha512 --enablefingerprint
rootpw password
selinux --disabled

#-----------------------------------------------------------------------------
# network configuration
#-----------------------------------------------------------------------------
firewall --disabled
network --device eth0 --bootproto dhcp

#-----------------------------------------------------------------------------
# storage configuration
#-----------------------------------------------------------------------------
bootloader --location=mbr --append="crashkernel=auto rhgb quiet"
clearpart --all

# with LVM
part /boot --fstype=ext4 --size=128
part pv.sys --size=1 --grow
volgroup vg.sys --pesize=4096 pv.sys
# logvol swap --size=2048
logvol /    --fstype=ext4 --size=4096 --name=lv.slash --vgname=vg.sys
logvol /var --fstype=ext4 --size=1    --name=lv.var   --vgname=vg.sys --grow

# without LVM
# part swap --size=2048
# part /    --fstype=ext4 --size=4096
# part /var --fstype=ext4 --size=1    --grow

#-----------------------------------------------------------------------------
# packages
#-----------------------------------------------------------------------------
repo --name="Red Hat Enterprise Linux" --baseurl=file:///mnt/source --cost=100
%packages --nobase
@core
-aic94xx-firmware
-atmel-firmware
-audit
-b43-openfwwf
-bfa-firmware
-checkpolicy
-cryptsetup-luks
-cryptsetup-luks-libs
-dbus-glib
-dbus-python
-device-mapper-multipath
-device-mapper-multipath-libs
-efibootmgr
-fcoe-utils
-ipw2100-firmware
-ipw2200-firmware
-ivtv-firmware
-iwl1000-firmware
-iwl3945-firmware
-iwl4965-firmware
-iwl5000-firmware
-iwl5150-firmware
-iwl6000-firmware
-iwl6050-firmware
-kpartx
-libertas-usb8388-firmware
-libgudev1
-libselinux-utils
-libsemanage
-m2crypto
-m4
-pciutils-libs
-policycoreutils
-pygobject2
-pyOpenSSL
-python-dmidecode
-python-ethtool
-python-gudev
-ql2100-firmware
-ql2200-firmware
-ql23xx-firmware
-ql2400-firmware
-ql2500-firmware
-rhn-check
-rhn-client-tools
-rhnlib
-rhnsd
-rhn-setup
-rt61pci-firmware
-rt73usb-firmware
-selinux-policy
-selinux-policy-targeted
-usermode
-ustr
-xorg-x11-drv-ati-firmware
-yum-rhn-plugin
-zd1211-firmware
%end

#-----------------------------------------------------------------------------
# post install
#-----------------------------------------------------------------------------
%post
# now that authconfig has been executed, clean up useless packages
yum remove -y authconfig newt slang system-config-firewall-base
