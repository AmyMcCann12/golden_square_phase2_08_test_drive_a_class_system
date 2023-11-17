from lib.music_library import MusicLibrary

"""
Initially there are no tracks
"""

def test_initially_has_no_tracks():
    music_library = MusicLibrary()
    assert music_library._tracks == []


"""
Searching for tracks initially gets an empty list
"""

def test_initially_searches_return_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title("hello") == []
