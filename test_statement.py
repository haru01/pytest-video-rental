from statement import statement

class _Obj(dict):
  __getattr__ = dict.get

def test_regular_case():
  customer = _Obj({
    'name': 'martin',
    'rentals': [
      _Obj({'movieID': 'F001', 'days': 3}),
      _Obj({'movieID': 'F002', 'days': 1}),
    ]
  })
  movies = _Obj({
    'F001': _Obj({'title': 'Ran',                     'code': 'regular'}),
    'F002': _Obj({'title': 'Trois Couleurs: Bleu',     'code': 'regular'}),
  })

  assert statement(customer, movies) == \
    'Rental Record for martin\n' + \
    '\tRan\t$3.5\n' + \
    '\tTrois Couleurs: Bleu\t$2\n' + \
    'mount owed is 5.5You earned 2 frequent renter points\n'

def test_new_case():
  customer = _Obj({
    'name': 'martin',
    'rentals': [
      _Obj({'movieID': 'F001', 'days': 3}),
      _Obj({'movieID': 'F002', 'days': 2}),
    ]
  })
  movies = _Obj({
    'F001': _Obj({'title': 'Ran',                     'code': 'new'}),
    'F002': _Obj({'title': 'Trois Couleurs: Bleu',     'code': 'new'}),
  })

  assert statement(customer, movies) ==  \
    'Rental Record for martin\n' + \
    '\tRan\t$9\n' + \
    '\tTrois Couleurs: Bleu\t$6\n' + \
    'mount owed is 15You earned 3 frequent renter points\n'

def test_childrens_case():
  customer = _Obj({
    'name': 'martin',
    'rentals': [
      _Obj({'movieID': 'F001', 'days': 3}),
      _Obj({'movieID': 'F002', 'days': 4}),
    ]
  })
  movies = _Obj({
    'F001': _Obj({'title': 'Ran',                     'code': 'childrens'}),
    'F002': _Obj({'title': 'Trois Couleurs: Bleu',     'code': 'childrens'}),
  })

  assert statement(customer, movies) ==  \
    'Rental Record for martin\n' + \
    '\tRan\t$1.5\n' + \
    '\tTrois Couleurs: Bleu\t$3.0\n' + \
    'mount owed is 4.5You earned 2 frequent renter points\n'