def add_time(start, duration, weekday=None):

    # Split the start time into hours, minutes and time of day
    start_time = start.split(":")
    start_hours = int(start_time[0])
    start_minutes = int(start_time[1].split(" ")[0])
    start_am_pm = start_time[1].split(" ")[1]

    # Split duration time
    duration_time = duration.split(":")
    duration_hours = int(duration_time[0])
    duration_minutes = int(duration_time[1])

    # Days
    day_count = 0
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Results
    new_hours = 0
    new_minutes = 0
    new_am_pm = ""
    new_day = ""
  
    # Check minutes and add to hours if needed
    while duration_minutes > 59:
        duration_hours += 1
        duration_minutes -= 60

    if start_minutes + duration_minutes > 59:
        new_minutes = (start_minutes + duration_minutes) - 60
        duration_hours += 1
    else:
        new_minutes = start_minutes + duration_minutes
    
    # Change hours to 24 system
    if start_am_pm == "PM":
        start_hours += 12

    # Hours and days(if needed) calculation
    new_hours = start_hours + duration_hours
    while new_hours >= 24:
        day_count += 1
        new_hours -= 24

    # Changes hours to 12 system and AM/PM verification
    if new_hours >= 12:
      new_am_pm = "PM"
      if new_hours > 12:
        new_hours -= 12
    elif new_hours == 0:
      new_hours = 12
      new_am_pm = "AM"
    else:
      new_am_pm = "AM"

    # Days calculation
    if day_count == 1 and weekday is not None:
        new_day = ", " + week[(week.index(weekday.lower()) + 1)].title() + " (next day)"
      
    elif day_count > 1 and weekday is not None:
      if day_count > 7:
          days = day_count % 7
      else:
          days = day_count

      index_day = week.index(weekday.lower())

      if index_day + int(days) > 6:
        index_day = (index_day + int(days)) - 7
      else:
        index_day = index_day + int(days)

      new_day = ", " + week[int(index_day)].title() + " (" + str(day_count) + " days later)"

    elif day_count == 1 and weekday is None:
      new_day = " (next day)"
    
    elif day_count > 1:
      new_day = " (" + str(day_count) + " days later)"

    elif weekday is not None:
      new_day =", " + weekday.title()
    

    # Format the time to the right format (1:00)
    format_time = "{:01d}:{:02d}".format(new_hours, new_minutes)

    # Result considering if theres a day or not
    if new_day != "":
      new_time = format_time + " " + new_am_pm + new_day
    else:
      new_time = format_time + " " + new_am_pm
    return new_time