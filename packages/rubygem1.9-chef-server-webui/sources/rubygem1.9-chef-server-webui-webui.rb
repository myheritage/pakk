# Configuration file for chef-server-webui

log_level    :info
log_location STDOUT
Mixlib::Log::Formatter.show_time = true

chef_server_url "http://localhost:4000"
ssl_verify_mode :verify_none

file_cache_path    "/var/cache/chef/server"

signing_ca_cert  "/etc/chef/certificates/cert.pem"
signing_ca_key   "/etc/chef/certificates/key.pem"
signing_ca_user  "chef"
signing_ca_group "chef"

web_ui_key         "/etc/chef/webui.pem"
web_ui_client_name "chef-webui"
