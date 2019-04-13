from datetime import date, timedelta
def period_is_late(last,today,cycle_length):
    diff=today-last
    if(diff.days>cycle_length):
        return True
    else:
        return False
        
        
