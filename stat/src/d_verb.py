from misc import *


def analyze_d_verb(pos_file: File_PATH, out_file: File_PATH):
    inf_verb: list[str] = FileOp.read_json(OutputFile.INF_POS)['Verb']
    sam_nouns: list[str] = FileOp.read_json(pos_file)['Noun']
    has: list[str] = []
    hasnot: list[str] = []

    for w in sam_nouns:
        t = w[:-2]+'d'
        # mannually check some words
        if t in inf_verb:
            has.append(w)
        else:
            hasnot.append(w)

    msg: str = ''
    for w in has:
        msg += f'{w}\n\t{w[:-2]+"d"}\n'
    msg += '\n'
    for w in hasnot:
        msg += f'{w}\n'
    # FileOp.write(out_file, msg)
    print(msg)
    print(
        f'{pos_file.name} total: {len(sam_nouns)}\n\t{len(has)} nouns has t-adj, {len(sam_nouns)-len(has)} hasn\'t'
    )


def main():
    analyze_d_verb(OutputFile.CE_POS, ...)


if __name__ == '__main__':
    main()
