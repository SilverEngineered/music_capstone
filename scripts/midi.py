import mido
import pickle
mid = mido.MidiFile('../Resources/midi/sw.mid')

midis =[i for i in  mid.play()]
filtered_midi = []

channel_nums = []

for i in midis:
	if i.type is 'note_on':
		channel_nums.append(i.channel)

num_channels = max(channel_nums)

best_channel = 0
max_variety = 0

for i in range(num_channels):
	this_channel_messages = []
	notes = []
	for message in midis:
		if message.type is 'note_on':
			if message.channel is i:
				this_channel_messages.append(message)
	for message in this_channel_messages:
		if message.type is 'note_on':
			notes.append(message.note)
	num_diff_notes = len(set(notes))
	if num_diff_notes > max_variety:
		max_variety = num_diff_notes
		best_channel = i

				
#save_channel = best_channel
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

pickle.dump(({'notes': notes, 'times': times}), open("../Resources/midi_dumps/swmid.p", "wb"))
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
