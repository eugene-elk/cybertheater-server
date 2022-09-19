import mido
import sys

def parse_midi(path_to_midi):
    mid = mido.MidiFile(path_to_midi)
    melody = []
    tempo = 0
    for msg in mid:
        if not msg.is_meta:
            break
        elif msg.type == "set_tempo":
            tempo = mido.tempo2bpm(msg.tempo)
    
    for msg in mid:
        # print(msg)
        if msg.type == 'note_on' or msg.type == 'note_off':
            # print(msg)
            melody.append([(msg.note - 60) % 12, msg.velocity, int(msg.time*1000)])

    return melody

def generate_output(type):
    
    if type == 0:
        
        for element in melody:
            if element[1] == 0:
                print("/play_note;", notes[element[0]], ";", element[2], sep='')
            else:
                print("/delay;", element[2], sep='')

    if type == 1:

        print("/delay;", melody[0][2], sep='')
        print("/turn_valve;1")
        


        for i in range(1, len(melody)-2):

            if melody[i][1] == 0:

                print("/play_note;", notes[melody[i][0]], ";", melody[i][2] * 2, sep='')

            else:
                    
                print("/delay;", melody[i][2] * 4, sep='')

    if type == 2:
        
        delay = 0
        print("/delay;", melody[0][2], sep='')
        delay += melody[0][2]
        print("/turn_valve;0")

        for i in range(1, len(melody)-2):

            if melody[i][1] == 0:

                print(delay, ";/play_note_simple", sep='')
                delay += melody[i][2]

            else:
                    
                print(delay, ";/prepare_note;", notes[melody[i][0] + 4], sep='')
                delay += melody[i][2] * 10
        
        print(delay + 500, ";/turn_compressor;0", sep='')
        print(delay + 700, ";/turn_valve;0", sep='')
        print(delay + 1200, ";/prepare", sep='')
        print('/reset_timer')


            

# notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notes = ["F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "x+1", "x+2", "x+3", "x+4"]

melody = parse_midi("midi_pirate2.mid")
file_path = 'output_pirate.txt'
sys.stdout = open(file_path, "w")

print("/show_info")
print("/prepare")
print("/turn_compressor;1")
print("/turn_valve;0")

generate_output(1)
