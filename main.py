import sipfullproxy as sfp
import socketserver

HOST, PORT = '192.168.0.128', 5060


sfp.recordroute = "Record-Route: <sip:%s:%d;lr>" % (HOST, PORT)
sfp.topvia = "Via: SIP/2.0/UDP %s:%d" % (HOST, PORT)
server = socketserver.UDPServer((HOST, PORT), sfp.UDPHandler)
server.serve_forever()