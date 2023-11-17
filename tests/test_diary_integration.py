import pytest #type: ignore

from lib.diary_entry import DiaryEntry
from lib.diary import Diary

"""
When we add one diary entry, we can get back that diary entry.
"""

def test_add_a_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry("My Diary Title", "My Diary Contents" )
    diary.add(diary_entry)
    assert diary.entries == [diary_entry]

"""
When we add an two diary entries, and we call the 'all' method, we get a list of 
the two diary entries that have been added
"""
def test_add_two_entries_and_run_all():
    diary = Diary()
    diary_entry_1 = DiaryEntry("My Diary Title 1", "My Contents 1")
    diary_entry_2 = DiaryEntry("My Diary Title 2", "My Contents 2")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry_1 , diary_entry_2]

"""
When we add two diary entries, and count the words, we get back the total number of 
words in both diary entries
"""
def test_add_two_entries_and_count_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry("My Diary 1", "one two three four")
    diary_entry_2 = DiaryEntry("My Diary 2", "one two three four five six")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 10

"""
When we add 3 diary entries, and we look at the reading time, 
we get back the estimated length of time (integer) for the user to read all 3 diary entries
"""
def test_add_three_entries_and_calculate_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("My Diary 1", "one two three four")
    diary_entry_2 = DiaryEntry("My Diary 2", "one two three four five six")
    diary_entry_3 = DiaryEntry("My Diary 3", "one two three four five")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.reading_time(4) == 4

"""
When we add four diary entries, given a wpm of 4 and number of minutes 2,
provides us with the closest entry to 8 words
"""

def test_add_four_entries_and_finds_best_entry_for_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("My Diary 1", "one two three four")
    diary_entry_2 = DiaryEntry("My Diary 2", "one two three four five six seven")
    diary_entry_3 = DiaryEntry("My Diary 3", "one two three four five")
    diary_entry_4 = DiaryEntry("My Diary 4", "one two three")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    diary.add(diary_entry_4)
    assert diary.find_best_entry_for_reading_time(2,3) == diary_entry_3

def test_add_two_entries_and_finds_best_entry_for_reading_time_where_entry_matches():
    diary = Diary()
    diary_entry_1 = DiaryEntry("My Diary 1", "one two three four")
    diary_entry_2 = DiaryEntry("My Diary 2", "one two three four five six seven")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.find_best_entry_for_reading_time(4,1) == diary_entry_1

def test_add_two_entries_and_both_too_large_to_find_best_entry_for_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("My Diary 1", "one two three four")
    diary_entry_2 = DiaryEntry("My Diary 2", "one two three four five six seven")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2,1)
    assert str(e.value) == "Diary entries are all too large for given parameters"