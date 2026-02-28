MOIS = ["Septembre","Octobre","Novembre","Decembre",
        "Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout"]
TYPE = ["Droit","Ecolage"]
SESSION_1 = ["Matin","Après-Midi"]
SESSION_2 = ["7:30","10:30","13:30","16:30"]
DROIT = 500000
ECOLAGE = {"prescolaire":31000,"primaire":30000,"secondaire":32000}



from sqlalchemy.inspection import inspect

def to_dict(obj, exclude=[]):
    data = {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs if c.key not in exclude}
    return data

import tkinter as tk
def show_window(text):
    root = tk.Tk()
    root.title("Test Tkinter")
    root.geometry("600x150")

    label = tk.Label(
        root,
        text=text,
        font=("Arial", 20)
    )

    label.pack(expand=True)

    root.mainloop()

