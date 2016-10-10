#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler
import json



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
        
    json.dumps(mytags, open('karaoke.json'))
    
            
    
    
    



