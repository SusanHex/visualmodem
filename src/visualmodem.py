import argparse
from email.policy import default
from mimetypes import init
import tkinter      
import pathlib
from os.path import getsize
# init tk window
window = tkinter.Tk()

# Define some arg parse stuff
ARGPARSER = argparse.ArgumentParser(description="This program turns abitrary data into an image")
ARGPARSER.add_argument("file", type=argparse.FileType('rb'))
ARGPARSER.add_argument("-o", "--output", default=False, nargs='?', help="Writes the generated image to the disk")
ARGPARSER.add_argument("-d", "--dimensions", nargs=2, default=window.maxsize(), type=int, help=f"Specify height and width of image. Eg: {window.maxsize()[0]} {window.maxsize()[1]}", )
PARSEDARGS = ARGPARSER.parse_args()

def padHex(num: int) -> str:
    temp_str = hex(num)[2:]
    if len(temp_str) < 6:
        temp_str = '0'*(6-len(temp_str)) + temp_str
    if len(temp_str[1:]) > 6:
        temp_str = "#000000"
    return '#'+temp_str


with PARSEDARGS.file as f:
    f.seek(0)
    
    window.title('Visual Modem')
    WIDTH, HEIGHT = PARSEDARGS.dimensions
    print(f"Max Bytes: {HEIGHT*WIDTH*3}")
    canvas = tkinter.Canvas(
        window,
        width = WIDTH, 
        height = HEIGHT
        )     
    canvas.pack()      
    img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
    image_str = " "
    for i in range(WIDTH):
        print(f"{int(i/WIDTH*100)}%")
        image_str += "{ "
        for j in range(HEIGHT):
            b = f.read(3)
            hex_part = padHex(int.from_bytes(b, "big"))+' '
            image_str += hex_part
            # if b:
            #     print(hex_part, b)

        image_str += "} "
        
            
    img.put(image_str, to=(0, 0, WIDTH, HEIGHT))
            
            

    canvas.create_image(
        0,
        0, 
        anchor=tkinter.NW, 
        image=img
        )
    # print(image_str)
    if PARSEDARGS.output:
        img.write("./output.png")
    window.mainloop()  