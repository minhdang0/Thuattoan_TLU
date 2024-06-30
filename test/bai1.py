def dayofmonth(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month==2:
        if namnhuan(year)==True:
            return 29
        else:
            return 28
    else:
        return 30

def tinhsongaytudaunam(d1,m1,y1):
    dayss=d1
    if m1==1:
        return dayss
    else:
        for j in range(1,m1):
            dayss+=dayofmonth(j,y1)
    return dayss

def tinhsongay(d,m,y):
    days=0
    for i in range (1,y):
        if namnhuan(i)==True:
            days+=366
        else:
            days+=365
    days+=tinhsongaytudaunam(d,m,y)
    return days

def namnhuan(year_):
    if  year_%4==0 and year_%100!=0 or year_%400==0:
        return True
    return False

def tinhkhoangcachngay(dd1,mm1,yy1,dd2,mm2,yy2):
    kc1=tinhsongay(dd1,mm1,yy1)
    kc2=tinhsongay(dd2,mm2,yy2)
    day=abs(kc1-kc2)
    return day
print(tinhsongay(30,3,2023))
print(tinhsongay(1,1,2024))
print(tinhkhoangcachngay(5,9,2023,3,2,2024))