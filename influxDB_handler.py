#!/usr/bin/python3
from influxdb import InfluxDBClient

# using HTTP
#client = InfluxDBClient(database='dbname')
#client = InfluxDBClient(host='127.0.0.1', port=8086, database='dbname')
idb = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='dbname')

# using UDP
# client = InfluxDBClient(host='127.0.0.1', database='dbname', use_udp=True, udp_port=4444)

# idb.write()
