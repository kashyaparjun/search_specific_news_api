import urllib3
import requests
import json
import re
from bs4 import BeautifulSoup
hk = raw_input()
king = "https://www.google.com/search?hl=en&gl=in&tbm=nws&authuser=0&q=" + hk

http = urllib3.PoolManager()
request = http.request('GET', king)
a = request.data
pay = json.dumps(a)
ul = BeautifulSoup(pay)
tmp = ul.findAll("a")
betr = []
for t in tmp:
    yl = str(t)
    gh = yl.find("http")
    tb = yl.find("html")
    gp = yl.find(".ece")
    gp = gp+4
    tb = tb+4
    kl = yl[gh:tb]
    gr = yl[gh:gp]
    if kl.find("http")>-1:
        betr.append(kl)
    if gr.find("http")>-1:
        betr.append(gr)
        
#print "here"
    
yp = []
for b in betr:
    gk = True
    for y in yp:
        if b==y:
            gk = False
    if gk==True:
        yp.append(b)
            
            
for p in yp:
    print p
    print " "