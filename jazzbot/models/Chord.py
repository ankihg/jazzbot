import Scale

scale_for_chords = {
    'M7': Scale.scales['major'],
    '7': Scale.scales['dominant dominished'],
    'm7': Scale.scales['dorian'],
}

print(scale_for_chords)

class ChordDef(object):
    def __init__(self, name, third=4, fifth=7, seventh=11):
        self.name = name
        self.root = 0
        self.third = third
        self.fifth = fifth
        self.seventh = seventh
        self.scale_def = scale_for_chords[self.name]

    def chord_tones(self):
        return [self.root, self.third, self.fifth, self.seventh]

M7 = ChordDef('M7')
_7  = ChordDef('7', seventh=10)
m7 = ChordDef('m7', 3, 7, 10)

class Chord(object):
    def __init__(self, root, _def, dur):
        self.root = root
        self._def = _def
        self.dur = dur

    def notes(self):
        return map(lambda x: self.root + x, self._def.chord_tones())

    def play(self, octv=5):
        return map(lambda x: Note(x, octv, self.dur), self.notes())

    def scale(self, state):
        return Scale.Scale(self.root, self._def.scale_def)
