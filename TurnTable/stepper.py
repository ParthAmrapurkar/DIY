from machine import Pin
import utime


button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(8, Pin.IN, Pin.PULL_DOWN)

#Define o/p pins
pin_a = Pin(0, Pin.OUT)
pin_b = Pin(1, Pin.OUT)
pin_c = Pin(2, Pin.OUT)
pin_d = Pin(3, Pin.OUT)

pin_a.low()
pin_b.low()
pin_c.low()
pin_d.low()

# number_of_steps = 1
# max_steps = 1000

# CW roate

#step    1 2 3 4
#        -------
# pin_a  1 0 0 1
# pin_b  1 1 0 0
# pin_c  0 1 1 0
# pin_d  0 0 1 1

# while True:
#     if button2.value():
#     utime.sleep(0.5)

rotation = "nr"

while True:
    if button1.value():
        rotation = "cw"
    
    if button2.value():
        rotation = "ccw"
        
    if button3.value():
        rotation = "nr"
    
    if rotation == "cw":
    
        #step 1
        pin_a.high()
        pin_b.low()
        pin_c.low()
        pin_d.high()
        utime.sleep(0.004)
        
        # step 2
        pin_a.high()
        pin_b.high()
        pin_c.low()
        pin_d.low()
        utime.sleep(0.004)
        
        # step 3
        pin_a.low()
        pin_b.high()
        pin_c.high()
        pin_d.low()
        utime.sleep(0.004)
        
        # step 4
        pin_a.low()
        pin_b.low()
        pin_c.high()
        pin_d.high()
        utime.sleep(0.004)
        
        #cal #of steps
#         number_of_steps +=1
        
#         if number_of_steps == max_steps:
#             # set pins to low = no voltage on colis
#             pin_a.low()
#             pin_b.low()
#             pin_c.low()
#             pin_d.low()
#             break
        
    if rotation == "ccw":
        #step 1
        pin_a.low()
        pin_b.low()
        pin_c.high()
        pin_d.high()
        utime.sleep(0.004)
        
        # step 2
        pin_a.low()
        pin_b.high()
        pin_c.high()
        pin_d.low()
        utime.sleep(0.004)
        
        # step 3
        pin_a.high()
        pin_b.high()
        pin_c.low()
        pin_d.low()
        utime.sleep(0.004)
        
        # step 4
        pin_a.high()
        pin_b.low()
        pin_c.low()
        pin_d.high()
        utime.sleep(0.004)
        
        #cal #of steps
#         number_of_steps +=1
        
#         if number_of_steps == max_steps:
#             # set pins to low = no voltage on colis
#             pin_a.low()
#             pin_b.low()
#             pin_c.low()
#             pin_d.low()
#             break
        
        if rotation == "nr":
            pin_a.low()
            pin_b.low()
            pin_c.low()
            pin_d.low()
            break
            
# if button1.value():
#     pin_a.low()
#     pin_b.low()
#     pin_c.low()
#     pin_d.low()
# CCW roate

#step    1 2 3 4
#        -------
# pin_a  0 0 1 1
# pin_b  0 1 1 0
# pin_c  1 1 0 0
# pin_d  1 0 0 1

# while True:
#     if button2.value():
# #     utime.sleep(0.5)
#         while True:
#             
#             #step 1
#             pin_a.low()
#             pin_b.low()
#             pin_c.high()
#             pin_d.high()
#             utime.sleep(0.002)
#             
#             # step 2
#             pin_a.low()
#             pin_b.high()
#             pin_c.high()
#             pin_d.low()
#             utime.sleep(0.002)
#             
#             # step 3
#             pin_a.high()
#             pin_b.high()
#             pin_c.low()
#             pin_d.low()
#             utime.sleep(0.002)
#             
#             # step 4
#             pin_a.high()
#             pin_b.low()
#             pin_c.low()
#             pin_d.high()
#             utime.sleep(0.002)
#             
#             #cal #of steps
#             number_of_steps +=1
#             
#             if number_of_steps == max_steps:
#                 # set pins to low = no voltage on colis
#                 pin_a.low()
#                 pin_b.low()
#                 pin_c.low()
#                 pin_d.low()
#                 break
