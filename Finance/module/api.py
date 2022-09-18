import requests

def get_data(stock):
	url = "https://alpha-vantage.p.rapidapi.com/query"
	querystring = {
					"interval":"5min",
					"function":"TIME_SERIES_INTRADAY",
					"symbol": stock,
					"datatype":"json",
					"output_size":"compact"
			}
	headers = {
		"X-RapidAPI-Key": "2801f39772msh9f24c76e31556dep1c6ccajsn9917b2e5a5dd",
		"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	return response.text