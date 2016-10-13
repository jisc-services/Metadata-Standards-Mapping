Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2 python-virtualenv python-pip
  SHELL
  config.vm.provision "shell", privileged: FALSE, inline: <<-SHELL
    cd /vagrant
    virtualenv venv
    source venv/bin/activate
    pip install django markdown
    ./build.sh
  SHELL
  config.vm.provision "shell", inline: <<-SHELL
    rm -rf /var/www/html
    ln -s /vagrant/build /var/www/html
  SHELL
end
