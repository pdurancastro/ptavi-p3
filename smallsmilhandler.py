#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""

        self.tags=[]

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.background_color = attrs.get('background-color',"")
            att={'width': self.width, 'height': self.height,
                'background_color': self.background_color}
            roottag={'root-layout':att}
            self.tags.append(roottag)
            #print(self.tags)

        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('rigth',"")
            att={'id': self.id, 'top': self.top, 'bottom': self.bottom,
                'left': self.left, 'right': self.right}
            rootag={'region':att}
            self.tags.append(rootag)
            print(self.tags)











    #def get_tags(self):
        #return self.misdatos



if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
