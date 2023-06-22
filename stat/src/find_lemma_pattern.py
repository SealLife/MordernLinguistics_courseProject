"""
-ce and -se are common affixes of nouns, while -t of adjectives.
So I searched all the nouns to check if they have a -t inflection
"""
from misc import *


def analyze_t_adj(pos_file: File_PATH, out_file: File_PATH):
    inf_adj: list[str] = FileOp.read_json(OutputFile.INF_POS)['Adj']
    sam_nouns: list[str] = FileOp.read_json(pos_file)['Noun']
    has: list[str] = []
    hasnot: list[str] = []

    for w in sam_nouns:
        t = w[:-2]+'t'
        # mannually check some words
        if t in inf_adj and w not in {
            'ambulance',
            'face',
            'fleece',
            'hose',
            'curse',
            'grease'
        }:
            has.append(w)
        else:
            hasnot.append(w)

    msg: str = ''
    for w in has:
        msg += f'{w}\n\t{w[:-2]+"t"}\n'
    msg += '\n'
    for w in hasnot:
        msg += f'{w}\n'
    FileOp.write(out_file, msg)
    print(
        f'{pos_file.name} total: {len(sam_nouns)}\n\t{len(has)} nouns has t-adj, {len(sam_nouns)-len(has)} hasn\'t'
    )


def main():
    m = input('Mode:\n\tc: -ce\n\ts: -se\n\tcs: both\nEnter: ')
    match m:
        case 'c':
            analyze_t_adj(OutputFile.CE_POS, OutputFile.CE_N_ADJ)
        case 's':
            analyze_t_adj(OutputFile.SE_POS, OutputFile.SE_N_ADJ)
        case 'cs':
            analyze_t_adj(OutputFile.CE_POS, OutputFile.CE_N_ADJ)
            analyze_t_adj(OutputFile.SE_POS, OutputFile.SE_N_ADJ)


if __name__ == '__main__':
    main()
