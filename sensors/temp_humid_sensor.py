#!/usr/bin/env python3

import time
import board
import busio
import adafruit_si7021

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)

start_time = time.time()
second_count = 10

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print('Temperature: {}'.format(sensor.temperature))
    print('Relative Humidity: {}'.format(sensor.relative_humidity))

    if elapsed_time > second_count:
        print('Finished iterating in: ' + str(int(elapsed_time)))
        break
