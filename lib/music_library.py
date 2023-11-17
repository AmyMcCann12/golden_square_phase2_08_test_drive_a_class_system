class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)
    
    def search_by_title(self, keyword):
        return [track for track in self._tracks if keyword in track.title]
