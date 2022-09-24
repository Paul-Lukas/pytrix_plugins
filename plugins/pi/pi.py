from ..basePlugin import BasePlugin
from decimal import getcontext, Decimal

class Tetrix(BasePlugin):
    def __init__(self, app, output):
        super().__init__(app, output)
        self.pluginName = "Pi"
        self.version = "3.14"
        
    def getColor(self,inp):
        color = [(0,0,0) for i in range(11)]
        
        color[1] = (246,206,55)
        color[2] = (221,91,35)
        color[3] = (214,40,31)
        color[4] = (187,38,65)
        color[5] = (95,61,59)
        color[6] = (109,81,118)
        color[7] = (1,96,162)
        color[8] = (48,143,187)
        color[9] = (62,191,148)
        color[0] = (49,69,59)
        
        color[10] = color[0]
        """
        outp = [0,0,0]
        for x in range(3):
            outp[x] = color[inp][x]-20
        return (outp[0],outp[1],outp[2])
        """
        return color[inp]
    
    def main(self,num_Digits):
        n = 0
        Pi = 0
        getcontext().prec = num_Digits+2
        n = 0
        a = 1
        b = 1/Decimal(2).sqrt()
        s = 1/Decimal(4)
        run = True

        while run:
            A = (a+b)/2
            B = Decimal(a*b).sqrt()
            S = s - 2**n * (a-A)**2



            if a==A:
                Pi = (str(A**2/s)[:-1])
                return Pi


            a = A
            b = B
            s = S

            n=n+1
        


    def run(self):
        pi = list(str(self.main(30*15+1000)))
        x = 0
        pixelBoard = [[0 for i in range(15)] for j in range(30)]
        for a in range(30):
            for b in range(15):
                pixelBoard[a][b] = self.getColor(int(pi[x+2]))
                x += 1
        print(pixelBoard)
        self.out.set_matrix(pixelBoard)
        self.out.submit_all()
                
        

    def input(self, inp):
        pass
    
    def get_html(self):
        return ""
