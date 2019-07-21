# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:37:26 2017

@author: Mario
"""

import unittest, random

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
            	unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]

class testPoint(unittest.TestCase):
    def setUp(self):
        self.seq = [random.randint(0,10000) for i in range(5)]
        
    def testSort(self):
        b = [i for i in self.seq]
        ordenamientoBurbuja(b)
        self.seq.sort()
        self.assertEqual(self.seq, b)

        
if __name__ == '__main__':
    unittest.main()