```socket(2, 1, 6)```
	1. Protocol family
	2. Socket type
	3. Particular protocol in protocol family
In `socket.h`, 1st arg `2` is `PF_INET` == AF_INET, 2nd arg is `SOCK_STREAM`, 3rd is found in `/etc/protocols` file.
=> TCP socket.

Use `netstat -tlp` to see what port the server is listening on, which is 31337


For some reasons, the heap segment is executable in the intended solution, but not on my machine.



