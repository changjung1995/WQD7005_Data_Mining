## Milestone 1 : Web crawling the real time data by using Python

### Title : Application of Data Mining in Price Movement of Cryptocurrency

### Team Member: 
### 1. Tan Chang Jung
### 2. Tan Sia Hong

### Presentation video: https://www.youtube.com/watch?v=fU2Db8uiP8U&t=1078s

### Documentation: https://github.com/changjung1995/WQD7005_Data_Mining/blob/master/Milestone_One/Milestone1_Tan_Chang_jung.pdf

### Beautiful Soup (https://pypi.org/project/bs4/) --pip install bs4

##### Introduction
How do the cryptocurrencies behave? What are the causes of the fluctuation of cryptocurrency value? How can we predict the future value of cryptocurrencies? 

There are a huge number of articles on the cryptocurrencies, are widespread with speculation these dats, with thousands of guide and forum advocating for the trends that experts expect to emerge.

Therefore, in the Data Mining assignment, we are going to explore and analyze the trend of cryptocurrency value by using the data mining technique.

##### Web scraping and BeautifulSoup 
Normally, the cryptocurrency data we are looking for is on a web page, which is neither ready to be downloaded nor available with API. Meanwhile, we can perform web scraping technique by scraping the web pages CoinMarketCap with Python using BeautifulSoup and requests. 

In CoinMarketCap, we have selected the top 20 cryptocurrencies from the list and identified the URL structure as the page we want to scrape for 20 cryptocurrencies.  

![image](https://user-images.githubusercontent.com/55917583/85194587-87ec3e80-b300-11ea-9893-fc97e8181e50.png)

The base url for web scraping is shown as above, we are required to change the highlighted part to the name of cryptocurrencies that would like to scrape, the the historical data including closing, opening, highest, lowest, volume and market capacity, will being scrape.  

Then, inspect on any of the value from the browser. The HTML line highlighted in gray corresponds to what we have seen on the web page.

![image](https://user-images.githubusercontent.com/55917583/85194638-a5b9a380-b300-11ea-9e04-949c41806f2f.png)

In Python, we were using BeautifulSoup to parse the HTML content. We parsed the response.text by creating a BeautifulSoup object, and assign this object to ‘soup’. 

![image](https://user-images.githubusercontent.com/55917583/85194712-be29be00-b300-11ea-8c1f-4e1ea0b9e35e.png)

There are many div containers on the webpages, we need to figure out what distinguishes the cryptocurrencies data from other div elements on that page. Often, the distinctive mark resides in the class attribute.  

However, we noticed that there are three div containers were using the same class id, which is ‘cmc-table__table-wrapper-outer’,
![image](https://user-images.githubusercontent.com/55917583/85194757-d7326f00-b300-11ea-82be-396d5847c2f7.png)

We found out that the data value for cryptocurrency that we would like to scrape is with the last div container. Inside the container, we search for all rows with tag tr and all columns td within each tr. Then we parse all the content of columns from row to row, and create a dataframe for the dataset. Finally, we cleaned and changed the data types for certain columns and saved it as csv file.

![image](https://user-images.githubusercontent.com/55917583/85194778-ec0f0280-b300-11ea-867c-eb1796b66597.png)
