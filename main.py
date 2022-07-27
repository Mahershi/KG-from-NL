import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.parse.stanford import StanfordDependencyParser
# from nltk.parse.corenlp import CoreNLPDependencyParser
from nltk.grammar import DependencyGrammar
stopwords = set(stopwords.words('english'))

path_to_jar = '/Users/mahershibhavsar/Downloads/stanford-parser-full-2020-11-17/stanford-parser.jar'
path_to_models = '/Users/mahershibhavsar/Downloads/stanford-parser-full-2020-11-17/stanford-parser-4.2.0-models.jar'

dependecy_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models)
# dependecy_parser = CoreNLPDependencyParser(url='http://localhost:9000')

txt = 'Google is based from Canada'
txt = 'Google will hold a podcast tomorrow'
txt = 'Google will hold a podcast outside'
txt = 'Google sells Android phones'
txt = 'Apple does not sell Android phones'
txt = 'Google sells great Android phones'
# txt = 'Apple sells only ios phones'
txt = 'Google stole the prototype built by Apple'
txt = 'Apple is more advanced than Google'

print(nltk.pos_tag(word_tokenize(txt)))
result = dependecy_parser.raw_parse(txt)
dep = result.__next__()

for d in list(dep.triples()):
    print(d)

