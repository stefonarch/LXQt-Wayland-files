#!/usr/bin/python3

import socket
import json as js
import os

def get_msg_template():
    # Create generic message template
    message = {}
    message["data"] = {}
    return message

class WayfireSocket:
    def __init__(self, socket_name):
        self.client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.client.connect(socket_name)

    def read_exact(self, n):
        response = bytes()
        while n > 0:
            read_this_time = self.client.recv(n)
            if not read_this_time:
                raise Exception("Failed to read anything from the socket!")
            n -= len(read_this_time)
            response += read_this_time

        return response

    def read_message(self):
        rlen = int.from_bytes(self.read_exact(4), byteorder="little")
        response_message = self.read_exact(rlen)
        return js.loads(response_message)

    def send_json(self, msg):
        data = js.dumps(msg).encode('utf8')
        header = len(data).to_bytes(4, byteorder="little")
        self.client.send(header)
        self.client.send(data)
        return self.read_message()

    def watch(self):
        message = get_msg_template()
        message["method"] = "wf/notifications/watch"
        return self.send_json(message)

    def set_view_alpha(self, view_id: int, alpha: float):
        message = get_msg_template()
        message["method"] = "wf/alpha/set_view_alpha"
        message["data"] = {}
        message["data"]["view-id"] = view_id
        message["data"]["alpha"] = alpha
        return self.send_json(message)

addr = os.getenv('WAYFIRE_SOCKET')
inbound_socket = WayfireSocket(addr)
outbound_socket = WayfireSocket(addr)

inbound_socket.watch()
last_view_id = -1

while True:
    msg = inbound_socket.read_message()
    print(msg)

    ev_type = msg["event"]
    if ev_type == "view-focused":
        view_id = msg["view-id"]
        if last_view_id != -1 and view_id != last_view_id:
            print(outbound_socket.set_view_alpha(last_view_id, 0.8))
            print(outbound_socket.set_view_alpha(view_id, 1.0))

        last_view_id = view_id
