# Projekts programmēšanā
Versija 0.2.1

Programma, kas pēc lietotāja vajadzībām atrod
izdevīgākās un pieejamākās bankas, kur apmainīt valūtu no EUR uz USD
nejuridiskām vajadzībām.

## Programmatūras lietošanas instrukcija

Lai lietotu programmatūru, uz operētājsistēmas jābut instalētam Python interpretētājam, un tam jābut atrodamam PATH vides mainīgajā (environmental variable).
Python var lejupielādēt [šeit](https://www.python.org/downloads/) vai arī izmantojot paku pārvaldītāju (package manager), skatoties pec operētājsistēmas.

Lai palaistu programmatūru, veiciet komandu no komandlīnijas interfeisa:

```
python projekta_programma.py
```

Pašiem jāpiegādā banku (no EUR uz USD) valūtas kursu datubāze (`val-kursi.csv`) CSV faila formātā, ja nepieciešami jaunāki valūtas kursi.
