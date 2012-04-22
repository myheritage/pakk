<?php

## Have a look in defaults.inc.php for examples of settings you can set here. DO NOT EDIT defaults.inc.php!

### Database config
$config['db_host'] = "localhost";
$config['db_user'] = "USERNAME";
$config['db_pass'] = "PASSWORD";
$config['db_name'] = "observium";

### Locations
$config['install_dir'] 	= "/usr/share/observium";
$config['html_dir']	    = $config['install_dir'] . "/html";
$config['rrd_dir'] 	    = "/var/lib/observium/rrd";
$config['log_file']     = "/var/log/observium/observium.log";
# $config['collectd_dir'] = "/var/lib/collectd/rrd/";

$config['fping'] = "/usr/sbin/fping"

### Thie should *only* be set if you want to *force* a particular hostname/port
### It will prevent the web interface being usable form any other hostname
#$config['base_url']	= "http://observium.company.com";

### Enable the below to use rrdcached. be sure rrd_dir is within the rrdcached dir
### and that your web server has permission to talk to rrdcached.
#$config['rrdcached']    = "unix:/var/run/rrdcached.sock";

### Default community
$config['snmp']['community'] = array("public");

### Authentication Model
$config['auth_mechanism'] = "mysql"; # default, other options: ldap, http-auth
#$config['http_auth_guest'] = "guest"; # remember to configure this user if you use http-auth

### List of networks to allow scanning-based discovery
$config['nets'][] = "172.22.0.0/16";
$config['nets'][] = "192.168.0.0/24";

$config['mono_font'] = "/usr/share/fonts/dejavu/DejaVuLGCSansMono.ttf"

include("includes/static-config.php");

?>
