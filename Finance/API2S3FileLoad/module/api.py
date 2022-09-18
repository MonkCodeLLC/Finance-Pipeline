import requests
import json
import os

def get_data(stock):
	
	XRapidAPIKey = None
	XRapidAPIHost = None

	path = os.path.join(os.path.dirname(os.path.realpath(__file__))).replace('module','config/API.json')

	with open(path, "r") as f:
		config = json.load(f)
		XRapidAPIKey = config["X-RapidAPI-Key"]
		XRapidAPIHost = config["X-RapidAPI-Host"]

	url = "https://alpha-vantage.p.rapidapi.com/query"
	querystring = {
					"interval":"5min",
					"function":"TIME_SERIES_INTRADAY",
					"symbol": stock,
					"datatype":"json",
					"output_size":"compact"
			}
	headers = {
		"X-RapidAPI-Key": XRapidAPIKey,
		"X-RapidAPI-Host": XRapidAPIHost  
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	return response.text