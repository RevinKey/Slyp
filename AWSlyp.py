import boto3
from subprocess import Popen
import os
# Custom Slyp Module for AWS
# This will encapsulate any sdk we may use
class AWSlyp:
    ec2 = boto3.resource('ec2')
    def powerOn(self, instance):
       ids = [instance]
       self.ec2.instances.filter(InstanceIds=ids).start()
       print("Successfully started instance "+instance)                
       return True
    def powerOff(self, instance):
       ids = [instance]
       self.ec2.instances.filter(InstanceIds=ids).stop()
       print("Successfully stopped instance "+instance)
    def vmImport(self, bucket, filename):
       os.system("C:/SLYP/awsin.bat "+bucket+" "+filename)
    def vmExport(self, instance, bucket):
       os.system("C:/SLYP/awsout.bat "+instance+" "+bucket+" >nul 2>nul")
