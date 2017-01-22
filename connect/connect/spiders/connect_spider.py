## Made by Prithi Pal Singh

## available for open source.

from splinter import Browser
import sys
import scrapy
import logging
import getopt


class connectSpider(scrapy.Spider) :
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    logging.getLogger('scrapy').propagate = False
    name = 'connect_spider'

    #accept command line arguments




    global b
    b = Browser('chrome')

    def start_requests(self) :

        b.visit('https://connect.sfu.ca')
        b.find_by_id('username').first.fill(str(self.username))
        b.find_by_id('password').first.fill(self.password)
        b.find_by_value('Sign In').first.click()
        #loged in
        cookiesFromSplinter= b.cookies.all()
        #print("response from splinter = ",str(b.url))
        yield scrapy.Request(url="https://connect.sfu.ca",callback=self.parse,cookies=cookiesFromSplinter)

    def parse(self,response) :
        print("response from scrapy = ",str(response.url))
        print("title from page = ",str(response.css('title::text').extract()))
        all_links = response.css('a::attr(href)').extract()
        print('start all_links')
        myfile = open('all_linke.txt','w')
        link_count=0
        link_processed = 0
        logout_link = ''
        new_link=""

        for i in all_links:
            if "logout" in i :
                logout_link = "https://connect.sfu.ca" + str(i)

            link_count=link_count+1

            if i[:6] == "search" : #opens the email into the sidebar
                print ("link = ",str(i))
                myfile.write("original = " + str(response.url) + "\n")
                myfile.write("new = " + str(i) + "\n")
                link_processed=link_processed+1
                new_link = str(response.url[:32]) + str(i)
                print("new_link = ",str(new_link))
                b.visit(str(new_link))
                print("browser new")

        print("crawling ended")
        myfile.write("total links = " + str(link_count) + "\n")
        myfile.write("total search links = " + str(link_processed) + "\n")
        print("logging out now")
        b.visit(str(logout_link))
