Slyp

Slyp is a Powershell/Python Application that allows for managment and transfer of a single Virtual Machine between platforms: ESXi, HyperV, and EC2 from Amazon Web Services. 

## Installation

Dependecies:
Python2.7
Virtual-env
PowerCli
HyperV Cmdlets

To Download and Install
git clone http://github.com/revinkey/Slyp.git

## Usage
From Powershell change directry into the cloned directory from git clone http://github.com/revinkey/Slyp.git
to activate the virtual-env run, "./env/Scripts/activate" 

To start Slyp Run:
	python run.py

If first start edit the "config" text file manually or run slyp and select the option to set the configuration 
From there You will need a share between your HyperV machine and the Slyp server. You will need to add your AWS key and Certificate to the .aws folder inorder for AWS EC2 integration. 

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D