# Configuration file for chef-client

log_level    :info
log_location STDOUT
Mixlib::Log::Formatter.show_time = true

chef_server_url "http://localhost:4000"
ssl_verify_mode :verify_none

file_cache_path  "/var/cache/chef/client"
file_backup_path "/var/lib/chef/client/backup"
cache_options({ :path => "/var/cache/chef/client/checksums", :skip_expires => true })

validation_client_name "chef-validator"
validation_key         "/etc/chef/validation.pem"
client_key             "/etc/chef/client.pem"
signing_ca_user        "chef"
