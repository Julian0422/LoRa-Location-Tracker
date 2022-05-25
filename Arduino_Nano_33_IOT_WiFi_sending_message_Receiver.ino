#include <SPI.h>
#include <RH_RF95.h>
#include <WiFiNINA.h>
#include <WiFiUdp.h>
#include "arduino_secrets.h" 

//Adafruit LoRa
#define RFM95_CS 10
#define RFM95_RST 9
#define RFM95_INT 2
//Arduino NNAO 33 IOT D12 MISO
//Arduino NNAO 33 IOT D11 MOSI

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 434.0
// Blinky on receipt
#define LED 13
// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

unsigned long int millisBefore;

int turn = 1;
boolean statusRepeater = 0;

int status = WL_IDLE_STATUS;

//WiFi
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen on

char packetBuffer[256]; //buffer to hold incoming packet
char  ReplyBuffer[] = "hi";       // a string to send back
int RSSI;
WiFiUDP Udp;

void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);
  
  Serial.begin(9600);

  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 5 seconds for connection:
    delay(5000);
  }
  Serial.println("Connected to WiFi");
  printWifiStatus();

  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  Udp.begin(localPort);

  Serial.println("Arduino LoRa RX Test!");
  
  if (!rf95.init()) 
    Serial.println("LoRa radio init failed");
    
  //Serial.println("LoRa radio init OK!");
  
  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  //Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);
  
  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on
  
  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(23, false);
  millisBefore = millis();
}

void loop()
{
  if (statusRepeater == 0) {
    if (millis() - millisBefore < 2000) {
      if (turn == 1) {
        //Serial.println("Send Request 1");
        //delay(100);
        SendRequest("C1"); 
        waitForAnswer();
        delay(500);
        turn = 2;
      }
    } else if ((millis() - millisBefore > 2000) && (millis() - millisBefore < 4000)) { 
      if (turn == 2) {
        //Serial.println("Send Request 2");
        //delay(100);
        SendRequest("C2");
        waitForAnswer();
        delay(500);
        turn = 3;
      }
    } else if ((millis() - millisBefore > 4000) && (millis() - millisBefore < 6000)) { 
      if (turn == 3) {
        //Serial.println("Send Request 3");
        //delay(100);
        SendRequest("C3");
        waitForAnswer();
        delay(500);
        millisBefore = millis();
        turn = 1;
      }
    }
  }
}

void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

void waitForAnswer() { //fungsi tunggu jawaban dari node
  // Now wait for a reply
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);
  if (rf95.waitAvailableTimeout(100))
  {
    //Serial.println("waitForAnswer");
    if (rf95.recv(buf, &len))
    {
      int dataLength;
      String Request = (char*)buf;
      //Serial.println(Request);
      if(Request.equals("1")||Request.equals("2")||Request.equals("3"))
      {
        Serial.print("Received at Server: ");
        Serial.println((char*)buf);
        String dataTotal = (char*)buf;
        //Serial.println(dataTotal);
        Serial.println(rf95.lastRssi(), DEC);
        //delay(10);
        
        RSSI = rf95.lastRssi();
        int packetSize = Udp.parsePacket();
        Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
        //Udp send same packet 3 times
        //for (int i = 0; i <=3; i++){
          Udp.print((char*)buf);
          Udp.print("#");
          Udp.print(RSSI);
          delay(400);
        //}
        //Udp.write(ReplyBuffer);
        //Serial.println(rf95.lastRssi(), DEC);
        Serial.print("WIFI: ");       
        //Transmitter Number
        Serial.print((char*)buf);
        Serial.print("#");
        Serial.println(RSSI);    
        //Serial.println("sent");
        //delay(100);
        Udp.endPacket();
      }
    }
    else
    {
      Serial.println("recv failed");
    }
  }
}

void SendRequest(String request) { //fungsi untuk Send request dengan variable parameter request
  String dataTotal = request;
  int dataLength = dataTotal.length(); 
  dataLength ++;
  uint8_t total[dataLength];
  dataTotal.toCharArray(reinterpret_cast<char *>(total), dataLength);
  rf95.send(total, dataLength);
  rf95.waitPacketSent();
}
