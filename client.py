import socket
import random
import time
TCP_IP = '10.0.0.118'
TCP_PORT = int(input("Enter port number to bind "))
BUFFER_SIZE = 1024
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc", "rb").read())
while(1):
	writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
	writer.append({"Rand_int_1": random.randint(0, 500), "Rand_int_2": random.randint(0, 500), "Rand_int_3": random.randint(0, 500), "Rand_int_4": random.randint(0, 500), "Rand_int_5": random.randint(0, 500)})
	writer.close()
	
	reader = DataFileReader(open("users.avro", "rb"), DatumReader())
	for a in reader:
		print (a)
	reader.close()
	s.send(str(a))
	time.sleep(1)
s.close()




