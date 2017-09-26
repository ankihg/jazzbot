from pyknon.pyknon.genmidi import Midi
from pyknon.pyknon.music import Note, NoteSeq
import random

class ChordDef(object):
    def __init__(self, name, third=4, fifth=7, seventh=11):
        self.name = name
        self.root = 0
        self.third = third
        self.fifth = fifth
        self.seventh = seventh

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

dm7 = Chord(2, m7, .5)
g7 = Chord(7, _7, .5)
cM7 = Chord(0, M7, 1)

# print(m7.chord_tones())
# print(dm7.notes())

# seq = NoteSeq(dm7.play(1))
# seq1 = NoteSeq(g7.play(1))
# seq2 = NoteSeq(cM7.play(1))
# print(seq)


durs = [.125, .125, .125, .25, .25, .5]

def any(arr):
    return arr[random.randrange(0, len(arr))]

def improvise(chords):
    improv = []
    for chord in chords:
        dur = 0
        while dur < chord.dur:
            n = any(chord.notes())
            d = any(durs)
            # print(n)
            # print(d)
            note = Note(n, 5, d).octavate(2)
            # note = Note(2, 5, .25)
            improv.append(note)
            dur += note.dur

    return NoteSeq(improv)


chords = [Chord(2, m7, 1), Chord(7, _7, 1), Chord(0, M7, 2)]
improv = improvise(chords)
chords = map(lambda x: NoteSeq(x.play()), chords)
print(chords)
print(improv)


midi = Midi(2)
midi.seq_notes(improv, track=0)
midi.seq_chords(chords, track=1)
midi.write('me.mid')



#
# # wholetone = NoteSeq([Note(x) for x in range(0,12,2)])
#
# maj_notes = [Note(0), Note(2), Note(4), Note(5), Note(7), Note(9), Note(11)]
# maj = NoteSeq(maj_notes)
#
# c3 = Note(0, 5, .25)
# d3 = Note(2, 5, .25)
# g3 = Note(7, 5, .25)
#
#
# dm7 = NoteSeq(d3.div_volume().harmonize(maj, size=4))
# g7 = NoteSeq(g3.div_volume().harmonize(maj, size=4))
# cM7 = NoteSeq(c3.div_volume().harmonize(maj, size=4))
#
# chords = [dm7, dm7, g7, g7, cM7, cM7, cM7, cM7]
#
#
# improv = NoteSeq([maj_notes[random.randrange(0, len(maj_notes))].octavate(2)  for i in range(0, 8)])
#
#
# midi = Midi(2)
# midi.seq_notes(improv, track=0)
# midi.seq_chords(chords, track=1)
# midi.write('me.mid')


### modeling
# for each chord, a set of scales, ranked by dissonance
# m7: m7 chord tones, m pentatonic, m dorian
# 7: 7 chord tones, dominant diminished
#

### feedback
# pitch momentum
# dissonance


# repeat rhythm

# transpose motif

# arppegiate
