def improvise(state):
    chord = state.chord()
    print('chord', chord)
    scale = chord.scale(state)
    print('scale', scale)
    print(scale.notes())
