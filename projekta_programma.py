import csv
import operator

def getAnswer(x,input_string):
   """Iegūst mainīgajam x vērtību 1 vai 2, parādot tekstu input_string.
      Ja ievadīta nepareiza vērtība, tad tiek paradīta kļūdas ziņa."""
   while True:
      try:
         x = int(input(input_string))
         if x < 1:
            raise ValueError
         elif x > 2:
            raise ValueError
         break
      except:
         print("Lūdzu ievadiet 1 vai 2.\n")
   return x
         
val_apm_veids = None
vai_atr_pie_ielas = None
velme_redz_nak_rezult = None


print("Programma, kas pēc lietotāja vajadzībām atrod izdevīgākās un pieejamākās bankas, kur apmainīt naudu no EUR uz USD nejuridiskām vajadzībām.\n")

# val_apm_veids = vai lietotājs apmainīs valūtu skaidrā veidā vai caur bankas pārskaitījumu?
val_apm_veids = getAnswer(val_apm_veids,"Ievadiet 1, ja jūs apmainīsiet valūtu skaidrā veidā\nIevadiet 2, ja jūs apmainīsiet valūtu caur bankas pārskaitījumu\n")

# ja lietotājs apmaina val caur skaidru naudu un atrodas Rīgā, vai_atr_pie_ielas = vai lietotājs atrodas tuvumā pie Latvijas Bankas?
if val_apm_veids == 1:
   atr_vieta = input("\nIevadiet jūsu atrašanās vietu\n")
   if atr_vieta.strip().lower() == "rīga" or atr_vieta.strip().lower() == "riga":
      vai_atr_pie_ielas = getAnswer(vai_atr_pie_ielas,"\nIevadiet 1, ja jūs atrodaties tuvumā pie K. Valdemāra ielas 2A. Ja neatrodaties, ievadiet 2.\n")

# ja lietotājs atrodas tuvumā pie Latvijas Bankas, velme_redz_nak_rezult = vai lietotājs vēlas redzēt citas bankas, kur apmainīt naudu? 
if vai_atr_pie_ielas == 1:
   print("\nVispieejamākā vieta, kur apmainīt valūtu ir Latvijas Banka.\n")
   velme_redz_nak_rezult = getAnswer(velme_redz_nak_rezult,"Ja jūs vēlaties redzēt visas bankas, kurās būtu izdevīgi apmainīt naudu, ievadiet 1. Ja nevēlaties, ievadiet 2.\n")
else: # citādāk, ja lietotājs neatrodas tuvumā pie LB, tad ir vēlme redzēt citas bankas, kur apmainīt naudu
   velme_redz_nak_rezult = 1

# ja lietotājs vēlas redzēt banku izdevīguma tabulu (ja lietotājs atrodas pie LB) vai neatrodas pie Latvijas Bankas, tad tā tiek parādīta
if velme_redz_nak_rezult == 1:
   try: val_kursi = csv.reader(open("val-kursi.csv"), delimiter=",")
   except: print("Kļūme datubāzes lasīšanā! Datubāzes failam jābūt CSV formātā kā 'val-kursi.csv'.\n")
   # sakārto valūtu kursu datubāzi augošā secībā
   val_kursi_sorted = sorted(val_kursi, key=operator.itemgetter(1), reverse=True) 
   # izvada sakārtotu izdevīgāko banku tabulu augošā secībā pēc valūtas kursiem 
   print("\n  Izdevīgāko banku tabula:")
   for Banka, Kurss in val_kursi_sorted:
      print("{:<21} {:<15}".format(Banka,Kurss))      
   exit()
else: exit()