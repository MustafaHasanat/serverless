import calendar
from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        month, year = dic.get("month"), dic("year")
        month, year = int(month), int(year)
        
        if (type(month) == int) and (type(year) == int):
            message = calendar.month(year, month)
        else:
            message = calendar.month(2022, 4)
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode())
        return
