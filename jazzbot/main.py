from models import State, Chord, Scale
import config
import improvise

print(Chord.M7)

print(config)

state = State.State(config)

while state.position < len(state.chord_by_beat):
    improvise.improvise(state)
    state.tic()
