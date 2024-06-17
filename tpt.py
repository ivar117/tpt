#!/usr/bin/env python3

from os import listdir, getcwd, replace
import os.path
from sys import stdin
import customtkinter as ctk
from copy import copy #Kopiera object property
import argparse
from PIL import ImageTk, Image, ImageOps
import configparser

from customtkinter.windows.widgets import image

##read config file
config = configparser.ConfigParser()
config.optionxform = str #don't switch lower-case to upper

#add default keybindings to config
# from binds import binds_dict
# config['binds'] = binds_dict

config['binds'] = {'l': 'show_next_slide',
                   'h': 'show_prev_slide',
                   'b': 'show_prev_slide',
                   'w': 'show_next_slide',
                   'n': 'show_next_slide',
                   'p': 'show_prev_slide',
                   'j': 'show_next_slide',
                   'k': 'show_prev_slide',
                   'g': 'show_first_slide',
                   'G': 'show_last_slide',
                   '$': 'show_last_slide',
                   '<Right>': 'show_next_slide',
                   '<Left>': 'show_prev_slide',
                   '<Down>': 'show_prev_slide',
                   '<Up>': 'show_next_slide',
                   '<Button-1>': 'show_next_slide',
                   '<Button-3>': 'show_prev_slide',
                   '<Button-4>': 'show_next_slide',
                   '<Button-5>': 'show_prev_slide',
                   '<space>': 'show_next_slide',
                   '<BackSpace>': 'show_prev_slide',
                   '<Return>': 'show_next_slide',
                   '<Home>': 'show_first_slide',
                   '<End>': 'show_last_slide',
                   't': 'setmark',
                   'm': 'show_marked',
                   'L': 'show_last_before_marked',
                   'c': 'switch_appearance',
                   'i': 'switch_appearance',
                   '<Escape>': 'reset_counter',
                   'q': 'exit'}

#read custom config
#todo read $XDG_CONFIG_HOME
config.read(os.path.expanduser('~/.config/tpt/config.ini'))

##appearance
ctk.set_appearance_mode(config.get('appearance', 'color_mode', fallback='dark')) #sets the theme. May be dark mode, light mode or system.

ctk.set_default_color_theme("blue") #Colorscheme?.

tk_root = ctk.CTk() #Sets the root ctk window
tk_root.geometry("900x600") #Size of window
tk_root.title("tpt")

def stdlabel(name, fontsize): #Standard för att definera vanlig textruta. 
    #name är den text som textrutan ska innehålla, fontsize är fontstorleken.
    #TODO: fontsize ska inte vara en parameter , ska ha samma hela tiden ändå lissom.
    stdfont = ctk.CTkFont(family='JetBrains Mono', size=fontsize, weight='normal', slant='italic')
    label = ctk.CTkLabel(tk_root,
                         # text_color = "white",
                         font=stdfont,
                         text = name,
                         justify = "left",
                         anchor="center")
                         # font=ctk.CTkFont(size=fontsize))
    return label

def message_exit(message):
    exit("tpt: " + message)

def destroy_widgets(): #removes all currently active widgets. Used when switching scene.
    list_of_widgets = tk_root.winfo_children()
    
    for item in list_of_widgets:
        if item.winfo_children():
            list_of_widgets.extend(item.winfo_children())
    for item in list_of_widgets:
        item.destroy()

