import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

names = [
    'əʊ',
    'aʊ',
    'uː',
    'eɪ',
    'aɪ',
    'ɜː',
    'iː',
    'ɔː',
    'ə',
    'ɛ',
    'ɪ',
    'ɔɪ',
    'ɑː',
    'ɒ',
    'p',
    'n',
    'l'
]
nouns = [8, 20, 11, 12, 11, 4, 7, 12, 2, 1, 4, 1, 2, 1, 6, 12, 2]
verbs = [19, 5, 16, 8, 15, 9, 7, 2, 1, 0, 1, 1, 1, 0, 2, 3, 1]

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax2.plot(np.array(verbs)/nouns, color='green', alpha=.8)
ax2.plot(np.array([85/124]*len(nouns)), 'k--', alpha=.8)
ax2.set_ylabel('Ratio (verbs/nouns)')
ax2.set_ybound(0., 3.)

ax1.bar(names, nouns, label='Nouns', alpha=0.5)
ax1.bar(names, verbs, bottom=nouns, label='Verbs', alpha=0.5)
ax1.set_xlabel('Vowels and consonants followed by -se')
ax1.set_ylabel('Frequency')
ax1.legend()
plt.show()
