import os
import getpass

#hadoop menu

def hadoop_menu():
    print("\n\t############################################################")
    print("""\n\t\tPress 1:Configure Hadoop Server
    \t\tPress 2:Start Hadoop Services
    \t\tPress 3:Show Cluster report
    \t\tPress 4:List the files which are uploaded in the cluster
    \t\tPress 5:Read files from Cluster
    \t\tPress 6:Upload file into the cluster
    \t\tPress 7:Stop Hadoop Services
    \t\tPress 8:Remove File from cluster
    \t\tPress 0:Exit from Menu""")
    print("\n\t############################################################")

def hdfs_conf(node,location):
    if location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' '>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
            master_dir=input("Enter the directory you want to use for the namenode:")
            os.system("echo '<name>dfs.name.dir</name>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<value>%s</value>'>> /etc/hadoop/hdfs-site.xml"%master_dir)
            os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("scp /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml"%remoteip)

        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' '>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
            slave_dir=input("Enter the directory you want to use for the datanode:")
            os.system("echo '<name>dfs.data.dir</name>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<value>%s</value>'>> /etc/hadoop/hdfs-site.xml"%slave_dir)
            os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("scp /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml"%remoteip)

    elif location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' '>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
            master_dir=input("Enter the directory you want to use for the namenode:")
            os.system("echo '<name>dfs.name.dir</name>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<value>%s</value>'>> /etc/hadoop/hdfs-site.xml"%master_dir)
            os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
        

        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' '>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
            slave_dir=input("Enter the directory you want to use for the datanode:")
            os.system("echo '<name>dfs.data.dir</name>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<value>%s</value>'>> /etc/hadoop/hdfs-site.xml"%slave_dir)
            os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
        



def core_conf(node,location):
    if location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' '>> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>'>> /etc/hadoop/core-site.xml")
            cluster_port=input("Enter the port number:")
            os.system("echo '<value>hdfs://0.0.0.0:%s</value>'>> /etc/hadoop/core-site.xml"%cluster_port)
            os.system("echo '</property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            os.system("scp /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/core-site.xml"%remoteip)

        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' '>> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>'>> /etc/hadoop/core-site.xml")
            master_ip=input("Enter the IP of namenode:")
            cluster_port=input("Enter the port number:")
            os.system("echo '<value>hdfs://%s:%s</value>'>> /etc/hadoop/core-site.xml"%(master_ip,cluster_port))
            os.system("echo '</property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            os.system("scp /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/core-site.xml"%remoteip)

    elif location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' '>> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>'>> /etc/hadoop/core-site.xml")
            cluster_port=input("Enter the port number:")
            os.system("echo '<value>hdfs://0.0.0.0:%s</value>'>> /etc/hadoop/core-site.xml"%cluster_port)
            os.system("echo '</property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            

        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\"href\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<!--Put site-specific property override in this file.-->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' '>> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>'>> /etc/hadoop/core-site.xml")
            master_ip=input("Enter the IP of namenode:")
            cluster_port=input("Enter the port number:")
            os.system("echo '<value>hdfs://%s:%s</value>'>> /etc/hadoop/core-site.xml"%(master_ip,cluster_port))
            os.system("echo '</property>'>> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            

def packages(node,location):
    dir=input("Enter the path where java and hadoop packeges resides:")
    print(dir)
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NAMENODE":
            os.system("rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm".format(dir))
            os.system("rpm -ivh {}/jdk-8u171-linux-x64.rpm".format(dir))
        elif node=="datanode" or node=="Datanode" or node=="DATANODE":
            os.system("rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm".format(dir))
            os.system("rpm -ivh {}/jdk-8u171-linux-x64.rpm".format(dir))

    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NAMENODE":
            os.system("ssh {} rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm --force".format(remoteip,dir))
            os.system("ssh {} rpm -ivh {}/jdk-8u171-linux-x64.rpm".format(remoteip,dir))
        elif node=="datanode" or node=="Datanode" or node=="DATANODE":
            os.system("ssh {} rpm -ivh {}/hadoop-1.2.1-1.x86_64.rpm --force".format(remoteip,dir))
            os.system("ssh {} rpm -ivh {}/jdk-8u171-linux-x64.rpm".format(remoteip,dir))


def start_services(node,location):
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop namenode -format")
            os.system("hadoop-daemon.sh start namenode")
            os.system("jps")
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop-daemon.sh start datanode")
            os.system("jps")
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop namenode -format")
            os.system("ssh {} hadoop-daemon.sh start namenode".format(remoteip))
            os.system("ssh {} jps".format(remoteip))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop-daemon.sh start datanode".format(remoteip))
            os.system("ssh {} jps".format(remoteip))

def cluster_report(node,location):
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop dfsadmin -report|less")
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop dfsadmin -report|less")
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop dfsadmin -report|less".format(remoteip))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop dfsadmin -report|less".format(remoteip))

def stop_services(node,location):
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop-daemon.sh stop namenode")
            os.system("jps")
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop-daemon.sh stop datanode")
            os.system("jps")
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop-daemon.sh stop namenode".format(remoteip))
            os.system("ssh {} jps".format(remoteip))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop-daemon.sh stop datanode".format(remoteip))
            os.system("ssh {} jps".format(remoteip))

def list_file(node,location):
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop fs -ls /")
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop fs -ls /")
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop fs -ls /".format(remoteip))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop fs -ls /".format(remoteip))


def read_file(node,location):
    file_name=input("Enter the name of uploaded file which you want to read:")
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop fs -cat /{}".format(file_name))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop fs -cat /{}".format(file_name))
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop fs -cat /{}".format(remoteip,file_name))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop fs -cat /{}".format(remoteip,file_name))        


