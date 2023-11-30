day = "Monday"

match day:
  case "Monday":
    print("Mondays are great for programming!")
  case "Tuesday":
    print("Tuesdays are for meetings.")
  case "Wednesday":
    print("Wednesdays are for writing.")
  case "Thursday":
    print("Thursdays are for testing.")
  case "Friday":
    print("Fridays are for deployment!")
  case _:
    print("I don't know what day it is!")