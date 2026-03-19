from textual.widgets import Button
from textual.widget import Widget



class PlaybackControls(Widget):
    DEFAULT_CSS = """
PlaybackControls {
    layout: horizontal;
    height: 3;
    align: center middle;
}

PlaybackControls Button {
    min-width: 5;
    height: 3;
}
"""
    def compose(self):
        yield Button("⏸", id="pause")
        yield Button("⟳", id="reset")
        yield Button("⏩", id="faster")
        yield Button("⏪", id="slower")