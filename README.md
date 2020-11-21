# Tangle enabled Real-time Water Distribution
## A Smart and Tamper-proof method for Water consumption payment system
Detect the water consumption in real-time and make auto payment as pay per use, store and analyze the data in tangle for tamper-proof IoT data
## Water Distribution ecosystem (Reference Architecture)
![Architecture](images/flow_diagram.JPG)

## Require Hardware
  1. [YF-Water Flow Sensor](https://robu.in/product/yf-s201-water-flow-measurement-sensor-with-1-30liter-min-flow-rate-2/?gclid=Cj0KCQiAkuP9BRCkARIsAKGLE8UxgRBkIr7N0A73nVRC6L-rj1wSw8ms-no1rjBF1aaWUuvCUBeDVyIaAiO2EALw_wcB)
     Approx. cost 300 INR
  2. Raspberry Pi (We can do it in ESP32 as well - just for PoC we used Pi)

## Wiring Connections between YF-Water flow Sensor and Pi
    - RED wire  to Pi 5V
    - Black wire to Pi GND
    - Yellow wire to Pi GPIO23
    
## Edge device installation
   1. [Streams-mqtt-gateway](https://github.com/iot2tangle/Streams-mqtt-gateway)
   2. Install mqtt python library
       sudo pip install phao-mqtt
   3. clone our [project](https://github.com/rgkrishnas/Tangle-enabled-Real-time-Water-Distribution)
### How to run the program and sample output

## Payment system

## Demo Video

## Contacts
[Gopal](rgkrishnas@gmail.com)