def upload_file(node,location):
    filename=input("Enter the name of file which you want to upload:")
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop fs -put {} /".format(filename))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop fs -put {} /".format(filename))
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop fs -put {} /".format(remoteip,filename))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop fs -put {} /".format(remoteip,filename))   

def remove_file(node,location):
    file_name=input("Enter the name of uploaded file which you want to remove:")
    if location=="local":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("hadoop fs -rm /{}".format(file_name))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("hadoop fs -rm /{}".format(file_name))
    elif location=="remote":
        if node=="namenode" or node=="Namenode" or node=="NameNode":
            os.system("ssh {} hadoop fs -rm /{}".format(remoteip,file_name))
        elif node=="datanode" or node=="Datanode" or node=="DataNode":
            os.system("ssh {} hadoop fs -rm /{}".format(remoteip,file_name))        

os.system("clear")
os.system("tput setaf 3")
print("\t\t\t!!!Welcome to Hadoop Automation!!!")
os.system("tput setaf 7")
print("\t**************************************************************")

#To set Password

i=0
while i<2:
    password=getpass.getpass("Enter the Password (pass1234):")
    actual_pass="pass1234"
    if password==actual_pass:
        os.system("tput setaf 6")
        print("Login successfully")
        os.system("tput setaf 7")
        break
    else:
        os.system("tput setaf 1")
        print("Wrong Password...Plase try again...")
        os.system("tput setaf 7")

    i+=1

else:
    os.system("tput setaf 1")
    print("Authentication Failed!!!\nExiting...")
    os.system("tput setaf 7")
    os.system("sleep 1")
    exit()      

location=input("Where do you want to perform task?(local/remote):")


while True:
    if location=="remote":
        remoteip=input("Enter the IP of remote server:")
        hadoop_menu()
        i=int(input("\n\t\tEnter your Choice:"))
        print(i)
        if i==1:
            
            node=input("Which node you want to configure?(namenode/datanode):")
            packages(node,location)
            node=input("Which node you want to configure?(namenode/datanode):")
            print("Configuring hdfs-site.xml...")
            hdfs_conf(node,location)
            print("Configuring core-site.xml...")
            core_conf(node,location)

        elif i==2:
            node=input("Which node's services you want to start?(datanode/namenode):")
            start_services(node,location)
        elif i==3:
            node=input("From Which node you want to see report?(datanode/namenode):")
            cluster_report(node,location)
            
        elif i==4:
            node=input("From Which node you want to list files?(datanode/namenode):")
            list_file(node,location)
            
        elif i==5:
            node=input("From Which node you want to read file?(datanode/namenode):")
            read_file(node,location)
        
        elif i==6:
            node=input("From Which node you want to upload file?(datanode/namenode):")
            upload_file(node,location)
            os.system("date")
        elif i==7:
            node=input("Which node's services you want to stop?(datanode/namenode):")
            stop_services(node,location)

        elif i==8:
            node=input("From Which node you want to remove file?(datanode/namenode):")
            remove_file(node,location)    
        elif i==0:
            print("Exiting from automation...")
            exit()
        else:
            print("Choice doesn't supported...")
            input("Press Enter to continue...")
            os.system("clear")
         
    elif location=="local":
        hadoop_menu()
        i=int(input("\n\t\tEnter your Choice:"))
        print(i)
        if i==1:
            
            node=input("Which node you want to configure?(namenode/datanode):")
            packages(node,location)
            print("Configuring hdfs-site.xml...")
            hdfs_conf(node,location)
            print("Configuring core-site.xml...")
            core_conf(node,location)

        elif i==2:
            node=input("Which node's services you want to start?(datanode/namenode):")
            start_services(node,location)
            
        elif i==3:
            node=input("From which node you want to see report?(datanode/namenode):")
            cluster_report(node,location)
            os.system("date")
        elif i==4:
            node=input("From Which node you want to list files?(datanode/namenode):")
            list_file(node,location)
            os.system("date")
        elif i==5:
            node=input("From Which node you want to read file?(datanode/namenode):")
            read_file(node,location)
            os.system("date")
        elif i==6:
            node=input("From Which node you want to upload file?(datanode/namenode):")
            upload_file(node,location)
            os.system("date")
        elif i==7:
            node=input("Which node's services you want to stop?(datanode/namenode):")
            stop_services(node,location)
            os.system("date")
        elif i==8:
            node=input("From Which node you want to remove file?(datanode/namenode):")
            remove_file(node,location)    
        elif i==0:
            print("Exiting from automation...")
            exit()
        else:
            print("Choice doesn't supported...")

        input("Press Enter to continue...")
        os.system("clear")
    else:
        print("Location doesn't supported...")
        exit()
