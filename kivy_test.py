from kivy.app import App
from kivy.lang import Builder

class HelloWorldApp(App):
    def build(self):
        return Builder.load_file("main.kv")
    

HelloWorldApp().run()

"""
See main.kv

Labels make text appear and have to be in a label
    You can set things like font size (font_size: 24)
Buttons is a clickable button with customizable text and behavior:
Ids let you pull/access stuff, basically a placeholder or a pointer
TextInput is user input for text
    Hint text gives the user ideas what to put
Orientation tells the computer how to orient it; technically, you can change the size
Checkboxes
    active makes it already checked
Slider
    Self explanatory, doesn't show you the values
Switch
    Labled on/off
ProgressBar:
    Define max and starting value (value)
Image:
    Allows you to display from a file or URL
    source: url/path
    allow_strech: Lets it strech
    keep_ratio: Keeps the aspect ratio

BoxLayout:
    Orientation
    Everything's inside it
    You can also do grid layout where you set the columns at the beginning
    FloatLayout lets you positoin and size your children
        size_hint: (size hint) - They're percentages
        position_hint: (position hint)
    ScreenManager lets you swap between screens
        transition: transition
        Then set screens
    """

#"I know you guys care deeply about your images" - LaRose
#"This one lets you lets you position and size your children" - LaRose