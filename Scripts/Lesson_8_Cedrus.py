import pyxid

devices = pyxid.get_xid_devices()
print(devices)

dev = devices[0]
if dev.is_response_device():
    dev.reset_base_timer()
    dev.reset_rt_timer()

returnedPort = []
returnedKey = []

cycles = 0
while cycles < 5:
    dev.poll_for_response()
    if dev.response_queue_size() > 0:
        response = dev.get_next_response()
        if response.get("pressed") == True and response.get("key") == 6:
            break
        if response.get("pressed") == True:
            print(response)
            port = response.get("port")
            key = response.get("key")
            returnedPort.append(port)
            returnedKey.append(key)
            cycles += 1

print(returnedPort)
print(returnedKey)


#########
## END ##
#########