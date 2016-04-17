import ssl
import sys
from os import system, path
from pyvim import connect
from pyVmomi import vim, vmodl
from sys import exit
from threading import Thread
from time import sleep
from datetime import datetime, date, timedelta
import requests
from ConfigParser import SafeConfigParser
# Disable HTTPS verification warnings.
from requests.packages import urllib3
urllib3.disable_warnings()
import os
import subprocess
import time
import tarfile
import re 
import xml.etree.ElementTree as ET


class vcenter():
    parser = SafeConfigParser()
    parser.read('config.ini')
    esxi = parser.get('VCenter','esxi')
    vcenter =parser.get('VCenter','vcenter')
    port = parser.get('VCenter','port')
    user = parser.get('VCenter','user')
    Vuser= parser.get('VCenter','Vuser')
    esxiPW = parser.get('VCenter','esxipw')
    vcenterPW =parser.get('VCenter','vcenterpw')
    vmdk_path = parser.get('VCenter','vmdk_path')
    ovf_path = parser.get('VCenter','ovf_path')
    vmname = parser.get('VCenter','vmnameVC')
    prefix_clone = "clone-"
    halt_vm = "no"

    
    def str2bool(self,val):
        if type(val) != bool:
            return val.lower() in ("yes", "true", "t", "1")

    def WaitForTasks(self, tasks, si):
        """
        Given the service instance si and tasks, it returns after all the
        tasks are complete
        """
        pc = si.content.propertyCollector

        taskList = [str(task) for task in tasks]

        # Create filter
        objSpecs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task)
                    for task in tasks]
        propSpec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
                                                              pathSet=[], all=True)
        filterSpec = vmodl.query.PropertyCollector.FilterSpec()
        filterSpec.objectSet = objSpecs
        filterSpec.propSet = [propSpec]
        filter = pc.CreateFilter(filterSpec, True)

        try:
            version, state = None, None

            # Loop looking for updates till the state moves to a completed state.
            while len(taskList):
                update = pc.WaitForUpdates(version)
                for filterSet in update.filterSet:
                    for objSet in filterSet.objectSet:
                        task = objSet.obj
                        for change in objSet.changeSet:
                            if change.name == 'info':
                                state = change.val.state
                            elif change.name == 'info.state':
                                state = change.val
                            else:
                                continue

                            if not str(task) in taskList:
                                continue

                            if state == vim.TaskInfo.State.success:
                                # Remove task from taskList
                                taskList.remove(str(task))
                            elif state == vim.TaskInfo.State.error:
                                raise task.info.error
                # Move to next version
                version = update.version
        finally:
            if filter:
                filter.Destroy()

    def GetConnectionESXI(self):

        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.verify_mode = ssl.CERT_NONE
        try:
            si = connect.SmartConnect(host=self.esxi, user=self.user, pwd=self.esxiPW, port=int(self.port),
                                      sslContext=context)
        except IOError:
            pass
            if not si:
                print("Cannot connect to specified host using specified username and password")
                sys.exit()
        return si

    def GetConnectionV(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.verify_mode = ssl.CERT_NONE
        try:
            si = connect.SmartConnect(host=self.vcenter, user=self.Vuser, pwd=self.vcenterPW, port=int(self.port),
                                      sslContext=context)
        except IOError:
            pass
            if not si:
                print("Vcenter Cannot connect to specified host using specified username and password")
                sys.exit()
        return si

    
    def PowerVMon(self, si):
        vmnames = self.vmname
        content = si.content
        objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                          [vim.VirtualMachine],
                                                          True)
        vmList = objView.view
        objView.Destroy()

        # Find the vm and power it on
        tasks = [vm.PowerOn() for vm in vmList if vm.name in vmnames]

        # Wait for power on to complete
        self.WaitForTasks(tasks, si)

        print("Virtual Machine(s) have been powered on successfully")

    def PowerVMoff(self, si):
        vmnames = self.vmname
        content = si.content
        objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                          [vim.VirtualMachine],
                                                          True)
        vmList = objView.view
        objView.Destroy()

        # Find the vm and power it on
        tasks = [vm.PowerOff() for vm in vmList if vm.name in vmnames]

        # Wait for power on to complete
        self.WaitForTasks(tasks, si)

        print("Virtual Machine(s) have been powered off successfully")

    def exportVM(self):
	p=subprocess.call(["powershell.exe","C:\\Slyp\\ExportVM.ps1", self.vcenter, self.Vuser, self.vcenterPW, self.vmname])

    def importVM(self):
	p=subprocess.call(["powershell.exe","C:\\Slyp\\ImportVM.ps1", self.vcenter, self.Vuser, self.vcenterPW, self.vmdk_path])

