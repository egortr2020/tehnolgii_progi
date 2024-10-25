from datetime import datetime, timedelta


def is_date_in_current_week(date_str):
    dates = date_str.split(',') 
    today = datetime.today()
    
    # Начало недели - текущий день
    start_of_week = today 

    # Конец недели - плюс 6 дней от начала
    end_of_week = start_of_week + timedelta(days=6) 

    print("Dates being checked:", [datetime.strptime(d.strip(), "%d.%m").replace(year=datetime.now().year) for d in dates])
    
    for date_part in dates:
        date_part = date_part.strip()
        try:
            date_obj = datetime.strptime(date_part, "%d.%m").replace(year=datetime.now().year)
            if start_of_week.date() <= date_obj.date() <= end_of_week.date():
              return True
        except ValueError:
            continue
    return False

def is_date_past(date_str):
  try:
    date_obj = datetime.strptime(date_str, "%d.%m").replace(year=datetime.now().year)
    return date_obj.date() < datetime.now().date() 
  except ValueError:   
    return False