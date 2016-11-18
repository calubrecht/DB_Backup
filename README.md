# DB\_Backup
A python script to backup files to a Dropbox account

DB\_Backup is a project intended to progammaticlly copy a file to a DropBox account. Configuration options will exist to control the number of previous backups to keep and when to purge old backups.

To begin with, at least, you will need to generate a developer API token: See instructions on dropbox's developer blog. https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/

This is a python script, so python and the dropbox python api v2 will need to be installed.

Expected usage:
pythong DB\_Backup.py -c DB\_Backup.conf <options> \[fileName\]
