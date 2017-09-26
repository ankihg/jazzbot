class State:
    def __init__(self, config):
        self.config = config
        self.chords = config.chords
        # self.beats = reduce(lambda x, y: x.dur + y.dur, self.chords)
        self.chord_by_beat = self.build_chord_by_beat()
        self.position = 0

    def tic(self):
        self.position += self.config.beat_step

    def build_chord_by_beat(self):
        position = 0
        chord_by_beat = {}
        for chord in self.chords:
            start_pos = position
            while position < start_pos + chord.dur:
                chord_by_beat[position] = chord
                position += self.config.beat_step
        return chord_by_beat

    def chord(self):
        return self.chord_by_beat[self.position]
