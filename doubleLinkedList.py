from nltk.parse.corenlp import CoreNLPDependencyParser
import networkx as nx
import matplotlib.pyplot as plt


head_label = '__HEAD__'
head_edge = '__head__'
head_tag = '__tag__'

graph_edges = []
graph_edge_labels = {}
graph_nodes = []
global dependency_parser

modifier_dependencies = ['amod', 'advmod', 'nmod']

class ModifierNode:
    root = None
    leaf = None
    label = None
    tag = None

    def __init__(self, root=None, leaf=None, label=None, tag=None):
        self.root = root
        self.leaf = leaf
        self.label = label
        self.tag = tag

class Node:
    next = None
    prev = None
    edge = None
    tag = None
    label = None
    mods = None
    mod_edge = None

    def __init__(self, prev = None, next=[], edge=[], tag=None, label=None, mod=[], mod_edge=[]):
        self.prev = prev
        self.label = label
        self.edge = edge
        self.next = next
        self.tag = tag
        self.mod = mod
        self.mod_edge = mod_edge

    @classmethod
    def create_head(cls):
        return cls(tag=head_tag, label=head_label)

    def attach(self, edge, node):
        self.next.append(node)
        self.edge.append(edge)

    def show(self):
        if self.prev:
            print("LABEL:", self.label, " TAG:", self.tag, " PREV:", self.prev.label)
        else:
            print("LABEL:", self.label, " TAG:", self.tag, " PREV: NONE",)
        for e, n in zip(self.edge, self.next):
            print(e)
            print(n)
            n.show()

head = Node.create_head()

def init():
    global dependency_parser
    dependency_parser = CoreNLPDependencyParser(url='http://localhost:9000')

def parse(sentence):
    global dependency_parser, graph_edges, graph_edge_labels
    parse = dependency_parser.raw_parse(sentence)
    dep = parse.__next__()
    head = Node.create_head()
    prev = head
    for i, d in enumerate(list(dep.triples())):
        print(i)
        print(d)
        if i == 0:
            c = Node(tag=d[0][1], label=d[0][0], prev=prev, next=[])
            print(c)
            # if not cleaning prev sentence from head, it merges
            prev.next = []
            prev.edge = []
            prev.attach(edge=head_edge, node=c)
            graph_edges.append([prev.label, c.label])
            graph_edge_labels[(prev.label, c.label)] = head_edge
            prev = prev.next[-1]
            # prev.show()

        while prev.label != d[0][0]:
            prev = prev.prev
        print("CUR root: ", prev.label)
        c = Node(tag=d[2][1], label=d[2][0], prev=prev, next = [])
        prev.attach(edge=d[1], node=c)
        graph_edges.append([prev.label, c.label])
        graph_edge_labels[(prev.label, c.label)] = d[1]

        prev = prev.next[-1]

    print(sentence)
    print("TRAVERSE ---------------------------------------------------------")
    head.show()
    print("---------------------------------------------------------")




def draw():
    graph = nx.Graph()
    graph.add_edges_from(graph_edges)
    pos = nx.spring_layout(graph)
    plt.figure()
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=graph_edge_labels)
    nx.draw(graph, pos, edge_color='black', width=2, labels={node: node for node in graph.nodes()}, with_labels=True)
    plt.axis('off')
    plt.show()

init()
parse("Apple is a surprisingly successful tech company")
# parse("Great Google sells Android phones")
# parse("Apple sells IOS phones")
# draw()



