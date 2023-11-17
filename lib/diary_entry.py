import math

class DiaryEntry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.start_reading = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("wpm cannot be zero, no reading time can be calculated")
        reading_time_count = math.ceil(len(self.contents.split()) / wpm)
        return reading_time_count

    def reading_chunk(self, wpm, minutes):
        reading_chunk_size = wpm * minutes
        reading_chunk = self.contents.split()[self.start_reading:(self.start_reading+ reading_chunk_size)]
        if self.start_reading + reading_chunk_size >= len(self.contents.split()):
            self.start_reading = 0
        else:
            self.start_reading += reading_chunk_size
        return " ".join(reading_chunk)
