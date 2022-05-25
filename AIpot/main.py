from machine import ADC, Pin
import time


soilPin26 = ADC(26)
waterPin27 = ADC(27)
relayModulePin21 = Pin(21, Pin.OUT)

ledTurnOn = "Swieci"
ledTurnOff = "Nie swieci"

watering = False

def moistureSensor():
    moistureSensorWork = soilPin26.read_u16()
    soilSensorPercent = int(((moistureSensorWork - 65535) * 100) / (15000 - 65535))
    print(soilSensorPercent)
    
    #data['soilPercent'].append(soilSensorPercent)
    relayModulePin21.high()
    if (soilSensorPercent < 50):
        waterLvl()
        relayModule(watering = True)
    elif (soilSensorPercent > 100):
        relayModulePin21.high()
    else:
        print("doNothing")
        time.sleep(1)


def waterLvl():
    while True:
        waterSensorWork = waterPin27.read_u16()
        waterSensorPercent = int(((waterSensorWork - 41000) * 100) / (58000 - 41000))
        #data['waterLvl'].append(waterSensorPercent)
        print(waterSensorPercent)
        if(waterSensorPercent < 30):
            print(ledTurnOn)
            time.sleep(3)
            moistureSensor()
        else:
            print(ledTurnOff)
            time.sleep(3)
            break


def relayModule(watering = False):
        if(watering == True):
            relayModulePin21.low()
            time.sleep(5)
            relayModulePin21.high()
        else:
            watering = False
            relayModulePin21.high()
            print("doNothing")
            time.sleep(1)


def lightSensor():
    lightPercent = 40
    if(lightPercent < 30):
        print(ledTurnOn)
        time.sleep(3)
    else:
        print(ledTurnOff)
        time.sleep(3)
    time.sleep(3)


while True:    
    moistureSensor()
    time.sleep(2)
    #lightSensor()
