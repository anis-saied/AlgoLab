from graphviz import Digraph

# Créer un objet Digraph
graph = Digraph('Python_Standard_Library', format='png')

# Configuration des options de style
graph.attr(rankdir='LR')  # Direction de gauche à droite
graph.attr('node', shape='box')  # Forme des nœuds
graph.attr('node', style='filled', color='lightgray')  # Style de remplissage des nœuds

# Niveau 0 : La bibliothèque standard Python
graph.node('Python_Standard_Library', label='La bibliothèque standard Python', color='orange')

# Niveau 1 : Fonctions_Intégrées
graph.node('Fonctions_Intégrées', label='Fonctions_Intégrées', color='lightblue')  # Couleur différente pour le niveau 1
graph.edge('Python_Standard_Library', 'Fonctions_Intégrées')

# Liste des fonctions intégrées avec leurs rôles et exemples
builtin_functions = [
    {'name': 'abs()', 'role': 'Retourne la valeur absolue d\'un nombre.', 'example': 'abs(-5) => 5'},
    {'name': 'aiter()', 'role': 'Crée un itérateur asynchrone pour un itérable.', 'example': 'aiter(my_list)'},
    {'name': 'all()', 'role': 'Retourne True si tous les éléments d\'un itérable sont vrais, sinon False.', 'example': 'all([True, True, False]) => False'},
    {'name': 'anext()', 'role': 'Récupère le prochain élément d\'un itérable asynchrone.', 'example': 'anext(my_async_iterator)'},
    {'name': 'any()', 'role': 'Retourne True si au moins un élément d\'un itérable est vrai, sinon False.', 'example': 'any([False, False, True]) => True'},
    {'name': 'ascii()', 'role': 'Renvoie une représentation ASCII de l\'objet.', 'example': 'ascii(\'é\') => \'\\xe9\''},
    {'name': 'bin()', 'role': 'Convertit un entier en chaîne binaire préfixée par "0b".', 'example': 'bin(10) => \'0b1010\''},
    {'name': 'bool()', 'role': 'Convertit une valeur en booléen (True ou False).', 'example': 'bool(0) => False'},
    {'name': 'breakpoint()', 'role': 'Interrompt l\'exécution et ouvre un débogueur (disponible à partir de Python 3.7).', 'example': 'breakpoint()'},
    {'name': 'bytearray()', 'role': 'Crée un tableau de bytes modifiable.', 'example': 'bytearray(b\'hello\')'},
    {'name': 'bytes()', 'role': 'Convertit une séquence de nombres en un objet bytes.', 'example': 'bytes([65, 66, 67]) => b\'ABC\''},
    {'name': 'callable()', 'role': 'Renvoie True si l\'objet peut être appelé comme une fonction, sinon False.', 'example': 'callable(my_function) => True'},
    {'name': 'chr()', 'role': 'Convertit un entier en un caractère Unicode.', 'example': 'chr(65) => \'A\''},
    {'name': 'classmethod()', 'role': 'Convertit une méthode en méthode de classe.', 'example': 'classmethod(my_method)'},
    {'name': 'compile()', 'role': 'Compile du code source Python en un objet code ou AST.', 'example': 'compile(\'print("Hello")\', \'\', \'exec\')'},
    {'name': 'complex()', 'role': 'Crée un nombre complexe à partir de parties réelles et imaginaires.', 'example': 'complex(3, 4) => 3+4j'},
    {'name': 'delattr()', 'role': 'Supprime un attribut d\'un objet.', 'example': 'delattr(my_object, \'attr_name\')'},
    {'name': 'dict()', 'role': 'Crée un nouveau dictionnaire (table de hachage).', 'example': 'dict(a=1, b=2) => {\'a\': 1, \'b\': 2}'},
    {'name': 'dir()', 'role': 'Renvoie la liste des noms dans l\'espace de noms local ou de l\'objet.', 'example': 'dir()'},
    {'name': 'divmod()', 'role': 'Effectue une division et renvoie le quotient et le reste.', 'example': 'divmod(10, 3) => (3, 1)'},
    {'name': 'enumerate()', 'role': 'Renvoie un itérable d\'indices et d\'éléments.', 'example': 'enumerate([\'a\', \'b\', \'c\'])'},
    {'name': 'eval()', 'role': 'Évalue une expression Python depuis une chaîne.', 'example': 'eval(\'2 + 2\') => 4'},
    {'name': 'exec()', 'role': 'Exécute du code Python à partir d\'une chaîne ou d\'un objet code.', 'example': 'exec(\'print("Hello")\')'},
    {'name': 'filter()', 'role': 'Filtre les éléments d\'un itérable avec une fonction de filtrage.', 'example': 'filter(None, [0, 1, 2]) => [1, 2]'},
    {'name': 'float()', 'role': 'Convertit un nombre ou une chaîne en un nombre à virgule flottante.', 'example': 'float(3.14) => 3.14'},
    {'name': 'format()', 'role': 'Formate une valeur en une chaîne en utilisant des spécificateurs de format.', 'example': 'format(3.14159, ".2f") => \'3.14\''},
    {'name': 'frozenset()', 'role': 'Crée un ensemble non modifiable.', 'example': 'frozenset([1, 2, 3])'},
    {'name': 'getattr()', 'role': 'Renvoie la valeur d\'un attribut d\'un objet.', 'example': 'getattr(my_object, \'attr_name\')'},
    {'name': 'globals()', 'role': 'Renvoie un dictionnaire représentant l\'espace de noms global actuel.', 'example': 'globals()'},
    {'name': 'hasattr()', 'role': 'Renvoie True si un objet a un attribut donné, sinon False.', 'example': 'hasattr(my_object, \'attr_name\')'},
    {'name': 'hash()', 'role': 'Calcule la valeur de hachage (hash) d\'un objet.', 'example': 'hash(\'hello\')'},
    {'name': 'help()', 'role': 'Affiche l\'aide interactive pour un objet.', 'example': 'help(list)'},
    {'name': 'hex()', 'role': 'Convertit un entier en une chaîne hexadécimale préfixée par "0x".', 'example': 'hex(255) => \'0xff\''},
    {'name': 'id()', 'role': 'Renvoie l\'identifiant unique d\'un objet.', 'example': 'id(my_object)'},
    {'name': 'input()', 'role': 'Lit une ligne depuis l\'entrée standard (généralement le clavier).', 'example': 'input(\'Entrez quelque chose : \')'},
    {'name': 'int()', 'role': 'Convertit un nombre ou une chaîne en un entier.', 'example': 'int(\'42\') => 42'},
    {'name': 'isinstance()', 'role': 'Renvoie True si un objet est une instance d\'une classe donnée, sinon False.', 'example': 'isinstance(my_object, int) => True'},
    {'name': 'issubclass()', 'role': 'Renvoie True si une classe est une sous-classe d\'une classe donnée, sinon False.', 'example': 'issubclass(MyClass, ParentClass)'},
    {'name': 'iter()', 'role': 'Renvoie un itérable à partir d\'un objet itérable.', 'example': 'iter([1, 2, 3])'},
    {'name': 'len()', 'role': 'Renvoie la longueur (nombre d\'éléments) d\'un objet.', 'example': 'len([1, 2, 3]) => 3'},
    {'name': 'list()', 'role': 'Crée une nouvelle liste.', 'example': 'list([1, 2, 3]) => [1, 2, 3]'},
    {'name': 'locals()', 'role': 'Renvoie un dictionnaire représentant l\'espace de noms local actuel.', 'example': 'locals()'},
    {'name': 'map()', 'role': 'Applique une fonction à tous les éléments d\'un itérable.', 'example': 'map(square, [1, 2, 3])'},
    {'name': 'max()', 'role': 'Renvoie le plus grand élément d\'un itérable.', 'example': 'max([1, 2, 3]) => 3'},
    {'name': 'memoryview()', 'role': 'Crée un objet "memory view" de la mémoire d\'un objet.', 'example': 'memoryview(my_array)'},
    {'name': 'min()', 'role': 'Renvoie le plus petit élément d\'un itérable.', 'example': 'min([1, 2, 3]) => 1'},
    {'name': 'next()', 'role': 'Renvoie le prochain élément d\'un itérable.', 'example': 'next(my_iterator)'},
    {'name': 'object()', 'role': 'Crée une nouvelle instance de la classe "object".', 'example': 'object()'},
    {'name': 'oct()', 'role': 'Convertit un entier en une chaîne octale préfixée par "0o".', 'example': 'oct(8) => \'0o10\''},
    {'name': 'open()', 'role': 'Ouvre un fichier pour lecture ou écriture.', 'example': 'with open(\'file.txt\', \'r\') as file:'},
    {'name': 'ord()', 'role': 'Renvoie la valeur entière Unicode d\'un caractère.', 'example': 'ord(\'A\') => 65'},
    {'name': 'pow()', 'role': 'Calcule la puissance d\'un nombre.', 'example': 'pow(2, 3) => 8'},
    {'name': 'print()', 'role': 'Affiche des valeurs à l\'écran (dans la sortie standard).', 'example': 'print(\'Hello, world!\')'},
    {'name': 'property()', 'role': 'Convertit une méthode en une propriété.', 'example': 'property(my_method)'},
    {'name': 'range()', 'role': 'Renvoie une séquence d\'entiers.', 'example': 'range(5) => [0, 1, 2, 3, 4]'},
    {'name': 'repr()', 'role': 'Renvoie une représentation sous forme de chaîne d\'un objet.', 'example': 'repr(\'hello\') => \'\'hello\'\''},
    {'name': 'reversed()', 'role': 'Renvoie un itérable de la séquence en sens inverse.', 'example': 'reversed([1, 2, 3])'},
    {'name': 'round()', 'role': 'Arrondit un nombre à un nombre donné de décimales.', 'example': 'round(3.14159, 2) => 3.14'},
    {'name': 'set()', 'role': 'Crée un nouvel ensemble.', 'example': 'set([1, 2, 3])'},
    {'name': 'setattr()', 'role': 'Attribue une valeur à un attribut d\'un objet.', 'example': 'setattr(my_object, \'attr_name\', value)'},
    {'name': 'slice()', 'role': 'Crée un objet "slice" pour accéder à une partie d\'une séquence.', 'example': 'slice(1, 3)'},
    {'name': 'sorted()', 'role': 'Renvoie une liste triée d\'éléments d\'un itérable.', 'example': 'sorted([3, 1, 2]) => [1, 2, 3]'},
    {'name': 'staticmethod()', 'role': 'Convertit une méthode en méthode statique.', 'example': 'staticmethod(my_method)'},
    {'name': 'str()', 'role': 'Convertit un objet en chaîne de caractères.', 'example': 'str(42) => \'42\''},
    {'name': 'sum()', 'role': 'Calcule la somme des éléments d\'un itérable.', 'example': 'sum([1, 2, 3]) => 6'},
    {'name': 'super()', 'role': 'Renvoie un objet "super" utilisé pour accéder aux méthodes parentes.', 'example': 'super()'},
    {'name': 'tuple()', 'role': 'Crée un nouveau tuple.', 'example': 'tuple([1, 2, 3]) => (1, 2, 3)'},
    {'name': 'type()', 'role': 'Renvoie le type d\'un objet (classe).', 'example': 'type(3.14) => <class \'float\'>'},
    {'name': 'vars()', 'role': 'Renvoie le dictionnaire __dict__ d\'un module, d\'une classe ou d\'une instance.', 'example': 'vars(my_object)'}
]


# Niveau 2 : Fonctions intégrées
for func in builtin_functions:
    graph.node(func['name'], label=func['name'])
    graph.edge('Fonctions_Intégrées', func['name'])

# Niveau 3 : Rôles et exemples
for func in builtin_functions:
    node_name = func['name']
    role_node_name = f'{node_name}_role'
    graph.node(role_node_name, label=func['role'], color='lightblue', shape='box', style='filled', align='left')
    graph.edge(node_name, role_node_name)
    
    example_node_name = f'{node_name}_example'
    graph.node(example_node_name, label=func['example'], color='lightgreen', shape='box', style='filled', align='left')
    graph.edge(node_name, example_node_name)

# Générer le graphe
graph.render(view=True)


