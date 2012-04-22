# Configuration file for chef-expander

solr_url "http://localhost:8983/solr"

amqp_host  "localhost"
amqp_port  "5672"
amqp_user  "chef"
amqp_pass  File.read('/etc/chef/amqp_passwd').chomp
amqp_vhost "/chef"
