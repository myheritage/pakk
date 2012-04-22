# Configuration file for chef-solr

user  "chef"
group "chef"

log_location STDOUT
Mixlib::Log::Formatter.show_time = true

search_index_path    "/var/lib/chef/search_index"

solr_jetty_path "/var/lib/chef/solr/jetty"
solr_home_path  "/var/lib/chef/solr/home"
solr_data_path  "/var/cache/chef/solr/data"
solr_heap_size  "256M"

solr_url        "http://localhost:8983"
#solr_java_opts  "-DSTART=#{Chef::Config[:solr_jetty_path]}/etc/start.config"
