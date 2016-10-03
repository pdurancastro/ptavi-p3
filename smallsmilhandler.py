#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
    
        self.width = "0"
        self.height = "0" 
        self.background_color = ""
        self.id = ""
        self.top = "0"
        self.bottom = "0"
        self.left = "0"
        self.right = "0"
    
    def startElement(self, name, attrs):
    
        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.background_color = attrs.get('background_color',"")
            
        if name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")    
            
            
            
        
    

    
    #def get_tags(self):
        #return self.misdatos
    
        
        
if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
           
        


