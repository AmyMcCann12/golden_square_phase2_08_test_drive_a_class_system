from lib.music_library import MusicLibrary
from lib.track import Track

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_adds_two_tracks_and_lists_them():
    library = MusicLibrary()
    track_1 = Track("Track Title 1", "Artist 1")
    track_2 = Track("Track Title 2", "Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library._tracks == [track_1, track_2]


"""
When we add two tracks, and search for the title of one of the tracks
I get that track back in the results
"""

def test_searches_by_title():
    library = MusicLibrary()
    track_1 = Track("Track Title 1", "Artist 1")
    track_2 = Track("Track Title 2", "Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Track Title 2") == [track_2]


"""
Given I add two tracks, if I search for part of the title
of one of the tracks, I get the matching track back in the results
"""

def test_searches_by_part_of_title():
    library = MusicLibrary()
    track_1 = Track("Track Title 1", "Artist 1")
    track_2 = Track("Track Title 2", "Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("1") == [track_1]

"""
Given I add two tracks, if I search for a word not in any track title, 
we get an empty list back
"""
def test_searches_by_word_not_in_title():
    library = MusicLibrary()
    track_1 = Track("Track Title 1", "Artist 1")
    track_2 = Track("Track Title 2", "Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("the") == []
