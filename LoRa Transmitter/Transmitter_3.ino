#include <SPI.h>
#include <RH_RF95.h>
#define RFM95_CS 10
#define RFM95_RST 9
#define RFM95_INT 2

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 434.0
// Blinky on receipt
#define LED 13
// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);


void setup()
{
  Serial.begin(9600);
  //while (!Serial) ; // Wait for serial port to be available
  if (!rf95.init())
    Serial.println("init failed");
  //rf95.setFrequency(433.0);
}
void loop()
{
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);
  if (rf95.waitAvailableTimeout(100))
  {
    // Should be a reply message for us now
    if (rf95.recv(buf, &len))
    {
      int dataLength;
      String Request = (char*)buf;
      Serial.println(Request);
      if (Request == "C3") {
        Serial.print("Client 3 Got Request, Answering Server...");
        String data = "3";
        int dataLength = data.length(); dataLength ++;
        uint8_t total[dataLength]; //variable for data to send
        data.toCharArray(reinterpret_cast<char *>(total), dataLength); //change type data from string ke uint8_t
        //Serial.println(data);
        Serial.println(rf95.lastRssi(), DEC);
        for (int i = 0; i <=10 ; i++){
          rf95.send(total, dataLength); //send data
          delay(10);
        }
        rf95.waitPacketSent();
      }
    }
  }
  else
  {
    Serial.println("No reply, is rf95_server running?");
  }
  delay(400);
}
