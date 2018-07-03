from operator import itemgetter
import vectorial_model
import numpy as np 
import math

class Ranking(object): 
    def __init__(self): 
        self.tf = {}
        self.idf = {}
        self.tfidf = {}

    def query_weightless(self, query):
        r = [1 for x in query]
        return r
            
    def remove_duplicates (self, query): 
        r = []
        for x in query: 
            if x not in r: 
                r.append(x)
        return r
    
    def document_weightless(self, query, document): 
        result = {} 
        for x in document:
            r = {} 
            for y in query:
                vec = []
                if y not in document[x].keys(): 
                    vec = [0 for i in query[y]]
                else: 
                    for term in query[y]: 
                        if term in document[x][y]: 
                            vec.append(1)
                        else: 
                            vec.append(0)
                r.update({y: vec})
            result.update({x: r})
        return result
    
    def query_weight(self, query): 
        result = {}
        #query = self.build_vec(query)
        #query = self.remove_duplicates(query)
        r = []
        
        for term in query:
            r.append(query.count(term))
        print(query, r)
        return r
    
    def build_vec(self, query, document=False, boolean=False): 
        #print(query)
        result = []
        #print(query, result)
        for att in query:
            for q in query[att]: 
                if not document or not boolean:  
                    result.append(q+'.'+att)
                else:
                    result.append(((q+'.'+att), query[att][q]))
        
        return result
    
    def document_weight(self, query, document):  
        vec_model = vectorial_model.Vectorial_Model()  
        result = {}
        idf = {}

        query = self.build_vec(query)
        query = self.remove_duplicates(query)
        
        for doc in document:
            tf = {}
            cur_doc = self.build_vec(document[doc], document=True)
            cur_doc = self.remove_duplicates(cur_doc)
            for term in query:
                vec = 0
                if(term in cur_doc):
                    q = term.split('.')
                    vec = document[doc][q[1]][q[0]]
                    if(term in idf.keys()):
                        idf[term] += 1
                    else: 
                        idf.update({term: 1})     
                else: 
                    vec = 0
                    if(term in idf.keys()):
                        idf[term] += 0
                    else: 
                        idf.update({term: 0})
                tf.update({term: vec})
            result.update({doc: tf})
        
        n_doc = len(document)
        query_vec = self.query_weight(query)
        rank = []
        for x in result: 
            r = []
            for term in query:
                if idf[term] != 0:
                    tfidf = result[x][term]*math.log10(n_doc/idf[term])
                else: 
                    tfidf = 0
                r.append(tfidf)
            cos = vec_model.cossine(r, query_vec)
            rank.append((x, cos))

        return rank
    
    def all_pairs (self, rank): 
        a = set()
        for i in range(len(rank)): 
            for j in range(i+1, len(rank)):
                a.add((rank[i], rank[j]))
        return a 

    # returns kendal tau correlation between two ranks 
    def kendaltau_correlation(self, rank1, rank2):
        k = len(rank1)
        pairs1 = self.all_pairs(rank1)
        pairs2 = self.all_pairs(rank2)
        conc = 0 
        disc = 0
        for x in pairs1: 
            if(x in pairs2): conc += 2
            else: disc += 2
        return abs(conc - disc)/ k*(k-1)

    def rank (self, query, inverted_file, boolean=False): 
        vec_model = vectorial_model.Vectorial_Model()
        doc_rank = {}

        if(not boolean): 
            doc_vec = self.document_weight(query, inverted_file)
            q_vec = self.query_weight(query)
        else: 
            doc_vec = self.document_weightless(query, inverted_file)
            q_vec = self.query_weightless(query)
        '''
        for doc in inverted_file: 
            for att in doc_vec[doc]:
                if att not in doc_rank.keys(): 
                    doc_rank.update({att: []})
                cos = vec_model.cossine(doc_vec[doc][att], q_vec[att])
                doc_rank[att].append((doc, cos))
        
        for att in doc_rank: 
            doc_rank[att] = sorted(doc_rank[att], key=itemgetter(1), reverse=True)
        
        '''
        
                

        
# TESTE 
r = Ranking() 
inverted_file = {178: {'resume': ['doctor']}, 57: {'resume': ['doctor']}, 155: {'resume': ['doctor']}, 386: {'resume': ['doctor']}, 67: {'resume': ['doctor']}, 305: {'resume': ['doctor']}, 111: {'resume': ['doctor']}, 52: {'resume': ['doctor']}, 224: {'resume': ['doctor']}, 55: {'resume': ['doctor']}}
query = {'title':['greys', 'doctor', 'doctor'], 'resume':['doctor', 'hospital','grey', 'greys', 'greys', 'hospital']}
doc = {67: {'title': ['doctor'], 'resume': ['doctor']}, 224: {'title': ['doctor'], 'resume': ['doctor']}, 178: {'resume': ['doctor']}, 57: {'resume': ['doctor']}, 155: {'resume': ['doctor']}, 386: {'resume': ['doctor']}, 305: {'resume': ['doctor']}, 111: {'resume': ['doctor']}, 52: {'resume': ['doctor']}, 55: {'resume': ['doctor']}}

doc_frec = {'67': {'title': {'doctor': 1}, 'resume': {'doctor': 1}}, 
'224': {'title': {'doctor': 1}, 'resume': {'doctor': 1}}, '178': {'resume': {'doctor': 1}}, 
'57': {'resume': {'doctor': 1}}, '155': {'resume': {'doctor': 1}}, '386': {'resume': {'doctor': 1}}, 
'305': {'resume': {'doctor': 1}}, '111': {'resume': {'doctor': 1}}, '52': {'resume': {'doctor': 1}}, 
'55': {'resume': {'doctor': 2}}}

#document = ['valdmeiro e muito falso porque ele e muito falso']
#a = r.query_weightless(query)
#a = r.query_weight(query)
#a = r.build_vec(doc_frec['67'], document=True, boolean=False)
b = r.document_weight(query, doc_frec)
print(b)
    # Duvida: 
    # 
    # como monta o vetor da query e documento (calcular o tfidf dentro da query e fazer que fiz antes)
    # como monta o vetor da query sem o tfidf 
    # é pra usar o cosseno? pode usar jaccard? (implementar ambos ) 
    # par importa a ordem que aparece no ranking (importa)
    # 
    # 
    # 
    # 
    #
    # 
#a = r.rank(query, doc_frec)