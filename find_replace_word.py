import mmap
from collections import Counter

def find_replace_word(filename, replace_word):
    with open(filename, 'r+') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmapped_file:
            text = mmapped_file.read().decode('utf-8')
            words = text.split()

            # Find the most occurred word
            word_counts = Counter(words)
            most_common_word = word_counts.most_common(1)[0][0]

            # Replace the most occurred word with the replacement word
            replaced_text = text.replace(most_common_word, replace_word)

            # Move the file cursor to the beginning and truncate the file
            file.seek(0)
            file.truncate()

            # Write the replaced text to the file
            file.write(replaced_text.encode('utf-8'))

# Usage
find_replace_word('large_file.txt', 'loopr')
