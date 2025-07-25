numbers = [1, 2, 3, 4, 5]
places = ["Paris", "London", "New York"]
age_comb =[[numbers, places] for number in numbers for place in places]
print(age_comb)

