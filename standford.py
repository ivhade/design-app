import tkinter as tk
from tkinter import *
from functools import partial
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
FONT = ("Arial", 10, "normal")

x1 = 0
y1 = 0
# This is just an app that helps fashion designers put together simple patterns in terms of shapes and sizes.
# Users would be expected to type in different shapes and sizes"""

# available colors , list can be updated
available_colors = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black',
                    'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse',
                    'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan',
                    'DarkGoldenRod', 'DarkGray', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen',
                    'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue',
                    'DarkSlateGray', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DodgerBlue',
                    'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold',
                    'GoldenRod', 'Gray', 'Green', 'GreenYellow', 'HoneyDew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory',
                    'Khaki', 'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral',
                    'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGreen', 'LightPink', 'LightSalmon',
                    'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSteelBlue', 'LightYellow', 'Lime',
                    'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid',
                    'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise',
                    'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy',
                    'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 'Orchid', 'PaleGoldenRod', 'PaleGreen',
                    'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue',
                    'Purple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen',
                    'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'Snow', 'SpringGreen',
                    'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
                    'WhiteSmoke', 'Yellow', 'YellowGreen']


#enter
def enter():
    n = int(Size.get())
    return n

#main function running the entire code
def main():
    global Size, Design, canvas
    #  main window
    window = tk.Tk()
    window.title("MY FIRST DESIGN APP")

    # window size
    # window.config doesn't extend the window from canvas so use geometry
    window.geometry("400x500")
    instruction_message = " Please put in a shape. Options include:\n circle, square, rectangle, horizontal_lines and vertical_lines.\n Shapes are adjustable based on the size you provide"
    ascii_art = """
    db   d8b   db d88888b db       .o88b.  .d88b.  .88b  d88. d88888b 
    88   I8I   88 88'     88      d8P  Y8 .8P  Y8. 88'YbdP`88 88'     
    88   I8I   88 88ooooo 88      8P      88    88 88  88  88 88ooooo 
    Y8   I8I   88 88~~~~~ 88      8b      88    88 88  88  88 88~~~~~ 
    `8b d8'8b d8' 88.     88booo. Y8b  d8 `8b  d8' 88  88  88 88.     
    `8b8' `8d8'  Y88888P Y88888P  `Y88P'  `Y88P'  YP  YP  YP Y88888P 


        """

    # canvas size
    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")

    # arranging ascii on canvas
    x_start = 5  # starting x position
    y_start = 150  # starting y position
    line_height = 10  # height between lines

    ascii_text = []  # List to store the texts from ascii

    # enables the ascii show exactly
    for i, line in enumerate(ascii_art.split('\n')):
        text = canvas.create_text(x_start, y_start + i * line_height, anchor="nw", text=line, fill="white",
                                  font=FONT)

        ascii_text.append(text)

    # delete ascii
    def delete_ascii():
        for text in ascii_text:
            canvas.delete(text)

    # Create an initial empty text item on the canvas with white color
    canvas_id = canvas.create_text(200, 150, text="", font=FONT, fill="white", anchor="center")

    # Schedule the messages
    schedule_messages(window, canvas, instruction_message, canvas_id)

    # receive input
    Design = Entry(border=3, width=9, highlightcolor='white')
    Design.place(x=80, y=425)

    Design_label = Label(height=2, width=9, text="Design", font=FONT)
    Design_label.place(x=15, y=425)

    Size = Entry(border=3, width=9, highlightcolor='white')
    Size.place(x=280, y=425)

    Size_label = Label(height=2, width=9, text="Shape Size", font=FONT)
    Size_label.place(x=210, y=425)

    Size_button = Button(padx=5, pady=1, text="Enter", font=FONT, anchor="w", command=design_choice)
    Size_button.place(x=300, y=460)

    canvas.pack()
    # deletes ascii from canvas
    window.after(1000, delete_ascii)
    # ensures canvas is clear for user entry
    window.after(7000, canvas.delete, canvas_id)



    window.mainloop()

    # Schedule the deletion of the ASCII art after 5 seconds (5000 milliseconds)

#square design
def square():
    global canvas
    for x1 in range(0, CANVAS_WIDTH, enter()):
        for y1 in range(0, CANVAS_HEIGHT, enter()):
            # filling in random colors
            fill_color = random.choice(available_colors)
            # drawing the shape
            canvas.create_rectangle(x1, y1, x1 + enter(), y1 + enter(), fill=fill_color)

#circle design
def circle():
    global canvas

    # adjusting the design to cover the entire canvas
    for x1 in range(0, CANVAS_WIDTH, enter()):
        for y1 in range(0, CANVAS_HEIGHT - 60, enter()):
            # filling in random colors
            fill_color = random.choice(available_colors)
            # drawing the shape
            canvas.create_oval(x1, y1, x1 + enter(), y1 + enter(), fill=fill_color)


# horizontal line design
def horizontal_lines():
    global canvas

    # adjusting the design to cover the entire canvas
    for x1 in range(0, CANVAS_WIDTH, enter()):
        for y1 in range(0, CANVAS_HEIGHT - 60, enter()):
            # filling in random colors
            fill_color = random.choice(available_colors)
            # drawing the shape
            canvas.create_line(x1, y1, x1 + enter(), y1, fill=fill_color)


# vertical line design
def vertical_lines():
    global canvas
    # adjusting the design to cover the entire canvas
    for x1 in range(0, CANVAS_WIDTH, enter()):
        for y1 in range(0, CANVAS_HEIGHT - 60, enter()):
            # filling in random colors
            fill_color = random.choice(available_colors)
            # drawing the shape
            canvas.create_line(x1, y1, x1, y1 + enter(), fill=fill_color)

# user choice
def design_choice():
    Design_pattern = Design.get().lower()
    if Design_pattern == "rectangle" or Design_pattern == "square":
        square()

    elif Design_pattern == "circle":
        circle()

    elif Design_pattern == "vertical_lines" or Design_pattern == "vertical_line":
        vertical_lines()

    elif Design_pattern == "horizontal_lines" or Design_pattern == "horizontal_line":
        horizontal_lines()

    else:
        print("Please check the options available and choose appropriately.")
        main()

# display message
def display_message(canvas, message, canvas_id):
    canvas.itemconfig(canvas_id, text=message)

# user guide
def schedule_messages(window, canvas, instruction_message, canvas_id):
    window.after(2000, partial(display_message, canvas, instruction_message, canvas_id))  # Display instruction message after 4 seconds




if __name__ == "__main__":
    main()
