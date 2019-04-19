import socket
import os
import json
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_config():
  with open(dir_path + "/config.json", "r") as f:
    return json.load(f)

def write_to_file (filename, message):
  print(filename, "<", message)
  with open(dir_path + "/" + filename, "a") as f:
    message_with_date = json.dumps({ "date": str(datetime.now()), "message": message })
    f.write(message_with_date)

OUTPUT_FILE = "output.txt"
DEBUG_FILE = "debug.txt"

def debug (message):
  write_to_file(filename=DEBUG_FILE, message=message)

ping = "PING ".encode()
pong = "PONG ".encode()

config = get_config()
server = config["server"]
port = config["port"]
nickname = config["nickname"]
username = config["username"]
real_name = config["real_name"]
channel = config["channel"]

# Connect
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))
outbound_port = client.getsockname()[1]
debug("Listening on port: {}".format(outbound_port))

def send (message):
  debug("SENDING: " + message)
  try:
    client.send(message)
  except Exception as err:
    debug("ERROR: " + err)

# Handshake
send(("NICK " + nickname + "\r\n").encode())
send(("USER " + username + " 0 * :" + real_name + "\r\n").encode())
send(("JOIN " + channel + "\r\n").encode())

while True:
  data = client.recv(1024)
  debug("RECEIVED: " + data)

  if data.startswith(ping):
    resp = data.strip(ping)
    response_to_ping = pong + resp
    send(response_to_ping)
  else:
    write_to_file(filename=OUTPUT_FILE, message=message)
