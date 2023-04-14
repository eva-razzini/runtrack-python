def draw_rectangle(width,height):
    print("|", ("-"*width), "|")
    for i in range(height - 2):
        print("|", (" "* width), "|")
    print("|", ("-"*width), "|")
draw_rectangle(int(input("largeur:")), int(input("longeur:")))