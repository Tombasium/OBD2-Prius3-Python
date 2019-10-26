# OBD2-Prius3-Python

This project uses the Pican 2 CAN backboard with a Raspberry Pi 3+ to harvest data during operation of a Toyota Prius 3. 

The ultimate objective is to develop this into a secondary dashboard for the vehicle which displays real-time data (such as speed / battery state), with hope to integrate accelerometer data, GPS and camera input to the system. 

It should also be possible to connect the device to Wifi networks / 3G to allow it to receive commands and transmit them to the vehicle in order to control functions such as heating, locks and power remotely - though this remains a pipe dream! 

## Project status

The current focus is to decipher the information available however, as by far the most prevalent information on the internet is aimed at users that want to extinguish the engine warning light on the dashboard rather than get data from the machines.

The only useful source so far found has been a document puclished by the University of Tulsa's Crash Reconstruction Research Consortium, available here: http://tucrrc.utulsa.edu/ToyotaCAN.html

This group acquired CAN bus data from a 2010 Toyota Camry (US model) which seems as good a place as any to start looking for information on a 2013 Prius' CAN bus architecture. 

## Methodology

By reading this document we have been able to verify that the most effective method to discern what data relates to what information is simply to systematically compare values gleaned from the CANbus data dump against expected values according to information known. 


For example in the UoT's case they steadily accelerated the vehicle to 50mph then applied cruise control, then sharply braked and turned the vehicle around while driving slowly. 

The vehicle speed should then be reasonably easy to find as one part of the dataset should show a steady increase to a value that peaks, then suddenly drops before increasing slightly to a lower level. 

Brake pedal pressure and ABS engagement should be able to be detected by looking out for the sharp deceleration towards the end of the data capture range. 

Steering wheel position can be found by watching for the turn at the end. 


Using a similar process we intend to carry out several separate tests to gather data.

## First Run

Initially a short drive was taken in normal driving conditions in order to get a feel for the data and attempt the first set of deductions regarding what data relates to what information. 

During this data capture session we found no fewer than 

From this we should be able to discover which fields in the received data contain which type of data from the following types:

* Continuous (ish) data such as speed / acceleration - This may be positive only (speed) or pos/neg (steering wheel position) 

* Discrete data such as button states - binary (power on / off) and multi-state (windscreen wiper settings)

* Static (such as vehicle chassis number or VIN)

* Empty


By using the method 

```range_data_to_csv()``` 

in 

```stripAndDetect.py```

we are able to produce a .csv file for ease of viewing. 

This method takes the raw data from ```candump-2019-10-04_125707.log``` and outputs a .csv with the following headings:

Code - the address for the message
Count - the number of messages with this destination that appear
Byte 1 - The number of different values observed for the first byte
Byte 2 - the number of different values observed for the second byte
Byte 3 ...


The idea is that by seeing what range values can take in any given byte position we can start to determine what each message address is most likely to be describing. 


To illustrate, we look at the output where we notice a few things. 

First, some bytes have a 0 values - in other words no values at all for that byte. This just indicates that the full length of the data package was shorter than the usual 8 bytes. 

Second, several message addresses have just 1 possible value for certain bytes. This could indicate either that the data never changes, being perhaps a fixed message that is sent, or that the data position indicates a switch that has not had its position changed over the course of the data collection period. 

This second distinction will be targeted in a later test, when we test various switches in turn over a perios in a known sequence.

Last, there are values which have full 255 ranges of values for the byte. These are likely to be the continuous data types described above. What is worth noting is that the values may well extend over more than one byte. Speed, for example, is likely to be measures in fractions of kph or mph, and as such will need more than 255 possible values. Further experimentation will be needed to fix these values. 
