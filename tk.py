import tkinter as tk
from tkinter import ttk
import konsolowa as k  # Zaimportuj odpowiedni moduł

# Załóżmy, że konsolowa.BatteryUsageReader jest prawidłowo zaimplementowane
bm = k.BatteryUsageReader('C:\\Users\\janax\\OneDrive\\Pulpit\\SM\\kod\\sm\\bm_argument.bat', "xiomi", "link to backend", 5)

# Tworzenie głównego okna
root = tk.Tk()
root.title("BM")

label = tk.Label(root, text="Battery Matter")
label.pack(pady=10)




def update_combobox1(event):
    current_device = combobox.get()
    options1 = bm.show_installed_apps(current_device)
    combobox1['values'] = options1
    if options1: 
        combobox1.current(0)
    else:
        combobox1.set('')

options = bm.show_devices()
combobox = ttk.Combobox(root, values=options, width=90)
combobox.current(0)
combobox.pack(pady=10)
combobox.bind('<<ComboboxSelected>>', update_combobox1)  


combobox1 = ttk.Combobox(root, width=90)
combobox1.pack(pady=10)
update_combobox1(None)  


def b_start_measurement():
    text = f"Wprowadzono: , Wybrano urządzenie: {combobox.get()}, Aplikację: {combobox1.get()}"
    label.config(text=text)
    print("Rozpoczęcie pomiaru dla:", combobox1.get())
    bm.run("C:\\Users\\janax\\OneDrive\\Pulpit\\SM\\kod\\sm\\bm_argument.bat", combobox1.get(), combobox.get())

button = tk.Button(root, text="Rozpocznij pomiary", command=b_start_measurement)
button.pack(pady=10)

root.mainloop()
