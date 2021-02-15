import blynklib
from gpiozero import LED
from time import sleep
import socket

#SETUP BLYNK
BLYNK_AUTH = 'YfJ_ySzoYcKfl2Z9LEE1rDa8XQN6VgX8' 

blynk = blynklib.Blynk(BLYNK_AUTH,server='0.0.0.0',port=8080)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

CONNECT_PRINT_MSG = '[CONNECT_EVENT]'

#SETUP GPIO

#MOTOR1
motor1_fwd = LED(27)
motor1_rev = LED(22)

#MOTOR2
motor2_fwd = LED(23)
motor2_rev = LED(24)

#MOTOR3
motor3_fwd = LED(5)
motor3_rev = LED(6)

#MOTOR4
motor4_fwd = LED(16)
motor4_rev = LED(26)

#Magnet
magnet = LED(17)


#Motor1 control with Blynk
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    if value[0] == '1':
        
        print("Motor 1 Fwd")
        motor1_rev.off()
        motor1_fwd.on()
        
    elif value[0] == '-1':
        
        print("Motor 1 Rev")
        motor1_fwd.off()
        motor1_rev.on()
        
    else:
        
        print("Motor 1 Off")
        motor1_rev.off()
        motor1_fwd.off()


#Motor2 control with Blynk
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    if value[0] == '1':
        
        print("Motor 2 Fwd")
        motor2_rev.off()
        motor2_fwd.on()
        
    elif value[0] == '-1':
        
        print("Motor 2 Rev")
        motor2_fwd.off()
        motor2_rev.on()
        
    else:
        
        print("Motor 2 Off")
        motor2_rev.off()
        motor2_fwd.off()


#Motor3 control with Blynk
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    if value[0] == '1':
        
        print("Motor 3 Fwd")
        motor3_rev.off()
        motor3_fwd.on()
        
    elif value[0] == '-1':
        
        print("Motor 3 Rev")
        motor3_fwd.off()
        motor3_rev.on()
        
    else:
        
        print("Motor 3 Off")
        motor3_rev.off()
        motor3_fwd.off()


#Motor4 control with Blynk
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    if value[0] == '1':
        
        print("Motor 4 Fwd")
        motor4_rev.off()
        motor4_fwd.on()
        
    elif value[0] == '-1':
        
        print("Motor 4 Rev")
        motor4_fwd.off()
        motor4_rev.on()
        
    else:
        
        print("Motor 4 Off")
        motor4_rev.off()
        motor4_fwd.off()


#Magnet control with Blynk
@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    if value[0] == '1':
        
        magnet.on()
        print("Magnet ON")
        
    elif value[0] == '0':
        
        magnet.off()
        print("Magnet OFF")
        
    else:
        
        print("Fucked Up")#IF THIS CODE RUN YOU FUCKED UP 



@blynk.handle_event('write V6')
def write_virtual_pin_handler(pin, value):
    print("refresh url clicked!")
    print('Sending this camera stream url')
    local_ip = socket.gethostbyname(socket.gethostname())
    send_url = f"http://{local_ip}:8080/?action=stream"
    print(f"url = {send_url}")
    blynk.set_property("V7", "url", send_url)

k
#connect even
@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sending this camera stream url')
    local_ip = socket.gethostbyname(socket.gethostname())
    send_url = f"http://{local_ip}:8080/?action=stream"
    print(f"url = {send_url}")
    blynk.set_property("V7", "url", send_url)

    

#START SYSTEM
while True:
    blynk.run()
