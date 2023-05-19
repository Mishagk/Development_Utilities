import json
import requests
import time
import numpy as np

# Crear endpoint para invocar modelo ML
http_host = "http://34.122.24.252"
port = 8007
url = http_host + ":" + str(port) + "/model"
print(url)

request_data = json.dumps({'age': 40, 'salary': 20000})
response = requests.post(url, request_data)
print("URL :: ", response.text)

# Initial values
age = 40
salary = 100

start_time = time.time()
num_pred = 200

for i in range(num_pred):
    request_data = json.dumps({'age': age, 'salary': salary})
    response = requests.post(url, request_data)
    print('[i=,', i, '],Input > age:', age, ' ; salary:', salary, ' ::: output:', response.text)

    # Update values
    age = age + i*0.2
    salary = salary + i*20

end_time = time.time()
tiempo_seg = (end_time - start_time)/1.0  # ya esta en segundos
print("Tiempo ejecucion de ", num_pred, " ejecuciones fue de ", np.round(tiempo_seg, 2)," [seg]")
print(" ------ Fin ------")
