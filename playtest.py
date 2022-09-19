import time, websocket

ws = websocket.create_connection("ws://localhost:80/ws/eval")
with open('notes5.txt') as f:
    for line in f.read().split('\n'):
        # if 'delay' in line:
        time.sleep(0.01)
        #     continue
        ws.send('robertHands;' + line)
        print('robertHands;' + line)
        # time.sleep(int(line.split(';')[1]) / 1000)
ws.send('robertHands;/reset_timer')