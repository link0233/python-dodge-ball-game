class sprite:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=canvas.create_rectangle(30,40,80,90)
        self.ra=10
        self.t=0
        self.text=self.canvas.create_text(10,20,text='生命'+str(self.ra))

    def loop(self,eventx,eventy,ballxy,ball2xy):
        self.moveby(eventx,eventy)
        self.xy=self.canvas.coords(self.item)
        if self.xy[0]<ballxy[2] and self.xy[2]>ballxy[0] and self.xy[1]<ballxy[3] and self.xy[3]>ballxy[1] and self.t==0:
            self.t=1
            self.ra-=1
        
        if self.xy[0]<ball2xy[2] and self.xy[2]>ball2xy[0] and self.xy[1]<ball2xy[3] and self.xy[3]>ball2xy[1] and self.t==0:
            self.t=1
            self.ra-=1

        if self.t>100000:
            self.t=0
        self.t*=2

        self.canvas.delete(self.text)
        self.text=self.canvas.create_text(10,20,text='生命'+str(self.ra))
        
    def moveby(self,x,y):
        self.xy=self.canvas.coords(self.item)
        self.x=x-(self.xy[0]+self.xy[2])//2
        self.y=y-(self.xy[1]+self.xy[3])//2
        self.canvas.move(self.item,self.x,self.y)