import socket

server = "irc.freenode.net"
name = "arandomnme"
port = 6667
channel = "#iitpkd"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send("NICK " + name + "\n")
irc.send("USER irccat 8 x : irccat\n")
irc.send("JOIN " + channel + "\n")
while True:

    def message(msg):
        irc.send("PRIVMSG " + channel + " :" + msg + "\n")

    data = irc.recv(1204)
    print data
    data = data.strip('\r\n')
    senderusr = data.split(" ")
    senderusr = senderusr[0]
    senderusr = senderusr.split("!")
    senderusr = senderusr[0]
    senderusr = senderusr.strip(":")

#    print data
#    message("Follow Angie on Twitter: https://twitter.com/AriayeHuntress")
    if data.find == "PONG" :
        irc.send("PING")

    #if data.find(":!twitter") and authlist.find(senderusr) != -1:
    #    message("Follow Angie on Twitter: https://twitter.com/AriayeHuntress")

    #if data.find(":!fanpage") and authlist.find(senderusr) != -1:
    #    message("Like Angie's Fanpage on Facebook: http://facebook.com/AriayeTheHuntress")  

    #if data.find(":!bg") and authlist.find(senderusr) != -1:
    #    message("Wanna play BGs with Angie on WoW? Add her battletag: Ariaye#1211")

    #if data.find(":!youtube") and authlist.find(senderusr) != -1:
    #    message("Subscribe to Angie on Youtube! http://youtube.com/ariayethehuntress")