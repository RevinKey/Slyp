# Main Wrapper
from AWSlyp import AWSlyp
from HyperVSlyp import hyperV
from VCSlyp import vcenter
import subprocess
import os
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('config.ini')
AWS = AWSlyp()
def AWSPowerOn():
    AWS.powerOn(parser.get('AWS','instance_id'))

def AWSStop():
    AWS.powerOff(parser.get('AWS','instance_id'))

def AWSImport():
    AWS.vmImport(parser.get('AWS','s3'), parser.get('AWS','image'))
    print("Importing to AWS")
    raw_input("Press Enter to continue...")

def AWSExport():
    AWS.vmExport(parser.get('AWS','instance_id'), parser.get('AWS','s3'))
    print("Exorting from AWS")
    
def logo():
    #os.system('cls')
    print("                                                           .                                                           ")
    print("                                                     ,  .           .,                                                 ")
    print("                                                  ..  .            #%%%                                                ")
    print("                                                      .%%%%%%(   ,%%%%.                                                ")
    print("                                                      %%%%%%%%* #%%%(                                                  ")
    print("                                              /#(,    #%%%%%%%,%%%%,                                                   ")
    print("                           .,*,.             .%%%%%%%/./%%%%(*%%%%.                                                    ")
    print("                        .///***///.      ,/*    ,(%%%%%%%%#/%%%%*           *////////////.                             ")
    print("                       .//,     .//*     ,/*         ,(%%%%%%%%,            */*        .//*                            ")
    print("                       .//.              ,/*               %%%#             */*          //*                           ")
    print("                        ///              ,/*               (%%%             */*          //*                           ")
    print("                             ,///.           ,/*               ,%%%,            */*         */*.                       ")
    print("                                *///.        ,/*                %%%#            *////////////.                         ")
    print("                                  *//*       ,/*                #%%%#((/**.     */*....                                ")
    print("                                    ,//*     ,/*                ,%%%%%%%%%%/    */*                                    ")
    print("                                     ,//.    ,/*                 *%%%, .(%%%,   */*                                    ")
    print("                          ,/,        ,//.    ,/*                  %%%#   *%%%.  */*                                    ")
    print("                           //*.     ,//*     ,/*                  *%%%,   (%%#. */*                                    ")
    print("                            .*///////,       ,///////////,         %%%#         */*                                    ")
    print("                                 .                            *..* /%%%.                                               ")
    print("                                                .(((((((((//%#(((#(/%%%(                                               ")
    print("                                               ,(((((((((((((#(((((((#(.                                               ")
    print("                                                      ,..,*/*.                                                         ")
    print("                                                                                                                       ")
    print("-----------------------------------------------------------------------------------------------------------------------")


def listOptions():                                                                                                                      
    logo()

    print(" Which Virtual Environment you would like to interact with")
    print("  1. AWS")
    print("  2. ESXi")
    print("  3. Hyper-V")

    print(" *To edit Configuration please enter 4 ")

    print("-------------------------------------------------")
    selection = input(" Enter choice: ")
    if(selection == 1):
        logo()
        print("  1 - Power On AWS Instance")
        print("  2 - Power Off AWS Instance")
        print("  3 - Deploy OVA to AWS EC2")
        print("  4 - Export OVA from AWS")

        sel = input(" Enter Option: ")
        if(sel == 1):
            AWSPowerOn()
        if(sel == 2):
            AWSStop()
        if(sel == 3):
            AWSImport()
        if(sel == 4):
            AWSExport()
    if(selection == 2):
        logo()
        print("  1 - Power On VM from Vcenter")
        print("  2 - Power Off VM from Vcenter")
        print("  3 - Deploy OVA to Vcenter")
        print("  4 - Export OVA from Vcenter")
        sel = input("Enter Option: ")
        if(sel == 1):
            vm = vcenter()
            si = vm.GetConnectionV()
            vm.PowerVMon(si)
        if(sel == 2):
            vm = vcenter()
            si = vm.GetConnectionV()
            vm.PowerVMoff(si)
        if(sel == 3):
            vm = vcenter()
            vm.importVM()

        if(sel == 4):
            vm = vcenter()
            vm.exportVM();
    if(selection == 3):
        logo()
        print("  1 - Power On VM from HyperV")
        print("  2 - Power Off VM from HyperV")
        print("  3 - Get HyperV Status")
        print("  4 - Deploy OVA to HyperV")
        print("  5 - Export OVA from HyperV")
        sel = input("Enter Option: ")
        if(sel == 1):
            vm = hyperV()
            vm.PowerON()
        if(sel == 2):
            vm = hyperV()
            vm.PowerOff()
        if(sel == 3):
            vm = hyperV()
            vm.getVMs()
        if(sel == 4):
            vm = hyperV()
            vm.importVHD()
        if(sel == 5):
            vm = hyperV()
            vm.exportVHD()
    if(selection == 4):
        logo()
        from configuration import config
while(True):
    listOptions()
