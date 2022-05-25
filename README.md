# LoRa-Location-Tracker

Hong Kong is facing an increasingly severe problem of an aging population. Moreover, Alzheimer's disease is more and more common in Hong Kong. Furthermore, some news in Hong Kong recently reported that COVID-19 patients escaped from hospitals. They all show that tracing persons in indoor and outdoor environments is important in many applications. Also, because of the COVID-19, the temperature needs to be measured when entering every place, especially in nursing homes. Therefore, in this project, we have a thermometer near the exit for the elderly and visitors to measure their body temperature before entering the elderly home.

This project aims to develop a tracing system called LoRa Location Tracker for an elderly home or an apartment where elderly people stay alone. The system can also be applied to trace COVID-19 patients. The system locates users’ positions continuously and reports to the staff of the elderly home and hospitals, or their family members if they are not in their appropriate locations. Recently, LoRa (Long Range communication) has been introduced for localization. In this system, the users need to wear their LoRa transmitters for localization. Note that the size of a LoRa transmitter is small and it can be installed in a necklace. LoRa receivers are installed around a venue (e.g., an elderly home, an apartment, or a hospital) to receive the transmission signals. This system measures the RSSI (Received Signal Strength Indicator) values of the transmission signals to locate their positions and determines whether they stay inside or outside the venue. If they are outside the venue (i.e., they escape from the venue), this system can identify their moving directions. Note that this system can trace their positions in both indoor and outdoor environments, while GPS (Global Positioning System), one of the most popular localization systems, can be used properly in an outdoor environment only. It is important because most elderly homes, apartments, and some hospitals are indoor environments in Hong Kong.

# LoRa

LoRa (Long Range communication) is a wireless modulation utilized to create the long-range communication link, and LoRa is a low power consumption device compared with other wireless communication devices. In addition, LoRa is a license-free Megahertz radio frequency band, Europe in 169Mhz, 433MHz, 868MHz, and North America in 915MHz. Besides, Lora WAN can also fill the technical gaps in cellular, Wi-Fi, and Bluetooth Low Energy (BLE) networks. Which require high bandwidth, power, or have limited range, or cannot go deep indoor environments.

#OBJECTIVE

This project is to develop an IoT (Internet of Things) system called LoRa Location Tracker to trace people for elderly homes, apartments where elderly people stay alone, and hospitals. This system locates their positions and reports their locations to people that are taking care of them (e.g., staff of the elderly home or hospitals, their family members … etc.).

In addition, the temperature measurement is a portable thermometer. The staff can measure the body temperature of the elderly anywhere and can also be placed at the exit of the nursing home.

#Overview

The block diagram of the LoRa location tracker system is shown in Fig. 1. This system is installed in a venue for a group of users. In this system, every user carries a necklace with a LoRa transmitter (there may be more than one user in a system). Some LoRa receivers are installed in the venue to receive the signals transmitted from different users (e.g., there are three receivers in Fig. 1). Note that the number of receivers should not be less than three because of the requirement of the Mathematical model of the LLS algorithm in. All receivers are connected to a web server. The server estimates the locations of different users by measuring the RSSI value of each signal and processing the measured data by the LLS algorithm. Based on the estimated locations, the server determines whether users stay inside or outside the venue and report to people that are taking care of them through a mobile app.

![image](https://user-images.githubusercontent.com/106225286/170229353-a724be0e-74bc-48d8-8f6c-e37769c5269d.png)
Fig. 1.

#LLS algorithm

We can get the distance between a user (transmitter) i and a receiver j (i.e., dij) from the following equation:

d_ij=10^(-(〖RSSI〗_ij-〖RSSI〗_0)/20α)	

where RSSIij is the measured RSSI values of the signal transmitted from the user i to the receiver j, RSSI0 is the reference RSSI value over one meter, and α is the path loss index. Note that all these three values are obtained by measurement. 

For each receiver, they are following the below equation to get the transmitter coordinate: 

〖(x_t-x_n)〗^2+〖(y_t-y_n)〗^2=d_ij^2.		

Take T1 as an example. We measure the RSSI values from the four receivers R1, R2, R3, and R4, R5.

From R1, we have 	〖x_t〗^2+〖y_t〗^2=d_11^2.							

From R2, we have 	〖x_t〗^2+〖(y_t-6)〗^2=d_12^2.						

From R3, we have 	〖(x_t-3)〗^2+〖(y_t-6)〗^2=d_13^2.					

From R4, we have 	〖(x_t-3)〗^2+y^2=d_14^2.						

From R5, we have 	〖(x_t-1.5)〗^2+y^2=d_14^2.						

To simplify the calculation, we consider ten sets of receivers (C_3^5=10). Set A is (R1, R2, R3), Set B is (R2, R3, R4), Set C is (R1, R3, R4), Set D is (R1, R2, R4), Set E is (R3, R2, R5), Set F is (R1, R2, R5), Set G is (R3, R4, R5), Set H is (R1, R3, R5), Set I is (R2, R4, R5), Set J is (R1, R4, R5). But in our setting, since Set J receivers are placed in parallel, we cannot use Set J to find the transmitter's position. Therefore, in total we have nine set of receivers. For each set of equation, we can calculate as a matrix, take Set A (R1, R2, R3) as an example, i.e.

[■(-2x_1&-2y_1&1@-2x_2&-2y_2&1@-2x_3&-2y_3&1)][■(x_t@y_t@〖x_t〗^2+〖y_t〗^2 )]=[■(d_ij^2-〖x_1〗^2-〖y_1〗^2@d_ij^2-〖x_2〗^2-〖y_2〗^2@d_ij^2-〖x_3〗^2-〖y_3〗^2 )],	

Thought equation we can get Set A (R1, R2, R3) xy-coordinate (x_A,y_A), then the estimated coordinate of the user is the average of the solutions of nine equations like above, i.e., 

x_t=(1/9(x_A+x_B+x_C+x_D+x_E+x_F+x_G+x_H+x_I)),

y_t=(1/9(y_A+y_B+y_C+y_D+y_E+y_F+y_G+y_H+y_I)) 

Note that R5 is also used to determine whether a user is inside or outside the venue. It is close to the exit and thus the measured RSSI value of signals received by R5 can help to precisely confirm the above issue happens or not.
