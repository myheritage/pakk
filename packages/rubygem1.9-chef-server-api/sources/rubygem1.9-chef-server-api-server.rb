# Configuration file for chef-server

log_level          :warn
log_location       STDOUT
Mixlib::Log::Formatter.show_time = true

chef_server_url    "http://localhost:4000"
ssl_verify_mode    :verify_none

cookbook_path      [ "/var/lib/chef/cookbooks" ]
cookbook_tarball_path "/var/lib/chef/cookbook-tarballs"

node_path       "/var/lib/chef/nodes"
sandbox_path    "/var/cache/chef/sandboxes"
checksum_path   "/var/cache/chef/checksums/server"
cache_options({ :path => "/var/cache/chef/server/checksums", :skip_expires => true })
file_cache_path "/var/cache/chef/server"

signing_ca_cert  "/etc/chef/certificates/cert.pem"
signing_ca_key   "/etc/chef/certificates/key.pem"
signing_ca_user  "chef"
signing_ca_group "chef"

validation_client_name "chef-validator"
validation_key         "/etc/chef/validation.pem"
client_key             "/etc/chef/client.pem"

amqp_pass File.read('/etc/chef/amqp_passwd').chomp

couchdb_database "chef"
