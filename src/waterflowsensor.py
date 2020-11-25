#!/usr/bin/env python

#### Developed by Gopal rgkrishnas@gmail.com 
#### Collect the water consumption data from a sensor into edge device.
#### This program is developed to publish the data into IOTA-Streams through MQTT gateway.

#### Prerequisite Stream-mqtt-gateway needs to be install and configure with mqtt broker.
#### Hardware Pi and Water Flow Sensor (model YF-S201)
#### Water Flow Sensor to Pi wiring connection
   # Red wire to Pi 5V
   # Black wire to Pi GND
   # Yellow wire to Pi GPIO23
#### Currently 1i is defined for 1 liter of water (just for PoC), we will continue to enhance in further for gallons as well as the whole consumption logic.
   
import paho.mqtt.client as mqttClient
import time
import config
import json
import RPi.GPIO as GPIO
import time, sys
import iota_payment_transfer

FLOW_SENSOR = 23  # Water Flow Sensor GPIO pin number 

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global water_flow_frequency
water_flow_frequency = 0
total_litters=0
total_litters_sum=0
total_litters_sum_min=0
is_contineous_flow=0
water_measurements = config.water_measurements;

currentTime = int(round(time.time() * 1000))
count_loopTime = currentTime

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
        print("Connected to MQTT Broker")
        global Connected               
        Connected = True                
    else:
        print("Connection to the MQTT Broker failed")
 
client = mqttClient.Client("WaterFlowSensor_"+str(time.time()))              
client.username_pw_set(config.user, password=config.password)   
client.on_connect= on_connect                    
client.connect(config.broker_address, port=config.port)          
 
client.loop_start()      

def countPulse(channel):
   global water_flow_frequency
   water_flow_frequency = water_flow_frequency+1

#GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

### The below function will publish the data into MQTT for I2T through "streams-mqtt-gateway" module
def publish2mq(value):
    #e.g. value ='{ "iot2tangle": [ { "sensor": "waterconsumed", "data": ["10 liters"] } ], "device": "DEVICE_ID_1", "timestamp": '+str(time.time())+' }'
    client.publish(config.topic,value)
while True:
    try:
        currentTime = int(round(time.time() * 1000))
        # Every second, calculate and print litres/hour
        if(currentTime >= (count_loopTime + 1000)):
            count_loopTime = currentTime; # Updating count_loopTime
            # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
            tmp_flow_frequency=water_flow_frequency;
            l_hour = (tmp_flow_frequency * 60 / 7.5); # (Pulse frequency x 60 min) / 7.5Q = flowrate in L/hour
            water_flow_frequency = 0; # Reset Counter
            #print(str(l_hour)+": L/hour ");
            
            if(l_hour !=0):
               total_litters_sum = total_litters_sum+l_hour
               #print(str(total_litters_sum) + "is_contineous_flow="+str(is_contineous_flow));
               if(is_contineous_flow==0):
                   is_contineous_flow=1;
                   flow_start_time=currentTime;
               
            else:
               if(is_contineous_flow):
                   is_contineous_flow=0;
                   #print("total_litters_sum="+str(total_litters_sum).strip());
                   total_litters=(total_litters_sum/3.3)/1000;  ## This for callibration to match the exact litters from the outgoing pipes 
                                                                ## (Our PoC Tested with water TDS is around 700) 
                                                                 ##3.2 value may need to be changed based on your area water source.
                   #print("Total Litters="+str(total_litters).strip());
                   if(total_litters >0):
                       json_data = '{ "iot2tangle": [ { "sensor": "waterconsumed", "data": ["'+str(total_litters).strip()+'", "'+water_measurements+'"] } ], "device": "DEVICE_ID_1", "timestamp": '+str(time.time())+' }'
                       print (json_data);
                       publish2mq(json_data)
                       if(total_litters>=1):
                           iota_payment_transfer.payment_transfer(config.water_dept_wallet_address)
                   total_litters_sum=0;
                   total_litters=0;
           
            previous_time=currentTime+1000;
        time.sleep(1)
    except KeyboardInterrupt:
        print ('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        client.disconnect()
        client.loop_stop()
        sys.exit()
