from ConfigParser import SafeConfigParser

class config():
  # Maintenance and Core Functionality
    def changeOptions(parser):
        print("------------------------------")
        print("            SLYP")
        print("------------------------------")
        print("Welcome to Slyp please configure the settings:")
        
        esxi=raw_input("What is the esxi IP/hostname: ")
        parser.set('VCenter', 'esxi',esxi)
        vcenter=raw_input("What is the Vcenter IP/hostname: ")
        parser.set('VCenter','vcenter',vcenter)
        port=raw_input("What is the vcenter port(443): ")
        parser.set('VCenter','port',port)
        Vuser=raw_input("What is the vcenter username: ")
        parser.set('VCenter','Vuser',Vuser)
        vcenterpw=raw_input("What is the vcenter password: ")
        parser.set('VCenter','vcenterpw',vcenterpw)
        esxiuser=raw_input("What is the esxi user: ")
        parser.set('VCenter','esxiuser',esxiuser)
        esxipw=raw_input("What is the esxi password: ")
        parser.set('VCenter','esxipw',esxipw)
        datacenter_name=raw_input("What is the datacenter_name: ")
        parser.set('VCenter','datacenter_name',datacenter_name)
        datastore_name=raw_input("What is the datastore_name: ")
        parser.set('VCenter','datastore_name',datastore_name)
        cluster_name=raw_input("What is the cluster_name: ")
        parser.set('VCenter','cluster_name',cluster_name)
        vmdk_path=raw_input("What is the vmdk_path: ")
        parser.set('VCenter','vmdk_path',vmdk_path)
        ovf_path=raw_input("What is the ovf_path: ")
        parser.set('VCenter','ovf_path',ovf_path)
        vmnameVC=raw_input("What is the vmname: ")
        parser.set('VCenter','vmnameVC',vmnameVC)
        print("------------------------------")
        print("Now for the hyperV setup")
        hyperv=raw_input("What is the hyperV hostname: ")
        parser.set('HyperV','hyperv',hyperv)
        xml_path=raw_input("What is the xml path: ")
        parser.set('HyperV','xml_path',xml_path)
        vmnameHV=raw_input("What is the vmname: ")
        parser.set('HyperV','vmnameHV',vmnameHV)
        vhd_path=raw_input("What is the vhd path: ")
        parser.set('HyperV','vhd_path',vhd_path)

      
        print("------------------------------")


    parser = SafeConfigParser()
    parser.read('config.ini')
    sel=raw_input("Would you like to change this config?(y/n):  ")
    if sel in ("y","Y"):
        changeOptions(parser);
    else:
        for section in parser.sections():
            print section
            for name, value in parser.items(section):
                print '  %s = %r' % (name, value)


