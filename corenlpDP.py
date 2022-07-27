from collections import defaultdict

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.corenlp import CoreNLPDependencyParser
from nltk.grammar import DependencyGrammar
stopwords = set(stopwords.words('english'))

# path_to_jar = '/Users/mahershibhavsar/Downloads/stanford-parser-full-2020-11-17/stanford-parser.jar'
# path_to_models = '/Users/mahershibhavsar/Downloads/stanford-parser-full-2020-11-17/stanford-parser-4.2.0-models.jar'

# dependecy_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models)
dependecy_parser = CoreNLPDependencyParser(url='http://localhost:9000')

txt = 'Google is based in Canada'
# txt = 'Google will hold a podcast tomorrow'
# txt = 'Google will hold a podcast outside'
# txt = 'Google sells Android phones'
# txt = 'Apple does not sell Android phones'
# txt = 'Google sells great Android phones'
# txt = 'Apple sells only ios phones'
txt = 'Google sells Android phones'
# txt = 'Apple sells ios phones'
# txt = 'Apple does not sell Android phones'
txt = 'Google sells great Android phones'
# txt = 'Google sells Android phones but not ios'
# txt = 'Google sells Android but not ios phones'
# txt = 'Google sells phones and tablet'
# txt = 'Google sells phones as well as tablets'
# txt = 'Google sells neither pants nor shirts'
# txt = 'Google was founded in 1990 by Ginny'
# txt = 'Ginny founded Google in 1990'
# txt = 'Amaxon was founded by Ginny and Jenny'
# txt = 'Ginny and Jenny founded Amaxon'
# txt = 'Google is a big tech company that sells phones'
# txt = 'Google stole the prototype built by Apple'
# txt = 'Apple is more advanced than Google'
# txt = 'Apple is more advanced in India'
# txt = "Google is a tech company"
txt = "Rahul is a professor"
# txt = "Google was founded in 1999"
# txt = "Google sells Android but not iOS Phones"
# txt = "Drunkenness reveals what soberness conceals"
# txt = "After moving to Canada, Mahershi graduated from the University of Regina"
txt = "Android phones were sold by Google"
txt = "Genny and Jinny founded Google"
txt = "Google was founded by Ginny and Jenny in 1999"
print(txt)
parse = dependecy_parser.raw_parse(txt)
dep = parse.__next__()
dependencies = defaultdict(list)
pos = defaultdict()
for d in list(dep.triples()):
    print(d)
    dependencies[d[1]].append((d[0][0], d[2][0]))
    pos[d[0][1]] = d[0][0]
    pos[d[2][1]] = d[2][0]


print(dependencies)
print(pos)
#
# print(nltk.pos_tag(word_tokenize(txt)))
# result = dependecy_parser.raw_parse(txt)
# dep = result.__next__()
#
# for d in list(dep.triples()):
#     print(d)

