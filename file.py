def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

file_name = 'example.txt'
file_content = read_file(file_name)
print(file_content)
def read_first_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = []
        for i in range(n):
            line = file.readline()
            if not line:
                break
            lines.append(line.rstrip('\n'))
    return lines

file_name = 'example.txt'
n = 5
lines = read_first_n_lines(file_name, n)
for line in lines:
    print(line)
def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines[-n:]

file_name = 'example.txt'
n = 5
lines = read_last_n_lines(file_name, n)
for line in lines:
    print(line)
def count_words(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
    return len(words)

file_name = 'example.txt'
word_count = count_words(file_name)
print(f"Number of words: {word_count}")
def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    if n >= len(lines):
        return lines
    else:
        return lines[-n:]

file_name = 'example.txt'
n = 5
lines = read_last_n_lines(file_name, n)
for line in lines:
    print(line)
