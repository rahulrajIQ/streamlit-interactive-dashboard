import datetime as dt

def variables():
    d = dt.date.today()
    while d.weekday() != 3:
        d += dt.timedelta(1)

    date = str(d.day)
    if len(str(d.day)) == 1:
        date =  '0' + str(d.day)
        
    month = d.strftime("%B")[0:3]

    if len(str(d.month)) == 2:
        mnth =str(d.month)
    else:
        mnth = '0' + str(d.month)

    year = str(d.year)
    exp = year + mnth + date

    ce= 'BANKNIFTY'+ ' ' + date + ' ' + month + ' ' + year + ' '  + 'CE' + ' '  
    pe= 'BANKNIFTY'+ ' ' + date + ' ' + month + ' ' + year + ' '  + 'PE' + ' '

    lot_size = 25

    today_date = dt.datetime.today()
    date1 = today_date.strftime("%Y-%m-%d") 
    date2 = today_date.strftime("%Y-%m-%d")

    return ce, pe, date1, date2