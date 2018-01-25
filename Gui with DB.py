import tkinter,pymongo
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['mycustomers']
collection = database['customers']
root = tkinter.Tk()
label1 = tkinter.Label(root,text="Name")
label2 = tkinter.Label(root,text="Last Name")
e1 = tkinter.Entry(root)
e2 = tkinter.Entry(root)


def entering_into_db():
    name = e1.get()
    last_name = e2.get()
    if name is not '':
        if last_name is not '':
            collection.insert({label1.cget("text"):name,label2.cget("text"):last_name})
            print("data inserted")
        else:
            print("enter the Last Name")
    else:
            print("enter the Name")


label1.grid(row=0)
label2.grid(row=1)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
but= tkinter.Button(root,text="add",command=entering_into_db)
but.grid(row=2,column=1)
root.mainloop()

