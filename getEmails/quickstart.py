
from __future__ import print_function
import httplib2
import os
import base64
import email
import geopy
import geocoder
import time

import datetime

from apiclient import errors


from apiclient import errors
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

## Geocoding Library from OpenStreeMaps
#geocoder PyPi library

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = [
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/gmail.modify',
    # Add other requested scopes.
]
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def ListLabels(service, user_id):
  """Get a list all labels in the user's mailbox.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.

  Returns:
    A list all Labels in the user's mailbox.
  """
  try:
    response = service.users().labels().list(userId=user_id).execute()
    labels = response['labels']
    for label in labels:
      print ('Label id: %s - Label name: %s' % (label['id'], label['name']))
    return labels
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

from apiclient import errors


def ListMessagesMatchingQuery(service, user_id, query=''):
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

#listALlMessage



def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()
    msg_str = str(base64.urlsafe_b64decode(message['raw'].encode('ASCII')))

    mime_msg = email.message_from_string(msg_str)
    messageMainType = mime_msg.get_content_maintype()
    return mime_msg
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)

def getAttributes(data):
    str1 = "User:*"
    str5 = "Service:*"

    str2 = "IP from which the login attempt was detected:"
    str3 = "Location:"
    str4 = "Time:"

    outputList = []

    index1 = (data.find(str1))
    index2 = (data.find(str5))
    rawStr = data[index1:index2:]
    rawList = rawStr.split('\\r\\n*')
    outputList = []
    for str in rawList:
        if str1 in str:
            endIndex = str.find('\\r\\n')
            outputList.append(str[7:endIndex:])
        if str2 in str:
            if str[47:50:] == 'r\\n':
                outputList.append(str[50::])
            else:
                outputList.append(str[47::])
        if str3 in str:
            outputList.append(str[11::])
        if str4 in str:
            outputList.append(str[7::])
    return(outputList)



def ModifyMessage(service, user_id, msg_id, msg_labels):
  """Modify the Labels on the given Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The id of the message required.
    msg_labels: The change in labels.

  Returns:
    Modified message, containing updated labelIds, id and threadId.
  """
  try:
    message = service.users().messages().modify(userId=user_id, id=msg_id,
                                                body=msg_labels).execute()

    label_ids = message['labelIds']

    print ('Message ID: %s - With Label IDs %s' % (msg_id, label_ids))
    return message
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)


def CreateMsgLabels():
  """Create object to update labels.

  Returns:
    A label update object.
  """
  return {'removeLabelIds': ['UNREAD'], 'addLabelIds': ['Label_1']}

def CreateUnreadMsgLabels():
  """Create object to update labels.

  Returns:
    A label update object.
  """
  return {'removeLabelIds': ['Label_1'], 'addLabelIds': ['UNREAD']}


def ListMessagesWithLabels(service, user_id, label_ids=[]):
  """List all Messages of the user's mailbox with label_ids applied.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.

  Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id,
                                                 labelIds=label_ids,
                                                 pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError as error:
    print( 'An error occurred: %s' % error)


def get_emails():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """

    # Create a Nominatim instance (OpenStreeMaps geocoding service)
    ##geolocator = Nominatim()

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    allMessages = ListMessagesWithLabels(service, 'me', ['UNREAD'])
    allRecords = [] # List for all email records (list of lists)

    ListLabels(service, 'me')

    messageLabels = CreateMsgLabels() # Removes 

    # for mess in allMessages:
    #     messageID = mess['id']
    #
    #     ModifyMessage(service, 'me', messageID, messageLabels)
    #     #print (getAttributes(str(GetMimeMessage(service, 'me', messageID))))
    #     record = getAttributes(str(GetMimeMessage(service, 'me', messageID)))  # [UserID, IP Address, Location, Time]
    #     if len(record) == 4:
    #
    #
    #         #record.append(geocoder.google(record[2]).latlng)# add city from IP - geocoder library
    #         print(record)
    #
    #     #allRecords.append(record)

    while len(allMessages) != 0:
        mess = allMessages[0] # store and remove an email record from allMessages
        allMessages.pop(0)
        messageID = mess['id']
        ModifyMessage(service, 'me', messageID, messageLabels) # Change label from ['UNREAD'] to ['Label_1']
        record = getAttributes(
            str(GetMimeMessage(service, 'me', messageID)))  # [UserID, IP Address, Location, Time]
        if len(record) == 4:
            try:
                tm = record[3]
                record.pop() # remove verbose string Time field
                # Add parsed YYY-MM-DD HH:MM:SS (24h time)
                parsetime = datetime.datetime.strptime(tm[0:-22], '%A, %B %d, %Y at %I:%M:%S %p')
                record.append(datetime.datetime.strftime(parsetime, '%Y-%m-%d %H:%M:%S'))
                # query Google geocoding API with string Location field
                record.append(geocoder.google(record[2]).lat)
                record.append(geocoder.google(record[2]).lng)
            except:
                # ISSUE: leaves None in some fields when it passes to next iteration.
                break
            print(record)
            allRecords.append(record) # Append record to list of lists with all records read this run
            
        # paging the process in order to get a stable connnection
        # else:
        #     for indexLimit in range(0,49):
        #         if len(allMessages) == 0:
        #             break
        #         else:
        #             mess = allMessages[indexLimit]
        #             messageID = mess['id']
        #             ModifyMessage(service, 'me', messageID, messageLabels)
        #             record = getAttributes(str(GetMimeMessage(service, 'me', messageID)))  # [UserID, IP Address, Location, Time]
        #             if len(record) ==4:
        #                 try:
        #                     tm = record[3]
        #                     record.pop()
        #                     parsetime = datetime.datetime.strptime(tm[0:-22], '%A, %B %d, %Y at %I:%M:%S %p')
        #                     record.append(datetime.datetime.strftime(parsetime, '%Y-%m-%d %H:%M:%S'))
        #                     allMessages.pop(0)
        #                     record.append(geocoder.google(record[2]).lat)
        #                     record.append(geocoder.google(record[2]).lng)
        #                 except:
        #                     pass
        #             if len(record) == 6:
        #                 allRecords.append(record)

    return allRecords

def unreadAllEmails():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    allMessages = ListMessagesWithLabels(service, 'me', ['INBOX'])
    ListLabels(service, 'me')

    messageLabels = CreateUnreadMsgLabels()


    for mess in allMessages:
        messageID = mess['id']
        ModifyMessage(service, 'me', messageID, messageLabels)

def main():
    get_emails()
if __name__ == '__main__':
    main()
