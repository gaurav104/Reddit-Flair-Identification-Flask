import os
import json
from .predictor import predict_flair

def modify_ext(name, extension):
	pre, ext = os.path.splitext(name)
	modified_name  = pre + extension
	return modified_name


def process_file(upload_path, filename):
	predictions = {}
	with open(upload_path, 'r') as fp:
		lines = fp.readlines()
		for line in lines:
			url = line.strip()
			pred_label = predict_flair(url)
			predictions[url] = pred_label
	
	# json_file_path = modify_ext(upload_path, '.json')


	# with open(json_file_path, 'w') as js:
	# 	json.dump(predictions, js)

	# filename = modify_ext(filename, ".json")
	return predictions

