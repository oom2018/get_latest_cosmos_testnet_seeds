#!/usr/bin/python
import sys
import urllib2
import json

#print "\n\n"

html = urllib2.urlopen(r'https://rpc.nylira.net/net_info')
#html = urllib2.urlopen(r'http://localhost:8080/net_info')
# print html.read()
hjson = json.loads(html.read())

# print hjson
#sys.stdout.write("out ")
out = ""
for p in hjson["result"]["peers"]:
    p=p["node_info"]
    if p["listen_addr"].startswith("10."):
        continue
    if p["listen_addr"].startswith("192."):
        continue
    if p["listen_addr"].startswith("172."):
        continue

    #sys.stdout.write(p["id"]+'@'+p["listen_addr"]+",")
    out = out + p["id"]+'@'+p["listen_addr"]+","
out = out[:-1]
print out


#print "\n\n"

for p in hjson["result"]["peers"]:
    p=p["node_info"]
    if p["listen_addr"].startswith("10."):
        continue
    if p["listen_addr"].startswith("192."):
        continue
    if p["listen_addr"].startswith("172."):
        continue

    #print p["network"]+" " + p["id"]+'@'+p["listen_addr"] +" " + p["moniker"] + " " + p['version']

