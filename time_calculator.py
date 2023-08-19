def add_time(start, duration, *args):
  new_time = ""
  startTime = start.split()[0]
  startNoon = start.split()[1]

  if (startNoon == "PM"):
    startHour = int(startTime.split(":")[0]) + 12
  else:
    startHour = int(startTime.split(":")[0])

  startMinute = int(startTime.split(":")[1])

  durationHour = int(duration.split(":")[0])
  durationMinute = int(duration.split(":")[1])

  daysOfTheWeek = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
    "Saturday"
  ]
  startingDayOfTheWeek = ""

  resultHour = 0
  resultMinute = 0
  resultNoon = ""
  resultNumberOfDays = 0
  resultDayOfTheWeek = ""

  if ((startMinute + durationMinute) < 60):
    resultMinute = startMinute + durationMinute
  else:
    resultMinute = (startMinute + durationMinute) % 60
    resultHour += (startMinute + durationMinute) // 60

  if ((startHour + durationHour + resultHour) < 24):
    resultHour += (startHour + durationHour)
  else:
    resultNumberOfDays += (startHour + durationHour + resultHour) // 24
    resultHour = (startHour + durationHour + resultHour) % 24

  if ((resultHour / 12) < 1):
    resultNoon = "AM"
  else:
    resultNoon = "PM"

  if (len(args) == 0):
    pass
  elif (len(args) == 1):
    try:
      if (args[0].capitalize() in daysOfTheWeek):
        startingDayOfTheWeek = args[0].capitalize()
        if (resultNumberOfDays > 0):
          resultDayOfTheWeek = daysOfTheWeek[
            (daysOfTheWeek.index(startingDayOfTheWeek) + resultNumberOfDays) %
            7]
        else:
          resultDayOfTheWeek = startingDayOfTheWeek
      else:
        raise "This is not in days of the week!"
    except AttributeError:
      return "The day of the week cannot be an integer!"
  else:
    raise "The day of the week must contain only one argument!"

  if (resultHour == 0):
    hString = "12"
  elif ((resultHour > 0) & (resultHour < 13)):
    hString = str(resultHour)
  else:
    hString = str(resultHour % 12)

  mString = str(resultMinute).zfill(2)

  if ((len(args) == 0) & (resultNumberOfDays == 0)):
    new_time = f"{hString}:{mString} {resultNoon}"
  elif ((len(args) == 0) & (resultNumberOfDays == 1)):
    new_time = f"{hString}:{mString} {resultNoon} (next day)"
  elif ((len(args) == 0) & (resultNumberOfDays > 1)):
    new_time = f"{hString}:{mString} {resultNoon} ({resultNumberOfDays} days later)"
  elif ((resultDayOfTheWeek in daysOfTheWeek) & (resultNumberOfDays == 0)):
    new_time = f"{hString}:{mString} {resultNoon}, {resultDayOfTheWeek}"
  elif ((resultDayOfTheWeek in daysOfTheWeek) & (resultNumberOfDays > 1)):
    new_time = f"{hString}:{mString} {resultNoon}, {resultDayOfTheWeek} ({resultNumberOfDays} days later)"
  else:
    new_time = f"{hString}:{mString} {resultNoon}, {resultDayOfTheWeek} (next day)"

  #resultHour, hString, resultMinute, mString,
  #resultNoon, resultNumberOfDays, resultDayOfTheWeek

  return new_time