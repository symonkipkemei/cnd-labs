"""
Write the necessary code to display the total population count for the next 3 years (without a leap year).

Here are the specifications:

In the country we want to investigate:

The current population is 380,123,456
One person is born every 6 seconds
One person dies every 12 seconds
One person immigrates every 40 seconds

"""


current_populations = 380123456
seconds_in_day = 3600 * 24
seconds_in_year = seconds_in_day * 365
seconds_in_three_years = seconds_in_year * 3

persons_born_in_3_years = seconds_in_three_years/6
persons_died_in_3_years = seconds_in_three_years/12
persons_migrate_in_3_years = seconds_in_three_years/40

population = (current_populations + persons_born_in_3_years) - (persons_died_in_3_years + persons_migrate_in_3_years)

print("The total population is", population)