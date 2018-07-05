# from indexer import processor
from indexer import index
from indexer import processor
from ranking import ranking
import json
import os

#iFile = index.Basic() #Basic() ou Positional()
#iFile.load()
#query = {'all':processor.text('the big bang theory'), 'resume': processor.text('seattle grace hospit')}
#document = iFile.search(query)
#print(document)
#result1 = rank.rank(query, document, boolean=True)
query = {'cast': processor.text('Will Smith, Niel Patrick Harry')}

iFile = index.Frequency()
iFile.load()
rank = ranking.Ranking(iFile)
f = iFile.search(query)
#print(f)
a = [576, 20284, 40, 11821, 17065, 676, 1149, 1454, 1502, 1622, 1629, 1643, 1668, 1700, 1892, 1894, 2912, 2940, 3109, 3330, 4000, 4212, 4786, 4795, 4885, 5132, 5160, 5215, 5258, 5467, 6684, 6747, 7199, 7831, 7887, 7908, 8146, 8482, 8620, 9224, 9240, 9665, 10113, 10301, 10394, 10458, 10582, 10800, 10887, 11217, 11278, 11470, 11610, 11847, 11875, 12008, 12560, 12921, 13068, 13115, 13322, 13545, 13641, 14105, 14817, 14935, 16152, 16481, 16574, 16655, 17145, 17360, 17523, 17862, 17965, 18425, 18540, 18700, 18741, 18995, 19468, 19722, 20222, 20355, 20483, 20549, 20617, 20719, 20729, 20767, 20934, 21034, 21105, 21112, 3220, 5321, 15957, 18366, 8798, 12535]
#doc = {'6385': {'title': {'pretti': 1}, 'resume': {'pretti': 7}}, '626': {'title': {'pretti': 1, 'littl': 1, 'liar': 1}, 'resume': {'pretti': 1, 'littl': 1, 'liar': 1}}, '11988': {'title': {'pretti': 1}}, '4790': {'title': {'pretti': 1}}}
result2 = rank.rank(query, f)
result3 = rank.rank(query, f, BM25=True)
result4 = rank.rank(query, f, zone_score=True)
print('lala: ', result2[:10])
print('with bm algorithm: ', result3[:10])
print(result4[:10])
print('aaaaaaaaaaaaaa: ', rank.kendaltau_correlation(result2, result3))
print('kendau tau between tfidf and zonesocre:', rank.kendaltau_correlation(result2, result4))
#print(result)
# {'67': {'title': {'doctor': [0]}, 'resume': {'doctor': [6]}}, '224': 
# {'title': {'doctor': [0]}, 'resume': {'doctor': [6]}}, '178': 
# {'resume': {'doctor': [3]}}, '57': {'resume': {'doctor': [3]}}, '155': 
# {'resume': {'doctor': [3]}}, '386': {'resume': {'doctor': [2]}}, '305': 
# {'resume': {'doctor': [2]}}, '111': {'resume': {'doctor': [11]}}, '52': 
# {'resume': {'doctor': [5]}}, '55': {'resume': {'doctor': [2, 16]}}}
# print(iFile.search({'all':['park', 'android']}))
#
# {
#     'title': processor.text('parque de diversao'),
#     'resume': processor.text('parque de diversao'),
#     'cast': processor.name(''),
#     'rate': processor.number(valor),
#     'genre': ['park', 'android']
# }


# filenames = list(os.walk('database/'))[0][2]
# filenames = sorted([ int(f[:-5]) for f in filenames if f != '.DS_Store' ])
# for i, filename in enumerate(filenames):
#     print(i, '-', filename)
#     with open('database/' + str(filename) + '.json') as fl:
#         item = json.load(fl)
#     for attr in ['title', 'genre', 'rate', 'resume', 'cast']:
#         aux = item.get(attr, None)
#         if aux is not None and aux != []:
#             if attr == 'title' or attr == 'resume':
#                 words = processor.text(aux)
#             elif attr == 'cast':
#                 words = []
#                 for actor in aux:
#                     words.extend(processor.name(actor))
#             elif attr == 'genre':
#                 words = processor.category(aux)
#             elif attr == 'rate':
#                 words = processor.number(aux)
#             iFile.insert(filename, attr, words)
# iFile.save()
#print(iFile.meanDocs())
#print(iFile.sumDocs())
