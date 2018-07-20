from Tkinter import Tk, StringVar
import tkMessageBox
import ttk
from Tkinter import *
import os

## THIS PYTHON CODE IS WRITTEN IN PYTHON 2.7.12, PLEASE CONVERT IT TO PYTHON 3 USING ONLINE CONVERTER FIRST IF YOU'RE
## USING PYTHON 3.x BECAUSE A LOT OF LIBRARY HAS BEEN CHANGED SINCE PYTHON 3 CAME OUT. THANK YOU. -warned by Hidayat-

#### -- (1) DECLARATIONS -- ###
##---------------Declare the container
root = Tk()                                                     ## Declare GUI object
root.wm_attributes("-topmost", 1)                               ## Make it stay topmost
winwidth = 450                                                  ## Declare window width
winheight = 97                                                  ## Declare window height
screenwidth = root.winfo_screenwidth()                          ## Get current display screen width
screenheight = root.winfo_screenheight()                        ## Get current display screen height
coorx = (screenwidth/2) - (winwidth/2)                          ## Calculate x-coordinate for center position
coory = (screenheight/2) - (winheight/2)                        ## Calculate y-coordinate for center position
root.title("UTF-8 Codepoint Converter")                         ## Declare main title
root.geometry('%dx%d+%d+%d' % (winwidth,winheight,coorx,coory)) ## Ask python to display window at specified size and position
root.configure(background='grey')                               ## Declare main background
datafile = "unip.ico"                                           ## Declare icon file
if not hasattr(sys, "frozen"):                                  ## Check if not running from exe
    datafile = os.path.join(os.path.dirname(__file__), datafile)## Use icon file reside in same directory as script
else:                                                           ## But if it is running from exe
    datafile = os.path.join(sys.prefix, datafile)               ## Use icon file from the temporary system directory
root.iconbitmap(default=datafile)                               ## Declare the small icon shown on window

##[1]---------------Declare the frames inside container
TopMainFrame = Frame(root, width=450, height=7, bg="grey", bd=8)
TopMainFrame.pack(side=TOP)
CenterMainFrame = Frame(root, width=450, height=90, bg="white", bd=8, relief="ridge")
CenterMainFrame.pack(side=TOP, expand=TRUE)

##[1]---------------Declare values needed to use
convertvalue = StringVar()      ## Character to be convert
tempvalue = StringVar()         ## Store temp result
resultvalue = StringVar()       ## Store result of converted codepoint

#### -- (2) DEFINITIONS -- ####
##[2]---------------Define convert resultvalue function
def conUnicode():
    tempvalue = ""                                   
    for i, c in enumerate(convertvalue.get()):
        tempvalue = tempvalue+"\\" + str(hex(ord(c)))
    resultvalue.set(tempvalue)
    root.clipboard_clear()
    root.clipboard_append(tempvalue)

##[2]---------------Define what to do for info button action
def ShowInfo():
    tkMessageBox.showinfo("UTF-8 Codepoint Converter","Unicode UTF-8 Codepoint Converter\n"+
                          "Intended to use with the Minetest client-side mod \"UnicodeParser\"\n\n"+
                          "Python script (C) 2018 muhdnurhidayat (MNH48.com) and contributors\n"+
						  "Available under The MIT License.\n"+
                          "https://github.com/MuhdNurHidayat/unicodeparser\n")

##[2]---------------Define what to do for exit button action
def AskExit():
    AskExit=tkMessageBox.askyesno("Exit System","Do you want to quit?")
    if AskExit>0:
        root.destroy()
        return

##[2]---------------Define what to do for reset button action
def Reset():
    convertvalue.set("")
    resultvalue.set("")

#### -- (3) MAIN CLASS OF THE PROGRAM -- ####
##[3]---------------Put buttons into top frames
btnInfo = Button(TopMainFrame, text='Info', padx=1, pady=1, bd=1, bg="grey", fg="black",
                    activebackground="grey", font=('arial', 10, 'normal'), width=8, height=1, command=ShowInfo, relief="raise")
btnInfo.grid(row=0,column=0)
btnConvert = Button(TopMainFrame, text='Convert', padx=1, pady=1, bd=1, bg="grey", fg="black",
                    activebackground="grey", font=('arial', 10, 'normal'), width=8, height=1, command=conUnicode, relief="raise")
btnConvert.grid(row=0,column=1)
btnReset = Button(TopMainFrame, text='Reset', padx=1, pady=1, bd=1, bg="grey", fg="black",
                    activebackground="grey", font=('arial', 10, 'normal'), width=8, height=1, command=Reset, relief="raise")
btnReset.grid(row=0,column=2)
btnExit = Button(TopMainFrame, text='Exit', padx=1, pady=1, bd=1, bg="grey", fg="black",
                    activebackground="grey", font=('arial', 10, 'normal'), width=8, height=1, command=AskExit, relief="raise")
btnExit.grid(row=0,column=3)

##[3]---------------Put text "input" into center frame
lblInput= Label (CenterMainFrame,font=('arial',10,'bold'), text='Input:', padx=1, pady=1, bd=1, fg="black", bg="white", width=10)
lblInput.grid(row=0,column=0)

##[3]---------------Put user input textbox into center frame
EntInput = Entry(CenterMainFrame,font=('arial',10,'bold'), textvariable=convertvalue, bd=1, fg="orange", width=50, justify='center')
EntInput.grid(row=0,column=1)

##[3]---------------Put text "output" into center frame
lblOut= Label (CenterMainFrame,font=('arial',10,'bold'), text='Output:', padx=1, pady=1, bd=1, fg="black", bg="white", width=10)
lblOut.grid(row=1,column=0)

##[3]---------------Put the converted output text into the center frame
EntOutput = Entry(CenterMainFrame,font=('arial',10,'bold'), textvariable=resultvalue, bd=1, fg="orange", width=50, justify='center', state='readonly', exportselection='true')
EntOutput.grid(row=1,column=1)

##[3]---------------Bind 'enter' key to convert as well
EntInput.bind("<Return>", (lambda event: conUnicode()))

##[3]---------------Make sure program GUI continues to run unless exited
root.mainloop()