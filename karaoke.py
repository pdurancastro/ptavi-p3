#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler



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
    print(mytags)
    
    
    print(mytags[0])
    
    



