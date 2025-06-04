import json
from enum import Enum
from pathlib import Path
from typing import IO, Any

REL_MAT_PATH = Path('material')
OUT_PATH = Path('output')


class File_PATH(Enum): ...


class Wordbook(File_PATH):
    COCA20000 = REL_MAT_PATH / 'coca20000.txt'
    INF2OF12 = REL_MAT_PATH / '2of12inf.txt'
    SEL_WORDS = REL_MAT_PATH / 'selected_words.txt'
    INF_WORDS = REL_MAT_PATH / 'inf_words.txt'
    CE_WORDS = REL_MAT_PATH / 'ce_words.txt'
    SE_WORDS = REL_MAT_PATH / 'se_words.txt'
    CE_PRON = REL_MAT_PATH / 'ce_pronunciation.txt'
    SE_PRON = REL_MAT_PATH / 'se_pronunciation.txt'


class OutputFile(File_PATH):
    INF_TAGGED = OUT_PATH / 'inf_tagged.txt'
    INF_POS = OUT_PATH / 'inf_pos.json'
    CE_TAGGED = OUT_PATH / 'ce_tagged.txt'
    CE_POS = OUT_PATH / 'ce_pos.json'
    CE_N_ADJ = OUT_PATH / 'ce_n_adj.txt'
    CE_SOUND = OUT_PATH / 'ce_sound_patt.txt'
    CE_SOUND_PATT = OUT_PATH / 'ce_sound_patt.txt'
    SE_TAGGED = OUT_PATH / 'se_tagged.txt'
    SE_POS = OUT_PATH / 'se_pos.json'
    SE_N_ADJ = OUT_PATH / 'se_n_adj.txt'
    SE_SOUND = OUT_PATH / 'se_sound_patt.txt'
    SE_SOUND_PATT = OUT_PATH / 'se_sound_patt.txt'


class FileOp:
    def __init__(self, path: File_PATH, mode: str) -> None:
        self.f: IO[Any]
        self.path = path
        self.mode = mode

    @classmethod
    def open(cls, path: File_PATH, mode: str = 'r'):
        return cls(path, mode)

    @classmethod
    def write(cls, path: File_PATH, data: str):
        with cls.open(path, 'w') as f:
            f.write(data)

    @classmethod
    def read_file_lines(cls, path: File_PATH) -> list[str]:
        with cls.open(path) as f:
            return f.readlines()

    @classmethod
    def write_json(cls, path: File_PATH, obj: Any):
        with cls.open(path, 'w') as f:
            json.dump(obj, f, indent=4)

    @classmethod
    def read_json(cls, path: File_PATH):
        with cls.open(path) as f:
            return json.load(f)

    def __enter__(self):
        self.f = open(self.path.value, self.mode, encoding='utf-8')
        return self.f

    def __exit__(self, type_, value, trace):
        self.f.close()
