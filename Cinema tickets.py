movie = input()
days = int(input())
tickets = int(input())
price = float(input())
cinema_percent = int(input())
total_tickets = tickets * days * price

cinema = cinema_percent/100 * total_tickets
profit = total_tickets - cinema

print (f'The profit from the movie {movie} is {profit:.2f} lv.')