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
query = {'resume': processor.text('Dexter'), 'title': processor.text('Dexter'), 'cast': processor.text('Dexter')}

iFile = index.Frequency()
iFile.load()
rank = ranking.Ranking(iFile)
f = iFile.search(query)
#print(f)
#doc = {'6385': {'title': {'pretti': 1}, 'resume': {'pretti': 7}}, '626': {'title': {'pretti': 1, 'littl': 1, 'liar': 1}, 'resume': {'pretti': 1, 'littl': 1, 'liar': 1}}, '11988': {'title': {'pretti': 1}}, '4790': {'title': {'pretti': 1}}}
result2 = rank.rank(query, f)
result3 = rank.rank(query, f, BM25=True)
result4 = rank.rank(query, f, zone_score=True)

fi = index.Basic()
fi.load()

result5 = rank.rank(query, f, boolean=True)
result6 = rank.rank(query, f, boolean=True, zone_score=True)
print('Frequencia: ', result2[:10])
print('BM25 ', result3[:10])
print('ZOne score tfidf: ', result4[:10])
print('boolean: ', result5[:10])
print('zone score boolean: ', result6[:10])

print('kendau tau between tfidf and BM25: ', rank.kendaltau_correlation(result2, result3))
print('kendau tau between tfidf and zonesocre:', rank.kendaltau_correlation(result2, result4))
print('kendau tau between tfidf and boolean:', rank.kendaltau_correlation(result2, result5))
print('kendau tau between zonescore and boolean:', rank.kendaltau_correlation(result5, result6))



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
