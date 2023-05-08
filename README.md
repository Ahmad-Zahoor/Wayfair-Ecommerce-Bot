
# Wayfair Ecommerce Bot

Wayfair Ecommerce Bot is a web scraping tool which made for Wayfair Furniture products data which  website link is https://www.wayfair.com/brand/bbb/browse-by-brand. Where the bot search different brands by alphabet letter, if alphabet found then bot will open it and scrape its target data. 
Wayfair Bot for scraping ecommerce website data would likely use a library such as Selenium to navigate and extract specific information from the website's HTML. The bot could be programmed to scrape data such as product names, prices, sku, and categories names and product links, and then organize and export that data into a format such as CSV for further analysis. The bot could also be set up to run on a regular schedule to continuously gather and update the data. Additionally, the bot may use web scraping tools such as Selenium or Scrapy to interact with the website and to bypass any anti-scraping measures put in place.

## What is Wayfair?

Wayfair is an online home goods retailer that offers a wide selection of furniture, home decor, and household essentials. The website features an easy-to-use interface and a wide variety of products, including sofas, chairs, tables, beds, rugs, lighting, and much more. Customers can shop by room, style, or brand to find the perfect items for their home.
In addition to a wide selection of products, Wayfair also offers a variety of services to make the shopping experience as easy and convenient as possible. These include free shipping on eligible items, a 30-day return policy, and a team of design experts available to answer any questions and offer advice.
Wayfair's website also features a variety of design inspiration and ideas, including curated collections and room tours that showcase different styles and trends. This can help customers get a sense of how different products will look in their own home, and make it easier to find the perfect items for their space.
Overall, Wayfair is a great choice for anyone looking for stylish and affordable home goods. With a wide selection of products, convenient services, and expert design advice, the website makes it easy to create a beautiful and functional home.

## Bot Functionalities

* GUI (Graphical User Interface) fields: Bot will take input file, Start counter, Folder name from GUI.

    * Input file: The file which consist of all Wayfair furniture brands links from which data will be scraped.
    * Start counter: The start counter mean that if an input file have 50 links and you want to start from 25 then you will use this start counter filed where you can input 25 and bot will start from it.
    * Folder name: Here Folder name mean that the data will be store in this folder after completing the scraping. 

* GUI (Graphical User Interface) Validation: 

    * if any input field in GUI empty bot will show an error box to fill that input filed.
    * If input file not exist bot will show an error box that your input file not exist in the directory. 
    * If counter less than 0 or equal to 0 bot will show an error box that enter greater than 0 numbers in counter field.
    * If starts counter greater that input file length then bot will show an error box that enter number between 1 and length of input file.

* List Creation: Bot will get all links from input file and store it in a list variable.
* Bot will display total links and New Folder name in CMD.
* Bot will lunch the browser using webdirver.
* Bot will scroll to “All Brands A-Z”.
* Bot will scrape all alphanumeric characters.
* If vendor name match with alphanumeric letter than bot will click on that letter.
* Bot will scrape all sub vendor list.
* If our vendor name found in Wayfair vendor list bot will store it in a list.
* Bot will open each vendor link.
* Bot will scrape brand name and make a folder with that name.
* Bot will scrape all categories of that vendor.
* Bot will open each category link.
* Bot will scrape each category products.
* Bot will scrape the following data:

    * Category Name: Bot will scrape each category name.
    * Product Name: Bot will scrape each product name. 
    * Product Link: Bot will scrape each product link.
    * Product SKU: Bot will scrape each product SKU.
    * Wayfair Price: Bot will scrape each product price.
    * Armand Price: Bot will subtract 5 from each Wayfair price and make an Armand price.

* Store Result Data: Bot will store all scraping data in a csv file.
* Close Driver: After completing the scraping data bot will close the driver.
* Stope Bot: If client want to stop the bot so the bot gui have a stop button from pressing it GUI will show a message box that you want to stop the program or not if client click ok then bot will stop the scraping and close the browser.
