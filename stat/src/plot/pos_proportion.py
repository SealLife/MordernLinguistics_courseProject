import matplotlib.pyplot as plt

pos = ['Noun', 'Verb', 'Adj', 'Adv', 'Others']
ce = [269, 44, 4, 6, 1]
se = [117, 91, 24, 5, 4]

plt.bar(pos, ce, label='ce', alpha=0.7)
plt.bar(pos, se, bottom=ce, label='se', alpha=0.7)
plt.xlabel('Part of Speech')
plt.ylabel('Frequency')
plt.legend()
plt.show()
