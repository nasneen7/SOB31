# A time traveler has suddenly appeared in your classroom!
# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


year = int(input("Greetings! What is your year of origin? "))
# '==' changed to '='
# int.input changed to int(input
# at the end before brackets ' is changed to "

if year <= 1900:  #colon added 
    print ("Woah, that's the past!")  # single qoutes are changes to double qoutes 
elif year > 1900 & year < 2020:  #replaces && with &
    print ("That's totally the present!")
else:   #elif changed to else
    print ("Far out, that's the future!!")
