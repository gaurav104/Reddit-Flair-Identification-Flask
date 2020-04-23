import os
import json
from .predictor import predict_flair

def decode_bytes(b_string):
	return b_string.decode('utf-8','ignore')

def process_file(file):
	predictions = {}
	lines = file.readlines()
	lines = map(decode_bytes, lines)
	for line in lines:
		if line.strip():
			url = line.strip()
			pred_label = predict_flair(url)
			predictions[url] = pred_label['label']
	return predictions
