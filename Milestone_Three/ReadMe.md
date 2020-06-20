## Milestone 3 : Accessing to hive database using Python

### Title : Application of Data Mining in Price Movement of Cryptocurrency

### Team Member: 
### 1. Tan Chang Jung
### 2. Tan Sia Hong

### Presentation Video: https://drive.google.com/file/d/1gp7MtpHjfgn9bRYkURwl3R8gEiLTqBJQ/view?usp=sharing

##### Python accessed to Hive database by using ODBC connection, which is required library 'pyodbc'.

### pyodbc : pip install pyodbc (https://pypi.org/project/pyodbc/)

### Notes:
1. Set the hive authorization to be PLAIN, which is ‘None’ in Hortonworks Sandbox.
![image](https://user-images.githubusercontent.com/55917583/85195132-a2271c00-b302-11ea-9f1d-082d991cb987.png)

2. Open ‘ODBC Data Source Administration’ in Windows, setup the ODBC connection. 
The default port for Hive is 10000.  
The default credentials for connection is: 
##### User: hive 
##### Password: hive 
![image](https://user-images.githubusercontent.com/55917583/85195153-d7cc0500-b302-11ea-8996-0d21901c72fa.png)

Then click ‘Test’ for testing the connection, make sure it shows Success! 
![image](https://user-images.githubusercontent.com/55917583/85195156-eaded500-b302-11ea-9491-b31e83db5797.png)
