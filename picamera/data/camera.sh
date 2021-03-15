#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -o /home/pi/iot_workspace/picamera/$DATE.jpg

