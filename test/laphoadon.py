from datetime import datetime
class Bill:
    def __init__(self,id,name_cus,room_num,total_day,money_a,moneyroom):
        self.id='KH{:02d}'.format(id+1)
        self.name_cus=name_cus
        self.room_num=room_num
        self.total_day=total_day+1
        self.money_a=money_a
        self.j=moneyroom
        self.totalcost=self.SumMoney()*self.j*self.total_day+self.money_a
    def SumMoney(self):
        array=[25,34,50,80]
        return array[self.j-1]
    def __str__(self):
        return f'{self.id} {self.name_cus} {self.room_num} {self.total_day} {self.totalcost}'
        
        
N=int(input())
list=[]
for i in range (N):
    name_cus = input()
    room_num = input()
    check_in = datetime.strptime(input(),"%d/%m/%Y")
    check_out= datetime.strptime(input(),"%d/%m/%Y")
    money_a  = int(input())
    total_day=(check_out-check_in).days
    moneyroom=int(room_num[:1])
    list.append(Bill(i,name_cus,room_num,total_day,money_a,moneyroom))
list.sort(key=lambda x : x.totalcost,reverse=True)
for x in list:
    print(x,sep='/n')