def switch_appearance():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def draw_img(current_slide):
    #TODO: draw_img måste köras i början. Måste se ifall en filepath är fel och isåfall quitta innan presentationen ens har börjat. 
    #Hantera ifall det skulle vara något problem med att visa en bild, t.ex. inte rätt filepath.
    image_path = ""
    for item in current_slide:
        if item[0] == "@":
            item_list = []
            for i in range(len(item)):
                item_list += item[i]
        
            del item_list[0] #ta bort @
            for i in range(len(item_list) - 1): #Minus 1 för att inte räkna med nyradstecken
                image_path += item_list[i]

    if image_path: #Om variabeln finns
        # selected_img = ImageTk.PhotoImage(selected_img)
        # state.label_image_slide = ctk.CTkLabel(tk_root, text="", image=selected_img)
        # state.label_image_slide.Image = selected_img
        # image_path = Image.open(image_path)
        # image_path = image_path.resize((int(0.4*tk_root.winfo_width()), int(0.4*tk_root.winfo_height())), Image.LANCZOS)
        # image_slide = ImageTk.PhotoImage(image_path)

        # image_slide = ctk.CTkImage(image_path)

        state.image = Image.open(image_path)
        width, height = state.image.size
        ratio = width / height

        # new_height = int(ratio * (0.4 * tk_root.winfo_height()))
        # # new_height = int(ratio * (0.4 * tk_root.winfo_height()))
        # # new_width = int(ratio * (0.4 * tk_root.winfo_width()))
        # new_width = int(ratio * new_height)

        # image_slide = ImageOps.contain(image, (new_width, new_height))

        # image_slide = image.resize((new_width, new_height), Image.LANCZOS)
        # image_slide = ImageOps.contain(image, (new_width, new_height))

        #Save the cropped image
        # resized_image.save('resizedimage.jpg')

        # image = image.resize((int(0.4*tk_root.winfo_width()), int(0.4*tk_root.winfo_height())), Image.LANCZOS)

        # image = ImageOps.contain(image, (int(0.4*tk_root.winfo_width()), int(0.4*tk_root.winfo_height())))
        # image = ImageOps.contain(image, size=(int(0.4*tk_root.winfo_width()), int(0.4*tk_root.winfo_height())))
        
        # image.thumbnail(((int(0.4*tk_root.winfo_width()), int(0.4*tk_root.winfo_height()))), Image.LANCZOS)
        
        new_height = int(ratio * (0.4 * tk_root.winfo_height()))
        new_width = int(ratio * new_height)
        image_slide = ctk.CTkImage(state.image, size=(new_width, new_height))

        state.label_image_slide = ctk.CTkLabel(tk_root, text="", image=image_slide)
        state.label_image_slide.pack(expand=True, fill=ctk.BOTH)
        return True

def bold_label():
    pass
    # _list = []
    # for i in range(len(slide_list)):
        # _list = list(slide_list[i])
        # if _list[0] == "*"
            # _list.remove(_list[0])
        # slide_list[i] = ""
        # slide_list[i] = slide_list[i].join(_list)

    # slide_text = ""
    # i = 0
    # for i in range(len(slide_list)):
        # slide_text += slide_list[i]
    # return slide_text

def remove_backslash(slide_list): #ta bort "\" i början av en rad
    #TODO: för varje slide så splittas den upp i en lista vid varje \n som skickas till denna funktion (samt draw_img) för att hantera \ o bilder.
    #Slide är text som görs om till en lista, slide_list
    #om det är ett ensamt \ så markerar det en tom slide.
    _list = []
    for i in range(len(slide_list)):
        _list = list(slide_list[i])
        if _list[0] == "\\":
            _list.remove(_list[0])
        slide_list[i] = ""
        slide_list[i] = slide_list[i].join(_list)
    return slide_list
    #Sedan ska slide_text omvandlas till en sträng där varje ny item i slide_text istället blir en \n innan.

def draw_progress(): #Kanske ha en ctk progressbar (se mitt frågesportspel)
    progress_style = config.get('appearance', 'progress_style', fallback='bar')
    if progress_style == "bar":
        state.progbar_slidesleft = ctk.CTkProgressBar(
            master=tk_root,
            width=int(0.04*tk_root.winfo_width()),
        )
        state.progbar_slidesleft.place(relx=0.5, rely=0.97, anchor=ctk.CENTER)
        # state.progbar_slidesleft.pack(padx=50, pady=40, expand=False)
        state.progbar_slidesleft.set(state.current_slide_index / (len(state.slides) - 1)) #adaptera progress bar till hur många frågor som är kvar.
        # state.progbar_slidesleft.place(relx=0.5, rely=0.97, anchor=ctk.CENTER)
    elif progress_style == "text":
        # counter_text = "[ slide " + str(state.current_slide_index + 1) + "/" + str(len(state.slides)) + " ]"
        counter_text = str(state.current_slide_index + 1) + "/" + str(len(state.slides))
        label_counter = stdlabel(counter_text, 20)
        # label_counter.pack(padx=50, pady=40)
        label_counter.place(relx=0.5, rely=0.97, anchor=ctk.CENTER)

