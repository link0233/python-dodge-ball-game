from tkinter import*
from pythonm.wd.ball import ball
from pythonm.wd.ball import ball2
from pythonm.wd.sprite import sprite
import time

class main(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('躲避球')
        super(main,self).__init__(self.root,width=640,height=480,bg='#aabbcc')
        self.pack()

        self.eventx=0
        self.eventy=0
        self.bind('<Motion>',self.mot)

        self.setp()
        while True:
            self.loop()
            self.root.update()
            time.sleep(0.01)
        self.root.mainloop()

    def setp(self):
        self.ball1=ball(self)
        self.ball2=ball2(self)
        self.sprite=sprite(self)
        self.speed=0.01

    def loop(self):
        self.ball1.loop(self.speed//3)
        self.ball2.loop(self.speed//5)
        self.sprite.loop(self.eventx,self.eventy,self.ball1.xy,self.ball2.xy)
        self.speed+=0.01
        if self.sprite.ra<1:
            import sys;sys.exit()

    def mot(self,event):
        self.eventx=event.x
        self.eventy=event.y

if __name__=='__main__':
    main()