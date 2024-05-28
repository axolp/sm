import tkinter as tk
import subprocess
import threading
import datetime
import time
from tkinter import ttk
import konsolowa as k  # Zaimportuj odpowiedni moduł


bm = k.BatteryUsageReader('C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat', "xiomi", "link to backend", 5)

def read_phone_power():
    cpu_power= 3.993+5.06+4.4
    #odczytac dane o procesorze z apliakcji od michala, ona zapisuje w pobranych data.txt
    return cpu_power
    
def thread(script_path, device_id, process_name):
    global stop_thread
    stop_thread= False
    while True:
        print("wartosc thread: ", stop_thread)
        if stop_thread:
            print("Pomiar zakonczony")
            stop_thread()
        else:
            result= subprocess.run([script_path, device_id, process_name], capture_output=True, text=True)
            #print("result: , ")

        #print(result.stdout)
        data= result.stdout.split("\n")
        cpu_usage= 0
        #process name jest zamieniony z device id
        for d in data:
            if device_id in d:
                cpu_usage= float(d.split(" ")[4])
        print("cpu usage: ", cpu_usage)
        print("Zuzycie energi: ", (cpu_usage/100)*read_phone_power(), "mA")
        date= datetime.datetime.now()
        #przekazuje device id bo to process name xd
        bm.send_data("https://battery-metter-backend.azurewebsites.net/api/measurement/add/", date, device_id, cpu_usage)
        time.sleep(5)

def start_thred():
    global bat_thread
    print("urucham pomiary watek")
    bat_thread = threading.Thread(target=thread, args=("C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat", combobox1.get(), combobox.get()))
    bat_thread.start()  # Start wątku uruchamiającego plik .bat
    

def stop_thread():
    global stop_thread
    global bat_thread
    print("zakoncz pomiary watek")
    stop_thread = True  # Ustawienie flagi na True zatrzyma pętlę w funkcji run_bat_file_continuously
    bat_thread.join()  # Czekamy na zakończenie wątku

        
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
    bm.run("C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat", combobox1.get(), combobox.get())
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


button = tk.Button(root, text="Rozpocznij pomiary", command=start_thred)
button.pack(pady=10)

button2 = tk.Button(root, text="Zakończ pomiary", command=stop_thread)
button2.pack(pady=10)

root.mainloop()
