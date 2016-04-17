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
        with open('config.INI', 'w') as configfile:    # save
            parser.write(configfile)
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
        print("Now for the AWS setup")
        aws=raw_input("What is the AWS Instance ID: ")
        parser.set('AWS','instance_id',aws)
        aws_s3=raw_input("What is the name of your S3 Bucket: ")
        parser.set('AWS','s3',aws_s3)
        aws_image=raw_input("What is the exported image name to look for in S3: ")
        parser.set('AWS','image',aws_image)

      
        with open('config.INI', 'w') as configfile:    # save
            parser.write(configfile)
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


