def statement(customer, movies):
  totalAmount = 0
  frequentRenterPoints = 0
  result = 'Rental Record for %s\n' % customer.name
  for r in customer.rentals:
    movie = movies[r.movieID]
    thisAmount = 0
    if movie.code == 'regular':
      thisAmount = 2
      if r.days > 2:
        thisAmount += (r.days - 2) * 1.5
    elif movie.code == 'new':
      thisAmount = r.days * 3
    elif movie.code == 'childrens':
      thisAmount = 1.5
      if r.days > 3:
        thisAmount += (r.days - 3) * 1.5

    frequentRenterPoints += 1
    if movie.code == 'new' and r.days > 2:
      frequentRenterPoints += 1

    result += '\t%s\t$%s\n' % (movie.title, thisAmount)
    totalAmount += thisAmount

  result += 'mount owed is %s' % totalAmount
  result += 'You earned %s frequent renter points\n' % frequentRenterPoints
  return result
