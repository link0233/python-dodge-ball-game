class ball:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=canvas.create_oval(0,0,20,20,fill='White')
        self.kd=[1,1]
    def loop(self,speed):
        self.canvas.move(self.item,speed*self.kd[0],speed*self.kd[1])
        self.xy=self.canvas.coords(self.item)
        if self.xy[0]<0 or self.xy[2]>640:
            self.kd[0]*=-1
        if self.xy[1]<0 or self.xy[3]>480:
            self.kd[1]*=-1

class ball2:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=canvas.create_oval(0,0,20,20,fill='White')
        self.kd=[1,1]
        self.xy=[0,0,0,0]
    def loop(self,speed):
        if speed>2:
            speed-=2
            self.canvas.move(self.item,speed*self.kd[0],speed*self.kd[1])
            self.xy=self.canvas.coords(self.item)
            if self.xy[0]<0 or self.xy[2]>640:
                self.kd[0]*=-1
            if self.xy[1]<0 or self.xy[3]>480:
                self.kd[1]*=-1