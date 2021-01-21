/*data set tips
 * days string
 * tips int
 */

String days[] = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};
int tips[] = {600,400,350,400,800,900,500};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Days");
  for (int i=0; i<7; i++){
    Serial.println(days[i]);
    delay(500);
  }

  for(int i =0; i<7; i++){
    Serial.println(tips[i]);
    delay(500);
  }

  while(1);

}
