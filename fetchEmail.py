import setup
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from datetime import datetime, date, time


def getEmails(service, dateAfter):
	messageList = service.users().messages().list(userId = 'me').execute()
	idList = []
	for message in messageList['messages']:
		idList.append(message['id'])
	messageObject = []
	for messageId in idList[:10]:
		message = service.users().messages().get(userId = 'me', id = messageId).execute()
		messageObject.append(message)
	for message in messageObject:
		if('UNREAD' in message['labelIds'] and 'IMPORTANT' in message['labelIds']):
			Time = message['payload']['headers'][12]['value'][-32:-12]
			dt = datetime.strptime(Time, "%d %b %Y %H:%M:%S")
			if(dt > dateAfter):
				print("\n")
				print('From:',message['payload']['headers'][19]['value'], '\nSubject',message['payload']['headers'][18]['value'], '\nTime',message['payload']['headers'][12]['value'][-37:],'\nText:', message['snippet'])
				print("\n")  




def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    id = 19 - From
    id = 18 - Subject
    id = 12, trunk -37 Time
    """
    credentials = setup.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    
    d = date(2016,6,4)
    t = time(9,15)
    now = datetime.combine(d,t)
    getEmails(service, now)
    


if __name__ == '__main__':
    main()