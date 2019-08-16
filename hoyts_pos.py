from tkinter import *
import tkinter.font as font
from functools import partial

root = Tk()
root.title("Book Tickets")
root.geometry('1200x700')
root.configure(background='#ccccdc')

class Movie:
    """ Movies will have a name, theatre, capacity, price, and length. """

    def __init__(self, length, name, theatre):
        """ init function. """

        self._length = length
        self._name = name
        self._theatre = theatre
        for t in theatres:
            if t.get_name() == theatre:
                self._available = t.get_capacity()
                self._price = t.get_price()
        movies.append(self)

    def ticket_confirmed(self):
        """ Reduces the number of available tickets by one. """
        self._available -= 1

    def get_length(self):
        return self._length

    def get_name(self):
        return self._name

    def get_available(self):
        return self._available

    def get_theatre(self):
        return self._theatre

    def get_price(self):
        return self._price


class Theatre:
    """ This has a name + capacity, as well as the price they charge. """

    def __init__(self, name, capacity, price):

        self._name = name
        self._capacity = capacity
        self._price = price
        theatres.append(self)

    def get_name(self):
        return self._name

    def get_capacity(self):
        return self._capacity

    def get_price(self):
        return self._price


class Tickets:
    """ They have a price. """

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

movies = []
theatres = []
tickets = []
in_this_theatre = []
Theatre("Mann Theatre", 80, 15)
Theatre("The Academy", 120, 15)
Theatre("Green Fern Cinema", 200, 15)
Movie(120, "Something about unicorns", "Mann Theatre")
Movie(117, "Booksmart", "The Academy")
Movie(115, "Kid's movie", "Mann Theatre")
Movie(109, "Palm Beach", "Mann Theatre")
Movie(135, "Dog Movie", "The Academy")
Movie(220, "Fast and Furious", "Green Fern Cinema")
Movie(97, "Yesterday", "Green Fern Cinema")


def add_ticket(theatre):
    in_this_theatre.clear()
    for m in movies:
        if m.get_theatre() == theatre:
            in_this_theatre.append(m)

    if theatre == "Mann Theatre":
        for x in listbox1.curselection():
            newticket = in_this_theatre[x]
            tickets.append(newticket)
        update_summary()

    elif theatre == "The Academy":
        for x in listbox2.curselection():
            newticket = in_this_theatre[x]
            tickets.append(newticket)
        update_summary()

    elif theatre == "Green Fern Cinema":
        for x in listbox3.curselection():
            newticket = in_this_theatre[x]
            tickets.append(newticket)
        update_summary()


def update_summary():
    summary_listbox.delete(0, END)
    for item in tickets:
        detail = item.get_name() + " x1  $" + str(m.get_price())
        summary_listbox.insert(END, detail)


def clear_order():
    summary_listbox.delete(0, END)


def update_movies():
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    listbox3.delete(0, END)
    for m in movies:
        if m.get_theatre() == "Mann Theatre":
            info = " " + m.get_name() + " (" + str(m.get_available()) + " seats available)  $" + str(m.get_price())
            listbox1.insert(END, info)
        elif m.get_theatre() == "The Academy":
            info = " " + m.get_name() + " (" + str(m.get_available()) + " seats available)  $" + str(m.get_price())
            listbox2.insert(END, info)
        elif m.get_theatre() == "Green Fern Cinema":
            info = " " + m.get_name() + " (" + str(m.get_available()) + " seats available)  $" + str(m.get_price())
            listbox3.insert(END, info)


def confirm_order():
    for l in tickets:
        l.ticket_confirmed()
    tickets.clear()
    summary_listbox.delete(0, END)
    update_movies()


def create_window():
    global window
    window = Toplevel()
    window.title("Admin")
    window.geometry('1200x700')
    window.configure(background="#ccccdc")

    title_txt = font.Font(size=50)
    admin_lbl = Label(window, bg="#eeeeef", text="Admin", width=10)
    admin_lbl['font'] = title_txt
    admin_lbl.place(x=425, y=50)

    display = Listbox(window, width=50, height=6)
    display.place(x=375, y=200)
    for x in movies:
        info = "       " + x.get_name() + "  " + x.get_theatre()
        display.insert(0, info)

    add_frame = Frame(window, height=250, width=400, bg="#ffffff").place(x=150, y=350)

    delete_frame = Frame(window, height=250, width=400, bg='#ffffff').place(x=650, y=350)

    def add_movie():
        Movie(new_length.get(), new_name.get(), selected_theatre.get())
        update_movies()
        update_listbox()

    def select_theatre():
        selected.set(selected_theatre.get())

    theatre_s = []
    for t in theatres:
        theatre_s.append(t.get_name())
    selected_theatre = StringVar()
    selected_theatre.set(theatres[0].get_name())
    theatre_select = OptionMenu(window, selected_theatre, *theatre_s)
    theatre_select.place(x=150, y=350)


    new_name = StringVar()
    new_length = IntVar()
    new_movie_name = Entry(window, textvariable=new_name).place(x=150, y=400)
    new_movie_length = Entry(window, textvariable=new_length).place(x=150, y=425)

    add_btn = Button(window, text="Add New Movie", command=add_movie).place(x=150, y=450)

    movie_box = Listbox(window, selectmode=MULTIPLE)
    movie_box.place(x=655, y=370)
    for x in movies:
        movie_box.insert(END, x.get_name())

    def delete_movie():
        for i in movie_box.curselection():
            del movies[i]
        update_movies()
        update_listbox()

    def update_listbox():
        movie_box.delete(0, END)
        display.delete(0, END)
        for x in movies:
            movie_box.insert(END, x.get_name())
            info = "       " + x.get_name() + "  " + x.get_theatre()
            display.insert(0, info)

    del_btn = Button(window, text="Delete Movie", command=delete_movie)
    del_btn.place(x=655, y=550)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

