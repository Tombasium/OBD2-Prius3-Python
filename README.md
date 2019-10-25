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


Using a similar process we intend to carry out several separate tests to gather data, initially a short drive was taken in normal driving conditions in order to get a feel for the data and attempt the first set of deductions regarding what data relates to what information. 

Subsequent 
