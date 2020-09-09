# MonitoringAndUpload
 A watchdog tool that uploads the modifications of local files to a remote server.
 It is very simple it needs only to have:
- one local directory to be watched
- one remote directory that you would like to sync with the local one
- password and ip of the server

To run the tool enter the directory of this app with the command:

,,,{bash}
cd /Users/...fill with the actual path here.../MonitoringAndUpload
,,,

Then type this:

,,,{python}
python3 main.py directory_to_watch_path username password server_ip remote_directory
,,,
