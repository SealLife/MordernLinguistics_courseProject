"""
-nse: 19 / 248
-nce: 205 / 326

*** Use utf-8 to open this file ***
English sound
find the vowel before /s/ or /z/
only one word "posse" is not ended with /s,z/
change  to ə
the pronuncation at lease contains 3 phonemes
"""

from misc import *

vowels = ['eɪ', 'aɪ', 'ɔɪ', 'aʊ', 'əʊ', 'iə', 'ɛə', 'ʊə', 'iː', 'ɔː', 'ɜː', 'uː', 'ɑː', 'ɪ', 'ə', 'ɒ', 'ʊ', 'ʌ', 'ɛ', 'æ']


def find_pattern(pron_file: File_PATH, pos_file: File_PATH, out_file: File_PATH):
    vdict: dict[str, list[str]] = {}
    cdict: dict[str, list[str]] = {}
    posd: dict[str, list[str]] = FileOp.read_json(pos_file)
    wordpos: dict[str, str] = {}
    for p in posd:
        for w in posd[p]:
            wordpos[w] = p
    for line in FileOp.read_file_lines(pron_file):
        word, pron = line.strip().split('\t')
        if not pron[-1] in {'s', 'z'}:
            print(f'{word} not ended with s,z')
            continue
        wordinfo = f'{word}\t{pron}\t{wordpos[word]}'
        p1 = pron[-3:-1]
        if p1 in vowels:
            vdict.setdefault(p1, []).append(wordinfo)
        else:
            p2 = pron[-2]
            if p2 in vowels:
                vdict.setdefault(p2, []).append(wordinfo)
            else:
                cdict.setdefault(p2, []).append(wordinfo)
    vcnt: int = 0
    cntdict: dict[str, int] = {}
    msg: str = 'vowels\n'
    for k in vdict:
        msg += f'\t{k}\n'
        for v in vdict[k]:
            msg += f'\t\t{v}\n'
            vcnt += 1
            cntdict[k] = cntdict.setdefault(k, 0) + 1
    ccnt: int = 0
    msg += '\nconsonants\n'
    for k in cdict:
        msg += f'\t{k}\n'
        for v in cdict[k]:
            msg += f'\t\t{v}\n'
            ccnt += 1
            cntdict[k] = cntdict.setdefault(k, 0) + 1
    FileOp.write(out_file, msg)

    print(f'{pron_file.name} total: {vcnt + ccnt}')
    print(f'\tfollowing a vowel: {vcnt}\n\t\t', end='')
    vpl = [f'{k}: {cntdict[k]}' for k in vdict]
    vpl.sort(key=lambda x: int(x[x.find(':') + 2 :]), reverse=True)
    print(', '.join(vpl))
    print(f'\tfollowing a consonant: {ccnt}\n\t\t', end='')
    cpl = [f'{k}: {cntdict[k]}' for k in cdict]
    cpl.sort(key=lambda x: int(x[x.find(':') + 2 :]), reverse=True)
    print(', '.join(cpl))


def main():
    m = input('Enter mode: ')
    match m:
        case 'c':
            find_pattern(Wordbook.CE_PRON, OutputFile.CE_POS, OutputFile.CE_SOUND)
        case 's':
            find_pattern(Wordbook.SE_PRON, OutputFile.SE_POS, OutputFile.SE_SOUND)
        case 'cs':
            find_pattern(Wordbook.CE_PRON, OutputFile.CE_POS, OutputFile.CE_SOUND)
            find_pattern(Wordbook.SE_PRON, OutputFile.SE_POS, OutputFile.SE_SOUND)


if __name__ == '__main__':
    main()
