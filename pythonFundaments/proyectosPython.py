is_day = False
lights_on = not is_day
  
print("Daytime?")
print(is_day)

print("Lights on?")
print(lights_on)

#####################

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock:")
print(in_stock)

######################

id_1 = "#4"
average_grade_1 = "A"
test_score_1= 90

id_2 = "#5"
average_grade_2 = "A"
test_score_2 = 70

no_duplicates = id_1 != id_2
print("No duplicate entries:")
print(no_duplicates)

same_average = average_grade_1 == average_grade_2
print("Same average grade:")
print(same_average)

higher_score = test_score_1 > test_score_2
print("id_1 has a higher score: ")
print(higher_score)

##########################

stock = 74
item = "webcams"
orders = 18

print(f"{stock} {item} in stock")

print(f"{orders} customer orders")

print(f"{stock - orders} available")

##############################

account = 100
interest_rate = 0.004
years = 3

print(f"Initial amount: {account}")

counter = 1
while counter <= years:
  accrued_interest = account * interest_rate
  account += accrued_interest
  print(f"year {counter}: {account}")
  counter += 1

###############################

flavors = ["cinnamon", "pumpkin", "apple pie"]
print("New flavors:")
print(flavors)

ratings = [4, 2.5, 3]
print("Consumer ratings:")
print(ratings)

passed = [True, False, True]
print("Release:")
print(passed)
