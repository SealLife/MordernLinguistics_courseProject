"""Convert the output file of tree-tagger to a json"""

from misc import *

pos_info: dict[str, str] = {
    'NN0': 'Noun',
    'NN1': 'Noun',
    'NN2': 'Noun',
    'VVB': 'Verb',
    'VVD': 'Verb',
    'VVI': 'Verb',
    'PRP': 'Prep',
    'AJ0': 'Adj',
    'AJC': 'Adj',
    'AJS': 'Adj',
    'AV0': 'Adv',
    'AVQ': 'Adv',
    'DT0': 'Det',
    'DTQ': 'Det',
    'CJS': 'Conj',
}


def analyze(tagged: File_PATH, output: File_PATH):
    tagged_lines = FileOp.read_file_lines(tagged)

    pos_words: dict[str, list[str]] = {}
    for line in tagged_lines:
        word, pos, _ = line.strip().split('\t')
        pos_words.setdefault(pos_info.get(pos, pos), []).append(word)

    FileOp.write_json(output, pos_words)
    pl = [f'{k}: {len(pos_words[k])}' for k in pos_words]
    pl.sort(key=lambda x: int(x[x.find(':') + 2 :]), reverse=True)
    print(f'{tagged.name}: {", ".join(pl)}')


def main():
    mode = input('Mode:\n\tc: ce_words\n\ts: se_words\n\tcs: both\n\tinf: inf_words\nEnter: ')
    match mode:
        case 'c':
            analyze(OutputFile.CE_TAGGED, OutputFile.CE_POS)
        case 's':
            analyze(OutputFile.SE_TAGGED, OutputFile.SE_POS)
        case 'cs':
            analyze(OutputFile.CE_TAGGED, OutputFile.CE_POS)
            analyze(OutputFile.SE_TAGGED, OutputFile.SE_POS)
        case 'inf':
            analyze(OutputFile.INF_TAGGED, OutputFile.INF_POS)


if __name__ == '__main__':
    main()
