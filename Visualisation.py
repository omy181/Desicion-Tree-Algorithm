import pydot
import graphviz.graphs
import graphviz


graph = pydot.Dot(graph_type='graph')

graphviz.Digraph(strict = True)

def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

 
def visit(node, parent=None):
    k = list(node.keys())[0]
    v = list(node.values())[0]
    
    if parent:
        draw(parent, k)

    if isinstance(v[0], dict):
        visit(v[0], k)              
    else:
        draw(k, k+" --> "+v[0])


    if isinstance(v[1], dict):
        visit(v[1], k)              
    else:
        draw(k, k+" --> "+v[1])


def VisualiseTree(tree):
    visit(tree)
    graph.write_png('DesicionTree.png')