## WQD 7005 Data Mining Assignment

### Title : Application of Data Mining in Price Movement of Cryptocurrency

### Team Member: 
### 1. Tan Chang Jung
### https://github.com/changjung1995/WQD7005_Data_Mining

### 2. Tan Sia Hong
### https://github.com/jasonhong94/-WQD7005_Data_Mining

### Summary for the assignment (from milestone 1 to 5)

##### 1. Milestone 1 (https://github.com/changjung1995/WQD7005_Data_Mining/tree/master/Milestone_One)
##### Presentation video: https://www.youtube.com/watch?v=fU2Db8uiP8U&t=1078s
In Milestone 1, I was crawled the price of cryptocurrencies from https://coinmarketcap.com/. The first 20 top cryptocurrencies was crawled by using Python BeautifulSoup. There are 6 columns exist in the dataset, which are close, high, low, open, volume and market capacity. The dataset was cleaned, and the data types were changed accordingly. Lastly, the cleaned dataset was save as csv files.

![image](https://user-images.githubusercontent.com/55917583/85192293-8e74b900-b2f4-11ea-8f9b-7cbd1a2ffbf4.png)

##### 2. Milestone 2 (https://github.com/changjung1995/WQD7005_Data_Mining/tree/master/Milestone_Two)
##### Presentation video: https://drive.google.com/file/d/1Edhkywf2lKtzASOhj_xPABT-_Jh4zHB_/view?usp=sharing
In Milestone 2, the crawled data are required to store in the data warehouse. We need data warehouse instead of RDBMS database as data warehouse is designed to separate the big data analysis and query process. This is designed to facilitate decision making by consolidate and analyze information at different levels. I was installing Hortonworks Sandbox, as Hortonworks comes with Apache Hadoop and Apache Hive on top of the Hadoop. Hortonworks is an open source, as it faster the deployment process. At the end of installation, I was successfully load the data into Hive database with mysql as database schema.

![image](https://user-images.githubusercontent.com/55917583/85192441-1c50a400-b2f5-11ea-8861-fd5435bee79d.png)

##### 3. Milestone 3 (https://github.com/changjung1995/WQD7005_Data_Mining/tree/master/Milestone_Three)
##### Presentation video: https://drive.google.com/file/d/1gp7MtpHjfgn9bRYkURwl3R8gEiLTqBJQ/view?usp=sharing
In Milestone 3, I was connected to Hive database via Python by using pyodbc library. First, it is required to create a data server name to using Microsoft ODBC data source, as the connection to Hive was done through ODBC connection. After connected with correct host and port, as well as its authorization, I was able to access Hive database by using Python. 

![image](https://user-images.githubusercontent.com/55917583/85192861-b9600c80-b2f6-11ea-833d-de19c17b82f7.png)

##### 4. Milestone 4 (https://github.com/changjung1995/WQD7005_Data_Mining/tree/master/Milestone_Four)
##### Presentation video: https://drive.google.com/file/d/1cahiU7gBkH0ZWA9OFyBGQlVXGcPr__gc/view?usp=sharing
In Milestone 4, I was doing descriptive analytics and predictive analytics on the cryptocurrencies dataset. From the descriptive analytics, it is obvious to see that, when there is one cryptocurrency increased in price, so do the other cryptocurrencies, or vice versa. Furthermore, the analytics told that the price of cryptocurrencies are fluctuated from time to time. In the predictive analytics, a Long-short Term Model from recurrent neural network, was trained to predict the future price with one day ahead. 

##### 5. Milestone 5 (https://github.com/changjung1995/WQD7005_Data_Mining/tree/master/Milestone_Five)
##### Presentation video: https://drive.google.com/file/d/1TzXuZFZEBHPbe4aUVoM1QOSjoOCdCtW2/view?usp=sharing
In Milestone 5, we were using python Dash to create the dashboard for web application. Dash is an open source framework on top of Flask. The web application was built to visualize the price of cryptocurrencies, as well as predicting the closing price for cryptocurrencies of next day. For the Android mobile application, we have converted our web application into mobile application by using Android Studio.

##### Web Application (http://cryptofortwp.herokuapp.com/)
![image](https://user-images.githubusercontent.com/55917583/85192720-28893100-b2f6-11ea-8eac-510ae72eb519.png)

##### Android Mobile App (https://drive.google.com/file/d/1V7mxJGB2b8lqo5kCZqARHbzFXjeewds3/view?usp=sharing)
![image](https://user-images.githubusercontent.com/55917583/85192742-3a6ad400-b2f6-11ea-823c-f40fb00ecc40.png)

