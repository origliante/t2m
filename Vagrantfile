# -*- mode: ruby -*-

Vagrant.configure("2") do |config|

    config.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--cpus", "1"]
        v.customize ["modifyvm", :id, "--memory", "1024"]
        v.customize ["modifyvm", :id, "--usb", "on"]
        v.customize ["modifyvm", :id, "--usbehci", "off"]
    end

    config.vm.box = "minimal/centos7"
    config.vm.box_version = "7.0"

    config.vm.network "private_network", ip: "192.168.42.42"

    config.vm.provision "shell", path: "provisioning/centos.sh"
    config.vm.provision "shell", inline: <<-SHELL
        killall -9 python
        python /vagrant/t2m.py 0.0.0.0 1999 &
    SHELL

    #TODO
    # Enable provisioning with Puppet stand alone.
    #config.vm.provision :puppet do |puppet|
        ## tell Puppet where to find the hiera config
    #    puppet.options = "--hiera_config hiera.yaml"

        ## boilerplate Vagrant/Puppet config
    #    puppet.manifests_path = "puppet/manifests"
    #    puppet.manifest_file = "default.pp"
    #    puppet.module_path  = "puppet/modules"

        ## custom facts provided to Puppet
    #    puppet.facter = {
            ## tells default.pp that we're running in Vagrant
    #        "is_vagrant" => true,
    #    }
    #end
end
