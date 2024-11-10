#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:08:49 2023

@author: user
"""
import asyncio
from websockets.sync.client import connect

def hello():
	with connect("ws://localhost:8765") as websocket:
		for i in range(1, 10):
			websocket.send("Request [" + str(i) + "] Hello world!")
			message = websocket.recv()
			print(f"Received: {message}")

hello()