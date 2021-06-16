# Web-Scraping-Challenge

The Mission_to Mars directory contains these files:

	* mission_to_mars jupyter notebook file	
	* scrape_mars python file
	* app python file
	* templates directory with index html file
	
1. Complete initial scraping using BeautifulSoup, Pandas, and Requests/Splinter using the mission_to_mars jupyter notebook. The data scraped is shown below:

	* Scrape the (https://redplanetscience.com/) and collect the latest News Title and Paragraph Text
	* Scrape the (https://spaceimages-mars.com) and collect the featured image url
	* Scrape the (https://galaxyfacts-mars.com) and collect the mars facts and convert to html table
	* Scrape the (https://marshemispheres.com/) and collect the image urls for the 4 hemisphere images

2. Convert mission_to_mars to a python file that has function called scrape that performs all the scraping created in the jupyter notebook

3. Use MongoDB with Flask templating to create a new HTML page (index.html) that displays all of the information that was scraped from the URLs above
