
def app(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body = ''	
	for elem in environ['QUERY_STRING'].split('&'):
		body = body + elem + '\n'	
	start_response(status, headers )
	return body.strip()
