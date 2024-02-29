from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import SWEPBASE
import ENTBASE
import BOTHBASE
from tkinter import*



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk() 

window.title('G.A.M (TheLargeOne)')

def run_script_swep():
    SWEPBASE.main()

def run_script_ent():
    ENTBASE.main()

def run_script_both():
    BOTHBASE.main()

window.geometry("775x575")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 575,
    width = 775,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    13.0,
    13.0,
    763.0,
    563.0,
    fill="#1F1F1F",
    outline="")

canvas.create_rectangle(
    25.0,
    27.0,
    750.0,
    552.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    38.0,
    38.0,
    738.0,
    538.0,
    fill="#1F1F1F",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_script_swep,
    relief="flat"
)
button_1.place(
    x=129.0,
    y=289.0,
    width=128.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_script_both,
    relief="flat"
)
button_2.place(
    x=518.0,
    y=288.0,
    width=128.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=run_script_ent,
    relief="flat"
)
button_3.place(
    x=326.0,
    y=289.0,
    width=128.0,
    height=55.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    259.0,
    308.0,
    image=image_image_1
)
icon = PhotoImage(file=relative_to_assets("icon.png"))
window.iconphoto(False, icon)
window.resizable(False, False)
window.mainloop()