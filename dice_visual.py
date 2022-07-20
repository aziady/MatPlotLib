import pygal

from die import Die

# Create two dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.add(result)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
