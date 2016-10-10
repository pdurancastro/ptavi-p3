#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler
import json
import urllib.request

try:
    ficherosys = sys.argv[1]
except:
    sys.exit("Usage: python3 karaoke.py file.smil.")


class KaraokeLocal():

    def __init__(self, ficherosys):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(ficherosys))
        self.mytags = cHandler.get_tags()

    def __str__(self):
        for Lista in self.mytags:
            for tag in Lista:
                newatt = " "
                for att, value in Lista[tag].items():
                    newatt = newatt + '\t' + att + "=" + value + '\t'
            print(tag + newatt + '\n')

    def to_json(self, var_json, nuevo_nombre=""):
        var_json = sys.argv[1][:-4]+"json"
        json.dump(self.mytags, open(var_json, 'w'))

    def do_local(self):
        for Lista in self.mytags:
            for tag in Lista:
                for att, value in Lista[tag].items():
                    if 'src' in att:
                        if value[:4] == "http":
                            urllib.request.urlretrieve(value,
                                                       value.split('/')[-1])

if __name__ == "__main__":

        karaokelocal1 = KaraokeLocal(ficherosys)
        karaokelocal1.__str__()
        karaokelocal1.to_json(ficherosys)
        karaokelocal1.do_local()
        karaokelocal1.to_json(ficherosys, "local.json")
        karaokelocal1.__str__()