def redraw():
    state.progbar_slidesleft = None
    state.label_currentslide = None
    state.label_image_slide = None

    slide = copy(state.current_slide()) #Gör en kopia av nurvarande med copy() funktion, då objektet inte ska ändras. Vanlig tilldelning ändrar på objektet.
    destroy_widgets()
    if not draw_img(slide):
        slide = remove_backslash(slide)

        slide_text = ""
        for i in range(len(slide)):
            slide_text += slide[i]
        state.label_currentslide = stdlabel(slide_text, int(0.04*tk_root.winfo_width()))
        state.label_currentslide.pack(expand=True, fill=ctk.BOTH)
        if len(state.slides) != 1:
            if config.getboolean('appearance', 'show_progress', fallback=True) == True:
                draw_progress()

def show_next_slide():
    if state.next_slide():
        redraw()
        #isimage() #Funktion för att skapa bild om @ i början av rad

# def prevslide(current_slide_index):
def show_prev_slide():
    if state.prev_slide():
        state.count = 0
        redraw()

def setmark():
    #TODO:markering i hörnet på slide som markeras
    # if state.marked_slide is None:
        # state.marked_slide = state.current_slide_index
    state.not_use_count = True
    if state.marked_slide != state.current_slide:
        state.marked_slide = state.current_slide_index

def show_marked():
    state.count = 0
    if state.marked_slide is None:
        pass
    elif state.marked_slide != state.current_slide_index:
        state.slide_index_before_marked = state.current_slide_index
        state.current_slide_index = state.marked_slide
        redraw()

def show_last_before_marked():
    state.count = 0
    if state.slide_index_before_marked is None:
        pass
    elif state.slide_index_before_marked != state.current_slide_index:
        state.current_slide_index = state.slide_index_before_marked
        redraw()

def show_first_slide():
    state.count = 0
    if state.current_slide_index != 0: #Gå inte till sista i onödan
        state.current_slide_index = 0
        redraw()
    
def show_last_slide():
    state.count = 0
    if state.current_slide_index != len(state.slides) - 1:
        state.current_slide_index = len(state.slides) - 1
        redraw()

def check_similar_filename(filename, filepath):
    #TODO: fixa så att kollar ifall tar bort filändelsen också
    #Måste om man gör från en directory måste kolla om directorin e rätt också. Bara skicka in filename
    #Mer avancerad algorithm som tar hänsyn till ifall det är en extra bokstav, siffra istället för bokstav (b0ys istället för boys) osv.
    #Just nu så blir det fel om man skriver fel directory, då returnerar en python felkod, inte min lolle

    dir_list = listdir(filepath)
    filename = filename.lower()
    
    for i in range(len(dir_list)):
        if dir_list[i].lower() == filename:
            return dir_list[i] #Ska jag bara ha filnamnet och dir separat, eller concatade?
            #return filepath + "/" + dir_list[i] 
    return False

