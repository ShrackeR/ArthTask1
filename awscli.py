#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:48:04 2020

@author: kartik_rama_arora
"""
import os

while True:
    print("\tPress 1: To Install AWS CLI\n\
          Press 2: To Configure AWS CLI\n\
       \tPress 3: To Use EC2 Service\n\
       \tPress 4: To Use IAM Service\n\
       \tPress 5: To Use S3 Service\n\
       \tPress 6: To Use Cloud Front\n")
    Input = input("Select To Use That Service: ")   
    if Input == "1":
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        print("successfully Installed!!")
    elif Input == "2":
        os.system("/usr/local/bin/aws configure")
    elif Input == "3":
        print("\tPress 1: Work With Instances\n\
              \tPress 2: Work with EBS\n\
              \tPress 3: work with Network & Security")
        Input = input("Select To Use That Service: ")
        if Input == "1":
           print("Press 1: Create Instances\n\
                  Press 2: Start Instances\n\
                  Press 3: Stoping Instances\n\
                  Press 3: Terminating Instance\n\
                  Press 4: Reboot Instance\n\
                  Press 5: Available Instances\n\
                  Press 6: Describe Instance\n\
                  Press 7: To Transfer File to Instance\n\
                  Press 8: To Retrive File From Instance\n\
                  ")
           Input = input("Select To Use That Service: ")
           if Input == "1":
               image_search = input("Do you want to list all the AMI ? :  ")
               if image_search == "yes":
                   print("Available Image IDs")
                   os.system("/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table")
               elif image_search == "no":
                   IS = input("Search your Desirable AMI: ")
                   print("Available Image IDs")
                   os.system(f"/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table | grep {IS}")
               image_id = input("choose The Image ID:")
               os.system("/usr/local/bin/aws ec2 describe-instance-types --output table | grep 'InstanceType\|DefaultVCpus\|SizeInMiB'")
               instance_type = input("Choose The Instance Type: ")
               os.system("/usr/local/bin/aws ec2 describe-key-pairs --output table")
               key_name = input("Choose The Key-Pair: ")
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
               Security_group = input("Choose The Security Group: ")
               os.system("/usr/local/bin/aws ec2 describe-subnets --output table")
               Subnet_id = input("Choose The Subnet ID: ")
               Count = input("Choose The Number of Instance you want to Launch: ")
               os.system(f"/usr/local/bin/aws ec2 run-instance\
                                          --image-id {image_id}\
                                          --instance-type {instance_type}\
                                          --key-name {key_name}\
                                          --security-group-ids {Security_group}\
                                          --subnet-id {Subnet_id} --count {Count} --output table")
           elif Input == "2":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To start: ") 
               os.system(f"/usr/local/bin/aws ec2 start-instances --instance-ids {instance_id} --output table")
           elif Input == "3":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To stop: ") 
               os.system(f"/usr/local/bin/aws ec2 stop-instances --instance-ids {instance_id} --output table")
           elif Input == "4":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Terminate: ") 
               os.system(f"/usr/local/bin/aws ec2 terminate-instances --instance-ids {instance_id} --output table")
           elif Input == "5":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Reboot: ") 
               os.system(f"/usr/local/bin/aws ec2 reboot-instances --instance-ids {instance_id} --output table")
           elif Input == "6":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
           elif Input == "7":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance ip: ")
               
               Path = input("Enter The Path Of your File: ")
               os.system("scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' {Path} ec2-user@{instance_ip}:/home/ec2-user/ ")
           elif Input == "8":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance: ")
               
               Path = input("Enter The Path Of your File: ")
               cwd = os.getcwd()
               os.system(f"scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' ec2-user@{instance_ip}:{Path} {cwd}")
        elif Input == "2":
            print("\tPress 1: To Create Volume\n\
              \tPress 2: To Delete Volume\n\
                  \tPress 3: To Modify volume\n\
              \tPress 4: To Attach Volume\n\
              \tPress 5: To Detaching Volume\n\
              \tPress 6: To Describe Volume\n\
                  \tPress 7: To Create Snapshot\n\
                      \tPress 8: To Delete Snapshot")
            Input_vol = input("Select The Service you Want To Use") 
            if Input_vol == "1":
            
                vol_type = input("Select The Available Volume Type: ")
                vol_size = input("Enter The Size Of Volume(in GiB): ")
                AZ = input("Enter The Avaliability Zone: ")
                os.system(f"/usr/local/bin/aws ec2 create-volume --volume-type --size {vol_size} --availability-zone {AZ} --output table")
            elif Input_vol == "2":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 delete-volume --volume-id {vol_id} --output table")
            elif Input_vol == "3":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Modify: ")
                ol_size = input("Enter The Size Of Volume(in GiB): ")
                os.system(f"/usr/local/bin/aws ec2 modify-volume --volume-id {vol_id} --size {vol_size} --output table")
            elif Input_vol == "4":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Attach: ")
                os.system("/usr/local/bin/aws ec2 describe-instances --output table")
                instance_id = input("Enter The ID of Your Instanace: ")
                os.system("/usr/local/bin/aws ec2 attach-volume --volume-id {vol_id}\
                      --instance-id {instance_id} --device --output table")
            elif Input_vol == "5":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 detach-volume --volume-id {vol_id} --output table")
            elif Input_vol == "6":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
            elif Input_vol == "7":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume for snapshot: ")
                vol_des = input("anything you want to put in Description:")
                if vol_des == "no" or "No":
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --output table")
                else:    
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --description {vol_des} --output table")
            elif Input_vol == "8":
                snap_id = input("Enter your Snapshot ID: ")
                os.system(f"/usr/local/bin/aws ec2 delete-snapshot --snapshot-id {snap_id} --output table") 
        elif Input == "3":
           print("Press 1: To Create Key-pair\n\
                 Press 2: To See Availiable Key-pairs\n\
                 Press 3: To Delete Key-Pair\n\
                 Press 4: To Create Security-group\n\
                 Press 5: To Delete Security-group\n\
                 Press 6: To Add Rules in Security Group\n\
                 Press 7: To See Available Security-group")
           Input_key = input("Select To Use That Service: ")
           if Input_key == "1":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} > {key_name}.pem --output table")
           elif Input_key == "2":
               key_name = input("Enter The Name Of Yout Key-Pair")
               os.system(f"/usr/local/bin/aws ec2 delete-key-pair --key-name {key_name} --output table") 
           elif Input_key == "3":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} --output table")
           elif Input_key == "4":
               GN = input("Enter The Name For Your Security Group")
               d = input("Add Description for your Security Group")
               os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {GN} --description {d} --output table")
           elif Input_key == "5":
               GN = input("Enter The Name of Your Security Group")
               os.system(f"/usr/local/bin/aws ec2 delete-security-group --group-name {GN} --output table")
           elif Input_key == "6":
               print("Press 1: To Adding egress rule\n\
                      Press 2: To Adding Ingress rule")
               rule = input("Choose The Desire Option:")
               if rule == "1":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       cidr = input("Enter the IP of the PC that you want to allow:")
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                   
               elif rule == "2":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   cidr = input("Enter the IP of the PC that you want to allow:")
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                  
           elif Input_key == "7":
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
    elif Input == "4":
        print("\tPress 1: To Create User\n\
              Press 2: To Delete User\n\
                  Press 3: To Create access Key And Secret Key\n\
                      Press 4: To Attach policy to User")
        Input_iam = input("Select To Use That Service: ")
        if Input_iam == "1":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-user --user-name {user_name} --output table")
        elif Input_iam == "2":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam delete-user --user-name {user_name} --output table")
        elif Input_iam == "3":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-access-key --user-name {user_name} --output table")
        elif Input_iam == "4":
            policy = input("Enter The Name Of Policy:")
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam attach-user-policy\
                      --policy-arn arn:aws:iam:199619846734:aws:policy/{policy} --user-name  {user_name} --output table")    
    elif Input == "5":
        print("\tPress 1: To Create Bucket\n\
              Press 2: To Delete Bucket\n\
                  Press 3: To Put Object in Bucket\n\
                      Press 4: To Delete Object in Bucket\n\
                          Press 5: To List Bucket in S3\n\
                              Press 6: To List Object in Bucket")
        Input_s3 = input("Select The Service:")
        if Input_s3 == "1":
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api create-bucket --bucket {bucket_name} --region ap-south-1 --output table")
        elif Input_s3 == "2":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api delete-bucket --bucket {bucket_name} --output table")
        elif Input_s3 == "3":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("name of File you Want To Transfer: ")
            os.system("/usr/local/bin/aws s3api put-object --bucket {bucket_name} --key dir-1/{file_name} --body {file_name} --output table")
        elif Input_s3 == "4":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("Name of Object you Want to Delete:")
            os.system(f"/usr/local/bin/aws s3api delete-object --bucket {bucket_name} --key {file_name} --output table")
        elif Input_s3 == "5":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
        elif Input_s3 == "6":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system(f"/usr/local/bin/aws s3api list-objects --bucket {bucket_name} --output table")
    elif Input == "6":
        print("\tPress 1: To Create Distribution\n\
           Press 2: To Delete Distribution\n\
           Press 3: To Update Distribution")
        Input_cf = input("Select The Service You Want To run:")
        if Input_cf == "1":
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object:")
            os.system(f"/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
        elif Input_cf == "2":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
        elif Input_cf == "3":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
            dis_id = input("Enter Your Dictribution ID: ")
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object: ")
            os.system(f"/usr/local/bin/aws cloudfront update-distribution --id {dis_id} --origin-domain-name {origin_name} --default-root-object {object_name} --output table")



          

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:48:04 2020

@author: kartik_rama_arora
"""
import os

