#!/usr/bin/env python3
#
# A script that will hopefully print out pinout mappings for arbitrary connections between devices
#

import json

file1 = "data/UDIhp-encoder-input.json"
file2 = "data/MP4U-encoder-input.json"

def readJsonFile(filename):
  with open(filename) as fh:
    contents = fh.read()
    data = json.loads(contents)
  return data.copy()

data1 = readJsonFile(file1)
data2 = readJsonFile(file2)

for pinDict in data1['pinout']:
	#print(pinDict['pin'], pinDict['name'])
	
	# Loop over pins on other connector
	for otherPinDict in data2['pinout']:
		#print('\t', otherPinDict['pin'], otherPinDict['name'])
		#print(pinDict['pin'], pinDict['function'],'\t', otherPinDict['pin'], otherPinDict['function'])
		
		if pinDict['function'] == otherPinDict['function']:
			print(pinDict['pin'], pinDict['function'],'\t', otherPinDict['pin'], otherPinDict['function'])
			break
	#print()
	
