import mmap

def read_large_file(filename):
    with open(filename, 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmapped_file:
            # Iterate over the memory-mapped file line by line
            for line in iter(mmapped_file.readline, b''):
                # Process each line as needed
                line = line.decode('utf-8')
                # Do something with the line, e.g., print it
                print(line, end='')

# Usage
read_large_file('large_file.txt')
