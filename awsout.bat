@echo off
:: i-509e53d0 se2016-slick
"C:\Program Files\Amazon\AWSCLI\aws.exe" ec2 create-instance-export-task --description "RHEL5 instance" --instance-id %1 --target-environment vmware --export-to-s3-task DiskImageFormat=vmdk,ContainerFormat=ova,S3Bucket=%2,S3Prefix=RHEL5