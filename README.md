# DB\_Backup
A python script to backup files to a Dropbox account

DB\_Backup is a project intended to progammaticlly copy a file to a DropBox account. It is intended for regular backups, so previous versions are available through DropbBox's interface for 30 days

To begin with, at least, you will need to generate a developer API token: See instructions on dropbox's developer blog. https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/

This is a python script, so python and the dropbox python api v2 will need to be installed. It relies on pyhon 2.7 for the argparse library

Expected usage:
python DB\_Backup.py -c DB\_Backup.cfg <options> \[fileName\]

The API Refresh token will be stored in the DB\_Backup.cfg file, under the config option "token"
API keys/secret for your dropbox app must be stored in the key and secret options in DB\_Backup.cfg
