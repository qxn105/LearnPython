import os
dir = f'{os.path.dirname(__file__)}/'

def missing_files(filename):
    with open(dir+'missing_files.txt', 'a', encoding='utf-8') as f:
        f.write(f'{filename}\n')

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        missing_files(filename) #pass # print(f'File not found: "{filename}"')
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

book_list = ['siddhartha.txt', 'alice.txt', 'moby_dick.txt', 'little_women.txt']
for book in book_list:
    count_words(dir+book)

