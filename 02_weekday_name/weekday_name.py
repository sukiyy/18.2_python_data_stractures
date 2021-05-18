def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    if day_of_week>0 and day_of_week<=7:
        return days[day_of_week-1]
    else:
        return 'None'


print(weekday_name(9)+', should be None')
print(weekday_name(0)+', should be None')
print(weekday_name(1)+', should be Sunday')
print(weekday_name(7)+', should be Saturday')
