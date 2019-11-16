
def wsgi_application(environ, start_response):
    status ='200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]

    query = environ['QUERY_STRING']
    query = '\n'.join(query.split('&'))

    body = bytes(query, 'utf-8')

    start_response(status, headers)
    return [body]