def readfile(): #Antingen ger man filen som argument till programmet eller om inget argument är angivet väljer man filen med file pickern
    # filename = ctk.filedialog.askopenfilename()
    #TODO: för att få den att skriva "did you mean HEJ.png (istället för hej) ska söka i samma dir efter alla filer, lägga innehåll i en lista, och sedan gör allt till lowercase, så att kan jämföra. Sedan då måste jämföra med nuvarande, och först ta bort nuvarande ifrån listan lol (innan lowercase)."
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='?', help="the source file for your slides")
    args = parser.parse_args()

    tk_root.withdraw() #Hide root window
    if not stdin.isatty(): #if piping the
        file_list = stdin.readlines()
        if len(file_list) == 0 or ''.join(file_list).isspace(): #Kanske kan vara kortare
            exit()
        filename = None #Fixa så inte behöver filename då
    else:
        if args.file is None:
            filename = ctk.filedialog.askopenfilename()
            if filename == (): #no file given
                exit()
        else:
            filename = args.file
            if not os.path.exists(filename):
                filename_base = os.path.basename(filename)
                filename_path = os.path.dirname(filename) #Extrahera filepath från filnamn
                if filename_path == "":
                    filename_path = getcwd()
                similar_filename = check_similar_filename(filename_base, filename_path) 
                if similar_filename != False:
                    #mer avancerat så ser ifall glömde en bokstav, kolla utan/med filändelse
                    message_exit(f"\"{filename}\": No such file or directory. Did you mean \"{similar_filename}\"?")
                else:
                    message_exit(f"\"{filename}\": No such file or directory.")

        infil = open(filename, 'r') #Öppna filen för läsning
        file_list = infil.readlines() #Spara alla rader som en lista i variabeln file_list
        infil.close() #Stäng filen

        if os.path.getsize(filename) == 0 or ''.join(file_list).isspace(): #Kanske kan vara kortare
            message_exit(f"The given file \"{filename}\" is empty.")
            #exit(f"tpt: \"{filename}\": The given file is empty.")
    
    tk_root.deiconify() #Show root window
    #tk_root.title(filename) #Använd filnamn som titeln. TODO: just nu visas hela filsökvägen, ksk ändra till bara filnamn
    return file_list, filename

def compile_slides(file_list, filename):
    file_lines = len(file_list)
    file_index = 0
    slides = [] #list of all the slides contents
    slide = [] #list of content of one slide

    def check_img_path(image_path, line):
        #TODO: för att få den att skriva "did you mean HEJ.png (istället för hej) ska söka i samma dir efter alla filer, lägga innehåll i en lista, och sedan gör allt till lowercase, så att kan jämföra. Sedan då måste jämföra med nuvarande, och först ta bort nuvarande ifrån listan lol (innan lowercase)."
        #Applicera check_similar_filename()
        nonlocal filename
        image_path = image_path[1:-1] #remove @ and newline chars
        # image_path = image_path[1:]
        # exit(list(image_path[:-1]))
        if not os.path.exists(image_path):
            #TODO: "did you mean" feature
            if filename == None:
                message_exit(f"Invalid filepath \"{image_path}\" on line {str(line)}.")
            else:
                message_exit(f"Invalid filepath \"{image_path}\" on line {str(line)} in \"{filename}\".")

    while file_index < file_lines:
        # Ta bort rader som börjar på #. Fått det att funka, men om har två comments på två rader och sedan raden efter är \n så blir \n en slide.
        # Hantera \

        # if file_list[file_index].isspace() == False and file_lines >= file_index: #Om index inte överstigit file_lines och nuvarande rad inte är whitespace:
        if file_list[file_index].isspace() == False: #Om index inte överstigit file_lines och nuvarande rad inte är whitespace:
            if file_list[file_index][0] == "#": #Om det är en kommentar så läggs den raden inte till och programmet går till nästa varv i loopen
                file_index += 1
                continue
            if file_list[file_index][0] == "@":
                check_img_path(file_list[file_index], file_index + 1)

            if file_list[file_index][0] == "*" and file_list[file_index][1] == " ":
                file_list[file_index] = file_list[file_index].replace("*", "•", 1)
            elif file_list[file_index][0] == ">" and file_list[file_index][1] == " ":
                file_list[file_index] = file_list[file_index].replace(">", "▸", 1)

            slide.append(file_list[file_index]) #slides ska ha sin egen index stegare
            file_index += 1
        elif file_list[file_index].isspace():
            if slide != []: #if it's not only been empty lines or comments
                slides.append(slide)
                slide = [] #Reset slide
            file_index += 1

    if slide != []:
        slides.append(slide)

    return slides

