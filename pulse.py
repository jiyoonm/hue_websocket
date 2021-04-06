import websocket
from lights import *
pulse1 = 0 
pulse2 = 0 

def on_message(ws, message):
    global pulse1
    global pulse2

    if "Client One" in message: 
        client1 = int(message.replace('Client One', ''))
        pulse1= (60/ client1)
        
    elif "Client Two" in message: 
        client2 = int(message.replace('Client Two', ''))
        pulse2= (60/ client2)
        # return pulse2
        
    client1_pulse(pulse1)    
    client2_pulse(pulse2)



def get_pulse():
    global pulse1
    return pulse1


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
     ws.send("Hello")
      

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://webscoket-unity.herokuapp.com/",
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.run_forever()
