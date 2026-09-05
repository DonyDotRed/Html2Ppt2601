#!/usr/bin/env python3
"""이 폴더를 http://localhost:8000 으로 띄웁니다. 종료는 Ctrl+C."""
import http.server, socketserver, pathlib, os

os.chdir(pathlib.Path(__file__).parent)
PORT = 8000
handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map['.js'] = 'text/javascript'
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"http://localhost:{PORT}  (Ctrl+C 로 종료)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n종료했습니다.")
