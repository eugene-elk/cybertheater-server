import time, websocket

ws = websocket.create_connection("ws://localhost:80/ws/eval")
with open('elsa.txt') as f:
    for line in f.read().split('\n'):
        # if 'delay' in line:
        # time.sleep(1)
        #     continue
        ws.send('elsa;' + line)
        print('elsa;' + line)
        # time.sleep(int(line.split(';')[1]) / 1000)
# ws.send('elsa;/reset_timer' + line)