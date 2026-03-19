from textual.app import App
from patterns import generate_random
from game import Game
from grid import Grid
from playback import PlaybackControls

class Board(App):
    def __init__(self):
        super().__init__()
        self.game=Game(cells=set())
    def compose(self):
        yield Grid(self.game)
        # yield PlaybackControls()
    
    def on_mount(self):
        self.game.cells=generate_random(self.size.width,self.size.height)
        self.set_interval(0.1, self.tick)

    def tick(self):
        self.game.step()
        grid=self.query_one(Grid)
        grid.refresh()
        
if __name__ == "__main__":
    app=Board()
    app.run()