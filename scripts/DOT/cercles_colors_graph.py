from graphviz import Graph

dot = Graph('Transparency', format='png')
dot.attr(layout='neato')
dot.attr(start='11')
dot.attr(bgcolor='#0000ff11')
dot.node_attr.update(shape='circle', width='2.22', label='', style='filled')
dot.node('5', color='#0000ff80', label='module5')
dot.node('6', color='#ee00ee80', label='module6')
dot.node('1', color='#ff000080', label='module1')
dot.node('2', color='#eeee0080', label='module2')
dot.node('3', color='#00ff0080', label='module3')
dot.node('4', color='#00eeee80', label='module4')

dot.edge('1', '2')
dot.edge('2', '3')
dot.edge('3', '4')
dot.edge('4', '5')
dot.edge('5', '6')
dot.edge('6', '1')

dot.render('Transparency', view=True)