class PresentationState:
    marked_slide = None
    slide_index_before_marked = None #Senast innan man bytte till markerade
    slides = None
    file_list, filename = readfile() #Skapa en lista utav source filen och ge filnamn till felmeddelande vid filsökvägfel
    slides = compile_slides(file_list, filename)
    current_slide_index = 0

    last_index_before_scaled = None
    last_text_before_scaled = ""

    label_currentslide = None
    label_image_slide = None
    progbar_slidesleft = None
    image = None

    #Counter
    count = 0
    not_use_count = False

    def next_slide(self):
        if self.count != 0:
            self.current_slide_index += self.count
            self.count = 0
            if self.current_slide_index > len(self.slides) - 1 or self.current_slide_index < 0:
                self.current_slide_index = len(self.slides) - 1
            return True
        else:
            self.count = 0
            if self.current_slide_index != len(self.slides) - 1: #Gör inget om är på sista sliden. TODO: Kanske ha så att du kommer till en exit grej som i PP.
                self.current_slide_index += 1
                return True
            return False

    def prev_slide(self):
        if self.count != 0:
            self.current_slide_index -= self.count
            self.count = 0
            if self.current_slide_index > len(self.slides) - 1 or self.current_slide_index < 0:
                self.current_slide_index = 0
            return True
        else:
            if self.current_slide_index != 0: #Gör inget om är på första sliden.
                self.current_slide_index -= 1
                return True
            return False

    def current_slide(self):
        return self.slides[self.current_slide_index]

state = PresentationState()
redraw() #run the first slide

def number_wait(number): # Handle a counter like in vim.
    #TODO: show an indicator in a corner, have this as an 
    list_of_digits = list(str(state.count))
    list_of_digits.append(str(number))
    
    string = ""
    for item in list_of_digits:
        string += item
    state.count = int(string)

def zero_keybinding_condition():
    if state.count == 0:
        show_first_slide()
    else:
        number_wait(0)

def reset_counter():
    state.count = 0

def resize(event): #Skala widgets i förhållande till root-fönstrets width
    if state.label_currentslide != None:
        if state.last_index_before_scaled != state.current_slide_index:
            state.last_index_before_scaled = state.current_slide_index

            state.last_text_before_scaled = ""
            for item in state.slides[state.current_slide_index]:
                state.last_text_before_scaled += item

        if tk_root.winfo_width() > len(state.last_text_before_scaled):

            width = tk_root.winfo_width()
            height = tk_root.winfo_height()
            ratio = width / height
            # new_height = int(ratio * (0.4 * tk_root.winfo_height()))
            # new_width = int(ratio * new_height)

            label_current_size = int(
                                0.04 * (tk_root.winfo_width() - len(state.last_text_before_scaled))
                                # (0.04 * tk_root.winfo_width() + 0.02 * tk_root.winfo_height()) - len(state.last_text_before_scaled)
                                # 0.02 * (tk_root.winfo_width() + tk_root.winfo_height()) - len(state.last_text_before_scaled)
                              )
        else:
            label_current_size = int(
                                0.04 * (tk_root.winfo_width())
                              )
        state.label_currentslide.configure(font=ctk.CTkFont(
            size=label_current_size
            ))
        state.label_currentslide.pack(expand=True, fill=ctk.BOTH)
    if state.progbar_slidesleft != None:
        state.progbar_slidesleft.configure(width=int(
            0.1 * (tk_root.winfo_width() + tk_root.winfo_height())
            ))
        state.progbar_slidesleft.place(relx=0.5, rely=0.97, anchor=ctk.CENTER)
    if state.label_image_slide != None:
        pass

        # width, height = state.image.size
        # ratio = width / height

        # new_height = int(ratio * (0.4 * tk_root.winfo_height()))
        # new_width = int(ratio * new_height)

        # image_slide = ctk.CTkImage(state.image, size=(new_width, new_height))

        # state.label_image_slide = ctk.CTkLabel(tk_root, text="", image=image_slide)
        # state.label_image_slide.pack(expand=True, fill=BOTH)

#read and bind keybindings
for key in config['binds']:
    func = config['binds'][key] #the function bound to the current key
    tk_root.bind(key, eval("lambda event:" + func + "()"))

tk_root.bind(0, lambda event: zero_keybinding_condition())
#iterate through and bind numbers 1-9 to number_wait function
for current_number in range(1, 10):
    def make_lambda(x):
        return lambda event:number_wait(x)
    tk_root.bind(current_number, make_lambda(current_number))

tk_root.bind("<Configure>", lambda event: resize(event)) #Kör resize när root fönstret ändras
tk_root.mainloop()
