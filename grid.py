from math import sqrt

from rich.color import Color
from rich.segment import Segment
from rich.style import Style

from textual.strip import Strip
from textual.widget import Widget


empty = Style.parse("#454545")


# finding the gradient by interpolating between two chosen colors based on t. 
def interpolate(t, stops):
    t = max(0.0, min(1.0, t))
    n = len(stops) - 1
    scaled = t * n
    i = min(int(scaled), n - 1)
    local_t = scaled - i
    r1, g1, b1 = stops[i]
    r2, g2, b2 = stops[i + 1]
    return (
        int(r1 + (r2 - r1) * local_t),
        int(g1 + (g2 - g1) * local_t),
        int(b1 + (b2 - b1) * local_t),
    )


# colors palettes -- GREEN
LIVE  = [(236,243,158),(144,169,85),(79,119,45),(144,169,85),(236,243,158)]
DEAD1 = [(128,137,48),(63,70,47),(37,48,27),(63,70,47),(128,137,48)]
DEAD2 = [(80,82,67),(48,49,46),(31,33,29),(48,49,46),(80,82,67)]
DEAD3 = [(70,70,70),(46,46,46),(29,29,29),(46,46,46),(70,70,70)]
LIVE = LIVE[::-1]
DEAD1=DEAD1[::-1]
DEAD2=DEAD2[::-1]
DEAD3=DEAD3[::-1]


class Grid(Widget):
    def __init__(self,game):
        super().__init__()
        self.game=game
        # ·


    def render_line(self, y: int):
        row=[] 
        cx=self.size.width // 4
        cy=self.size.height // 2
        max_dist=sqrt((cx**2)+(cy**2))
        if max_dist == 0:
            max_dist = 1
        for x in range(self.size.width):
            dx=(x-cx)
            dy=(y-cy)
            # t is how far a coordinate is from the center in percentage (0.0 to 1.0)
            t=sqrt((dx**2)+(dy**2))/max_dist

            if (x,y) in self.game.cells:
                r, g, b = interpolate(t, LIVE)
                row.append(Segment("██",Style(color=Color.from_rgb(r, g, b))))
            else:
                if (x,y) in self.game.dying:
                    if self.game.dying[(x,y)]==2:
                        r, g, b = interpolate(t, DEAD1)
                        row.append(Segment("▒▒",Style(color=Color.from_rgb(r, g, b))))
                    elif self.game.dying[(x,y)]==1:
                        r, g, b = interpolate(t, DEAD2)
                        row.append(Segment("░░",Style(color=Color.from_rgb(r, g, b))))
                    elif self.game.dying[(x,y)]==0:
                        r, g, b = interpolate(t, DEAD3)
                        row.append(Segment("░░",Style(color=Color.from_rgb(r, g, b))))
                else:
                    row.append(Segment("··",empty))
        return Strip(row)