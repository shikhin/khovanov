import networkx as nx
import matplotlib.pyplot as plt
from Braid import *
from C2Minus import *
from FCC import *


# for testing that braids actually look the way they should
def view(g, b):
    height = 5+len(b.word)

    edges = [('t0p'+e[0][3:], e[1]) if e[0][:3] == 'top' else e for e in g.edges]
    vertices = g.vdict.keys() + ['t0p'+str(i) for i in range(1, b.n+1)]

    pos = {}
    for v in vertices:
        if v[:3]=='top':
            pos[v]=(int(v[3:]), height)
        elif v[:3]=='t0p':
            pos[v] = (int(v[3:]), 0)
        elif v[:3]=='mid':
            pos[v]=(int(v[3:])+.5, height-1)
        elif v[:3]=='bot':
            pos[v]=(int(v[3:])+1, height-2)
        elif v[:1]=='b':
            if v[1]=='l':
                pos[v]=(0.9+abs(b.word[int(v[2:])-1])/2, height-int(v[2:])-3)
            elif v[1]=='r':
                pos[v]=(1.1+abs(b.word[int(v[2:])-1])/2, height-int(v[2:])-3)
            else:
                pos[v]=(1+abs(b.word[int(v[1:])-1])/2, height-int(v[1:])-3)

    graph = nx.MultiDiGraph()
    for v in vertices:
        graph.add_node(v)
    for e in edges:
        graph.add_edge(*e)

    nx.draw_networkx(graph, pos=pos, labels={v: v for v in vertices})
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels={e:i+1 for i,e in enumerate(edges)})
    plt.show()


b = Braid(2, (1,2))
c = b.cube_of_resolutions()

# commented out because Sam hates the feather
# for r in c:
#     print("{0:b}".format(r))
#     view(c[r], b)

m = np.array([[0,1,3],[0,0,0],[0,2,0]])
fcc = FCC(m)
fcc.reduce()
print(fcc.m)


g = c[0b00]
x = C2Minus(g)
