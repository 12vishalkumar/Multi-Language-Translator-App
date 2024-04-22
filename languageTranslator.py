#************************************** Importing required libararies *************************
from tkinter import *
from translate import *
import speech_recognition as sr


#************************************** Variable and function assigning ************************
root = Tk()
root.title("Translator")
root.resizable(False, False)
mainframe = Frame(root)
mainframe.columnconfigure(0, weight=1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2, column=1)

#************************************* Lanaguage translation function *************************
def translate():
    translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
    translation = translator.translate(var.get()) 
    var1.set(translation)

#************************************* Language Talk function *********************************
def talk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please! speak something.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Sphinx thinks you said " + text)
        var.set(text)
        translate()
    except sr.UnknownValueError:
        print("Sphinx could not understand your audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

        
#******************************************* Function calls ********************************
lan1 = StringVar(root)
lan2 = StringVar(root)
choices = {'English', 'Hindi', 'French', 'Spanish', 'German','Italian', 'Japanese', 'Swedish', 'Tamil', 'Arabic', 'Thai', 'Danish', 'Greek'}
lan1.set('English')
lan2.set('Hindi')
lan1menu = OptionMenu(mainframe, lan1, *choices)
Label(mainframe, text="Please! Select the language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)
lan2menu = OptionMenu(mainframe, lan2, *choices)
Label(mainframe, text="Please! Select the language").grid(row=0, column=2)
lan2menu.grid(row=1, column=2)
Label(mainframe, text="Enter in your text").grid(row=2, column=0)
Label(mainframe, text="Output:").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1).grid(row=2, column=3)
b = Button(mainframe, text='Translate', command=translate).grid(row=3, column=1, columnspan=1)
s = Button(mainframe, text='Please! Speak', command=talk).grid(row=3, column=2, columnspan=3)
root.mainloop()