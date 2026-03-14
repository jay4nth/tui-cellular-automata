from rich.segment import Segment
from rich.style import Style

from textual.app import App
from textual.strip import Strip
from textual.widget import Widget

from game import Game

live   = Style.parse("#aaff00")
dead_1 = Style.parse("#4a7a00")
dead_2 = Style.parse("#1f3d00")
dead_3 = Style.parse("#0a1500")

class Grid(Widget):
    def __init__(self,game):
        super().__init__()
        self.game=game
        
    def render_line(self, y: int):
        row=[]
        
        for x in range(self.size.width):
            if (x,y) in self.game.cells:
                row.append(Segment("██",live))
            else:
                if (x,y) in self.game.dying:
                    if self.game.dying[(x,y)]==2:
                        row.append(Segment("▓▓",dead_1))
                    elif self.game.dying[(x,y)]==1:
                        row.append(Segment("▒▒",dead_2))
                    elif self.game.dying[(x,y)]==0:
                        row.append(Segment("░░",dead_3))
                else:
                    row.append(Segment("  "))
        return Strip(row)

class Board(App):
    def __init__(self):
        super().__init__()
        self.game=Game(cells={(2,1), (3,2), (3,3), (2,3), (1,3)})
    def compose(self):
        yield Grid(self.game)
    
    def on_mount(self):
        self.set_interval(0.1, self.tick)

    def tick(self):
        self.game.step()
        self.query_one(Grid).refresh()
        
if __name__ == "__main__":
    app=Board()
    app.run()