import pytest #type: ignore
from lib.diary_entry import DiaryEntry

"""
Construct a diary entry and get the title and contents of the diary entry
"""

def test_construct_diary_entry_and_get_title_and_contents():
    diary_entry = DiaryEntry("My Diary", "This is the contents of my diary")
    assert diary_entry.title == "My Diary"
    assert diary_entry.contents == "This is the contents of my diary"

"""
Create a diary entry and count the number of words in the diary entrys contents
"""
def test_word_count_for_contents():
    diary_entry = DiaryEntry("My Diary", "This is the contents of my diary")
    assert diary_entry.count_words() == 7

"""
Create a diary entry and calculate the time if will take to read that entry
"""

def test_reading_time_for_contents():
    diary_entry = DiaryEntry("My Diary", "one two three four five six seven eight nine ten")
    assert diary_entry.reading_time(3) == 4

"""
Create a diary entry and if wpm is zero when 
reading_time is called, raise an error.
"""
def test_reading_time_when_wpm_is_zero():
    diary_entry = DiaryEntry("My Diary", "one two three four five six seven eight nine ten")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "wpm cannot be zero, no reading time can be calculated"

"""
Create a diary entry and request one reading chunk
"""
def test_reading_chunk_one_call():
    diary_entry = DiaryEntry("My Diary", "one two three four five six seven eight nine ten")
    assert diary_entry.reading_chunk(3,2) == "one two three four five six"

"""
Create a diary entry and request two reading chunks; the second reading chunk call
should skip the amount that has already been read
"""
def test_reading_chunk_two_calls():
    diary_entry = DiaryEntry("My Diary", "one two three four five six seven eight nine ten")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,3) == "three four five six seven eight"

"""
Create a diary entry and test reading chunk wraps around 
when end of contents has been reached
"""

def test_reading_chunk_wraps_around():
    diary_entry = DiaryEntry("My Diary", "one two three four five six seven eight nine ten")
    assert diary_entry.reading_chunk(4,2) == "one two three four five six seven eight"
    assert diary_entry.reading_chunk(3,1) == "nine ten"
    assert diary_entry.reading_chunk(2,1) == "one two"