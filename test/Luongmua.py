class Rain_salary:
    def __init__(self,index,sta_name,Rainsalary,Period):
        self.ID="T{:02d}".format(index)
        self.sta_name=sta_name
        self.Rainsalary=Rainsalary
        self.Period=Period
    def medium_rain(self):
        return self.Rainsalary/(self.Period/60)
    def __str__(self):
        return '{} {} {:.2f}'.format(self.ID, self.sta_name,self.medium_rain())

station={}
index=0
N=int(input())
for _ in range(N):
    sta_name=input()
    start_rain=input()
    end_rain=input()
    Rainsalary=float(input())
    Period=( (int(end_rain[:2])*60+int(end_rain[3:])) -  (int(start_rain[:2])*60+int(start_rain[3:])) )
    if sta_name in station:
        station[sta_name].Rainsalary+=Rainsalary
        station[sta_name].Period+=Period
    else:
        index+=1
        station[sta_name]=Rain_salary(index,sta_name,Rainsalary,Period)
for x in station :
    print(station[x])