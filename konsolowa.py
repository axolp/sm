import subprocess
import time
#import request


script_path = 'C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat'
#process_name = 'com.tinder'

class BatteryUsageReader:

    def __init__(self, script_path, phone_model, backend_link, frequency):
        self.script_path= script_path
        self.phone_model= phone_model
        self.backend_link= backend_link
        self.frequency= frequency
        self.mesurments= {}

    def show_installed_apps(self):
        data= ""
        print(data)

    def _read_cpu_usage(self, script_path, process_name):
        try:
            result = subprocess.run([script_path, process_name], capture_output=True, text=True)
            data= result.stdout.split("\n")
            for i, line in enumerate(data):
                if process_name in line:
                    odp= data[i]
                print("Output:\n", odp)

        except Exception as e:
            print("Error:", e)

    def compute_battery_usage(self):
        battery_usage= 0
        return battery_usage
    
    def send_data(self):
        flag= False
        response= request.post(url, json=data)
        if response.status_code == 200:
            print("Sukces:", response.json())
            flag= True
        else:
            print("Błąd:", response.status_code, response.text)
            flag= False
        return flag
    
    def run(self):
        while True:
            self._read_cpu_usage(self.script_path, 'com.tinder' )
            time.sleep(self.frequency)
            
bm= BatteryUsageReader('C:\\Users\\PC\\Desktop\\adb\\bm_argument.bat', "xiomi", "link to backend", 5) 
bm.run()



