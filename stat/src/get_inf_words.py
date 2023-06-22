from misc import *


def main():
    words: list[str] = []
    lines = FileOp.read_file_lines(Wordbook.INF2OF12)
    for line in lines:
        line = line.strip()
        for c in line:
            if not c.isalpha():
                break
        else:
            # only unannotated words are considered
            words.append(line)
    FileOp.write(Wordbook.INF_WORDS, '\n'.join(words))
    print(f'inf_words: {len(words)}')


if __name__ == '__main__':
    main()
