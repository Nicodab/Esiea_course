import os
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def rc4(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256].to_bytes(1, byteorder='big')

def generate_keys(seed, num_keys):
    keys = []
    for _ in range(num_keys):
        key = [seed[i % len(seed)] for i in range(8)]
        keys.append(bytes(key))
    return keys

def analyze_distribution(keys, num_positions):
    position_frequencies = Counter()

    for key in keys:
        rc4_generator = rc4(key)
        for _ in range(num_positions):
            output = next(rc4_generator)
            position_frequencies[output[0]] += 1

    return position_frequencies

def plot_line_chart(position_frequencies):
    keys = list(position_frequencies.keys())
    values = list(position_frequencies.values())

    # Répartir les nombres sur l'axe des abscisses de 0 à 255
    x = np.arange(256)

    plt.plot(x, values, marker='o')
    plt.xlabel('Position de l\'octet')
    plt.ylabel('Fréquence d\'apparition')
    plt.title('Fréquence d\'apparition des positions des octets de 0 à 255')
    plt.grid(True)
    plt.show()

# 20 graines aléatoires
seeds = [os.urandom(8) for _ in range(20)]

# On génère une keystream pour chaque graine avec 10^6 itérations
keys = [key for seed in seeds for key in generate_keys(seed, 10**7)]

# On analyse la distribution des octets pour les 256 positions
position_frequencies = analyze_distribution(keys, 256)

# On trace un graphique en ligne avec répartition pour toutes les positions
plot_line_chart(position_frequencies)
plt.savefig("frequence_positions_octets_1e7.png")
