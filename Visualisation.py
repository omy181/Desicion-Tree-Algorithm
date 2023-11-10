import pydot
import graphviz.graphs
import graphviz

# General Tree Visualisation as PNG

NodeIndex = 0

def CreateNode(graph,Label,Shape='oval'):
    global NodeIndex 
    NodeIndex += 1

    node = pydot.Node(shape=Shape,label = Label,name=NodeIndex)
    graph.add_node(node)
    return node

def CreateEdge(graph,Label,parent_node,child_node):
    edge = pydot.Edge(src=parent_node,dst=child_node,label=Label)
    graph.add_edge(edge)
    return edge

def visit(graph,tree, parent=None):
    k = list(tree.keys())[0]
    v = list(tree.values())[0]
    
    if parent == None:
       parent = CreateNode(graph,k)   
    
    if isinstance(v[0], dict):       
        node = CreateNode(graph,list(v[0].keys())[0])
        CreateEdge(graph,"Yes",parent,node)
        visit(graph,v[0], node)              
    else:
        node = CreateNode(graph,v[0],"rectangle")
        CreateEdge(graph,"Yes",parent,node)


    if isinstance(v[1], dict):
        node = CreateNode(graph,list(v[1].keys())[0])
        CreateEdge(graph,"No",parent,node)
        visit(graph,v[1], node)                 
    else:
        node = CreateNode(graph,v[1],"rectangle")
        CreateEdge(graph,"No",parent,node)


def VisualiseTree(tree):
    graph = pydot.Dot(graph_type='digraph',strict=True)
    visit(graph,tree)
    graph.write_png('DesicionTree.png')