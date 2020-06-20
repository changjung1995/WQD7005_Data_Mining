## Milestone 5 : Deployment in Web and Mobile App  

### Title : Application of Data Mining in Price Movement of Cryptocurrency

### Team Member: 
### 1. Tan Chang Jung
### 2. Tan Sia Hong

### Presentation Video: https://drive.google.com/file/d/1TzXuZFZEBHPbe4aUVoM1QOSjoOCdCtW2/view?usp=sharing

### Web link: https://cryptofortwp.herokuapp.com/

### Mobile .apk file: https://drive.google.com/file/d/1V7mxJGB2b8lqo5kCZqARHbzFXjeewds3/view?usp=sharing

##### Part 1 Web Application 
In milesone 5, we are required to deploy our works that generated from Milestone 1 to 4, in the web application and mobile application. In the development, we were using python ‘Dash’. Dash is an interactive Python framework that developed by Plotly. Dash aimed for building the web applications, it built on top of Flask. It enables us to build the dashboards using pure Python. Furthermore, Dash is an open source, and its application able to run on the web browser. 

![image](https://user-images.githubusercontent.com/55917583/85195253-72c4df00-b303-11ea-9110-42838cd952d3.png)

Firstly, the historical data for closing, opening, highest, and lowest prices of cryptocurrencies will be crawl by using Beautiful Soup. A function for web scraping is written as function ‘web_scraper’ in tests.py, so that the function able to scrape the historical dataset as the cryptocurrency is selected by end-user.

Then, the crawled dataset will be used to plot the line graph and caddlestick. 
![image](https://user-images.githubusercontent.com/55917583/85195273-98ea7f00-b303-11ea-9228-a8949af05f42.png)

Other than that, the crawled dataset was used to present in the table data. 
![image](https://user-images.githubusercontent.com/55917583/85195305-d8b16680-b303-11ea-9f1d-3a49e350f8a3.png)

Furthermore, the previous 90-days of closing price will be used to predict the one-step ahead closing price by using the trained LSTM model. 
![image](https://user-images.githubusercontent.com/55917583/85195318-e961dc80-b303-11ea-9e3c-3679a29c6dda.png)

In addition, we have used the NewsAPI for crawling the news headline related to cryptocurrencies. When user clicks on the headline, the web will redirect the user to the news webpage.  
 
##### Part 2 Mobile App 
The Android mobile application was created by using Android Studio.  

1. Inside the app/src/main/res/layout/activity_main.xml, under the Palette section, we created a WebView. We set the properties of webview with both height and width to be “fill_parent’. 

2. Under the ‘MainActivity.java’, we created a private class for WebView, which is under the public class MainActivity.  
![image](https://user-images.githubusercontent.com/55917583/85195335-0696ab00-b304-11ea-9e4e-24e786f2051b.png)
The webview will load the url from our web application. 

3. Under the AndroidManifest.xml, we added the user permission with internet permission inside the xml
<uses-permission android:name="android.permission.INTERNET"></uses-permission> 

4. To make sure the app is suitable with any screen size, we added the following properties
![image](https://user-images.githubusercontent.com/55917583/85195348-2af28780-b304-11ea-96fe-c3db7206f80e.png)

The final view of mobile app will looks as below:

![image](https://user-images.githubusercontent.com/55917583/85195359-3940a380-b304-11ea-953a-b6bb8d1bbb2b.png)
