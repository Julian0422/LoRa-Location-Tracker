# LoRa-Location-Tracker

Hong Kong is facing an increasingly severe problem of an aging population. Moreover, Alzheimer's disease is more and more common in Hong Kong. Furthermore, some news in Hong Kong recently reported that COVID-19 patients escaped from hospitals. They all show that tracing persons in indoor and outdoor environments is important in many applications. Also, because of the COVID-19, the temperature needs to be measured when entering every place, especially in nursing homes. Therefore, in this project, we have a thermometer near the exit for the elderly and visitors to measure their body temperature before entering the elderly home.
This project aims to develop a tracing system called LoRa Location Tracker for an elderly home or an apartment where elderly people stay alone. The system can also be applied to trace COVID-19 patients. The system locates users’ positions continuously and reports to the staff of the elderly home and hospitals, or their family members if they are not in their appropriate locations. Recently, LoRa (Long Range communication) has been introduced for localization. In this system, the users need to wear their LoRa transmitters for localization. Note that the size of a LoRa transmitter is small and it can be installed in a necklace. LoRa receivers are installed around a venue (e.g., an elderly home, an apartment, or a hospital) to receive the transmission signals. This system measures the RSSI (Received Signal Strength Indicator) values of the transmission signals to locate their positions and determines whether they stay inside or outside the venue. If they are outside the venue (i.e., they escape from the venue), this system can identify their moving directions. Note that this system can trace their positions in both indoor and outdoor environments, while GPS (Global Positioning System), one of the most popular localization systems, can be used properly in an outdoor environment only. It is important because most elderly homes, apartments, and some hospitals are indoor environments in Hong Kong.
