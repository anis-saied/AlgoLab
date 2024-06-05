from graphviz import Digraph

dot = Digraph('ER', format='png')
dot.attr(fontname='Helvetica,Arial,sans-serif')
dot.node_attr.update(fontname='Helvetica,Arial,sans-serif')
dot.edge_attr.update(fontname='Helvetica,Arial,sans-serif')
dot.attr(layout='neato')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('course', shape='box')
    s.node('institute', shape='box')
    s.node('student', shape='box')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('name0', shape='ellipse', label='name')
    s.node('name1', shape='ellipse', label='name')
    s.node('name2', shape='ellipse', label='name')
    s.node('code', shape='ellipse')
    s.node('grade', shape='ellipse')
    s.node('number', shape='ellipse')

dot.node('C-I', shape='diamond', style='filled', color='lightgrey')
dot.node('S-C', shape='diamond', style='filled', color='lightgrey')

dot.edge('name0', 'course')
dot.edge('code', 'course')
dot.edge('course', 'C-I', label='n', len='1.00')
dot.edge('C-I', 'institute', label='1', len='1.00')
dot.edge('institute', 'name1')
dot.edge('institute', 'S-I', label='1', len='1.00')
dot.edge('S-I', 'student', label='n', len='1.00')
dot.edge('student', 'grade')
dot.edge('student', 'name2')
dot.edge('student', 'number')
dot.edge('student', 'S-C', label='m', len='1.00')
dot.edge('S-C', 'course', label='n', len='1.00')

dot.attr(label='\n\nEntity Relation Diagram\ndrawn by NEATO')
dot.attr(fontsize='20')

dot.render('ER', view=True)

