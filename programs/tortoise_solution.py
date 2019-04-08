def race(v1, v2, g):
    print("{0},{1},{2}".format(v1,v2,g))
    if v1>=v2:
        return None
    v1pm=float(v1)/60  #720/60=12
    v2pm=float(v2)/60  #850/60=14.16
    diffpm=v2pm-v1pm   
    ttcpm=g/diffpm # 32.40=70/2.16    
    hour=0
    ttcpmh=round(ttcpm,2)
    if(ttcpmh>60):
        hour=int(ttcpmh)/60        
    print(ttcpm)
    minute=int(round(ttcpm,2)%60)
    seconds=int(round(ttcpm,3)%1*60)
    print("hour,minute,seconds - {0},{1},{2}".format(hour,minute,seconds))
    return [hour,minute,seconds]