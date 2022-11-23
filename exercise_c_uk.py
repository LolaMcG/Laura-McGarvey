united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

united_kingdom[1]["capital"] = "Cardiff"
# print(united_kingdom[1])

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).

nor_ire_dict = {
  "name": "Northern Ireland",
  "population": 1811000,
  "capital": "Belfast"
}
# print(nor_ire_dict)
united_kingdom.append(nor_ire_dict)
# print(united_kingdom)
# a better way to do it is below, more succint
# united_kingdom.append({
  # "name": "Northern Ireland",
  # "population": 1811000,
  # "capital": "Belfast"
# })


# 3. Use a loop to print the names of all the countries in the UK.

for country in united_kingdom:
  print(country["name"])

# 4. Use a loop to find the total population of the UK.

# I didn't do this exercise, John did! Noted for posterity
# For each country take the population, then add it to a running total
running_total = 0
for country in united_kingdom:
  country_pop = country["population"]
  running_total += country_pop

print(running_total)