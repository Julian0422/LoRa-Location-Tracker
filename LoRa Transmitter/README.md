Communicate with each receiver; the transmitter will work through LoRa to send the message to the receiver. I used Round Robin to take turns for each transmitter to prevent the collision of messages received by each receiver. Hence, there are a few differences in the program in each transmitter.

The LoRa module will keep waiting for the receiver's reply. If the LoRa module is available and receives the response, it will print out the received message and start the round-robin. The receiver sends the received message to take turns which transmitter can reply to the message. For example, if the transmitter receives "C1", it will send a message back to the receiver, including the transmitter's number.

Each receiver has the appropriate program to send back their number to the receiver.
