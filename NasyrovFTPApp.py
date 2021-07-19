import tkinter as tk
import sqlite3


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("1080x720")
        self.minsize(720, 480)
        self.config(background="#F16446")
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#F16446")
        tk.Label(self, text="FTP Data Base", font=("Arial", 40), bg="#F16446", fg="white").pack(side="top", fill="both",
                                                                                                pady=10)
        tk.Button(self, text="Add",
                  command=lambda: master.switch_frame(AddPage), font=("Arial", 25), bg="#F16446", fg="white").pack()
        tk.Button(self, text="Search",
                  command=lambda: master.switch_frame(SearchPage), font=("Arial", 25), bg="#F16446", fg="white").pack()


class AddPage(tk.Frame):
    def __init__(self, master):
        self.add_data = {"ftpServerName": tk.StringVar(), "ftpID": tk.StringVar(), "ftpPWD": tk.StringVar(),
                         "ftpDirectory": tk.StringVar(), "ftpPort": tk.StringVar(), "ftpType": tk.StringVar(),
                         }
        self.entries = []
        tk.Frame.__init__(self, master, bg="#F16446")
        tk.Label(self, text="Please fill every section below:", font=("Arial", 40), bg="#F16446").pack(side="top",
                                                                                                       fill="both",
                                                                                                       pady=10)
        for name in self.add_data.keys():
            tk.Label(self, text=name, bg="#F16446").pack()
            new = tk.Entry(self, textvariable=self.add_data[name])
            new.pack()
            self.entries.append(new)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side="bottom")
        create_button = tk.Button(self, text="Create")
        create_button.pack(side="bottom")
        create_button.bind('<Button-1>', self.press_create_button)

    def press_create_button(self, event):
        i = 0
        for entry in self.entries:
            self.add_data[list(self.add_data.keys())[i]] = entry.get()
            if self.add_data[list(self.add_data.keys())[i]] == "":
                tk.Label(self, text="Fill every field please.", font=("Arial", 40), fg="red", bg="#F16446").pack()
                break
            i += 1
        values = tuple(self.add_data.values())
        self.add_acc(ftpServerName=values[0], ftpID=values[1], ftpPWD=values[2],
                     ftpDirectory=values[3], ftpPort=values[4], ftpType=values[5])

    def add_acc(self, ftpServerName, ftpID, ftpPWD, ftpDirectory, ftpPort, ftpType):
        try:
            with sqlite3.connect("Data_base.db") as conn:
                conn.execute("INSERT INTO FTPAccounts VALUES(?,?,?,?,?,?)",
                             (ftpServerName, ftpID, ftpPWD, ftpDirectory, ftpPort, ftpType))
        except():
            tk.Label(self, text="There is an error! Check your entries!", font=("Arial", 40), fg="red",
                     bg="#F16446").pack()


class SearchPage(tk.Frame):
    def __init__(self, master):
        self.search_data = {"ftpServerName": tk.StringVar(), "ftpID": tk.StringVar(), "ftpPWD": tk.StringVar(),
                            "ftpDirectory": tk.StringVar(), "ftpPort": tk.StringVar(), "ftpType": tk.StringVar(),
                            }
        self.entries = []
        tk.Frame.__init__(self, master, bg="#F16446")
        tk.Label(self, text="Enter search information:", bg="#F16446").pack(side="top", fill="x", pady=10)
        for name in self.search_data.keys():
            tk.Label(self, text=name, bg="#F16446").pack()
            new = tk.Entry(self, textvariable=self.search_data[name])
            new.pack()
            self.entries.append(new)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        search_button = tk.Button(self, text="Search")
        search_button.pack(side="bottom")
        search_button.bind('<Button-1>', self.click_search_button)

    def click_search_button(self, event):
        i = 0
        for entry in self.entries:
            self.search_data[list(self.search_data.keys())[i]] = entry.get()
            if self.search_data[list(self.search_data.keys())[i]] == '':
                self.search_data.pop(list(self.search_data.keys())[i])
                i -= 1
            i += 1
        # values = tuple(self.search_data.values())
        self.search_acc(self.search_data)
        self.search_data = {"ftpServerName": tk.StringVar(), "ftpID": tk.StringVar(), "ftpPWD": tk.StringVar(),
                            "ftpDirectory": tk.StringVar(), "ftpPort": tk.StringVar(), "ftpType": tk.StringVar(),
                            }

    def search_acc(self, information):
        try:
            comm = ""
            for key, value in information.items():
                comm = comm + key + '=' + "'" + value + "'" + " AND "
            comm = comm[:-5]
            with sqlite3.connect("Data_base.db") as conn:
                cur = conn.cursor()
                cur.execute(f"""SELECT ftpServerName, ftpID, ftpPWD, ftpDirectory, ftpPort, ftpType 
                            FROM FTPAccounts 
                            WHERE """ + comm)
                print(cur.fetchone())
        except(AttributeError, EOFError, TypeError):
            tk.Label(self, text="There is an error! Check your entries!", font=("Arial", 40), fg="red",
                     bg="#F16446").pack()


if __name__ == "__main__":
    with sqlite3.connect("Data_base.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS "FTPAccounts" (
                            "ftpServerName"	TEXT NOT NULL,
                            "ftpID"	TEXT,
                            "ftpPWD"	TEXT,
                            "ftpDirectory"	TEXT,
                            "ftpPort"	INTEGER DEFAULT 21,
                            "ftpType"	TEXT,
                            PRIMARY KEY("ftpServerName"))""")
    app = SampleApp()
    app.mainloop()
