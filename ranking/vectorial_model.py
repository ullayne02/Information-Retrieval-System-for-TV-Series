import numpy as np 
import math

class Vectorial_Model(object): 
    def __init__(self): 
        self.a = []

    def norm (self, document): 
        size = [x**2 for x in document]
        size = math.sqrt(sum(size))
        if (size != 0):
            normalized = [x/size for x in document]
        else: normalized = document
        return normalized

    def cossine(self, document, query): 
        document = self.norm(document)
        query = self.norm(query)
        cos = np.dot(document, query)
        return cos

a = Vectorial_Model()
b = [1,2,3]
c = [2,3,2]
b_nomr = a.norm(b)
c_nomr = a.norm(c)

#print(b_nomr, c_nomr)
#print(a.cossine(b_nomr, c_nomr))