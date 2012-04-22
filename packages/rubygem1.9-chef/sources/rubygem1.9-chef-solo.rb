# Configuration file for chef-solo

log_level    :info
log_location STDOUT
Mixlib::Log::Formatter.show_time = true

file_cache_path    "/var/cache/chef/client"

cookbook_path [ "/var/lib/chef/cookbooks" ]
role_path     [ "/var/lib/chef/roles" ]
#recipe_url    "http://www.example.com/chef/cookbooks.tar.gz"

#json_attribs "/var/tmp/node.json"
#json_attribs "http://www.example.com/chef/node.json"
