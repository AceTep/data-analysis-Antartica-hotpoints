import numpy as np
import pandas as pd

# Učitavanje podataka iz .csv datoteke
df = pd.read_csv('dataset.csv')

# Izdvajanje stupaca za analizu
brightness = df['brightness']
scan = df['scan']
track = df['track']
bright_t31 = df['bright_t31']
frp = df['frp']

# 1. Izračunavanje srednje vrijednosti (prosječne vrijednosti) temperature požara.
mean_brightness = np.mean(brightness)
print("Srednja vrijednost intenziteta požara:", mean_brightness)

# 2. Pronalaženje maksimalne i minimalne vrijednosti temperature požara.
max_brightness = np.max(brightness)
min_brightness = np.min(brightness)
print("Maksimalna vrijednost intenziteta požara:", max_brightness)
print("Minimalna vrijednost intenziteta požara:", min_brightness)

# 3. Izračunavanje standardne devijacije temperature požara.
std_dev_brightness = np.std(brightness)
print("Standardna devijacija intenziteta požara:", std_dev_brightness)

# 4. Sortiranje podataka po intenzitetu požara.
sorted_brightness = np.sort(brightness)
print("Sortirani intenziteti požara:", sorted_brightness)

# 5. Izračunavanje korelacije između intenziteta požara i temperature.
correlation = np.corrcoef(brightness, bright_t31)[0, 1]
print("Korelacija između intenziteta požara i temperature:", correlation)

# 6. Izračunavanje mediane temperature požara.
median_brightness = np.median(brightness)
print("Medijan intenziteta požara:", median_brightness)


df_filtered = df[df['type'].isin([0, 1, 2, 3])]

# Izdvajanje atributa za analizu
type_of_fire = df_filtered['type']

# Izračunavanje korelacije
correlation_type_brightness = np.corrcoef(type_of_fire, brightness)[0, 1]
print("Korelacija između tipa požara i temperature požara:", correlation_type_brightness)


# https://www.kaggle.com/datasets/brsdincer/antarctica-hotpoints-20002021climate-change-nasa