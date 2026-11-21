"""Assign each České Budějovice question to one thematic quiz."""

SECTIONS = {
    'biology': ('Biologie a somatologie', (
        'Anatomie', 'Biologie', 'Biologie člověka', 'Fyziologie', 'Fyziologie člověka',
        'Buněčná biologie a smysly', 'Genetika', 'Genetika a dělení buněk', 'Evoluce',
        'Buňka', 'Nádorová biologie', 'Metabolismus', 'Pojiva', 'Pohyb', 'Kostry',
        'Kostra', 'Pohybová soustava', 'Páteř', 'Klouby', 'Svaly', 'Kostní tkáň',
        'Růst kostí', 'Hrudník', 'Chrup', 'Kůže', 'Zrak', 'Hormony', 'Vitaminy',
        'Krev a oběh', 'Krevní oběh', 'Krevní skupiny', 'Srdce', 'Nervová soustava',
        'Ledviny a nervová soustava', 'Dýchání a trávení', 'Hrtan',
        'Dýchací soustava', 'Trávení', 'Močová soustava',
    )),
    'physics': ('Fyzika', ('Fyzika',)),
    'chemistry': ('Chemie', ('Chemie',)),
    'math': ('Matematika a logika', ('Matematika', 'Početní úlohy', 'Logika')),
    'computing': ('Informatika', ('Informatika',)),
    'nursing': ('Ošetřovatelství', ('Ošetřovatelství', 'Dějiny zdravotnictví')),
    'physiotherapy': ('Fyzioterapie a motivace', ('Fyzioterapie', 'Fyzioterapie a základy přírodních věd')),
    'social-work': ('Sociální práce a management', ('Sociální práce', 'Management')),
    'social-studies': ('Společenské vědy a všeobecný přehled', (
        'Společenské vědy', 'Všeobecná informovanost', 'Psychologie', 'Sociologie',
        'Filozofie', 'Filozofie a dějiny vědy', 'Etika a filozofie', 'Etika',
        'Ekonomie', 'Právní pojmy', 'Sociologie a komunikace', 'Kultura',
        'Komunikace', 'Občanská orientace', 'Dějiny',
    )),
}

OVERRIDES = {
    159: 'math', 161: 'math', 166: 'math', 175: 'math',
    301: 'biology', 302: 'biology', 303: 'social-studies',
    306: 'physics', 307: 'chemistry', 309: 'biology', 310: 'physics',
    311: 'social-studies', 312: 'biology', 318: 'math', 320: 'chemistry',
    322: 'social-studies', 324: 'math', 325: 'math', 326: 'social-studies',
    352: 'computing', 382: 'computing', 383: 'computing', 384: 'computing',
    415: 'biology', 430: 'social-work', 444: 'computing',
}


def group_questions(questions):
    category_keys = {
        category: key for key, (_, categories) in SECTIONS.items() for category in categories
    }
    groups = {key: {'name': name, 'ids': []} for key, (name, _) in SECTIONS.items()}
    for question in questions:
        key = OVERRIDES.get(question['id']) or category_keys[question['category']]
        groups[key]['ids'].append(question['id'])
    return groups
