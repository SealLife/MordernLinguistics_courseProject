import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

names = [
    'aɪ',
    'iː',
    'ɪ',
    'eɪ',
    'ɔɪ',
    'uː',
    'ɜː',
    'ɔː',
    'ə',
    'ɑː',
    'ɛ'
]
nouns = [11, 9, 28, 19, 3, 3, 1, 6, 4, 1, 0]
verbs = [2, 0, 3, 8, 1, 8, 1, 3, 1, 0, 2]

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax2.plot(np.array(verbs)/nouns, color='green', alpha=.8)
ax2.plot(np.array([47/264]*len(nouns)), 'k--', alpha=.8)
ax2.set_ylabel('Ratio (verbs/nouns)')
ax2.set_ybound(0., 3.)

ax1.bar(names, nouns, label='Nouns', alpha=0.5)
ax1.bar(names, verbs, bottom=nouns, label='Verbs', alpha=0.5)
ax1.set_xlabel('Vowels followed by -ce')
ax1.set_ylabel('Frequency')
ax1.legend()
plt.show()
