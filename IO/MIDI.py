import mido
import rtmidi

if __name__ == '__main__': 

    inputs = mido.get_input_names()
    with mido.open_input(inputs[0]) as port:
        for msg in port:
            print (msg)
