import calendar
from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        month = dic.get("month")
        month = int(month)
        
        if month:
            message = calendar.month(2022, month)
        else:
            message = calendar.month(2022, 4)
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode())
        return





# from http.server import HTTPServer

# def main():
#     port = 3030
#     server = HTTPServer(('', port), handler)
#     print('Started httpserver on port {}'.format(port))
#     server.serve_forever()

# if __name__ == '__main__':
#     main()