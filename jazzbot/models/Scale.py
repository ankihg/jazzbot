class ScaleDef:
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

class Scale:
    def __init__(self, root, _def):
        self.root = root
        self._def = _def

    def notes(self):
        return map(lambda x: self.root + x, self._def.notes)

scales = {
    'major': ScaleDef('major', [0, 2, 4, 5, 7, 9, 11]),
    'dorian': ScaleDef('dorian', [0, 2, 3, 5, 7, 8, 11]),
    'dominant dominished': ScaleDef('dominant dominished', [0, 1, 3, 4, 6, 7, 9, 10]),
}
