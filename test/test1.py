import sys

from urllib.request import urlopen


def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            #line_words = line.split()                  # as bytes
            line_words = line.decode('utf-8').split()   # as strings
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    # comment to test push
    # another comment to test push
    # another comment to test push2
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    #'http://sixty-north.com/c/t.txt'
    main(sys.argv[1])
