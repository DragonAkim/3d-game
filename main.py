from tkinter import *
from math import *
from player import *
from block import *
from raycaster import *
from copy import *
from random import *

root = Tk()

canvas = Canvas(width=590, height=300, bg="#000000")
canvas.pack() 

player = Player(center=(250, 150), canvas=canvas)

block = Block()
for i in range(randint(10, 20)):
    __ = (randint(-100, 100), randint(-100, 100))
    block.add_block(__[0], __[1], __[0] - 20, __[1] - 20, "block")

# block.add_block(20, 20, 50, 50, "block")
# block.add_block(-20, -20, -50, -50, "block")

selected_data = []

raycaster = Raycaster(0)

direction = 0
keys = []

def rgb(r, g, b):
    return f"#{floor(r):02x}{floor(g):02x}{floor(b):02x}"


settings = {
        "graphics possibilities": ["rough", "smooth", "simplified"],
        "graphics": "simplified",
        "FOV": 60,
        "Render Distance": 1,
        "test mode": [False, {"map": {"show map": False, "show raycasting progress on map":False}, "raycasting speed": 1, "screen width":590, "gap": False}]
    }

def mainloop():
    global keys, direction, settings
    canvas.delete("all")

    # player.draw()

    # canvas.create_line(player.center[0], player.center[1], player.center[0] + cos(radians(direction))*50, player.center[1] + sin(radians(direction)) * 50)
    # canvas.create_oval(raycaster.x-5+player.center[0], raycaster.y-5-player.y+player.center[1], raycaster.x+5-player.x+player.center[0], raycaster.y+5-player.y+player.center[1])

    selected_data = block.data.copy()

    # for i in range(len(selected_data)):
    #     canvas.create_rectangle(selected_data[i][0][0][0]-player.x+player.center[0], selected_data[i][0][0][1]-player.y+player.center[1], selected_data[i][0][1][0]-player.x+player.center[0], selected_data[i][0][1][1]-player.y+player.center[1])
    array = raycaster.raycast(player.x, player.y, direction, settings["FOV"] + settings["test mode"][1]["addon FOV"], [[i[0], i[2]] for i in selected_data], settings["Render Distance"]*100, settings["test mode"][1]["raycasting speed"], dirspeed=1)

    distance = settings["Render Distance"]*100
    calc = ceil(255/distance)

    if settings["graphics"] == "rough":
        for i in range(len(array)):
            if array[i][0] is not None:
                calc2 = [(i*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], (distance*2 - array[i][0])*2), (i*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], -(distance*2 - array[i][0])*2 + 300)]

                canvas.create_line(calc2, width=10, fill=rgb(255-min((array[i][0]*calc), 255), 255-min((array[i][0]*calc), 255), 255-min((array[i][0]*calc), 255)))
    elif settings["graphics"] == "smooth":
        for i in range(len(array) - 1):
            if array[i+1][0] is not None and array[i][0] is not None:
                    if array[i][1] == array[i+1][1]:
                        calc2 = [(i*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], (distance*2 - array[i][0])*2), (i*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], -(distance*2 - array[i][0])*2 + 300)]

                        canvas.create_polygon([calc2[1], 
                                               calc2[0], 
                                               ((i+1)*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], 
                                                (distance*2 - array[i+1][0])*2), 
                                                ((i+1)*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], 
                                                -(distance*2 - array[i+1][0])*2 + 300)
                                                                                  ]
                                                                                  , fill=rgb(255-min((array[i+1][0]*calc), 255), 255-min((array[i+1][0]*calc), 255), 255-min((array[i+1][0]*calc), 255)))

    elif settings["graphics"] == "simplified":
        for i in range(len(array)):
            if array[i][0] is not None:
                dataindex = i
                index = i
                for j in range(len(array) - i - 2):
                    if array[index + 1][0] is not None:
                        if array[index + 1][1] == array[dataindex][1]:
                            index += 1
                        else:
                            break
                    else:
                        break
                i = index
                if i > len(array):
                    break
                calc2 = [(dataindex*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], (distance*2 - array[dataindex][0])*2), (dataindex*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], -(distance*2 - array[dataindex][0])*2 + 300)]

                canvas.create_polygon([calc2[1], 
                                               calc2[0], 
                                               ((index)*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], 
                                                (distance*2 - array[i][0])*2), 
                                                ((index)*(settings["test mode"][1]["screen width"]+settings["test mode"][1]["addon width"])/settings["FOV"], 
                                                -(distance*2 - array[i][0])*2 + 300)
                                                                                  ]
                                                                                  , fill=rgb(255-min((array[index][0]*calc), 255), 255-min((array[index][0]*calc), 255), 255-min((array[index][0]*calc), 255)))
                



    canvas.update()

    # print([i[0] for i in selected_data])
    # print(raycaster.x, raycaster.y)

    # print(degrees(atan2(root.winfo_pointery()+player.center[1]-player.y, root.winfo_pointerx()+player.center[0]-player.x)))
    # player.move(atan2(root.winfo_pointery()-player.y, root.winfo_pointerx()-player.x), 1)
    rvel = int('d' in keys) - int('a' in keys)
    mvel = int('w' in keys) - int('s' in keys)
    # print(keys, ('d' in keys or 'a' in keys or 's' in keys or 'w' in keys))
    # print(player.vel)
    direction += rvel*5
    player.vel += mvel
    player.vel = (min(max(-10, player.vel), 10) * 0.9)
    if player.vel < 0: player.vel = ceil(player.vel * 100) /100
    else: player.vel = floor(player.vel * 100) / 100

    player.move(direction, player.vel)
    
    root.after(16, mainloop)

def key_down(e):
    global keys
    if not e.keysym in keys: keys.append(e.keysym)
    # print(keys)

def key_up(e):
    global keys
    for i in range(len(keys)):
        if keys[i] == e.keysym:
            keys.pop(i)
            break

root.bind("<KeyPress>", key_down) 
root.bind("<KeyRelease>", key_up)

mainloop()

root.mainloop()