import subprocess
import time
import datetime
import requests


script_path = 'C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat'
#process_name = 'com.tinder'

class BatteryUsageReader:

    def __init__(self, script_path, phone_model, backend_link, frequency):
        self.script_path= script_path
        self.phone_model= phone_model
        self.backend_link= backend_link
        self.frequency= frequency
        self.mesurments= {}

    def show_installed_apps(self, device_id):
        result = subprocess.run(["C:\\Users\\PC\\Desktop\\adb\\show_installed_apps.bat", device_id], capture_output=True, text=True)
        data= result.stdout.split("\n")
        cleaned_data= []
        for line in data:
            cleaned_data.append(line.split(":")[-1])

        print(cleaned_data)
        return cleaned_data

    def show_devices(self):
        try:
            result = subprocess.run(["C:\\Users\\PC\\Desktop\\adb\\show_devices.bat"], capture_output=True, text=True)
            data= result.stdout.split("\n")

            cleaned_data= []
            for line in data[1:]:
                cleaned_data.append(line.split("\t", 1)[0])
                if len(line) <=3:
                    continue
            return cleaned_data

        except Exception as e:
            print("Error:", e)

    def _read_cpu_usage(self, script_path, process_name, device_id):
        try:
            result = subprocess.run([script_path, process_name, device_id], capture_output=True, text=True)
            data= result.stdout.split("\n")
            print("data: ", data)
            odp= ""
            for i, line in enumerate(data):
                if process_name in line:
                    odp= data[i]
            if odp == "":
                cpu_usage= 0
            else:
                print("Output:\n", odp)
                cpu_usage= str(data).split(" ")[4]
            print("cpu: ", cpu_usage)
            date= datetime.datetime.now()
          
            mesurment= float(cpu_usage)/100 * (4+5+4) #odczyatc dane z pliku
    
            self.send_data("https://battery-metter-backend.azurewebsites.net/api/measurement/add/", date, process_name, mesurment)

          

            return odp

        except Exception as e:
            print("Error:", e)

    def compute_battery_usage(self):
        battery_usage= 0
        return battery_usage
    
    def send_data(self, url, date, package_name, mesurment):
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "application_name": package_name,
            "measurement_date": str(date),
            "energy_consumption": mesurment
        }

        response = requests.post(url, json=data, headers=headers)
        print(response)
    
    def run(self, script_path,package_name, device_id):
        while True:
            self._read_cpu_usage(script_path, package_name, device_id)
            time.sleep(self.frequency)
            
bm= BatteryUsageReader('C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat', "xiomi", "link to backend", 5) 
bm.show_installed_apps("ZY22H23QP4")



