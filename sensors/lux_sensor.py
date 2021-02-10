#!/usr/bin/env python3

import time
import board
import busio
import adafruit_tsl2561

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)

start_time = time.time()
second_count = 10

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print('Lux: {}'.format(sensor.lux))
    print('Broadband: {}'.format(sensor.broadband))
    print('Infrared: {}'.format(sensor.infrared))
    print('Luminosity: {}'.format(sensor.luminosity))

    if elapsed_time > second_count:
        print('Finished iterating in: ' + str(int(elapsed_time)))
        break
