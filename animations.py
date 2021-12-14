import turtle as trtl


#----- def screen size vars
screen_h = 810
screen_w = 2060

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

# img init for 0th section
def chc_0():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/IMG_0493 (1).PNG.gif") 

# img init for 1st section
def chc_1():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/IMG_0492 (1).gif")

# img init for 2nd section
def chc_2():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/IMG_0478.gif")

# SKIP #3

# img init for 4th section
def chc_4():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/IMG_0480.gif")

def spdr():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/IMG_0482.gif")

def cave():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/IMG_0479-_1__1.gif")

def choice():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/choose.gif")
wn.mainloop()