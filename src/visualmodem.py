from tkinter import *      
from sys import argv

def padHex(num: int) -> str:
    temp_str = hex(num)[2:]
    if len(temp_str) < 6:
        temp_str = '0'*(6-len(temp_str)) + temp_str
    if len(temp_str[1:]) > 6:
        temp_str = "#000000"
    return '#'+temp_str

with open(argv[1], 'rb') as f:
    f.seek(0)
    window = Tk()
    window.title('Visual Modem')
    WIDTH, HEIGHT = window.maxsize()
    print(f"Max Bytes: {HEIGHT*WIDTH*3}")
    canvas = Canvas(
        window,
        width = WIDTH, 
        height = HEIGHT
        )     
    canvas.pack()      
    img = PhotoImage(width=WIDTH, height=HEIGHT)
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
        anchor=NW, 
        image=img
        )
    # print(image_str)
    window.mainloop()  