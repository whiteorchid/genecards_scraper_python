### https://gist.github.com/pontikos/1635ddc88cb26c132b0b42592376e377  (thanks for the left link, according to this make a little modify and use it to get the Gene Function discription from gene card website: https://www.genecards.org )
from __future__ import print_function
import sys
import re
from selenium import webdriver
from random import randint
from time import sleep

dr = webdriver.Chrome('chromedriver')
#dr = webdriver.Chrome('chromedriver')
#dr.get('http://www.genecards.org')
#dr.get('http://www.genecards.org/cgi-bin/carddisp.pl?gene=%s' % "TP53")

with open('E:\\f.e3.txt','r',encoding='UTF-8') as f:
    for line in f.readlines():
        a = line.split()
        b = a[1]
        try:
            #dr = webdriver.Chrome('chromedriver')
            dr.get('http://www.genecards.org/cgi-bin/carddisp.pl?gene=%s' % b)
            dr.get_cookies()
            p=dr.page_source
            sleep(randint(1,10))
            #print(b, re.compile(r'Function:((\n|.)*?)<ul').search(p).group(1))
            #con =    b + re.compile(r'Function:((\n|.)*?)<ul').search(p).group(1)
            con = re.compile(r'Function:((\n|.)*?)<ul').search(p).group(1)
            con2 = con.replace("\<\/dt\>","") ## this has not been solved as I want to remove the line that contains </dt>
            con3 = con2.replace("\<dd\>","")  ##this has not been solved as I want to remove the line that contains <dd>
            con4 = con3.replace("\n","\t")
            print(con4)
            break
            #con.writelines('E:\\genefunc.txt','a')
        except:
            con =    b + "\t" + "NA"
            print(con)
            #con.writelines('E:\\genefunc.txt','a')
f.close()
