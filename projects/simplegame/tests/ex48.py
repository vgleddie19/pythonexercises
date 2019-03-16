class lexicon(object):
    def __init__(sefl,name,description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(sefl, direction):
        return self.paths.get(direction,None)

    def add_paths(self, paths):
        self.paths.update(paths)

