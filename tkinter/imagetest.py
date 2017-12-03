import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="giphy.gif")


#example 1


wl = tk.Label(root, image=logo).pack(side = "right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root,
			justify=tk.LEFT,
			padx = 10,
			text = explanation).pack(side = "left")

root.mainloop()

#example 2

'''
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w = tk.Label(root,
			compound = tk.CENTER,
			text = explanation,
			image = logo).pack(side = "right")


root.mainloop()
'''