#### This is developed by Gopal rgkrishnas@gmail.com for the main program mqtt_publish.py

DEVICE_ID='0001'
# Define the delay  time
delay_time = 5
# MQTT Host name or IP address with tcp
broker_address= 'localhost'
port = 1883  # MQTT port number
user = ''  # MQTT user id if available
password = '' # MQTT password if available
topic = 'iot2tangle'  # MQTT message topic 
water_measurements='liters'  # liters/gallons
water_dept_wallet_address = 'EnterAddressTowhomWalletMachineNeedsToPay' # to who the system needs to make the payment
mywatersensor_seed='EnterYourWaterSensorwalletSeed'
