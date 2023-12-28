Initial Outline:

1. Setup various source for kafka like:
   - A docker image producing data to websocket. 
   - An API based app in python that is continuously generating data. 
   - An existing API like weather API, Twitter API etc 





Libraries used for websocket
pip install websocket-client
pip install websockets

### How to kill websocket app 

1. Get the process id:
```
ps aux | grep python
```

2. Kill the process: 
```
kill -9 <pid>
```
