
int edo, num, pi;
String temp;

void setup() {
  Serial.begin(9600);
  edo = 0;
}

void loop(){
  switch(edo){
    case 0:
      Serial.print("Introduzca Numero: ");
      edo++;
      break;
    case 1:
      if(Serial.available()>0){
        temp= Serial.readString();
        num = temp.toInt();
        edo++;
      }
      break;
    case 2:
      pi = num%2;
      edo++;
      break;
    case 3:
      if(pi==0){
        Serial.println("Par");
        edo++;
      }else{
        Serial.println("Impar");
        edo++;
      }
      break;
    case 4:
      Serial.println("Repetir Programa? 1=Y 2=N");
      edo++;
      break;
    case 5:
      if(Serial.available()>0){
        temp= Serial.readString();
        num = temp.toInt();
        if(num == 1){
          edo=0;
        }else{
          edo = 6; 
        } 
      }   
      break;
    case 6:
      break;
  }
  delay(100);
}
