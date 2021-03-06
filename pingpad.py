import tkinter as tk#for importing tkinter!
from tkinter import filedialog#like a file explorer
from tkinter import messagebox#now we need a message box
class Menubar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 9)#font
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)
        file_dropdown = tk.Menu(menubar)
        #here u can change the labels probably for forks or mods for this text editor (yes mods on a text editor its weird but good)
        file_dropdown.add_command(label="New file", accelerator="Ctrl+N", command=parent.new_file)
        file_dropdown.add_command(label="Open file", accelerator="Ctrl+O", command=parent.open_file)
        file_dropdown.add_command(label="Save current file", accelerator="Ctrl+S", command=parent.save)
        file_dropdown.add_command(label="Save as...", accelerator="Ctrl+Shift+S", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Quit pingpad", command=parent.master.destroy)
        help_dropdown = tk.Menu(menubar, font=font_specs)
        help_dropdown.add_command(label="Release notes", command=self.show_release_notes)
        help_dropdown.add_separator()
        help_dropdown.add_command(label="About", command=self.show_about_message)
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="Help", menu=help_dropdown)
    def show_about_message(self):
        box_title = "About pingpad"
        box_message = "Version 0.1"
        messagebox.showinfo(box_title, box_message)
    def show_release_notes(self):
        box_title = "Release notes"
        box_message = "Inital release"
        messagebox.showinfo(box_title, box_message)
class StatusBar:
    def __init__(self, parent):
        font_specs = ("ubuntu", 12)
        self.status = tk.StringVar()
        self.status.set("PingPad - 0.1")#version
        label = tk.Label(parent.textarea, textvariable=self.status, fg="black", 
                        bg="grey", anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)
    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Saved current file!")
        else:
            self.status.set("PingPad - 0.1")#the status is the bottom grey thing
class PingPad:
    def __init__(self, master):#init method
        master.title("Untitled - PingPad")#normally thats how it would be BUT if we open a file then Untitled will change to the file path for example my text document is in E:\ImportantDocuments\sometext.txt it would look like this E:/ImportantDocuments/sometext.txt
        master.geometry("1280x720")#resolution
        font_specs = ("ubuntu", 18)#font and no this was not made on ubuntu it was made on windows but the ubuntu fonts look so good the 18 is the font size
        self.master = master
        self.filename = None
        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.menubar = Menubar(self)
        self.statusbar = StatusBar(self)
        self.bind_shortcuts()
    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - PingPad")#here is where we implement the method where it would change the name based off of where the file is
        else:
            self.master.title("Untitled - PingPad")#but if there is no files opened or nothing is saved yet it would say untitled
    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            #here u can change the file types
            filetypes=[("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Markdown Documents", "*.md"),
            ("Python Scripts", "*.py"),
            ("Javascript Files", "*.js"),
            ("CSS Documents", "*.css"),
            ("HTML Documents", "*.html"),
            ("Java Files", "*.java")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)#deletes everything except the top bar
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()
    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
            initialfile="Untitled.txt",
            defaultextension=".txt",
            #kinda the same thing as open_file but whatever
            #here u can add new file types!
                filetypes=[("All Files", "*.*"),
                           ("Text Documents", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css"),
	            ("Data Files", "*.dat")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:#the exception e part is just for errors and stuff u can comment this line out
            print(e)
    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)#the thing is the user will be pressing control+shift+s and then that will make the s uppercase
        self.textarea.bind('<Key>', self.statusbar.update_status)
if __name__ == "__main__":#basically if the name of the window is unloaded (which is what python does when the window closes)
    master = tk.Tk()#we will tell tk to handle all of this junk
    pt = PingPad(master)#switch to master
    master.mainloop()#kill off the main loop cuz the main loop runs the program so we are basically making an error on purpose XD





