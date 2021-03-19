class Kluda(Exception):
   pass

val_apm_veids = None
vai_atr_pie_ielas = None
velme_redz_nak_rezult = None


print("Programma, kas pēc lietotāja vajadzībām atrod izdevīgākās un pieejamākās bankas, kur apmainīt naudu no EUR uz USD nejuridiskām vajadzībām.\n")

# val_apm_veids = vai lietotājs apmainīs valūtu skaidrā veidā vai caur bankas pārskaitījumu?
while True:
   try: 
      val_apm_veids = int(input("Ievadiet 1, ja jūs apmainīsiet valūtu skaidrā veidā\nIevadiet 2, ja jūs apmainīsiet valūtu caur bankas pārskaitījumu\n"))    
      if val_apm_veids < 1:
         raise Kludaj
      elif val_apm_veids > 2:
         raise Kluda
      break
   except:
      print("Lūdzu ievadiet 1 vai 2.\n")

# ja lietotājs apmaina val caur skaidru naudu un atrodas Rīgā, vai_atr_pie_ielas = vai lietotājs atrodas tuvumā pie Latvijas Bankas?
if val_apm_veids == 1:
   atr_vieta = input("Ievadiet jūsu atrašanās vietu\n")
   if atr_vieta.strip() == "Rīga" or atr_vieta.strip() == "Riga":
      while True:
         try:
            vai_atr_pie_ielas = int(input("Ievadiet 1, ja jūs atrodaties tuvumā pie K. Valdemāra ielas 2A. Ja neatrodaties, ievadiet 2.\n"))
            if vai_atr_pie_ielas < 1:
               raise Kluda
            elif vai_atr_pie_ielas > 2:
               raise Kluda
            break
         except:
            print("Lūdzu ievadiet 1 vai 2.\n")

# ja lietotājs atrodas tuvumā pie Latvijas Bankas, velme_redz_nak_rezult = vai lietotājs vēlas redzēt citas bankas, kur apmainīt naudu? 
if vai_atr_pie_ielas == 1:
   print("\nVisizdevīgākā un pieejamākā vieta, kur apmainīt valūtu ir Latvijas Banka.\n")
   while True:
      try:
         velme_redz_nak_rezult = int(input("Ja jūs vēlaties redzēt citas bankas, kuras būtu izdevīgi apmainīt naudu, ievadiet 1. Ja nevēlaties, ievadiet 2.\n"))
         if velme_redz_nak_rezult < 1:
            raise Kluda
         elif velme_redz_nak_rezult > 2:
            raise Kluda
         break
      except:
         print("Lūdzu ievadiet 1 vai 2.\n")

if velme_redz_nak_rezult == 1:
   print("Izdevīgākās bankas")
elif velme_redz_nak_rezult == 2:
   exit()