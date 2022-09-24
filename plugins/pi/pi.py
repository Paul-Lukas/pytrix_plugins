from ..basePlugin import BasePlugin
from decimal import getcontext, Decimal

class Tetrix(BasePlugin):
    def __init__(self, app, output):
        super().__init__(app, output)
        self.pluginName = "Pi"
        self.version = "3.14"

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
        pi = list(str(self.main(500)))
        x = 0
        pixelBoard = [[0 for i in range(15)] for j in range(30)]
        for a in range(30):
            for b in range(15):
                pixelBoard[a][b] = pi[x]
                x += 1
        self.out.set_matrix(pixelBoard)
        self.out.submit_all()
                
        

    def input(self, inp):
        bla = int(inp.get("Wert"))
    
    def get_html(self):
        return """<h1>Tetryx_6.9</h1>
        <table border="1" align="left">
     <tr>
      <th onclick="ccw()">ccw_move</th>
      <th onclick="t()">test</th>
      <th onclick="cw()">cw_move</th>
     </tr><tr>
      <td onclick="l()">l_move</td>
      <td onclick="d()">d_move</td>
      <td onclick="r()">r_move</td>
     </tr>
    </table>
    <script>
    document.addEventListener('keydown', (event) => {
        var name = event.key;
        var code = event.code;
            if (name== "a") l();
            if (name== "d") r();
            if (name== "s") d();
            if (name== "ArrowLeft") ccw();
            if (name== "ArrowRight") cw();
    }, false);
    
    function t() {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "/plugin/{{ start_id }}/input?Wert=6", false );
        xmlHttp.send( null );
    }
    function r() {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "/plugin/{{ start_id }}/input?Wert=1", false );
        xmlHttp.send( null );
    }
    function l() {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "/plugin/{{ start_id }}/input?Wert=2", false );
        xmlHttp.send( null );
    }
    function d() {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "/plugin/{{ start_id }}/input?Wert=3", false );
        xmlHttp.send( null );
    }
    function cw() {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "/plugin/{{ start_id }}/input?Wert=4", false );
        xmlHttp.send( null );
    }
    function ccw() {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "/plugin/{{ start_id }}/input?Wert=5", false );
        xmlHttp.send( null );
    }
    </script>"""
