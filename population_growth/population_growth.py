'''# Population Growth Calculator

Write the necessary code to display the total population count for the next 3 years (without a leap year).

Here are the specifications:

In the country we want to investigate:

- The current population is 380,123,456
- One person is born every 6 seconds
- One person dies every 12 seconds
- One person immigrates every 40 seconds
'''

current_pop = 380123456
sec_per_day = 86400


born = (sec_per_day / 6)
death = (sec_per_day / 12)
immigrate = (sec_per_day / 40)
per_day = (born + immigrate - death)
per_year = per_day * 365
total_pop = current_pop + per_year * 3

print(total_pop)