while True:
    print("\tPress 1: To Install AWS CLI\n\
          Press 2: To Configure AWS CLI\n\
       \tPress 3: To Use EC2 Service\n\
       \tPress 4: To Use IAM Service\n\
       \tPress 5: To Use S3 Service\n\
       \tPress 6: To Use Cloud Front\n")
    Input = input("Select To Use That Service: ")   
    if Input == "1":
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        print("successfully Installed!!")
    elif Input == "2":
        os.system("/usr/local/bin/aws configure")
    elif Input == "3":
        print("\tPress 1: Work With Instances\n\
              \tPress 2: Work with EBS\n\
              \tPress 3: work with Network & Security")
        Input = input("Select To Use That Service: ")
        if Input == "1":
           print("Press 1: Create Instances\n\
                  Press 2: Start Instances\n\
                  Press 3: Stoping Instances\n\
                  Press 3: Terminating Instance\n\
                  Press 4: Reboot Instance\n\
                  Press 5: Available Instances\n\
                  Press 6: Describe Instance\n\
                  Press 7: To Transfer File to Instance\n\
                  Press 8: To Retrive File From Instance\n\
                  ")
           Input = input("Select To Use That Service: ")
           if Input == "1":
               image_search = input("Do you want to list all the AMI ? :  ")
               if image_search == "yes":
                   print("Available Image IDs")
                   os.system("/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table")
               elif image_search == "no":
                   IS = input("Search your Desirable AMI: ")
                   print("Available Image IDs")
                   os.system(f"/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table | grep {IS}")
               image_id = input("choose The Image ID:")
               os.system("/usr/local/bin/aws ec2 describe-instance-types --output table | grep 'InstanceType\|DefaultVCpus\|SizeInMiB'")
               instance_type = input("Choose The Instance Type: ")
               os.system("/usr/local/bin/aws ec2 describe-key-pairs --output table")
               key_name = input("Choose The Key-Pair: ")
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
               Security_group = input("Choose The Security Group: ")
               os.system("/usr/local/bin/aws ec2 describe-subnets --output table")
               Subnet_id = input("Choose The Subnet ID: ")
               Count = input("Choose The Number of Instance you want to Launch: ")
               os.system(f"/usr/local/bin/aws ec2 run-instance\
                                          --image-id {image_id}\
                                          --instance-type {instance_type}\
                                          --key-name {key_name}\
                                          --security-group-ids {Security_group}\
                                          --subnet-id {Subnet_id} --count {Count} --output table")
           elif Input == "2":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To start: ") 
               os.system(f"/usr/local/bin/aws ec2 start-instances --instance-ids {instance_id} --output table")
           elif Input == "3":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To stop: ") 
               os.system(f"/usr/local/bin/aws ec2 stop-instances --instance-ids {instance_id} --output table")
           elif Input == "4":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Terminate: ") 
               os.system(f"/usr/local/bin/aws ec2 terminate-instances --instance-ids {instance_id} --output table")
           elif Input == "5":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Reboot: ") 
               os.system(f"/usr/local/bin/aws ec2 reboot-instances --instance-ids {instance_id} --output table")
           elif Input == "6":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
           elif Input == "7":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance ip: ")
               
               Path = input("Enter The Path Of your File: ")
               os.system("scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' {Path} ec2-user@{instance_ip}:/home/ec2-user/ ")
           elif Input == "8":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance: ")
               
               Path = input("Enter The Path Of your File: ")
               cwd = os.getcwd()
               os.system(f"scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' ec2-user@{instance_ip}:{Path} {cwd}")
        elif Input == "2":
            print("\tPress 1: To Create Volume\n\
              \tPress 2: To Delete Volume\n\
                  \tPress 3: To Modify volume\n\
              \tPress 4: To Attach Volume\n\
              \tPress 5: To Detaching Volume\n\
              \tPress 6: To Describe Volume\n\
                  \tPress 7: To Create Snapshot\n\
                      \tPress 8: To Delete Snapshot")
            Input_vol = input("Select The Service you Want To Use") 
            if Input_vol == "1":
            
                vol_type = input("Select The Available Volume Type: ")
                vol_size = input("Enter The Size Of Volume(in GiB): ")
                AZ = input("Enter The Avaliability Zone: ")
                os.system(f"/usr/local/bin/aws ec2 create-volume --volume-type --size {vol_size} --availability-zone {AZ} --output table")
            elif Input_vol == "2":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 delete-volume --volume-id {vol_id} --output table")
            elif Input_vol == "3":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Modify: ")
                ol_size = input("Enter The Size Of Volume(in GiB): ")
                os.system(f"/usr/local/bin/aws ec2 modify-volume --volume-id {vol_id} --size {vol_size} --output table")
            elif Input_vol == "4":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Attach: ")
                os.system("/usr/local/bin/aws ec2 describe-instances --output table")
                instance_id = input("Enter The ID of Your Instanace: ")
                os.system("/usr/local/bin/aws ec2 attach-volume --volume-id {vol_id}\
                      --instance-id {instance_id} --device --output table")
            elif Input_vol == "5":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 detach-volume --volume-id {vol_id} --output table")
            elif Input_vol == "6":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
            elif Input_vol == "7":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume for snapshot: ")
                vol_des = input("anything you want to put in Description:")
                if vol_des == "no" or "No":
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --output table")
                else:    
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --description {vol_des} --output table")
            elif Input_vol == "8":
                snap_id = input("Enter your Snapshot ID: ")
                os.system(f"/usr/local/bin/aws ec2 delete-snapshot --snapshot-id {snap_id} --output table") 
        elif Input == "3":
           print("Press 1: To Create Key-pair\n\
                 Press 2: To See Availiable Key-pairs\n\
                 Press 3: To Delete Key-Pair\n\
                 Press 4: To Create Security-group\n\
                 Press 5: To Delete Security-group\n\
                 Press 6: To Add Rules in Security Group\n\
                 Press 7: To See Available Security-group")
           Input_key = input("Select To Use That Service: ")
           if Input_key == "1":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} > {key_name}.pem --output table")
           elif Input_key == "2":
               key_name = input("Enter The Name Of Yout Key-Pair")
               os.system(f"/usr/local/bin/aws ec2 delete-key-pair --key-name {key_name} --output table") 
           elif Input_key == "3":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} --output table")
           elif Input_key == "4":
               GN = input("Enter The Name For Your Security Group")
               d = input("Add Description for your Security Group")
               os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {GN} --description {d} --output table")
           elif Input_key == "5":
               GN = input("Enter The Name of Your Security Group")
               os.system(f"/usr/local/bin/aws ec2 delete-security-group --group-name {GN} --output table")
           elif Input_key == "6":
               print("Press 1: To Adding egress rule\n\
                      Press 2: To Adding Ingress rule")
               rule = input("Choose The Desire Option:")
               if rule == "1":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       cidr = input("Enter the IP of the PC that you want to allow:")
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                   
               elif rule == "2":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   cidr = input("Enter the IP of the PC that you want to allow:")
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                  
           elif Input_key == "7":
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
    elif Input == "4":
        print("\tPress 1: To Create User\n\
              Press 2: To Delete User\n\
                  Press 3: To Create access Key And Secret Key\n\
                      Press 4: To Attach policy to User")
        Input_iam = input("Select To Use That Service: ")
        if Input_iam == "1":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-user --user-name {user_name} --output table")
        elif Input_iam == "2":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam delete-user --user-name {user_name} --output table")
        elif Input_iam == "3":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-access-key --user-name {user_name} --output table")
        elif Input_iam == "4":
            policy = input("Enter The Name Of Policy:")
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam attach-user-policy\
                      --policy-arn arn:aws:iam:199619846734:aws:policy/{policy} --user-name  {user_name} --output table")    
    elif Input == "5":
        print("\tPress 1: To Create Bucket\n\
              Press 2: To Delete Bucket\n\
                  Press 3: To Put Object in Bucket\n\
                      Press 4: To Delete Object in Bucket\n\
                          Press 5: To List Bucket in S3\n\
                              Press 6: To List Object in Bucket")
        Input_s3 = input("Select The Service:")
        if Input_s3 == "1":
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api create-bucket --bucket {bucket_name} --region ap-south-1 --output table")
        elif Input_s3 == "2":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api delete-bucket --bucket {bucket_name} --output table")
        elif Input_s3 == "3":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("name of File you Want To Transfer: ")
            os.system("/usr/local/bin/aws s3api put-object --bucket {bucket_name} --key dir-1/{file_name} --body {file_name} --output table")
        elif Input_s3 == "4":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("Name of Object you Want to Delete:")
            os.system(f"/usr/local/bin/aws s3api delete-object --bucket {bucket_name} --key {file_name} --output table")
        elif Input_s3 == "5":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
        elif Input_s3 == "6":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system(f"/usr/local/bin/aws s3api list-objects --bucket {bucket_name} --output table")
    elif Input == "6":
        print("\tPress 1: To Create Distribution\n\
           Press 2: To Delete Distribution\n\
           Press 3: To Update Distribution")
        Input_cf = input("Select The Service You Want To run:")
        if Input_cf == "1":
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object:")
            os.system(f"/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
        elif Input_cf == "2":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
        elif Input_cf == "3":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
            dis_id = input("Enter Your Dictribution ID: ")
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object: ")
            os.system(f"/usr/local/bin/aws cloudfront update-distribution --id {dis_id} --origin-domain-name {origin_name} --default-root-object {object_name} --output table")



          

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:48:04 2020

@author: kartik_rama_arora
"""
import os

while True:
    print("\tPress 1: To Install AWS CLI\n\
          Press 2: To Configure AWS CLI\n\
       \tPress 3: To Use EC2 Service\n\
       \tPress 4: To Use IAM Service\n\
       \tPress 5: To Use S3 Service\n\
       \tPress 6: To Use Cloud Front\n")
    Input = input("Select To Use That Service: ")   
    if Input == "1":
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        print("successfully Installed!!")
    elif Input == "2":
        os.system("/usr/local/bin/aws configure")
    elif Input == "3":
        print("\tPress 1: Work With Instances\n\
              \tPress 2: Work with EBS\n\
              \tPress 3: work with Network & Security")
        Input = input("Select To Use That Service: ")
        if Input == "1":
           print("Press 1: Create Instances\n\
                  Press 2: Start Instances\n\
                  Press 3: Stoping Instances\n\
                  Press 3: Terminating Instance\n\
                  Press 4: Reboot Instance\n\
                  Press 5: Available Instances\n\
                  Press 6: Describe Instance\n\
                  Press 7: To Transfer File to Instance\n\
                  Press 8: To Retrive File From Instance\n\
                  ")
           Input = input("Select To Use That Service: ")
           if Input == "1":
               image_search = input("Do you want to list all the AMI ? :  ")
               if image_search == "yes":
                   print("Available Image IDs")
                   os.system("/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table")
               elif image_search == "no":
                   IS = input("Search your Desirable AMI: ")
                   print("Available Image IDs")
                   os.system(f"/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table | grep {IS}")
               image_id = input("choose The Image ID:")
               os.system("/usr/local/bin/aws ec2 describe-instance-types --output table | grep 'InstanceType\|DefaultVCpus\|SizeInMiB'")
               instance_type = input("Choose The Instance Type: ")
               os.system("/usr/local/bin/aws ec2 describe-key-pairs --output table")
               key_name = input("Choose The Key-Pair: ")
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
               Security_group = input("Choose The Security Group: ")
               os.system("/usr/local/bin/aws ec2 describe-subnets --output table")
               Subnet_id = input("Choose The Subnet ID: ")
               Count = input("Choose The Number of Instance you want to Launch: ")
               os.system(f"/usr/local/bin/aws ec2 run-instance\
                                          --image-id {image_id}\
                                          --instance-type {instance_type}\
                                          --key-name {key_name}\
                                          --security-group-ids {Security_group}\
                                          --subnet-id {Subnet_id} --count {Count} --output table")
           elif Input == "2":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To start: ") 
               os.system(f"/usr/local/bin/aws ec2 start-instances --instance-ids {instance_id} --output table")
           elif Input == "3":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To stop: ") 
               os.system(f"/usr/local/bin/aws ec2 stop-instances --instance-ids {instance_id} --output table")
           elif Input == "4":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Terminate: ") 
               os.system(f"/usr/local/bin/aws ec2 terminate-instances --instance-ids {instance_id} --output table")
           elif Input == "5":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Reboot: ") 
               os.system(f"/usr/local/bin/aws ec2 reboot-instances --instance-ids {instance_id} --output table")
           elif Input == "6":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
           elif Input == "7":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance ip: ")
               
               Path = input("Enter The Path Of your File: ")
               os.system("scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' {Path} ec2-user@{instance_ip}:/home/ec2-user/ ")
           elif Input == "8":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance: ")
               
               Path = input("Enter The Path Of your File: ")
               cwd = os.getcwd()
               os.system(f"scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' ec2-user@{instance_ip}:{Path} {cwd}")
        elif Input == "2":
            print("\tPress 1: To Create Volume\n\
              \tPress 2: To Delete Volume\n\
                  \tPress 3: To Modify volume\n\
              \tPress 4: To Attach Volume\n\
              \tPress 5: To Detaching Volume\n\
              \tPress 6: To Describe Volume\n\
                  \tPress 7: To Create Snapshot\n\
                      \tPress 8: To Delete Snapshot")
            Input_vol = input("Select The Service you Want To Use") 
            if Input_vol == "1":
            
                vol_type = input("Select The Available Volume Type: ")
                vol_size = input("Enter The Size Of Volume(in GiB): ")
                AZ = input("Enter The Avaliability Zone: ")
                os.system(f"/usr/local/bin/aws ec2 create-volume --volume-type --size {vol_size} --availability-zone {AZ} --output table")
            elif Input_vol == "2":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 delete-volume --volume-id {vol_id} --output table")
            elif Input_vol == "3":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Modify: ")
                ol_size = input("Enter The Size Of Volume(in GiB): ")
                os.system(f"/usr/local/bin/aws ec2 modify-volume --volume-id {vol_id} --size {vol_size} --output table")
            elif Input_vol == "4":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Attach: ")
                os.system("/usr/local/bin/aws ec2 describe-instances --output table")
                instance_id = input("Enter The ID of Your Instanace: ")
                os.system("/usr/local/bin/aws ec2 attach-volume --volume-id {vol_id}\
                      --instance-id {instance_id} --device --output table")
            elif Input_vol == "5":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 detach-volume --volume-id {vol_id} --output table")
            elif Input_vol == "6":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
            elif Input_vol == "7":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume for snapshot: ")
                vol_des = input("anything you want to put in Description:")
                if vol_des == "no" or "No":
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --output table")
                else:    
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --description {vol_des} --output table")
            elif Input_vol == "8":
                snap_id = input("Enter your Snapshot ID: ")
                os.system(f"/usr/local/bin/aws ec2 delete-snapshot --snapshot-id {snap_id} --output table") 
        elif Input == "3":
           print("Press 1: To Create Key-pair\n\
                 Press 2: To See Availiable Key-pairs\n\
                 Press 3: To Delete Key-Pair\n\
                 Press 4: To Create Security-group\n\
                 Press 5: To Delete Security-group\n\
                 Press 6: To Add Rules in Security Group\n\
                 Press 7: To See Available Security-group")
           Input_key = input("Select To Use That Service: ")
           if Input_key == "1":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} > {key_name}.pem --output table")
           elif Input_key == "2":
               key_name = input("Enter The Name Of Yout Key-Pair")
               os.system(f"/usr/local/bin/aws ec2 delete-key-pair --key-name {key_name} --output table") 
           elif Input_key == "3":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} --output table")
           elif Input_key == "4":
               GN = input("Enter The Name For Your Security Group")
               d = input("Add Description for your Security Group")
               os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {GN} --description {d} --output table")
           elif Input_key == "5":
               GN = input("Enter The Name of Your Security Group")
               os.system(f"/usr/local/bin/aws ec2 delete-security-group --group-name {GN} --output table")
           elif Input_key == "6":
               print("Press 1: To Adding egress rule\n\
                      Press 2: To Adding Ingress rule")
               rule = input("Choose The Desire Option:")
               if rule == "1":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       cidr = input("Enter the IP of the PC that you want to allow:")
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                   
               elif rule == "2":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   cidr = input("Enter the IP of the PC that you want to allow:")
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                  
           elif Input_key == "7":
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
    elif Input == "4":
        print("\tPress 1: To Create User\n\
              Press 2: To Delete User\n\
                  Press 3: To Create access Key And Secret Key\n\
                      Press 4: To Attach policy to User")
        Input_iam = input("Select To Use That Service: ")
        if Input_iam == "1":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-user --user-name {user_name} --output table")
        elif Input_iam == "2":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam delete-user --user-name {user_name} --output table")
        elif Input_iam == "3":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-access-key --user-name {user_name} --output table")
        elif Input_iam == "4":
            policy = input("Enter The Name Of Policy:")
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam attach-user-policy\
                      --policy-arn arn:aws:iam:199619846734:aws:policy/{policy} --user-name  {user_name} --output table")    
    elif Input == "5":
        print("\tPress 1: To Create Bucket\n\
              Press 2: To Delete Bucket\n\
                  Press 3: To Put Object in Bucket\n\
                      Press 4: To Delete Object in Bucket\n\
                          Press 5: To List Bucket in S3\n\
                              Press 6: To List Object in Bucket")
        Input_s3 = input("Select The Service:")
        if Input_s3 == "1":
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api create-bucket --bucket {bucket_name} --region ap-south-1 --output table")
        elif Input_s3 == "2":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api delete-bucket --bucket {bucket_name} --output table")
        elif Input_s3 == "3":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("name of File you Want To Transfer: ")
            os.system("/usr/local/bin/aws s3api put-object --bucket {bucket_name} --key dir-1/{file_name} --body {file_name} --output table")
        elif Input_s3 == "4":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("Name of Object you Want to Delete:")
            os.system(f"/usr/local/bin/aws s3api delete-object --bucket {bucket_name} --key {file_name} --output table")
        elif Input_s3 == "5":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
        elif Input_s3 == "6":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system(f"/usr/local/bin/aws s3api list-objects --bucket {bucket_name} --output table")
    elif Input == "6":
        print("\tPress 1: To Create Distribution\n\
           Press 2: To Delete Distribution\n\
           Press 3: To Update Distribution")
        Input_cf = input("Select The Service You Want To run:")
        if Input_cf == "1":
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object:")
            os.system(f"/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
        elif Input_cf == "2":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
        elif Input_cf == "3":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
            dis_id = input("Enter Your Dictribution ID: ")
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object: ")
            os.system(f"/usr/local/bin/aws cloudfront update-distribution --id {dis_id} --origin-domain-name {origin_name} --default-root-object {object_name} --output table")



          

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:48:04 2020

@author: kartik_rama_arora
"""
import os

while True:
    print("\tPress 1: To Install AWS CLI\n\
          Press 2: To Configure AWS CLI\n\
       \tPress 3: To Use EC2 Service\n\
       \tPress 4: To Use IAM Service\n\
       \tPress 5: To Use S3 Service\n\
       \tPress 6: To Use Cloud Front\n")
    Input = input("Select To Use That Service: ")   
    if Input == "1":
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        print("successfully Installed!!")
    elif Input == "2":
        os.system("/usr/local/bin/aws configure")
    elif Input == "3":
        print("\tPress 1: Work With Instances\n\
              \tPress 2: Work with EBS\n\
              \tPress 3: work with Network & Security")
        Input = input("Select To Use That Service: ")
        if Input == "1":
           print("Press 1: Create Instances\n\
                  Press 2: Start Instances\n\
                  Press 3: Stoping Instances\n\
                  Press 3: Terminating Instance\n\
                  Press 4: Reboot Instance\n\
                  Press 5: Available Instances\n\
                  Press 6: Describe Instance\n\
                  Press 7: To Transfer File to Instance\n\
                  Press 8: To Retrive File From Instance\n\
                  ")
           Input = input("Select To Use That Service: ")
           if Input == "1":
               image_search = input("Do you want to list all the AMI ? :  ")
               if image_search == "yes":
                   print("Available Image IDs")
                   os.system("/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table")
               elif image_search == "no":
                   IS = input("Search your Desirable AMI: ")
                   print("Available Image IDs")
                   os.system(f"/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table | grep {IS}")
               image_id = input("choose The Image ID:")
               os.system("/usr/local/bin/aws ec2 describe-instance-types --output table | grep 'InstanceType\|DefaultVCpus\|SizeInMiB'")
               instance_type = input("Choose The Instance Type: ")
               os.system("/usr/local/bin/aws ec2 describe-key-pairs --output table")
               key_name = input("Choose The Key-Pair: ")
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
               Security_group = input("Choose The Security Group: ")
               os.system("/usr/local/bin/aws ec2 describe-subnets --output table")
               Subnet_id = input("Choose The Subnet ID: ")
               Count = input("Choose The Number of Instance you want to Launch: ")
               os.system(f"/usr/local/bin/aws ec2 run-instance\
                                          --image-id {image_id}\
                                          --instance-type {instance_type}\
                                          --key-name {key_name}\
                                          --security-group-ids {Security_group}\
                                          --subnet-id {Subnet_id} --count {Count} --output table")
           elif Input == "2":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To start: ") 
               os.system(f"/usr/local/bin/aws ec2 start-instances --instance-ids {instance_id} --output table")
           elif Input == "3":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To stop: ") 
               os.system(f"/usr/local/bin/aws ec2 stop-instances --instance-ids {instance_id} --output table")
           elif Input == "4":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Terminate: ") 
               os.system(f"/usr/local/bin/aws ec2 terminate-instances --instance-ids {instance_id} --output table")
           elif Input == "5":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Reboot: ") 
               os.system(f"/usr/local/bin/aws ec2 reboot-instances --instance-ids {instance_id} --output table")
           elif Input == "6":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
           elif Input == "7":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance ip: ")
               
               Path = input("Enter The Path Of your File: ")
               os.system("scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' {Path} ec2-user@{instance_ip}:/home/ec2-user/ ")
           elif Input == "8":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance: ")
               
               Path = input("Enter The Path Of your File: ")
               cwd = os.getcwd()
               os.system(f"scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' ec2-user@{instance_ip}:{Path} {cwd}")
        elif Input == "2":
            print("\tPress 1: To Create Volume\n\
              \tPress 2: To Delete Volume\n\
                  \tPress 3: To Modify volume\n\
              \tPress 4: To Attach Volume\n\
              \tPress 5: To Detaching Volume\n\
              \tPress 6: To Describe Volume\n\
                  \tPress 7: To Create Snapshot\n\
                      \tPress 8: To Delete Snapshot")
            Input_vol = input("Select The Service you Want To Use") 
            if Input_vol == "1":
            
                vol_type = input("Select The Available Volume Type: ")
                vol_size = input("Enter The Size Of Volume(in GiB): ")
                AZ = input("Enter The Avaliability Zone: ")
                os.system(f"/usr/local/bin/aws ec2 create-volume --volume-type --size {vol_size} --availability-zone {AZ} --output table")
            elif Input_vol == "2":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 delete-volume --volume-id {vol_id} --output table")
            elif Input_vol == "3":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Modify: ")
                ol_size = input("Enter The Size Of Volume(in GiB): ")
                os.system(f"/usr/local/bin/aws ec2 modify-volume --volume-id {vol_id} --size {vol_size} --output table")
            elif Input_vol == "4":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Attach: ")
                os.system("/usr/local/bin/aws ec2 describe-instances --output table")
                instance_id = input("Enter The ID of Your Instanace: ")
                os.system("/usr/local/bin/aws ec2 attach-volume --volume-id {vol_id}\
                      --instance-id {instance_id} --device --output table")
            elif Input_vol == "5":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 detach-volume --volume-id {vol_id} --output table")
            elif Input_vol == "6":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
            elif Input_vol == "7":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume for snapshot: ")
                vol_des = input("anything you want to put in Description:")
                if vol_des == "no" or "No":
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --output table")
                else:    
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --description {vol_des} --output table")
            elif Input_vol == "8":
                snap_id = input("Enter your Snapshot ID: ")
                os.system(f"/usr/local/bin/aws ec2 delete-snapshot --snapshot-id {snap_id} --output table") 
        elif Input == "3":
           print("Press 1: To Create Key-pair\n\
                 Press 2: To See Availiable Key-pairs\n\
                 Press 3: To Delete Key-Pair\n\
                 Press 4: To Create Security-group\n\
                 Press 5: To Delete Security-group\n\
                 Press 6: To Add Rules in Security Group\n\
                 Press 7: To See Available Security-group")
           Input_key = input("Select To Use That Service: ")
           if Input_key == "1":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} > {key_name}.pem --output table")
           elif Input_key == "2":
               key_name = input("Enter The Name Of Yout Key-Pair")
               os.system(f"/usr/local/bin/aws ec2 delete-key-pair --key-name {key_name} --output table") 
           elif Input_key == "3":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} --output table")
           elif Input_key == "4":
               GN = input("Enter The Name For Your Security Group")
               d = input("Add Description for your Security Group")
               os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {GN} --description {d} --output table")
           elif Input_key == "5":
               GN = input("Enter The Name of Your Security Group")
               os.system(f"/usr/local/bin/aws ec2 delete-security-group --group-name {GN} --output table")
           elif Input_key == "6":
               print("Press 1: To Adding egress rule\n\
                      Press 2: To Adding Ingress rule")
               rule = input("Choose The Desire Option:")
               if rule == "1":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       cidr = input("Enter the IP of the PC that you want to allow:")
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                   
               elif rule == "2":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   cidr = input("Enter the IP of the PC that you want to allow:")
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                  
           elif Input_key == "7":
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
    elif Input == "4":
        print("\tPress 1: To Create User\n\
              Press 2: To Delete User\n\
                  Press 3: To Create access Key And Secret Key\n\
                      Press 4: To Attach policy to User")
        Input_iam = input("Select To Use That Service: ")
        if Input_iam == "1":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-user --user-name {user_name} --output table")
        elif Input_iam == "2":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam delete-user --user-name {user_name} --output table")
        elif Input_iam == "3":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-access-key --user-name {user_name} --output table")
        elif Input_iam == "4":
            policy = input("Enter The Name Of Policy:")
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam attach-user-policy\
                      --policy-arn arn:aws:iam:199619846734:aws:policy/{policy} --user-name  {user_name} --output table")    
    elif Input == "5":
        print("\tPress 1: To Create Bucket\n\
              Press 2: To Delete Bucket\n\
                  Press 3: To Put Object in Bucket\n\
                      Press 4: To Delete Object in Bucket\n\
                          Press 5: To List Bucket in S3\n\
                              Press 6: To List Object in Bucket")
        Input_s3 = input("Select The Service:")
        if Input_s3 == "1":
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api create-bucket --bucket {bucket_name} --region ap-south-1 --output table")
        elif Input_s3 == "2":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api delete-bucket --bucket {bucket_name} --output table")
        elif Input_s3 == "3":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("name of File you Want To Transfer: ")
            os.system("/usr/local/bin/aws s3api put-object --bucket {bucket_name} --key dir-1/{file_name} --body {file_name} --output table")
        elif Input_s3 == "4":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("Name of Object you Want to Delete:")
            os.system(f"/usr/local/bin/aws s3api delete-object --bucket {bucket_name} --key {file_name} --output table")
        elif Input_s3 == "5":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
        elif Input_s3 == "6":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system(f"/usr/local/bin/aws s3api list-objects --bucket {bucket_name} --output table")
    elif Input == "6":
        print("\tPress 1: To Create Distribution\n\
           Press 2: To Delete Distribution\n\
           Press 3: To Update Distribution")
        Input_cf = input("Select The Service You Want To run:")
        if Input_cf == "1":
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object:")
            os.system(f"/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
        elif Input_cf == "2":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
        elif Input_cf == "3":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
            dis_id = input("Enter Your Dictribution ID: ")
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object: ")
            os.system(f"/usr/local/bin/aws cloudfront update-distribution --id {dis_id} --origin-domain-name {origin_name} --default-root-object {object_name} --output table")



          

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:48:04 2020

@author: kartik_rama_arora
"""
import os

while True:
    print("\tPress 1: To Install AWS CLI\n\
          Press 2: To Configure AWS CLI\n\
       \tPress 3: To Use EC2 Service\n\
       \tPress 4: To Use IAM Service\n\
       \tPress 5: To Use S3 Service\n\
       \tPress 6: To Use Cloud Front\n")
    Input = input("Select To Use That Service: ")   
    if Input == "1":
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        print("successfully Installed!!")
    elif Input == "2":
        os.system("/usr/local/bin/aws configure")
    elif Input == "3":
        print("\tPress 1: Work With Instances\n\
              \tPress 2: Work with EBS\n\
              \tPress 3: work with Network & Security")
        Input = input("Select To Use That Service: ")
        if Input == "1":
           print("Press 1: Create Instances\n\
                  Press 2: Start Instances\n\
                  Press 3: Stoping Instances\n\
                  Press 3: Terminating Instance\n\
                  Press 4: Reboot Instance\n\
                  Press 5: Available Instances\n\
                  Press 6: Describe Instance\n\
                  Press 7: To Transfer File to Instance\n\
                  Press 8: To Retrive File From Instance\n\
                  ")
           Input = input("Select To Use That Service: ")
           if Input == "1":
               image_search = input("Do you want to list all the AMI ? :  ")
               if image_search == "yes":
                   print("Available Image IDs")
                   os.system("/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table")
               elif image_search == "no":
                   IS = input("Search your Desirable AMI: ")
                   print("Available Image IDs")
                   os.system(f"/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table | grep {IS}")
               image_id = input("choose The Image ID:")
               os.system("/usr/local/bin/aws ec2 describe-instance-types --output table | grep 'InstanceType\|DefaultVCpus\|SizeInMiB'")
               instance_type = input("Choose The Instance Type: ")
               os.system("/usr/local/bin/aws ec2 describe-key-pairs --output table")
               key_name = input("Choose The Key-Pair: ")
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
               Security_group = input("Choose The Security Group: ")
               os.system("/usr/local/bin/aws ec2 describe-subnets --output table")
               Subnet_id = input("Choose The Subnet ID: ")
               Count = input("Choose The Number of Instance you want to Launch: ")
               os.system(f"/usr/local/bin/aws ec2 run-instance\
                                          --image-id {image_id}\
                                          --instance-type {instance_type}\
                                          --key-name {key_name}\
                                          --security-group-ids {Security_group}\
                                          --subnet-id {Subnet_id} --count {Count} --output table")
           elif Input == "2":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To start: ") 
               os.system(f"/usr/local/bin/aws ec2 start-instances --instance-ids {instance_id} --output table")
           elif Input == "3":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To stop: ") 
               os.system(f"/usr/local/bin/aws ec2 stop-instances --instance-ids {instance_id} --output table")
           elif Input == "4":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Terminate: ") 
               os.system(f"/usr/local/bin/aws ec2 terminate-instances --instance-ids {instance_id} --output table")
           elif Input == "5":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Reboot: ") 
               os.system(f"/usr/local/bin/aws ec2 reboot-instances --instance-ids {instance_id} --output table")
           elif Input == "6":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
           elif Input == "7":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance ip: ")
               
               Path = input("Enter The Path Of your File: ")
               os.system("scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' {Path} ec2-user@{instance_ip}:/home/ec2-user/ ")
           elif Input == "8":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance: ")
               
               Path = input("Enter The Path Of your File: ")
               cwd = os.getcwd()
               os.system(f"scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' ec2-user@{instance_ip}:{Path} {cwd}")
        elif Input == "2":
            print("\tPress 1: To Create Volume\n\
              \tPress 2: To Delete Volume\n\
                  \tPress 3: To Modify volume\n\
              \tPress 4: To Attach Volume\n\
              \tPress 5: To Detaching Volume\n\
              \tPress 6: To Describe Volume\n\
                  \tPress 7: To Create Snapshot\n\
                      \tPress 8: To Delete Snapshot")
            Input_vol = input("Select The Service you Want To Use") 
            if Input_vol == "1":
            
                vol_type = input("Select The Available Volume Type: ")
                vol_size = input("Enter The Size Of Volume(in GiB): ")
                AZ = input("Enter The Avaliability Zone: ")
                os.system(f"/usr/local/bin/aws ec2 create-volume --volume-type --size {vol_size} --availability-zone {AZ} --output table")
            elif Input_vol == "2":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 delete-volume --volume-id {vol_id} --output table")
            elif Input_vol == "3":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Modify: ")
                ol_size = input("Enter The Size Of Volume(in GiB): ")
                os.system(f"/usr/local/bin/aws ec2 modify-volume --volume-id {vol_id} --size {vol_size} --output table")
            elif Input_vol == "4":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Attach: ")
                os.system("/usr/local/bin/aws ec2 describe-instances --output table")
                instance_id = input("Enter The ID of Your Instanace: ")
                os.system("/usr/local/bin/aws ec2 attach-volume --volume-id {vol_id}\
                      --instance-id {instance_id} --device --output table")
            elif Input_vol == "5":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 detach-volume --volume-id {vol_id} --output table")
            elif Input_vol == "6":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
            elif Input_vol == "7":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume for snapshot: ")
                vol_des = input("anything you want to put in Description:")
                if vol_des == "no" or "No":
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --output table")
                else:    
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --description {vol_des} --output table")
            elif Input_vol == "8":
                snap_id = input("Enter your Snapshot ID: ")
                os.system(f"/usr/local/bin/aws ec2 delete-snapshot --snapshot-id {snap_id} --output table") 
        elif Input == "3":
           print("Press 1: To Create Key-pair\n\
                 Press 2: To See Availiable Key-pairs\n\
                 Press 3: To Delete Key-Pair\n\
                 Press 4: To Create Security-group\n\
                 Press 5: To Delete Security-group\n\
                 Press 6: To Add Rules in Security Group\n\
                 Press 7: To See Available Security-group")
           Input_key = input("Select To Use That Service: ")
           if Input_key == "1":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} > {key_name}.pem --output table")
           elif Input_key == "2":
               key_name = input("Enter The Name Of Yout Key-Pair")
               os.system(f"/usr/local/bin/aws ec2 delete-key-pair --key-name {key_name} --output table") 
           elif Input_key == "3":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} --output table")
           elif Input_key == "4":
               GN = input("Enter The Name For Your Security Group")
               d = input("Add Description for your Security Group")
               os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {GN} --description {d} --output table")
           elif Input_key == "5":
               GN = input("Enter The Name of Your Security Group")
               os.system(f"/usr/local/bin/aws ec2 delete-security-group --group-name {GN} --output table")
           elif Input_key == "6":
               print("Press 1: To Adding egress rule\n\
                      Press 2: To Adding Ingress rule")
               rule = input("Choose The Desire Option:")
               if rule == "1":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       cidr = input("Enter the IP of the PC that you want to allow:")
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                   
               elif rule == "2":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   cidr = input("Enter the IP of the PC that you want to allow:")
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                  
           elif Input_key == "7":
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
    elif Input == "4":
        print("\tPress 1: To Create User\n\
              Press 2: To Delete User\n\
                  Press 3: To Create access Key And Secret Key\n\
                      Press 4: To Attach policy to User")
        Input_iam = input("Select To Use That Service: ")
        if Input_iam == "1":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-user --user-name {user_name} --output table")
        elif Input_iam == "2":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam delete-user --user-name {user_name} --output table")
        elif Input_iam == "3":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-access-key --user-name {user_name} --output table")
        elif Input_iam == "4":
            policy = input("Enter The Name Of Policy:")
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam attach-user-policy\
                      --policy-arn arn:aws:iam:199619846734:aws:policy/{policy} --user-name  {user_name} --output table")    
    elif Input == "5":
        print("\tPress 1: To Create Bucket\n\
              Press 2: To Delete Bucket\n\
                  Press 3: To Put Object in Bucket\n\
                      Press 4: To Delete Object in Bucket\n\
                          Press 5: To List Bucket in S3\n\
                              Press 6: To List Object in Bucket")
        Input_s3 = input("Select The Service:")
        if Input_s3 == "1":
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api create-bucket --bucket {bucket_name} --region ap-south-1 --output table")
        elif Input_s3 == "2":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api delete-bucket --bucket {bucket_name} --output table")
        elif Input_s3 == "3":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("name of File you Want To Transfer: ")
            os.system("/usr/local/bin/aws s3api put-object --bucket {bucket_name} --key dir-1/{file_name} --body {file_name} --output table")
        elif Input_s3 == "4":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("Name of Object you Want to Delete:")
            os.system(f"/usr/local/bin/aws s3api delete-object --bucket {bucket_name} --key {file_name} --output table")
        elif Input_s3 == "5":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
        elif Input_s3 == "6":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system(f"/usr/local/bin/aws s3api list-objects --bucket {bucket_name} --output table")
    elif Input == "6":
        print("\tPress 1: To Create Distribution\n\
           Press 2: To Delete Distribution\n\
           Press 3: To Update Distribution")
        Input_cf = input("Select The Service You Want To run:")
        if Input_cf == "1":
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object:")
            os.system(f"/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
        elif Input_cf == "2":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
        elif Input_cf == "3":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
            dis_id = input("Enter Your Dictribution ID: ")
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object: ")
            os.system(f"/usr/local/bin/aws cloudfront update-distribution --id {dis_id} --origin-domain-name {origin_name} --default-root-object {object_name} --output table")



          

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:48:04 2020

@author: kartik_rama_arora
"""
import os

while True:
    print("\tPress 1: To Install AWS CLI\n\
          Press 2: To Configure AWS CLI\n\
       \tPress 3: To Use EC2 Service\n\
       \tPress 4: To Use IAM Service\n\
       \tPress 5: To Use S3 Service\n\
       \tPress 6: To Use Cloud Front\n")
    Input = input("Select To Use That Service: ")   
    if Input == "1":
        os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip' -o 'awscliv2.zip'")
        os.system("unzip awscliv2.zip")
        os.system("sudo ./aws/install")
        print("successfully Installed!!")
    elif Input == "2":
        os.system("/usr/local/bin/aws configure")
    elif Input == "3":
        print("\tPress 1: Work With Instances\n\
              \tPress 2: Work with EBS\n\
              \tPress 3: work with Network & Security")
        Input = input("Select To Use That Service: ")
        if Input == "1":
           print("Press 1: Create Instances\n\
                  Press 2: Start Instances\n\
                  Press 3: Stoping Instances\n\
                  Press 3: Terminating Instance\n\
                  Press 4: Reboot Instance\n\
                  Press 5: Available Instances\n\
                  Press 6: Describe Instance\n\
                  Press 7: To Transfer File to Instance\n\
                  Press 8: To Retrive File From Instance\n\
                  ")
           Input = input("Select To Use That Service: ")
           if Input == "1":
               image_search = input("Do you want to list all the AMI ? :  ")
               if image_search == "yes":
                   print("Available Image IDs")
                   os.system("/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table")
               elif image_search == "no":
                   IS = input("Search your Desirable AMI: ")
                   print("Available Image IDs")
                   os.system(f"/usr/local/bin/aws ec2 describe-images --query 'Images[*].[ImageId,Description,name]' --output table | grep {IS}")
               image_id = input("choose The Image ID:")
               os.system("/usr/local/bin/aws ec2 describe-instance-types --output table | grep 'InstanceType\|DefaultVCpus\|SizeInMiB'")
               instance_type = input("Choose The Instance Type: ")
               os.system("/usr/local/bin/aws ec2 describe-key-pairs --output table")
               key_name = input("Choose The Key-Pair: ")
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
               Security_group = input("Choose The Security Group: ")
               os.system("/usr/local/bin/aws ec2 describe-subnets --output table")
               Subnet_id = input("Choose The Subnet ID: ")
               Count = input("Choose The Number of Instance you want to Launch: ")
               os.system(f"/usr/local/bin/aws ec2 run-instance\
                                          --image-id {image_id}\
                                          --instance-type {instance_type}\
                                          --key-name {key_name}\
                                          --security-group-ids {Security_group}\
                                          --subnet-id {Subnet_id} --count {Count} --output table")
           elif Input == "2":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To start: ") 
               os.system(f"/usr/local/bin/aws ec2 start-instances --instance-ids {instance_id} --output table")
           elif Input == "3":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To stop: ") 
               os.system(f"/usr/local/bin/aws ec2 stop-instances --instance-ids {instance_id} --output table")
           elif Input == "4":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Terminate: ") 
               os.system(f"/usr/local/bin/aws ec2 terminate-instances --instance-ids {instance_id} --output table")
           elif Input == "5":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_id = input("Enter The ID of Your Instanace That you want To Reboot: ") 
               os.system(f"/usr/local/bin/aws ec2 reboot-instances --instance-ids {instance_id} --output table")
           elif Input == "6":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
           elif Input == "7":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance ip: ")
               
               Path = input("Enter The Path Of your File: ")
               os.system("scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' {Path} ec2-user@{instance_ip}:/home/ec2-user/ ")
           elif Input == "8":
               os.system("/usr/local/bin/aws ec2 describe-instances --output table")
               instance_ip = input("Select The Desire Instance: ")
               
               Path = input("Enter The Path Of your File: ")
               cwd = os.getcwd()
               os.system(f"scp -i '/Users/kartik_rama_arora/Downloads/RHEL-8.pem' ec2-user@{instance_ip}:{Path} {cwd}")
        elif Input == "2":
            print("\tPress 1: To Create Volume\n\
              \tPress 2: To Delete Volume\n\
                  \tPress 3: To Modify volume\n\
              \tPress 4: To Attach Volume\n\
              \tPress 5: To Detaching Volume\n\
              \tPress 6: To Describe Volume\n\
                  \tPress 7: To Create Snapshot\n\
                      \tPress 8: To Delete Snapshot")
            Input_vol = input("Select The Service you Want To Use") 
            if Input_vol == "1":
            
                vol_type = input("Select The Available Volume Type: ")
                vol_size = input("Enter The Size Of Volume(in GiB): ")
                AZ = input("Enter The Avaliability Zone: ")
                os.system(f"/usr/local/bin/aws ec2 create-volume --volume-type --size {vol_size} --availability-zone {AZ} --output table")
            elif Input_vol == "2":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 delete-volume --volume-id {vol_id} --output table")
            elif Input_vol == "3":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Modify: ")
                ol_size = input("Enter The Size Of Volume(in GiB): ")
                os.system(f"/usr/local/bin/aws ec2 modify-volume --volume-id {vol_id} --size {vol_size} --output table")
            elif Input_vol == "4":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Attach: ")
                os.system("/usr/local/bin/aws ec2 describe-instances --output table")
                instance_id = input("Enter The ID of Your Instanace: ")
                os.system("/usr/local/bin/aws ec2 attach-volume --volume-id {vol_id}\
                      --instance-id {instance_id} --device --output table")
            elif Input_vol == "5":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume You Want to Delete: ")
                os.system(f"/usr/local/bin/aws ec2 detach-volume --volume-id {vol_id} --output table")
            elif Input_vol == "6":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
            elif Input_vol == "7":
                os.system("/usr/local/bin/aws ec2 describe-volumes --output table")
                vol_id = input("Enter The ID of Volume for snapshot: ")
                vol_des = input("anything you want to put in Description:")
                if vol_des == "no" or "No":
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --output table")
                else:    
                    os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol_id} --description {vol_des} --output table")
            elif Input_vol == "8":
                snap_id = input("Enter your Snapshot ID: ")
                os.system(f"/usr/local/bin/aws ec2 delete-snapshot --snapshot-id {snap_id} --output table") 
        elif Input == "3":
           print("Press 1: To Create Key-pair\n\
                 Press 2: To See Availiable Key-pairs\n\
                 Press 3: To Delete Key-Pair\n\
                 Press 4: To Create Security-group\n\
                 Press 5: To Delete Security-group\n\
                 Press 6: To Add Rules in Security Group\n\
                 Press 7: To See Available Security-group")
           Input_key = input("Select To Use That Service: ")
           if Input_key == "1":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} > {key_name}.pem --output table")
           elif Input_key == "2":
               key_name = input("Enter The Name Of Yout Key-Pair")
               os.system(f"/usr/local/bin/aws ec2 delete-key-pair --key-name {key_name} --output table") 
           elif Input_key == "3":
               key_name = input("Enter the Desire Name To Your Key Pair: ")
               os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {key_name} --output table")
           elif Input_key == "4":
               GN = input("Enter The Name For Your Security Group")
               d = input("Add Description for your Security Group")
               os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {GN} --description {d} --output table")
           elif Input_key == "5":
               GN = input("Enter The Name of Your Security Group")
               os.system(f"/usr/local/bin/aws ec2 delete-security-group --group-name {GN} --output table")
           elif Input_key == "6":
               print("Press 1: To Adding egress rule\n\
                      Press 2: To Adding Ingress rule")
               rule = input("Choose The Desire Option:")
               if rule == "1":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       cidr = input("Enter the IP of the PC that you want to allow:")
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-egress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                   
               elif rule == "2":
                   os.system("/usr/local/bin/aws ec2 describe-security-groups --output table ")
                   sg_id = input("Enter your Security Group Id:")
                   protocol =	{
                       "HTTP": 80,
                       "SSH": 22,
                       "SMTP": 25 ,
                       "DNS":53 ,
                       "POP3":110 ,
                       "IMAP":143 ,
                       "LDAP":389 ,
                       "HTTPS":443 ,
                       "SMB":445,
                       "SMTPS":465 ,
                       "IMAPS":993 ,
                       "POP3s":995 ,
                       "MSSQL":1433 ,
                       "NFS":2049 ,
                       "MYSQL/AURORA":3306 ,
                       "RDP":3389 ,
                       "Redshift":5439 ,
                       "Postgresql":5432 ,
                       "All Traffic": 0-65535
                      }
                   print("\n\1. HTTP\n\
                       2. SSH\n\
                       3. SMTP\n\
                       4. DNS\n\
                       5. POP3\n\
                       6. IMAP\n\
                       7. LDAP\n\
                       8. HTTPS\n\
                       9. SMB\n\
                       10. SMTPS\n\
                       11. IMAPS\n\
                       12. POP3s\n\
                       13. MSSQL\n\
                       14. NFS\n\
                       15. MYSQL/AURORA\n\
                       16. RDP\n\
                       17. Redshift\n\
                       18. Postgresql\n\
                       19. All Traffic")
                   P = input("Enter The Protocol Name:")
                   cidr = input("Enter the IP of the PC that you want to allow:")
                   if P == "All Traffic":
                           os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol all --port {protocol[{P}]} --cidr 0.0.0.0/0 --output table")
                
                   else:
                       os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {sg_id} --protocol tcp --port {protocol[{P}]} --cidr {cidr} --output table")
                  
           elif Input_key == "7":
               os.system("/usr/local/bin/aws ec2 describe-security-groups --output table")
    elif Input == "4":
        print("\tPress 1: To Create User\n\
              Press 2: To Delete User\n\
                  Press 3: To Create access Key And Secret Key\n\
                      Press 4: To Attach policy to User")
        Input_iam = input("Select To Use That Service: ")
        if Input_iam == "1":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-user --user-name {user_name} --output table")
        elif Input_iam == "2":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam delete-user --user-name {user_name} --output table")
        elif Input_iam == "3":
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam create-access-key --user-name {user_name} --output table")
        elif Input_iam == "4":
            policy = input("Enter The Name Of Policy:")
            user_name = input("Enter Ther User Name:")
            os.system(f"/usr/local/bin/aws iam attach-user-policy\
                      --policy-arn arn:aws:iam:199619846734:aws:policy/{policy} --user-name  {user_name} --output table")    
    elif Input == "5":
        print("\tPress 1: To Create Bucket\n\
              Press 2: To Delete Bucket\n\
                  Press 3: To Put Object in Bucket\n\
                      Press 4: To Delete Object in Bucket\n\
                          Press 5: To List Bucket in S3\n\
                              Press 6: To List Object in Bucket")
        Input_s3 = input("Select The Service:")
        if Input_s3 == "1":
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api create-bucket --bucket {bucket_name} --region ap-south-1 --output table")
        elif Input_s3 == "2":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system("/usr/local/bin/aws s3api delete-bucket --bucket {bucket_name} --output table")
        elif Input_s3 == "3":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("name of File you Want To Transfer: ")
            os.system("/usr/local/bin/aws s3api put-object --bucket {bucket_name} --key dir-1/{file_name} --body {file_name} --output table")
        elif Input_s3 == "4":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket: ")
            file_name = input("Name of Object you Want to Delete:")
            os.system(f"/usr/local/bin/aws s3api delete-object --bucket {bucket_name} --key {file_name} --output table")
        elif Input_s3 == "5":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
        elif Input_s3 == "6":
            os.system("/usr/local/bin/aws s3api list-buckets --output table")
            bucket_name = input("Enter The Name Of The Bucket:")
            os.system(f"/usr/local/bin/aws s3api list-objects --bucket {bucket_name} --output table")
    elif Input == "6":
        print("\tPress 1: To Create Distribution\n\
           Press 2: To Delete Distribution\n\
           Press 3: To Update Distribution")
        Input_cf = input("Select The Service You Want To run:")
        if Input_cf == "1":
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object:")
            os.system(f"/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
        elif Input_cf == "2":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
        elif Input_cf == "3":
            os.system("/usr/local/bin/aws cloudfront list-distributions --output table")
            dis_id = input("Enter Your Dictribution ID: ")
            origin_name = input("Enter The Name Of Origin: ")
            object_name = input("Enter The Name Of Object: ")
            os.system(f"/usr/local/bin/aws cloudfront update-distribution --id {dis_id} --origin-domain-name {origin_name} --default-root-object {object_name} --output table")
