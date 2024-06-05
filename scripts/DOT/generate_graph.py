from graphviz import Digraph

# Créer un nouvel objet Digraph
dot = Digraph('bibliotheque_standard_python', format='png')

# Définir les options du graphe
dot.attr(rankdir='LR')
dot.node('os', 'os')
dot.node('sys', 'sys')
dot.node('math', 'math')
dot.node('json', 'json')
dot.node('re', 're')
dot.node('datetime', 'datetime')

# Ajouter les relations entre les modules
dot.edge('os', 'sys')
dot.edge('os', 'json')
dot.edge('sys', 'math')
dot.edge('json', 're')
dot.edge('math', 'datetime')

# Générer le graphe au format PNG
# L'option view=True permettra d'ouvrir le fichier PNG généré automatiquement.
dot.render('bibliotheque_standard_python', view=True)

