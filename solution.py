from socket import *


def smtp_client(port=1025, mailserver="127.0.0.1"):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
#    if recv1[:3] != '250':
#        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    print("Sending MAIL FROM command.")
    mailFromCommand = bytes("MAIL FROM: <bellogabe@gmail.com>\r\n", "utf-8")
    clientSocket.send(mailFromCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
#    if recv1[:3] != '250':
#        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    print("Sneding RCPT TO command.")
    rcptToCommand = bytes("RCPT TO: <bellogabe@gmail.com>\r\n", "utf-8")
    clientSocket.send(rcptToCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
#    if recv1[:3] != '250':
#        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    print("Sneding DATA command.")
    dataCommand = bytes("DATA\r\n", "utf-8")
    clientSocket.send(dataCommand)
    recv1 = clientSocket.recv(1024)
#    print(recv1)
    # Fill in end

    # Send message data. Message ends with a single period.
    # Fill in start
    print("Sending message data.")
    msg = bytes("SUBJECT: SMTP Test\nIs this thing on\n.\r\n", "utf-8")
    clientSocket.send(msg)
#    recv1 = clientSocket.recv(1024)
#    print(recv1)
#    if recv1[:3] != '250':
#        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    print("Sending Quit")
    quitCommand = bytes("QUIT\r\n", "utf-8")
    clientSocket.send(quitCommand)
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '221':
        print('221 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
