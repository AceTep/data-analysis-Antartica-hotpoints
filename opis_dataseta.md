### Opis dataseta

#### Antarctica Hotpoints 2000-2021/Climate Change NASA

Ovaj skup podataka sadrži informacije o "hotpoints"-ima na Antarktici tijekom razdoblja od 2000. do 2021. godine, prikupljene od strane NASA-e. "Hotpoints" se odnose na lokacije na Antarktici na kojima su detektirane izuzetno visoke temperature ili požari.

Link: [Antarctica Hotpoints Dataset](https://www.kaggle.com/datasets/brsdincer/antarctica-hotpoints-20002021climate-change-nasa)

#### Atributi

- **Latitude**: Geografska širina centra detektiranog "hotpointa".
- **Longitude**: Geografska dužina centra detektiranog "hotpointa".
- **Brightness**: Temperatura detektiranog "hotpointa", izražena u određenim jedinicama (npr. Kelvin).
- **Scan**: Veličina "hotpointa" duž osi skeniranja.
- **Track**: Veličina "hotpointa" duž osi praćenja.
- **Acq_Date**: Datum detekcije "hotpointa".
- **Acq_Time**: Vrijeme detekcije "hotpointa" u UTC vremenskoj zoni.
- **Satellite**: Satelit koji je detektirao "hotpoint".
- **Confidence**: Pouzdanost detekcije "hotpointa", izražena kao niska, srednja ili visoka.
- **Bright_t31**: Temperatura požara detektiranog infracrvenim senzorom, izražena u određenim jedinicama (npr. Kelvin).
- **FRP**: Fire Radiative Power (požarni radijacijski kapacitet), izražen u megavatima.
- **Type**: Tip detektiranog "hotpointa", koji može biti: 
  - 0 = pretpostavljeni požar vegetacije
  - 1 = aktivan vulkan
  - 2 = drugi statički kopneni izvor
  - 3 = detekcija iznad vode.