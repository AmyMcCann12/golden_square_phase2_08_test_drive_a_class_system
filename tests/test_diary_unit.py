from lib.diary import Diary

"""
Initially there are no diary entries
"""

def test_diary_entries_empty_initially():
    diary = Diary()
    assert diary.entries == []

"""
Searching for all diary entries initially provides an empty list
"""

def test_diary_all_initially_empty():
    diary = Diary()
    assert diary.all() == []

"""
Initial word count with no diary entries is 0
"""

def test_word_count_initially_zero():
    diary = Diary()
    assert diary.count_words() == 0