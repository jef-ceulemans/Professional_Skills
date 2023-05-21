import time
import wiringpi
from ch7_ClassLCD import LCD

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)


#SETUP
BUTTON1 = 0
BUTTON2 = 1
BUTTON3 = 2
BUTTON4 = 3
BUTTON5 = 4
BUTTON6 = 5

buttonArray = [BUTTON1, BUTTON2, BUTTON3, BUTTON4, BUTTON5, BUTTON6]
buttonArrayNames = ["Azië", "Afrika", "Antartica", "Zuid-Amerika", "Stille oceaan", "Noord-Amerika"]

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   15,
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

pin_CS_lcd = 13
wiringpi.wiringPiSetup()

wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)

wiringpi.pinMode(1, wiringpi.OUTPUT)
wiringpi.pinMode(2, wiringpi.OUTPUT)

wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)
wiringpi.pinMode(pin_CS_lcd , 1)
lcd_1 = LCD(PIN_OUT)

wiringpi.pinMode(BUTTON1, 0)
wiringpi.pinMode(BUTTON2, 0)
wiringpi.pinMode(BUTTON3, 0)
wiringpi.pinMode(BUTTON4, 0)
wiringpi.pinMode(BUTTON5, 0)
wiringpi.pinMode(BUTTON6, 0)

ActivateLCD()

try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        time.sleep(0.5)
        index = 0            # Python's indexing starts at zero
        for button in buttonArray:   # Python's for loops are a "for each" loop 
            if wiringpi.digitalRead(button) == 1:
                print(buttonArrayNames[index])
                ActivateLCD()
                lcd_1.clear()
                lcd_1.go_to_xy(0, 0)
                lcd_1.put_string(buttonArrayNames[index])
                lcd_1.refresh()
                DeactivateLCD()
            index += 1


except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")
