from datetime import datetime
class Timegame:
    def __init__(self,magame,name,giovao,giora):
        self.magame=magame
        self.name=name
        self.giovao=giovao
        self.giora=giora
    def totaltime(self):
        return int((self.giora-self.giovao).total_seconds())
    def __str__(self):
        return f'{self.magame} {self.name} {self.totaltime() // 3600} gio {(self.totaltime() %3600) //60} phut'
    
array=[]
for _ in range (int(input())):
    
    magame=input()
    name=input()
    giovao=datetime.strptime(input(),'%H:%M')
    giora=datetime.strptime(input(),'%H:%M')
    array.append(Timegame(magame,name,giovao,giora))
array.sort(key=lambda Timegame:-Timegame.totaltime())
for x in array:
        print(x)