top_padding = Frame(root, bg="#ccccdc", height=10, width=0).grid(row=4, column=0, sticky="n")

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ---------------------  TOP TABS --------------------------

top_left_frame = Frame(root, bg="#ccccdc", height=60, width=40).grid(row=5, column=1)



space_frame = Frame(root, bg="#ccccdc", height=700, width=20).grid(row=5, column=3, rowspan=30)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# -------------------- TOP TAB BUTTONS ---------------------

tab_name = font.Font(size=20)
movie_tab = Label(root, text="Tickets", bg="#feeebb", height=2, width=50)
movie_tab['font'] = tab_name
movie_tab.grid(row=5, column=2, columnspan=2)

admin_tab = Button(root, text="Admin", bg="#feeebb", command=create_window, height=2, width=20)
admin_tab['font'] = tab_name
admin_tab.grid(row=5, column=4, sticky=E)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ----------------  THEATRE + MOVIE SELECTION --------------

content_padding = Frame(root, bg="#ccccdc", height=30, width=600).grid(row=6, column=1, columnspan=6)
cinema_1_frame = Frame(root, bg="#eeeeef", height=150, width=400).grid(row=7, column=2, sticky="nw")

content_padding_2 = Frame(root, bg="#ccccdc", height=30, width=600).grid(row=8, column=1, columnspan=6)
cinema_2_frame = Frame(root, bg="#eeeeef", height=150, width=400).grid(row=9, column=2, sticky="nw")

content_padding_3 = Frame(root, bg="#ccccdc", height=30, width=600).grid(row=10, column=1, columnspan=6)
cinema_3_frame = Frame(root, bg="#eeeeef", height=150, width=400).grid(row=11, column=2, sticky="nw")

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ----------------  CINEMA NAME LABELS ---------------------

cinema_name = font.Font(size=30)

cinema_1_name = Label(cinema_1_frame, text="Mann Theatre", bg="#eeeeef")
cinema_1_name['font'] = cinema_name
cinema_1_name.grid(row=7, column=2, sticky=NW)

cinema_2_name = Label(cinema_2_frame, text="The Academy", bg="#eeeeef")
cinema_2_name['font'] = cinema_name
cinema_2_name.grid(row=9, column=2, sticky=NW)

cinema_3_name = Label(cinema_3_frame, text="Green Fern Cinema", bg="#eeeeef")
cinema_3_name['font'] = cinema_name
cinema_3_name.grid(row=11, column=2, sticky=NW)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# -------------- AVAILABLE MOVIE SELECTIONS ----------------

listbox1 = Listbox(cinema_1_frame, selectmode=SINGLE, yscrollcommand=(1, UNITS))
listbox1.config(height=5, width=43)
listbox1.place(x=45, y=165)

for m in movies:
    if m.get_theatre() == "Mann Theatre":
        info = " " + m.get_name() + " (" + str(m.get_available()) + " seats available)  $" + str(m.get_price())
        listbox1.insert(END, info)

listbox2 = Listbox(cinema_2_frame, selectmode=SINGLE, yscrollcommand=(1, UNITS))
listbox2.config(height=5, width=43)
listbox2.place(x=45, y=352)

for m in movies:
    if m.get_theatre() == "The Academy":
        info = " " + m.get_name() + " (" + str(m.get_available()) + " seats available)  $" + str(m.get_price())
        listbox2.insert(END, info)

listbox3 = Listbox(cinema_3_frame, selectmode=SINGLE, yscrollcommand=(1, UNITS))
listbox3.config(height=5, width=43)
listbox3.place(x=45, y=540)

for m in movies:
    if m.get_theatre() == "Green Fern Cinema":
        info = " " + m.get_name() + " (" + str(m.get_available()) + " seats available)  $" + str(m.get_price())
        listbox3.insert(END, info)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# --------------- ADD TICKET BUTTONS -----------------------

btn_txt = font.Font(size=50)

add_ticket_btn_1 = Button(root, text="+1", command=partial(add_ticket, "Mann Theatre"))
add_ticket_btn_1['font'] = btn_txt
add_ticket_btn_1.grid(row=7, column=2, sticky=E)

add_ticket_btn_2 = Button(root, text="+1", command=partial(add_ticket, "The Academy"))
add_ticket_btn_2['font'] = btn_txt
add_ticket_btn_2.grid(row=9, column=2, sticky=E)

add_ticket_btn_3 = Button(root, text="+1", command=partial(add_ticket, "Green Fern Cinema"))
add_ticket_btn_3['font'] = btn_txt
add_ticket_btn_3.grid(row=11, column=2, sticky=E)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# -------------- ORDER SUMMARY FRAMES ----------------------

order_summary_window = Frame(root, bg="#eeeeef", height=525, width=400)\
    .grid(row=6, column=4, columnspan=2, rowspan=7, sticky="s")
summary = Frame(order_summary_window, bg="white", height=320, width=375).grid(row=7, column=4, rowspan=4)
confirm_and_info = Frame(order_summary_window, bg="white", height=130, width=375).grid(row=11, column=4)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# --------------- CONFIRM AND DEL --------------------------
clr_btn = Button(confirm_and_info, text="Clear", command=clear_order)
clr_btn['font'] = btn_txt
clr_btn.place(x=710, y=525)


conf_btn = Button(confirm_and_info, text="Confirm", command=partial(confirm_order))
conf_btn['font'] = btn_txt
conf_btn.place(x=870, y=525)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# --------------- SUMMARY LISTBOX --------------------------

summary_listbox = Listbox(summary, selectmode=SINGLE, height=18, width=40)
summary_listbox.grid(row=7, column=4, rowspan=4)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––





root.mainloop()