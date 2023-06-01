import configparser as ConfigParser
import dropbox
import os

DEFAULT_CONFIGFILE = 'DB_Backup.cfg'

def getDropboxClient(configFile):
  if not configFile:
    configFile = DEFAULT_CONFIGFILE
  configParser = ConfigParser.RawConfigParser()
  p = os.path.dirname(os.path.realpath(__file__))
  configParser.read(p + os.sep + configFile)
  token = configParser.get("DB_Backup", 'token')
  key = configParser.get("DB_Backup", 'key')
  secret = configParser.get("DB_Backup", 'secret')
  return dropbox.Dropbox(app_key=key, app_secret=secret, oauth2_refresh_token=token)


def uploadFile(client, fileName, uploadPath):
  sessionId = client.files_upload_session_start(None).session_id
  chunkSize = 100 * 1024 * 1024
  f = open(fileName, mode='rb')
  data = f.read(chunkSize)
  i = 0
  while data:
    client.files_upload_session_append(data, sessionId, i)
    i = i + len(data)
    data = f.read(chunkSize)
  client.files_upload_session_finish(
    None,
    dropbox.files.UploadSessionCursor(sessionId, i),
    dropbox.files.CommitInfo(uploadPath + fileName, autorename=False, mode=dropbox.files.WriteMode.overwrite))
  

if __name__ == '__main__':
  from argparse import ArgumentParser
  import sys
  parser = ArgumentParser()
  parser.add_argument('-c', action='store', dest='config', help="specify file for configuration options, default " + DEFAULT_CONFIGFILE, default=DEFAULT_CONFIGFILE)
  parser.add_argument('fileName', action='store', help="specify file for configuration options, default " + DEFAULT_CONFIGFILE, default=DEFAULT_CONFIGFILE)
  parser.add_argument('destination', action='store', nargs='?', help="Detination folder", default='/')
  args = parser.parse_args()
  
  if not args:
    parser.print_help()
    sys.exit(1)
  
  dbc = getDropboxClient(args.config)
  dest = args.destination
  if not dest.startswith('/'):
    dest = '/' + dest
  if not dest.endswith('/'):
    dest =  dest + '/'
  uploadFile(dbc, args.fileName, dest)

