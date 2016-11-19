import ConfigParser
import dropbox
import os

DEFAULT_CONFIGFILE = 'DB_Backup.cfg'

def getDropboxClient(configFile):
  if not configFile:
    configFile = DEFAULT_CONFIGFILE
  configParser = ConfigParser.RawConfigParser()
  p = os.path.dirname(os.path.realpath(__file__))
  configParser.read(p + os.sep + configFile)
  token = configParser("DB_Backup", 'token')
  return dropbox.DropBox(token)


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
    dropbox.files.CommitInfo(uploadPath + filename, autorename=True))
  

def purgeOldFiles(client, fileName, numberToPreserve):
  pass

if __name__ == '__main__':
  from argparse import ArgumentParser
  import sys
  parser = ArgumentParser()
  parser.add_argument('-c', action='store', dest='config', help="specify file for configuration options, default " + DEFAULT_CONFIGFILE, default=DEFAULT_CONFIGFILE)
  parser.add_argument('fileName', action='store', help="specify file for configuration options, default " + DEFAULT_CONFIGFILE, default=DEFAULT_CONFIGFILE)
  args = parser.parse_args()
  
  if not args:
    parser.print_help()
    sys.exit(1)
  print  str(args)
