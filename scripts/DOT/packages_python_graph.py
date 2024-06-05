from graphviz import Digraph

# Créer un nouvel objet Digraph
dot = Digraph('PythonStandardLibrary', format='png')
dot.attr(rankdir='LR')  # Orientation du graphe
dot.attr(fontname='Arial')

# Ajouter le noeud principal "The Python Standard Library"
dot.node('root', 'The Python Standard Library', shape='box', style='filled', fillcolor='lightblue')

# Liste des niveaux 1 et leurs descendants
niveaux = {
    'Fonctions intégrées': [
        'Constantes intégrées',
        'Types intégrés',
        'Exceptions intégrées',
        'Services de traitement de texte',
        'Services de données binaires',
        'Types de données',
        'Modules numériques et mathématiques',
        'Modules de programmation fonctionnelle',
        'Accès aux fichiers et aux répertoires',
        'Persistance des données',
        'Compression et archivage des données',
        'Formats de fichiers',
        'Services cryptographiques',
        'Services de système d\'exploitation génériques',
        'Exécution simultanée',
        'Mise en réseau et communication interprocessus',
        'Traitement des données Internet',
        'Outils de traitement de balisage structuré',
        'Protocoles Internet et assistance',
        'Services multimédias',
        'Internationalisation',
        'Cadres de programme',
        'Interfaces utilisateur graphiques avec Tk',
        'Outils de développement',
        'Débogage et profilage',
        'Emballage et distribution de logiciels',
        'Services d\'exécution Python',
        'Interpréteurs Python personnalisés',
        'Importer des modules',
        'Services de langage Python',
        'Services spécifiques à MS Windows',
        'Services spécifiques à Unix',
        'Modules remplacés',
        'Considérations de sécurité'
    ],
    'Fonctions intégrées': [
        'abs()',
        'aiter()',
        'all()',
        'anext()',
        'any()',
        'ascii()',
        'bin()',
        'bool()',
        'breakpoint()',
        'bytearray()',
        'bytes()',
        'callable()',
        'chr()',
        'classmethod()',
        'compile()',
        'complex()',
        'delattr()',
        'dict()',
        'dir()',
        'divmod()',
        'enumerate()',
        'eval()',
        'exec()',
        'filter()',
        'float()',
        'format()',
        'frozenset()',
        'getattr()',
        'globals()',
        'hasattr()',
        'hash()',
        'help()',
        'hex()',
        'id()',
        'input()',
        'int()',
        'isinstance()',
        'issubclass()',
        'iter()',
        'len()',
        'list()',
        'locals()',
        'map()',
        'max()',
        'memoryview()',
        'min()',
        'next()',
        'object()',
        'oct()',
        'open()',
        'ord()',
        'pow()',
        'print()',
        'property()',
        'range()',
        'repr()',
        'reversed()',
        'round()',
        'set()',
        'setattr()',
        'slice()',
        'sorted()',
        'staticmethod()',
        'str()',
        'sum()',
        'super()',
        'tuple()',
        'type()',
        'vars()',
        'zip()',
        '__import__()'
    ],
    'Constantes intégrées': [
        'Constantes ajoutées par le sitemodule'
    ],
    'Types intégrés': [
        'Test de valeur de vérité',
        'Opérations booléennes — and, or, not',
        'Comparaisons',
        'Types numériques — int, float, complex',
        'Types d\'itérateurs',
        'Types de séquence — list, tuple, range',
        'Type de séquence de texte — str',
        'Types de séquence binaire — bytes, bytearray, memoryview',
        'Types d\'ensembles — set, frozenset',
        'Types de mappage — dict',
        'Types de gestionnaires de contexte',
        'Types d\'annotations de type – Alias générique, Union',
        'Autres types intégrés',
        'Attributs spéciaux',
        'Limitation de la longueur de conversion de chaîne entière'
    ],
    'Exceptions intégrées': [
        'Contexte des exceptions',
        'Héritage des exceptions intégrées',
        'Cours de base',
        'Exceptions concrètes',
        'Avertissements',
        'Groupes d\'exceptions',
        'Hiérarchie des exceptions'
    ],
    'Services de traitement de texte': [
        'string — Opérations courantes sur les chaînes',
        're — Opérations d\'expression régulière',
        'difflib — Aides pour le calcul des deltas',
        'textwrap — Habillage et remplissage du texte',
        'unicodedata — Base de données Unicode',
        'stringprep — Préparation des chaînes Internet',
        'readline — Interface de lecture GNU',
        'rlcompleter — Fonction de complétion pour GNU readline'
    ],
    'Services de données binaires': [
        'struct — Interpréter les octets comme des données binaires compressées',
        'codecs — Registre des codecs et classes de base'
    ],
    'Types de données': [
        'datetime — Types de date et d\'heure de base',
        'zoneinfo — Prise en charge du fuseau horaire IANA',
        'calendar — Fonctions générales liées au calendrier',
        'collections — Types de données de conteneur',
        'collections.abc — Classes de base abstraites pour les conteneurs',
        'heapq — Algorithme de file d\'attente de tas',
        'bisect — Algorithme de bissection de tableau',
        'array — Tableaux efficaces de valeurs numériques',
        'weakref — Faibles références',
        'types — Création de types dynamiques et noms pour les types intégrés',
        'copy — Opérations de copie superficielle et profonde',
        'pprint — Jolie imprimante de données',
        'reprlib — repr() Mise en œuvre alternative',
        'enum — Prise en charge des énumérations',
        'graphlib — Fonctionnalité permettant de fonctionner avec des structures de type graphique'
    ],
    'Modules numériques et mathématiques': [
        'numbers — Classes de base abstraites numériques',
        'math — Fonctions mathématiques',
        'cmath — Fonctions mathématiques pour les nombres complexes',
        'decimal — Arithmétique décimale à virgule fixe et à virgule flottante',
        'fractions — Nombres rationnels',
        'random — Générer des nombres pseudo-aléatoires',
        'statistics — Fonctions statistiques mathématiques'
    ],
    'Modules de programmation fonctionnelle': [
        'itertools — Fonctions créant des itérateurs pour un bouclage efficace',
        'functools — Fonctions et opérations d\'ordre supérieur sur des objets appelables',
        'operator — Opérateurs standards comme fonctions'
    ],
    'Accès aux fichiers et aux répertoires': [
        'pathlib — Chemins de système de fichiers orientés objet',
        'os.path — Manipulations courantes des noms de chemin',
        'fileinput — Itérer sur les lignes de plusieurs flux d\'entrée',
        'stat — Interprétation stat() des résultats',
        'filecmp — Comparaisons de fichiers et de répertoires',
        'tempfile — Générer des fichiers et répertoires temporaires',
        'glob — Extension du modèle de chemin d\'accès de style Unix',
        'fnmatch — Correspondance de modèle de nom de fichier Unix',
        'linecache — Accès aléatoire aux lignes de texte',
        'shutil — Opérations de fichiers de haut niveau'
    ],
    'Persistance des données': [
        'pickle — Sérialisation d\'objet Python',
        'copyreg — Enregistrer les fonctions de support pickle',
        'shelve — Persistance d\'objet Python',
        'marshal — Sérialisation interne des objets Python',
        'dbm — Interfaces avec les « bases de données » Unix',
        'sqlite3 — Interface DB-API 2.0 pour les bases de données SQLite'
    ],
    'Compression et archivage des données': [
        'zlib — Compression compatible avec gzip',
        'gzip — Prise en charge des fichiers gzip',
        'bz2 — Prise en charge de la compression bzip2',
        'lzma — Compression utilisant l\'algorithme LZMA',
        'zipfile — Travailler avec des archives ZIP',
        'tarfile — Lire et écrire des fichiers d\'archive tar'
    ],
       'Formats de fichiers': [
        'csv — Lecture et écriture de fichiers CSV',
        'configparser — Analyseur de fichiers de configuration',
        'tomllib — Analyser les fichiers TOML',
        'netrc — Traitement de fichiers netrc',
        'plistlib — Générer et analyser les fichiers .plist Apple'
    ],
    'Services cryptographiques': [
        'hashlib — Sécuriser les hachages et les résumés de messages',
        'hmac — Hachage à clé pour l\'authentification des messages',
        'secrets — Générez des nombres aléatoires sécurisés pour gérer les secrets'
    ],
    'Services de système d\'exploitation génériques': [
        'os — Diverses interfaces du système d\'exploitation',
        'io — Outils de base pour travailler avec les flux',
        'time — Accès au temps et conversions',
        'argparse — Analyseur pour les options de ligne de commande, les arguments et les sous-commandes',
        'getopt — Analyseur de style C pour les options de ligne de commande',
        'logging — Facilité de journalisation pour Python',
        'logging.config — Configuration de la journalisation',
        'logging.handlers — Gestionnaires de journalisation',
        'getpass — Saisie de mot de passe portable',
        'curses — Gestion du terminal pour les affichages de cellules de caractères',
        'curses.textpad — Widget de saisie de texte pour les programmes de malédictions',
        'curses.ascii — Utilitaires pour les caractères ASCII',
        'curses.panel — Une extension de pile de panneaux pour les malédictions',
        'platform — Accès aux données d\'identification de la plateforme sous-jacente',
        'errno — Symboles standard du système errno',
        'ctypes — Une bibliothèque de fonctions étrangères pour Python'
    ],
    'Exécution simultanée': [
        'threading — Parallélisme basé sur les threads',
        'multiprocessing — Parallélisme basé sur les processus',
        'multiprocessing.shared_memory — Mémoire partagée pour un accès direct entre les processus',
        'concurrent.futures — Lancement de tâches parallèles',
        'subprocess — Gestion des sous-processus',
        'sched — Planificateur d\'événements',
        'queue — Une classe de file d\'attente synchronisée',
        'contextvars — Variables de contexte',
        '_thread — API de threading de bas niveau'
    ],
    'Mise en réseau et communication interprocessus': [
        'asyncio — E/S asynchrones',
        'socket — Interface réseau de bas niveau',
        'ssl — Wrapper TLS/SSL pour les objets socket',
        'select — En attente de l\'achèvement des E/S',
        'selectors — Multiplexage d\'E/S de haut niveau',
        'signal — Définir des gestionnaires pour les événements asynchrones',
        'mmap — Prise en charge des fichiers mappés en mémoire'
    ],
    'Traitement des données Internet': [
        'email — Un package de gestion des e-mails et MIME',
        'json — Encodeur et décodeur JSON',
        'mailbox — Manipuler des boîtes aux lettres dans différents formats',
        'mimetypes — Mapper les noms de fichiers aux types MIME',
        'base64 — Encodages de données Base16, Base32, Base64, Base85',
        'binascii — Convertir entre binaire et ASCII',
        'quopri — Encoder et décoder les données imprimables entre guillemets MIME'
    ],
    'Outils de traitement de balisage structuré': [
        'html — Prise en charge du langage de balisage hypertexte',
        'html.parser — Analyseur HTML et XHTML simple',
        'html.entities — Définitions des entités générales HTML',
        'Modules de traitement XML',
        'xml.etree.ElementTree — L\'API XML ElementTree',
        'xml.dom — L\'API du modèle d\'objet de document',
        'xml.dom.minidom — Implémentation minimale du DOM',
        'xml.dom.pulldom — Prise en charge de la construction d\'arborescences DOM partielles',
        'xml.sax — Prise en charge des analyseurs SAX2',
        'xml.sax.handler — Classes de base pour les gestionnaires SAX',
        'xml.sax.saxutils — Utilitaires SAX',
        'xml.sax.xmlreader — Interface pour les analyseurs XML',
        'xml.parsers.expat — Analyse XML rapide à l\'aide d\'Expat'
    ],
    'Protocoles Internet et assistance': [
        'webbrowser — Contrôleur de navigateur Web pratique',
        'wsgiref — Utilitaires WSGI et implémentation de référence',
        'urllib — Modules de gestion d\'URL',
        'urllib.request — Bibliothèque extensible pour ouvrir des URL',
        'urllib.response — Classes de réponse utilisées par urllib',
        'urllib.parse — Analyser les URL en composants',
        'urllib.error — Classes d\'exception levées par urllib.request',
        'urllib.robotparser — Analyseur pour robots.txt',
        'http — Modules HTTP',
        'http.client — Client de protocole HTTP',
        'ftplib — Client de protocole FTP',
        'poplib — Client de protocole POP3',
        'imaplib — Client de protocole IMAP4',
        'smtplib — Client de protocole SMTP',
        'uuid — Objets UUID selon RFC 4122',
        'socketserver — Un cadre pour les serveurs de réseau',
        'http.server — Serveurs HTTP',
        'http.cookies — Gestion de l\'état HTTP',
        'http.cookiejar — Gestion des cookies pour les clients HTTP',
        'xmlrpc — Modules serveur et client XMLRPC',
        'xmlrpc.client — Accès client XML-RPC',
        'xmlrpc.server — Serveurs XML-RPC de base',
        'ipaddress — Bibliothèque de manipulation IPv4/IPv6'
    ],
    'Services multimédias': [
        'wave — Lire et écrire des fichiers WAV',
        'colorsys — Conversions entre systèmes de couleurs'
    ],
    'Internationalisation': [
        'gettext — Services d\'internationalisation multilingue',
        'locale — Services d\'internationalisation'
    ],
     'Cadres de programme': [
        'turtle — Graphiques de tortue',
        'cmd — Prise en charge des interpréteurs de commandes orientés ligne',
        'shlex — Analyse lexicale simple'
    ],
    'Interfaces utilisateur graphiques avec Tk': [
        'tkinter — Interface Python vers Tcl/Tk',
        'tkinter.colorchooser — Boîte de dialogue de choix de couleur',
        'tkinter.font — Wrapper de police Tkinter',
        'Boîtes de dialogue Tkinter',
        'tkinter.messagebox — Invites de message Tkinter',
        'tkinter.scrolledtext — Widget de texte défilé',
        'tkinter.dnd — Prise en charge du glisser-déposer',
        'tkinter.ttk — Widgets sur le thème Tk',
        'tkinter.tix — Widgets d\'extension pour Tk',
        'INACTIF'
    ],
    'Outils de développement': [
        'typing — Prise en charge des indications de type',
        'pydoc — Générateur de documentation et système d\'aide en ligne',
        'Mode de développement Python',
        'doctest — Tester des exemples Python interactifs',
        'unittest — Cadre de test unitaire',
        'unittest.mock — bibliothèque d\'objets fictifs',
        'unittest.mock — commencer',
        '2to3 — Traduction automatisée de code Python 2 à 3',
        'test — Package de tests de régression pour Python',
        'test.support — Utilitaires pour la suite de tests Python',
        'test.support.socket_helper — Utilitaires pour les tests de socket',
        'test.support.script_helper — Utilitaires pour les tests d\'exécution Python',
        'test.support.bytecode_helper — Outils de support pour tester la génération correcte de bytecode',
        'test.support.threading_helper — Utilitaires pour les tests de threading',
        'test.support.os_helper — Utilitaires pour les tests du système d\'exploitation',
        'test.support.import_helper — Utilitaires pour les tests d\'importation',
        'test.support.warnings_helper — Utilitaires pour les tests d\'avertissements'
    ],
    'Débogage et profilage': [
        'Tableau des événements d\'audit',
        'bdb — Cadre de débogage',
        'faulthandler — Vider le traçage Python',
        'pdb — Le débogueur Python',
        'Les profileurs Python',
        'timeit — Mesurer le temps d\'exécution de petits extraits de code',
        'trace — Tracer ou suivre l\'exécution des instructions Python',
        'tracemalloc — Tracer les allocations de mémoire'
    ],
        'Emballage et distribution de logiciels': [
        'distutils — Construire et installer des modules Python',
        'ensurepip — Amorçage de l\'installateur pip',
        'venv — Création d\'environnements virtuels',
        'zipapp — Gérer les archives zip Python exécutables'
    ],
    'Services d\'exécution Python': [
        'sys — Paramètres et fonctions spécifiques au système',
        'sysconfig — Fournir un accès aux informations de configuration de Python',
        'builtins — Objets intégrés',
        '__main__ — Environnement de code de niveau supérieur',
        'warnings — Contrôle d\'avertissement',
        'dataclasses — Catégories de données',
        'contextlib — Utilitaires pour le bloc with - statement',
        'abc — Classes de base abstraites',
        'atexit — Gestionnaires de sortie',
        'traceback — Imprimer ou récupérer un traçage de pile',
        '__future__ — Définitions des énoncés futurs',
        'gc — Interface du collecteur de déchets',
        'inspect — Inspecter les objets vivants',
        'site — Hook de configuration spécifique au site'
    ],
    'Interpréteurs Python personnalisés': [
        'code — Cours de base pour interprètes',
        'codeop — Compiler le code Python'
    ],
    'Importer des modules': [
        'zipimport — Importer des modules à partir d\'archives Zip',
        'pkgutil — Utilitaire d\'extension de paquet',
        'modulefinder — Rechercher les modules utilisés par un script',
        'runpy — Localisation et exécution de modules Python',
        'importlib — L\'implémentation de l\'import',
        'importlib.resources — Lecture, ouverture et accès aux ressources du package',
        'importlib.resources.abc — Classes de base abstraites pour les ressources',
        'importlib.metadata — Accéder aux métadonnées du package',
        'L\'initialisation du sys.path chemin de recherche du module'
    ],
    'Services de langage Python': [
        'ast — Arbres de syntaxe abstraite',
        'symtable — Accès aux tables de symboles du compilateur',
        'token — Constantes utilisées avec les arbres d\'analyse Python',
        'keyword — Test des mots-clés Python',
        'tokenize — Générateur de jetons pour la source Python',
        'tabnanny — Détection d\'indentation ambiguë',
        'pyclbr — Prise en charge du navigateur de modules Python',
        'py_compile — Compiler les fichiers sources Python',
        'compileall — Bibliothèques Python compilées par octets',
        'dis — Désassembleur pour le bytecode Python',
        'pickletools — Outils pour les développeurs de pickle'
    ],
    'Services spécifiques à MS Windows': [
        'msvcrt — Routines utiles du runtime MS VC++',
        'winreg — Accès au registre Windows',
        'winsound — Interface de lecture audio pour Windows'
    ],
    'Services spécifiques à Unix': [
        'posix — Les appels système POSIX les plus courants',
        'pwd — La base de données de mots de passe',
        'grp — La base de données du groupe',
        'termios — Contrôle tty de style POSIX',
        'tty — Fonctions de contrôle des terminaux',
        'pty — Utilitaires pseudo-terminaux',
        'fcntl — Les appels système fcntl et ioctl',
        'resource — Informations sur l\'utilisation des ressources',
        'syslog — Routines de la bibliothèque syslog Unix'
    ],
    'Modules remplacés': [
        'aifc — Lire et écrire des fichiers AIFF et AIFC',
        'asynchat — Gestionnaire de commande/réponse de socket asynchrone',
        'asyncore — Gestionnaire de sockets asynchrones',
        'audioop — Manipuler des données audio brutes',
        'cgi — Prise en charge de l\'interface de passerelle commune',
        'cgitb — Gestionnaire de traçage pour les scripts CGI',
        'chunk — Lire les données fragmentées IFF',
        'crypt — Fonction pour vérifier les mots de passe Unix',
        'imghdr — Déterminer le type d\'une image',
        'imp — Accéder aux composants internes de l\'importation',
        'mailcap — Gestion des fichiers Mailcap',
        'msilib — Lire et écrire des fichiers Microsoft Installer',
        'nis — Interface avec le NIS de Sun (Pages Jaunes)',
        'nntplib — Client de protocole NNTP',
        'optparse — Analyseur pour les options de ligne de commande',
        'ossaudiodev — Accès aux appareils audio compatibles OSS',
        'pipes — Interface avec les pipelines shell',
        'smtpd — Serveur SMTP',
        'sndhdr — Déterminer le type de fichier son',
        'spwd — La base de données des mots de passe fantômes',
        'sunau — Lire et écrire des fichiers Sun AU',
        'telnetlib — Client Telnet',
        'uu — Encoder et décoder les fichiers uuencode',
        'xdrlib — Encoder et décoder les données XDR'
    ],
    'Considérations de sécurité': [
        # This section appears to be incomplete or missing in your provided text.
    ]
}

# Ajouter les niveaux et leurs descendants au graphe
for niveau, descendants in niveaux.items():
    dot.node(niveau, niveau, shape='box', style='filled', fillcolor='lightgreen')
    for descendant in descendants:
        dot.node(descendant, descendant, shape='ellipse')

        # Ajouter les liaisons entre les niveaux et leurs descendants
        dot.edge(niveau, descendant)

# Générer le graphe au format PNG
dot.render('PythonStandardLibrary', view=True)

