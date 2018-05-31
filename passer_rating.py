# Create Calc class
class FavoriteQB:
	best_rating = []

	def __init__(self, fn = "Aaron", ln = "Rodgers"):
		self.first_name = fn
		self.last_name  = ln

	def ratings(self):
		self.best_rating.append(nfl_passer_rating(16, 9, 65, 0, 1))
		self.best_rating.append(nfl_passer_rating(15, 6, 46, 0, 0))
		self.best_rating.append(nfl_passer_rating(28, 20, 218, 1, 0))
		self.best_rating.append(nfl_passer_rating(536, 341, 4038, 28, 13))
		self.best_rating.append(nfl_passer_rating(541, 350, 4434, 30, 7))

			

# This function defines the  NFL QB passer rating calculation
def nfl_passer_rating(att, comp, yds, td, intcp):
  	a = calc_a(att, comp) 
  	b = calc_b(yds, att)
  	c = calc_c(td, att)
  	d = calc_d(intcp, att)
  	temp = (a + b + c + d)/6
  	rating = (temp)*100
  	return rating

# Defines function that checks the min and max values for each compoent of rating

def check_min_max(value, valueMin, valueMax):
	if value < valueMin: 
		return valueMin 
	elif value > valueMax:
		return valueMax
	else: 
		return value 


def calc_a(att, comp):
	temp = comp/att
	a = (temp-0.3)*5 
	return check_min_max(a, 0, 2.375)
	

def calc_b(yds, att):
 	temp = yds/att
 	b = (temp-3)*0.25
 	return check_min_max(b, 0, 2.375)

def calc_c(td, att):
	c = (td/att)*20
	return check_min_max(c, 0, 2.375)

def calc_d(intcp, att):
	temp = (intcp/att)*25
	d = 2.375 - temp
	return check_min_max(d, 0, 2.375)


# nfl_passer_rating(att, comp, yds, td, intcp)

#Rodgers2005 = nfl_passer_rating(16, 9, 65, 0, 1)
#print(Rodgers2005)

Aaron = FavoriteQB()
Aaron.ratings()
print(max(Aaron.best_rating))






