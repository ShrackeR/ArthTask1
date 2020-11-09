import os
import subprocess

def SPM_menu():
    os.system("clear")
    print("MENU - Static Partition Management:\n")
    print("1. View all Disk Partitions")
    print("2. View Specific Disk Partition")
    print("3. Delete a Partition")
    print("4. Create a New Partition")
    print("5. Format a Partition")
    print("6. Exit\n")
    choice = input("Enter your choice: ")

    if(choice == "1"):
        partlist = os.system("fdisk -l")
        print(partlist)
        input("Enter any key to go to menu.")
        SPM_menu()

    elif(choice == '2'):
        diskname = input("Enter disk name (For eg. /dev/sdb): ")
        disklist = os.system("fdisk -l " + diskname)
        print(disklist)
        input("Enter any key to go to menu.")
        SPM_menu()

    elif(choice=='3'):
        diskname = input("Enter Disk name (For eg. /dev/sdb): ")
        disklist = os.system("fdisk -l " + diskname)
        print(disklist)
        partno = input("Enter Partition no to delete: ")
        proc = subprocess.Popen(["sudo", "fdisk", diskname], stdin = subprocess.PIPE)
        cmd = 'd\n' + partno + '\nw'
        cmd = bytes(cmd, encoding='utf8')
        proc.communicate(cmd)
        input("Enter any key to go to menu.")
        SPM_menu()
    
    elif(choice=='4'):
        diskname = input("Enter Disk name (For eg. /dev/sdb): ")
        disksize = input("Enter Partition size in GB: ")
        disksize = '+' + disksize + 'G'
        proc = subprocess.Popen(["sudo", "fdisk", diskname], stdin = subprocess.PIPE)
        cmd = 'n\n\n\n\n'+ disksize + '\nw'
        cmd = bytes(cmd, encoding='utf8')
        proc.communicate(cmd)
        input("Enter any key to go to menu.")
        SPM_menu()

    elif(choice=='5'):
        diskname = input("Enter Disk name to format(For eg. /dev/sdb): ")
        disklist = os.system("fdisk -l " + diskname)
        print(disklist)
        partno = input("Enter Partition no to format: ")
        proc = subprocess.Popen(["sudo", "mkfs.ext4", diskname], stdin = subprocess.PIPE)
        proc.communicate(b'y')
        input("Enter any key to go to menu.")
        SPM_menu()
SPM_menu()


    
    
        


