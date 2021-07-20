# import sqlite3
#
# from ftplib import FTP
# from tkinter import *
#
#
# def add_acc(ftpServerName, ftpID, ftpPWD, ftpDirectory, ftpPort, ftpType):
#     with sqlite3.connect("Data_base.db") as conn:
#         conn.execute("INSERT INTO Accounts VALUES(?,?,?,?,?,?)",
#                      (ftpServerName, ftpID, ftpPWD, ftpDirectory, ftpPort, ftpType))
#
#
# def search_acc(ftpServerName, ftpID):
#     with sqlite3.connect("Data_base.db") as conn:
#         cur = conn.cursor()
#         cur.execute(f"""SELECT ftpServerName, ftpID
#                     FROM Accounts
#                     WHERE ftpServerName = '{ftpServerName}' AND ftpID = '{ftpID}' """)
#         print(cur.fetchone())
#
#
# # def check(name, password):
# #     with FTP("ftp.files.com") as ftp:
# #         try:
# #             ftp.login(user=name, passwd=password)
# #             ftp.dir()
# #         except:
# #             print("HUINYA")
#
#
# def add():
#     frame1.destroy()
#     frame = Frame(window)
#     add_ftpServerName = Entry(frame)
#     add_ftpID = Entry(frame)
#     add_ftpPWD = Entry(frame)
#     add_ftpDirectory = Entry(frame)
#     add_ftpPort = Entry(frame)
#     add_ftpType = Entry(frame)
#     add_ftpServerName_content = StringVar()
#     add_ftpID_content = StringVar()
#     add_ftpPWD_content = StringVar()
#     add_ftpDirectory_content = StringVar()
#     add_ftpPort_content = StringVar()
#     add_ftpType_content = StringVar()
#
#     frame.pack()
#
#
# def search():
#     frame1.destroy()
#
#     # search_server.pack(side=LEFT)
#     # search_server_content = tkinter.StringVar()
#
#
# def manage():
#     frame1.destroy()
#
#
#
# if __name__ == "__main__":
#     window = Tk()
#     window.title("FTP Data Base")
#     window.geometry("1080x720")
#     window.minsize(720, 480)
#     window.config(background="#F16446")
#
#     # frame creation
#     frame1 = Frame(window, bg="#F16446")
#
#     # labels creation
#     label_title = Label(frame1, text="FTP Data Base", font=("Arial", 40), bg="#F16446", fg="white")
#     label_title.pack(expand=YES)
#
#     button_search = Button(frame1, text="Search", font=("Arial", 25), command=
#     search, bg="#F16446", fg="white")
#     button_search.pack(side=LEFT)
#
#     button_add = Button(frame1, text="Add", font=("Arial", 25), command=
#     add(), bg="#F16446", fg="white")
#     button_add.pack(side=LEFT)
#
#     button_manage = Button(frame1, text="Manage", font=("Arial", 25), command=
#     manage, bg="#F16446", fg="white")
#     button_manage.pack(side=LEFT)
#
#     frame1.pack(expand=YES)
#
#     search_server = Entry(frame1)
#     search_server.pack(side=LEFT)
#     search_server_content = StringVar()
#
#     search_server["textvariable"] = search_server_content
#     search_server.bind('<Key-Return>', print(search_server_content))
#
#     # add_server["textvariable"] = add_server_content
#     # add_server
#
#     window.mainloop()
#
add_data = {"ftpServerName": "ftpServerName", "ftpID": "ftpServerName", "ftpPWD": "ftpServerName",
            "ftpDirectory": "ftpServerName", "ftpPort": "ftpServerName", "ftpType": "ftpServerName"
            }
for key, value in add_data.items():
    print(key + '=' + value, sep=' AND ')
