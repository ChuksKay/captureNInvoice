import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\u2713 Server running at http://localhost:{PORT}")
    print(f"\u2713 Press Ctrl+C to stop")
    httpd.serve_forever()
