## Milestone 2 : Store data into Hive data warehouse

### Title : Application of Data Mining in Price Movement of Cryptocurrency

### Team Member: 
### 1. Tan Chang Jung
### 2. Tan Sia Hong

### Presentation Video: https://drive.google.com/file/d/1Edhkywf2lKtzASOhj_xPABT-_Jh4zHB_/view?usp=sharing

### Hortonworks Sandbox HDP : https://www.cloudera.com/downloads/hortonworks-sandbox.html

### WinSCP : https://sourceforge.net/projects/winscp/files/WinSCP/5.17.6/WinSCP-5.17.6-Setup.exe/download


##### PART 1 Install Hortonworks HDP
Hortonworks sandbox will be used for the milestone 2. 

1. Download Hortonworks HDP from https://www.cloudera.com/downloads/hortonworkssandbox.html (20GB). 

2. Import .ova into VM Virtualbox. 
![image](https://user-images.githubusercontent.com/55917583/85194976-6d669500-b301-11ea-9025-060fe017ef14.png)
![image](https://user-images.githubusercontent.com/55917583/85194989-7fe0ce80-b301-11ea-920a-8c30d4833318.png)
*Optimize the number of CPU cores and RAM resources before import. 

3. Run the Hortonworks Sandbox HDP 3.0 for extraction and installation. Notice that first time installation will take around 15 minutes. 

4. In the web browser, go to web shell client by accessing http://localhost:4200/. The default root user login credentials will be: 
User: root 
Password: hadoop 

After logging in by default password, you will be requested to change password. Please change the password for root user.
![image](https://user-images.githubusercontent.com/55917583/85195016-ab63b900-b301-11ea-8e93-88943c172f97.png)

5. Ambari enables system administrators to provision, manage and monitor a Hadoop cluster. Now, type ‘ambari-admin-password-reset’ to reset the Ambari’ administrator password.
![image](https://user-images.githubusercontent.com/55917583/85195035-d64e0d00-b301-11ea-91c7-4499e3c5820c.png)

6. Access to http://localhost:8080/ for Ambari login.
![image](https://user-images.githubusercontent.com/55917583/85195047-ec5bcd80-b301-11ea-94b2-1ba89bea90c3.png)

7. After logging in, you will see the sandbox is taking some time to starting all the required services (around 15 mins). 
![image](https://user-images.githubusercontent.com/55917583/85195056-fd0c4380-b301-11ea-9f3b-c989c196b854.png)

8. The hive and HDFS are completely set up and ready to be used.

##### PART 2 Store data into hive database
1. Download and install WinSCP 
https://winscp.net/eng/download.php 

2. Send the local Windows’ data into sandbox (VM) by using WinSCP
![image](https://user-images.githubusercontent.com/55917583/85195072-1ad9a880-b302-11ea-9446-2cf4e75783b6.png)

3. Go to web shell client,  
hdfs fs -put /root/data/*.csv /user/root/datamining/data/ 
This is to copy the file from root directory into another directory of HDFS. 

4. Open hive in web shell client, use the database preferred, then create a table under the database. 
Eg. Table ‘bitcoin’
![image](https://user-images.githubusercontent.com/55917583/85195094-4066b200-b302-11ea-935e-cfbbcd16b698.png)

Then load the csv data from HDFS into bitcoin table. 
![image](https://user-images.githubusercontent.com/55917583/85195104-53798200-b302-11ea-87fd-4bad71405f75.png)
