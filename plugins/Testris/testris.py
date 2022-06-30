from ..basePlugin import BasePlugin
import os
import pathlib
import time


class Testris(BasePlugin):
    def __init__(self, app, output):
        super().__init__(app, output)
        self.pluginName = "Testris"
        self.version = "pre 0.1"

    def run(self):
        self.line()
        return ""

    def input(self, inp):
        if int(inp.get("inp_id")) == 1:
            self.corners()
        else:
            self.line()
        return ""
      
    def corners(self):
        self.out[0, 0] = (0, 0, 255)
        self.out[14, 0] = (0, 255, 255)
        self.out[0, 29] = (0, 255, 255)
        self.out[14, 29] = (0, 255, 0)

    def line(self):
        for i in range(30):
            for j in range(15):
                if (i + j) % 2 == 0:
                    self.out[j, i] = (255, 0, 0)
                else:
                    self.out[j, i] = (0, 0, 255)

                time.sleep(0.25)
                self.out.submit_all()
                
    def get_html(self):
        path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'testris.html')
        with open(path, "r") as f:
            return f.read()
