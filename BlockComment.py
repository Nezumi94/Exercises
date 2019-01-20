'''
Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakladamy ze:
-liczba mrugniec na minute to 20
-liczba minut w godzinie to 60
-liczba godzin w dobie 24
-liczba lat (czyli nasz X) 50
Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
powinna wynosic 16
'''

#inline = ilość mrugnięć okiem na minutę

blinksPerMin = 20

#ilość minut na godzinę i ilość godzin w dobie

minInHour = 60
hoursInDay = 24
daysInYear = 365
activeHours = 16

#ilosc lat

years = 50

#ilosc mrugniec w ciagu X lat

print(blinksPerMin * minInHour * activeHours * daysInYear * years)


#definitionOfVariables
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print((daysOfWorkPerMonth * monthsInYear - vacation)*yearsOfWOrk)