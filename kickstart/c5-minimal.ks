#-----------------------------------------------------------------------------
# installation
#-----------------------------------------------------------------------------
install
cdrom

#-----------------------------------------------------------------------------
# system configuration
#-----------------------------------------------------------------------------
keyboard us
lang en_US.UTF-8
timezone --utc UTC
authconfig --enableshadow --enablemd5
rootpw password
selinux --disabled

#-----------------------------------------------------------------------------
# network configuration
#-----------------------------------------------------------------------------
network --device eth0 --bootproto dhcp
firewall --disabled

#-----------------------------------------------------------------------------
# storage configuration
#-----------------------------------------------------------------------------
bootloader --location=mbr
clearpart --all
# part swap --size=2048
part /    --size=4096
part /var --size=1    --grow

#-----------------------------------------------------------------------------
# packages
#-----------------------------------------------------------------------------
%packages --nobase
@core
man
man-pages
-atk
-bitstream-vera-fonts
-cairo
-cryptsetup-luks
-cups-libs
-dbus
-dbus-glib
-dbus-libs
-dhcpv6-client
-ecryptfs-utils
-fontconfig
-freetype
-gnu-efi
-gnutls
-gtk2
-hal
-hicolor-icon-theme
-kudzu
-libgcrypt
-libgpg-error
-libhugetlbfs
-libjpeg
-libpng
-libtiff
-libusb
-libX11
-libXau
-libXcursor
-libXdmcp
-libXext
-libXfixes
-libXft
-libXi
-libXinerama
-libXrandr
-libXrender
-pango
-pm-utils
-prelink
-setools
-tcl
-trousers
-udftools
-xorg-x11-filesystem
