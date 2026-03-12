from textual.app import App, ComposeResult
from textual.widgets import Label, Button

class MyApp(App):
    
    def compose(self):
        yield Label("Hello World, First Commit")
        yield Button("Exit",id="exited",variant="primary")
        

    def on_button_pressed(self, event):
        self.exit(event.button.id)

if __name__=="__main__":
    app=MyApp()
    reply=app.run()
    print(reply)