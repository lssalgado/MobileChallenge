#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import os
sys.path.insert(0,'.')
import fruitShop


fs = fruitShop


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__


def checkOneFruit():
    blockPrint()
    expected = u"\n0 - Apple\nPrice:  $35.00\nPreço: R$122.50"
    fruitsJson = fs.getJson("")["fruits"]
    fs.jsonIterator(fruitsJson)
    result = fs.buildString(fruitsJson, 0)
    enablePrint()
    if result == expected:
        print "checkOneFruit() PASSED"
        
    else:
        print "checkOneFruit() FAILED"
        print "expected was:"
        print expected
        print "\nresult was:"
        print result 
        
    
def checkAllFruits():
    blockPrint()
    expected = [u'\n0 - Apple\nPrice:  $35.00\nPre\xe7o: R$122.50', u'\n1 - Banana\nPrice:  $12.00\nPre\xe7o: R$42.00', u'\n2 - Grapes\nPrice:  $45.00\nPre\xe7o: R$157.50', u'\n3 - Pineapple\nPrice:  $200.00\nPre\xe7o: R$700.00', u'\n4 - Cherry\nPrice:  $13.00\nPre\xe7o: R$45.50', u'\n5 - Clementine\nPrice:  $12.40\nPre\xe7o: R$43.40', u'\n6 - Olive\nPrice:  $9.50\nPre\xe7o: R$33.25', u'\n7 - Tomato\nPrice:  $8.75\nPre\xe7o: R$30.63', u'\n8 - Huckleberry\nPrice:  $11.75\nPre\xe7o: R$41.13', u'\n9 - Papaya\nPrice:  $2.75\nPre\xe7o: R$9.63', u'\n10 - Lime\nPrice:  $5.75\nPre\xe7o: R$20.13', u'\n11 - Pear\nPrice:  $4.75\nPre\xe7o: R$16.63']
    fruitsJson = fs.getJson("")["fruits"]
    fs.jsonIterator(fruitsJson)
    i = 0
    result = []
    for j in fruitsJson:
        resultString = fs.buildString(fruitsJson, i)
        result.append(resultString)
        i += 1
    enablePrint()
    if result == expected:
        print "checkAllFruits() PASSED"
        
    else:
        print "checkAllFruits() FAILED"
        print "expected was:"
        print expected
        print "\nresult was:"
        print result 
        

def checkOutOfBounds():
    blockPrint()
    expected = u"\n0 - Apple\nPrice:  $35.00\nPreço: R$122.50"
    fruitsJson = fs.getJson("")["fruits"]
    fs.jsonIterator(fruitsJson)
    try:
        result = fs.buildString(fruitsJson, len(fruitsJson))
    except:
        try:
            result = fs.buildString(fruitsJson, "a")
        except:
            enablePrint()
            print "checkOutOfBounds() PASSED"
            return
    enablePrint()
    print "checkOutOfBounds() FAILED"
    

def main():
    checkOneFruit()
    checkAllFruits()
    checkOutOfBounds()


if __name__ == "__main__":
    main()