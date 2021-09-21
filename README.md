# Web Scraping Homework - Mission to Mars

For this assignment, I built a web application that scrapes various websites for data related to Mars. To accomplish this, first I had to develop the code to scrape the websites (after reviewing the sites, of course), then develop the flask app and html page to display the data. I used MongoDb to store the mars information every time the web scraping is performed from the app.

### Contents:
 - Jupyter notebook used to develop and test the web scraping code
 - Python code to define the scrape function
 - Python code to run the flask app and HTML page
 - HTML page within the templates folder that displays the scraped data (and runs the scrape function through the click of a button)

### How It Works:

1. Open the app.py file and run the code to open the web application. 
2. You will first see a Mission to Mars webpage with titles only, no data.
3. Click the Scrape New Data! button and you'll get the following:</br></br>
   <ul>
       <li>- Latest News Headline and Summary regarding Mars (website scraped: https://redplanetscience.com/)</li>
       <li>- A Featured Image of Mars (website scraped: https://spaceimages-mars.com/)</li>
       <li>- Mars Facts (website scraped: https://galaxyfacts-mars.com/)</li>
       <li>- An image for each of Mars' hemispheres (websites scraped:https://marshemispheres.com/)</li>
   </ul>
4. Note: the scraped data is stored in a newly created MongoDb called mars_db and a collection. If exists, each new scrape will be added as a document within the collection.
 

### Screenshots of the Web Application:

![1  mission_to_mars_webpage](https://user-images.githubusercontent.com/82002107/134254873-66585a89-5bd7-466c-8db4-45a6e8ce84eb.jpg)


![2  mission_to_mars_bottom_half](https://user-images.githubusercontent.com/82002107/134254891-60d21bb4-1e9b-40a1-bf59-3d2f0ab7cefb.jpg)
