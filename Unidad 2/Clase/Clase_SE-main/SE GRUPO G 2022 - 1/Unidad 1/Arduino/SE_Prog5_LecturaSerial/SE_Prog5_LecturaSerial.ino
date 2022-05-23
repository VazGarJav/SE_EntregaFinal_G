int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(100);
}

int v;
void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available()>0){
      v = Serial.readString().toInt(); //0 - 7
      digitalWrite(leds[v], 1);      
    }
  delay(100);
  
}
