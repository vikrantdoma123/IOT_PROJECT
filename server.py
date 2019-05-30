import socket
import threading
from datetime import datetime
import os
import time

# current date and time
import datetime
currentDT = datetime.datetime.now()
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIARVCBX5KOUZUGYMZX '
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'project-iot-v1'
FILE_NAME = 'test.txt';

data = open(FILE_NAME, 'rb')
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

counter=0
print (str(currentDT))


class ThreadedServer:
	def __init__(self, port):
		self.host = '10.0.0.118'
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))

	def listen(self):
		self.sock.listen(5)
		while True:
			client, address = self.sock.accept()
			client.settimeout(60)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()


	def listenToClient(self, client, address):
		size = 1024
		print ("Connecting to client having address" + str(address)+ "\n")
		with open('test.txt','a+') as f:
  			f.write("\n\n_________________________" + str(datetime.datetime.now()) + "_______________________________\n\n")
		start = time.time()
		while 1:
			try:
				global counter
				data = client.recv(size)
				counter+=1
				if not data:
					break				
				print("received data:", data)
				with open('test.txt','a+') as f:
					f.write(data + "\n")
				if time.time()-start > 10:
					os.system('python example.py')
					with open('test.txt','a+') as f:
  						f.write("\n\n_________________________" + str(datetime.datetime.now()) + "_______________________________\n\n")
						start = time.time()
					counter=0
			
			except KeyboardInterrupt :
				client.close()
				sock.close()
			
port=int(input("Enter port number to bind "))
serverIOT = ThreadedServer(port)
serverIOT.listen()
