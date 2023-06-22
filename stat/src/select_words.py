""" Select words that consist of only letter. Repeated words are ommited as well """
from misc import *


def main():
    # alphabet list
    alpha = range(ord('a'), ord('z')+1)
    all_alpha_words: list[str] = []

    lines = FileOp.read_file_lines(Wordbook.COCA20000)
    for line in lines:
        for c in line.strip():
            if ord(c.lower()) not in alpha:
                break
        else:
            all_alpha_words.append(line.strip())
    all_alpha_words = list(set(all_alpha_words))
    FileOp.write(Wordbook.SEL_WORDS, '\n'.join(all_alpha_words))

    print(f'all_alpha_words: {len(all_alpha_words)}')


if __name__ == '__main__':
    main()
