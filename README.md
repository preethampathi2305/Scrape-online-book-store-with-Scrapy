# Scrape-online-book-store-with-Scrapy
Scraping all the image URLs ,Book titles and prices of all the books from an online book store.

The main file which contains the code to recursively scrape all the pages available through the next page button is in "../bookstore/spiders/book.py".
1.To run this, first install scrapy with "conda install -c conda-forge scrapy" command in your terminal. 
2.Then run "scrapy startproject bookstore" in the terminal.
3.Then download the "../bookstore/spiders/book.py" file and place it inside the "bookstore/spiders/" directory.
4.Then run "scrapy crawl book_spider -o output.json" in your terminal. (book_spider is the name of the spider set in the book.py file)

You can now check the output.json file in your main directory where you will find the json file with the desired data.
