import tkinter as tk
import subprocess
import threading
import datetime
import time
from tkinter import ttk
import konsolowa as k  # Zaimportuj odpowiedni moduł


bm = k.BatteryUsageReader('C:\\Users\\janax\\OneDrive\\Pulpit\\SM\\final version\\sm\\bm_argument.bat', "xiomi", "link to backend", 5)

def read_phone_power():
    cpu_power= 3.993+5.06+4.4
    #odczytac dane o procesorze z apliakcji od michala, ona zapisuje w pobranych data.txt
    return cpu_power
def thread(script_path, device_id, process_name):
    global stop_thread
    while not stop_thread:
        print("wartosc thread: ", stop_thread)
        result = subprocess.run([script_path, device_id, process_name], capture_output=True, text=True)
        data = result.stdout.split("\n")
        cpu_usage = 0
        for d in data:
            if device_id in d:
                cpu_usage = float(d.split(" ")[4])
        print("cpu usage: ", cpu_usage)
        print("Zuzycie energi: ", (cpu_usage / 100) * read_phone_power(), "mA")
        date = datetime.datetime.now()
        bm.send_data("https://battery-metter-backend.azurewebsites.net/api/measurement/add/", date, device_id, cpu_usage)
        time.sleep(5)
    
    print("Pomiar zakonczony")
    #stop_thread_func()

def start_thread():
    global bat_thread
    global stop_thread
    print("urucham pomiary watek")
    stop_thread = False
    bat_thread = threading.Thread(target=thread, args=("C:\\Users\\janax\\OneDrive\\Pulpit\\SM\\final version\\sm\\bm_argument.bat", combobox1.get(), combobox.get()))
    bat_thread.start()  # Start wątku uruchamiającego plik .bat

def stop_thread_func():
    global stop_thread
    global bat_thread
    print("zakoncz pomiary watek")
    stop_thread = True  # Ustawienie flagi na True zatrzyma pętlę w funkcji thread
    if bat_thread is not None:
        bat_thread.join()  # Czekamy na zakończenie wątku
        bat_thread = None

        
# Załóżmy, że konsolowa.BatteryUsageReader jest prawidłowo zaimplementowane
#zmienic siezki


# Tworzenie głównego okna
root = tk.Tk()
root.title("BM")
process= None

label = tk.Label(root, text="Battery Matter")
label.pack(pady=10)




def update_combobox1(event):
    current_device = combobox.get()
    options1 = bm.show_installed_apps(current_device)
    print(options1)
    combobox1['values'] = options1
    if options1: 
        combobox1.current(0)
    else:
        combobox1.set('')



def b_start_measurement():
    global process
    text = f"Wprowadzono: , Wybrano urządzenie: {combobox.get()}, Aplikację: {combobox1.get()}"
    label.config(text=text)
    print("Rozpoczęcie pomiaru dla:", combobox1.get())
    bm.run("C:\\Users\\janax\\OneDrive\\Pulpit\\SM\\final version\\sm\\bm_argument.bat", combobox1.get(), combobox.get())
    #process = subprocess.Popen(["C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat", combobox1.get(), combobox.get()])

def b_stop_measurement():
    global process
    print("zakoncz pomiar")

options = bm.show_devices()
combobox = ttk.Combobox(root, values=options, width=90)
combobox.current(0)
combobox.pack(pady=10)
combobox.bind('<<ComboboxSelected>>', update_combobox1)  


combobox1 = ttk.Combobox(root, width=90)
combobox1.pack(pady=10)
update_combobox1(None)  


button = tk.Button(root, text="Rozpocznij pomiary", command=start_thread)
button.pack(pady=10)

button2 = tk.Button(root, text="Zakończ pomiary", command=stop_thread_func)
button2.pack(pady=10)

print("siemma")
options1 = bm.show_installed_apps("ZY22H23QP4")
print(options1)


root.mainloop()
