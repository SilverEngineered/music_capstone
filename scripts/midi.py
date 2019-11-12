import mido
import pickle
mid = mido.MidiFile('sw.mid')

midis =[i for i in  mid.play()]
filtered_midi = []

save_channel = 2

abs_midis = []
time = 0
for i in midis:
	if i.time:
		time += i.time
		i.time =time
	abs_midis.append(i)
for i in abs_midis:
	if i.type is 'note_on':
		if i.channel is save_channel:
			filtered_midi.append(i)

prev_time = 0
times = []
notes = [[]]
for i in filtered_midi:
	if i.time is prev_time:
		notes[-1].append(i.note)
	else:
		time = i.time
		times.append(time)
		notes.append([i.note])

pickle.dump(({'notes': notes,'times': times}), open( "swmid.p", "wb" ) )
'''
mini = 100

with open('swmid.p', 'rb') as pickle_file:
    content = pickle.load(pickle_file)


for i in notes:
	for j in i:
		if j < mini:
			mini = j


maxi = 0
for i in notes:
	for j in i:
		if j > maxi:
			maxi = j
			'''