#!/bin/bash

username=""
io_key=""
feed_key=""

#curl -F 'value=42' -H "X-AIO-Key: ${io_key}" https://io.adafruit.com/api/v2/${username}/feeds/${feed_key}/data

curl -H "Content-Type: application/json" -d '{"value": 42, "lat": 23.1, "lon": "-73.3"}' -H "X-AIO-Key: ${io_key}" https://io.adafruit.com/api/v2/${username}/feeds/${feed_key}/data
