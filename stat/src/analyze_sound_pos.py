from misc import *


def analyze(sound_patt_file: File_PATH):
    lines = FileOp.read_file_lines(sound_patt_file)
    wd: dict[str, dict[str, int]] = {}
    now: str
    for line in lines:
        if line.startswith('\t\t'):
            word, pron, pos = line[2:-1].split('\t')
            ori = wd.setdefault(now, {}).setdefault(pos, 0)
            wd[now][pos] = ori+1
        elif line.startswith('\t'):
            now = line[1:-1]
    msg: str = ''
    for k in wd:
        msg += f'{k}:\t'
        total: int = 0
        for p in wd[k]:
            total += wd[k][p]
        dl = [f'{p}: {wd[k][p]} ({wd[k][p]/total:.0%})' for p in wd[k]]
        dl.sort(key=lambda x: int(
            x[x.find(':')+2:x.find('(')-1]), reverse=True)
        msg += ', '.join(dl)
        msg += '\n'
    print(msg)


def main():
    print('ce:')
    analyze(OutputFile.CE_SOUND_PATT)
    print('se:')
    analyze(OutputFile.SE_SOUND_PATT)


if __name__ == '__main__':
    main()
