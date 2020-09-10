![doberman](https://img.point.pet/images/doberman-171840260-resized-56a26aa35f9b58b7d0c9ff92.jpg)

# MonitoringAndUpload

 A watchdog tool that uploads the modifications of local files to a remote server.
 It is very simple it needs only to have:

- one local directory to be watched
- one remote directory that you would like to sync with the local one
- password and ip of the server



Compatibility:

- MacOs -> natively
- Linux -> natively
- WinOs -> we don't like it but if you install Ubuntu subsystem it will hopefully work:)



[SETUP]

Make a list of the things that you would like to monitor! An example here:

```python
import os

def to_watch(dir_path):
	with open("./files_to_monitor.txt",mode="w") as ff:
		ff.write("\n".join(arr))
		
to_watch(...)
```

Does the txt file need to be called "files_to_monitor.txt"? Yes, please.



[RUN] To run the tool enter the directory of this app with the command:

```bash
cd /Users/...fill with the actual path here.../MonitoringAndUpload
```



[RUN] Then type this:

```bash
python3 main.py directory_to_watch_path username password server_ip remote_directory
```



Issues:

- Drop me an email: [riccardo.bernardi@rocketmail.com](mailto:riccardo.bernardi@rocketmail.com)
- Linkedin: https://www.linkedin.com/in/riccardobernardi/



Are you happy with this?

- drop me a star
- fork
- write me an email and we can start a partnership

