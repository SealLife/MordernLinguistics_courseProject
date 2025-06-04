"""Find ce and se words"""

from misc import *


def main():
    all_words: list[str] = FileOp.read_file_lines(Wordbook.SEL_WORDS)
    ce_words: list[str] = []
    se_words: list[str] = []
    for word in all_words:
        word = word.strip()
        # Proper names not considered
        if not word.islower():
            continue
        if word[-2:] == 'ce':
            # mannually omit some words
            if word == 'fiance':
                continue
            ce_words.append(word)
        elif word[-2:] == 'se':
            se_words.append(word)
    FileOp.write(Wordbook.CE_WORDS, '\n'.join(ce_words))
    FileOp.write(Wordbook.SE_WORDS, '\n'.join(se_words))

    print(f'-ce: {len(ce_words)}, -se: {len(se_words)}')


if __name__ == '__main__':
    main()
