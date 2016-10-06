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
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""

        self.tags=[]

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.background_color = attrs.get('background-color',"")
            att={'width': self.width, 'height': self.height,
                'background_color': self.background_color}
            roottag={'root-layout': att}
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
            regiontag={'region': att}
            self.tags.append(regiontag)

        elif name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            att={'src': self.src, 'region': self.region, 'begin': self.begin,
                'dur': self.dur}
            imgtag={'img': att}
            self.tags.append(imgtag)

        elif name == 'audio':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            att={'src': self.src, 'begin': self.begin, 'dur': self.dur}
            audiotag={'audio':att}
            self.tags.append(audiotag)

        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            att={'src': self.src, 'region': self.region}
            texttag={'textstream':att}
            self.tags.append(texttag)


    def get_tags(self):
        return self.tags


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    mytags=cHandler.get_tags()
    print(mytags)
