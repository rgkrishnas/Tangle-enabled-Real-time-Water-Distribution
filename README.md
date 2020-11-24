# Tangle enabled Real-time Water Distribution
## A Smart IOTA Tangle based Tamper-proof water distribution metering and Payment System.
Fresh water availability is taking a serious hit world-wide and is considered to be one of the main reasons that would trigger a third world war.
The existing water distribution systems in existance does not have exact and real-time monitoring of water usage and metering is often done on average or approximate use. This PoC demonstrates the use of sensors to monitor real-time water usage along with integration with IOTA tangle to enable tamper proof data management with payment integration.
## Brief Overview
The Waterflow sensors stream waterflow to a procesing unit(Raspberry Pi used in this PoC). A python program runs to calculate the consumption and stores locally as well as streams to a Steams-MQTT-gateway. User can check the real-time water consumption or the accumulated consumption at any point of time. During the billing cycle the charges for consumption is calculated in IOTA tokens and sent to the users client app. User can clear the dues which gets updated in IOTA wallet.
## Advantages
1. Real-time monitoring triggers alarms on water wastage due to possible leaks
2. Tamper-proof data management due to use of IOTA tangle technology
3. Smart system with exact real-time consumption measurements and automatic payment as pay per use
4. Simple and easy to install
5. Low cost sensor and hardware.
## Reference Architecture -(Water Distribution ecosystem)
![Architecture](images/flow_diagram.JPG)

## Require Hardware (BoM)
  1. [YF-Water Flow Sensor](https://robu.in/product/yf-s201-water-flow-measurement-sensor-with-1-30liter-min-flow-rate-2/?gclid=Cj0KCQiAkuP9BRCkARIsAKGLE8UxgRBkIr7N0A73nVRC6L-rj1wSw8ms-no1rjBF1aaWUuvCUBeDVyIaAiO2EALw_wcB)
     Approx. cost 300 INR
  2. [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/?resellerType=home) (We can do it in ESP32 as well - just for PoC we used Pi)
  3. Three strand jumper wire set (male to female)

## Schematics Diagram 
#### Wiring Connections between YF-Water flow Sensor and Pi
    - RED wire  to Pi 5V
    - Black wire to Pi GND
    - Yellow wire to Pi GPIO23
![Wiring Diagram](images/Pi2WaterFlowSensor.JPG)
## Edge device installation and configuration
   1. [Streams-mqtt-gateway](https://github.com/iot2tangle/Streams-mqtt-gateway)
   2. Install mqtt python library
       - $ sudo pip install phao-mqtt
   3. Edit the config.json file and update the host name
   4. Clone our [project](https://github.com/rgkrishnas/Tangle-enabled-Real-time-Water-Distribution)
   5. Edit the config.py file and update the MQTT host name, user id, password and message topic
   6. Install [pyota](https://github.com/iotaledger/iota.py) if python2 is default try to install "sudo pip3 install pyota"
   
### How to run the program and sample output
1. Power the Pi 
2. Go to the Streams-mqtt-gateway folder and start run
   - $ cargo run --release
   Copy the return seed for verification in tangle
3. Go to our project directory "Tangle-enabled-Real-time ...." where you cloned and run the below command
   - $ python3 waterflowsensor.py
4. Open the Valve (once the water flow is happened you could see the consumed water quantity in litters)
5. A payment request will be initiated based on some litters/gallon threashold value
6. Edge device will make the payment with the real-time consumed water.

## Demo Video
[![Working Prototype Demo](images/VideoThumb.png)](https://youtu.be/EH2FJtxiFEA)

## Contacts
Gopal (rgkrishnas@gmail.com)
