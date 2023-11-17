import math

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        counter = 0
        for entry in self.entries:
            counter += entry.count_words()
        return counter

    def reading_time(self, wpm):
        total_words = self.count_words()
        return math.ceil(total_words / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        max_words_to_be_read = wpm * minutes
        best_entry_words = 0
        for entry in self.entries:
            if entry.count_words() <= max_words_to_be_read and entry.count_words() > best_entry_words:
                best_entry = entry
                best_entry_words = entry.count_words()
            if best_entry_words == 0:
                raise Exception("Diary entries are all too large for given parameters")
        return best_entry