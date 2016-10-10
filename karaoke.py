#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler
import json
import urllib.request



if __name__ == "__main__":

    try:
        ficherosys = sys.argv[1]
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")
            
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(ficherosys))
    mytags = cHandler.get_tags() 
    
    
    for Lista in mytags:
        for tag in Lista:
            newatt=""      
            for att, value in Lista[tag].items():
                newatt= newatt + '\t' + att + "=" + value + '\t'
        print (tag + newatt + '\n')
        
   
    #Pasar mi karaoke SMIL a JSON
    var_json = sys.argv[1][:-4]+"json"
    json.dump(mytags,open (var_json, 'w'))
    
    
    
    
    #EJ 5
    #local_filename, headers = urllib.request.urlretrieve('http://www.content-networking.com/smil/')
    #html = open(local_filename)
    
    
    for Lista in mytags:
        for tag in Lista:
            for att, value in Lista[tag].items():
                if 'src' in att:
                    if value[:4] == "http":  
                        print(value)                                         
                        urllib.request.urlretrieve(value,value.split('/')[-1])
                        
                  
                        
    
    



