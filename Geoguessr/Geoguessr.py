import json
import os
def reset():
   for c in CountryList:
      c.cget = 0
      c.durschnitt = 0 
      c.camount = 0 
      c.gscore = 0
   main()
def Speichern():

 if os.path.exists("countries.json"):
   print("Die Datei existiert bereits und wird überschrieben.")

   with open("countries.json", "w", encoding="utf-8") as f:
    json.dump(
        [{"name": c.country, "camount": c.camount, "cget": c.cget, "gscore": c.gscore, "durschnitt": c.durschnitt } for c in CountryList],
        f,
        ensure_ascii=False,
        indent=2
    )
 else:     
    with open("countries.json", "w", encoding="utf-8") as f:
    # Wir speichern nur die relevanten Daten für JSON
      json.dump(
        [{"name": c.country, "camount": c.camount, "cget": c.cget, "gscore": c.gscore, "durschnitt": c.durschnitt} for c in CountryList],
        f,
        ensure_ascii=False,
        indent=2
    )
    print("countries.json wurde erstellt!")

def menu():
  print("Drücke 1 um Daten einzulesen")
  print("Drücke 2 um Daten auszulesen")
  print("Drücke 3 um zu Datei zu speichern")
  print("Drücke 4 um Daten zu reseten")

def menu2():
   print("Drücke 1 wenn du das Land bekommen hast")
   print("Drücke 2 wenn du das Land nicht bekommen hast")
CountryList = []
class country():
    def __init__(self, country):
        self.country = country 
        self.camount = 0
        self.cget = 0
        self.gscore = 0
        self.durschnitt = 0
        CountryList.append(self)

    def Durschnitt(self, score):
        self.gscore += score
        self.durschnitt = self.gscore / self.camount
    def __str__(self):
        return  f"Dein Land {self.country} \n Du hast dieses Land {self.cget} von {self.camount} bekommen \n dein Durschnittswert ist {self.durschnitt}"

Albania = country("Albania")
Andorra = country("Andorra")
Argentinia = country("Argentinia")
Australia = country("Australia")
Austria = country("Austria")
Bangladesch = country("Bangladesch")
Belgium = country("Belgium")
Bhutan = country("Bhutan")
Brasil = country("Brasil")
Bolivia = country("Bolivia") 
Botswana = country("Botswana")
Bosnia = country("Bosnia")
Bulgaria = country("Bulgaria")
Canada = country("Canada")
Colombia = country("Colombia")
Cambodia = country("Cambodia") 
Chile = country("Chile")
Curacau = country("Curacau")
Croatia = country("Croatia")
Costa_Rica = country("Costa_Rica")
Cyprus = country("Cyprus")
Czechia = country("Czechia")    
Denmark = country("Denmark")
Domenica = country("Domenica")   
Estland	= country("Estland")
Eswatini = country("Eswatini")	
France = country("France")	
Finnland = country("Finnland")	
Germany	= country("Germany")
Ghana = country("Ghana") 	
Greenland = country("Greenland") 	
Greek = country("Greek")	
Guatamala = country("Guatamala")	
Hungary = country("Hungary")	
Hong_Kong = country("Hong_Kong")	
Indien = country("India")	
Indonesia = country("Indonesia")	
Italy = country("Italy")	
Ireland	= country("Ireland")
Island	= country("Island")
Israel = country("Israel")	
Japan  = country("Japan")	
Jordan = country("Jordan")	
Jersey = country("Jersey")
Kazakhstan = country("Kazakhstan")	
Kenia = country("Kenia") 	
Kyrgistan = country("Kyrgistan")	
Latvia = country("Latvia") 	
Lesotho = country("Lesotho")	
Libanon	= country("Libanon")
Lithuania = country("Lithuania") 	
Luxembourg = country("Luxembourg")	
Macau = country("Macau")	
Malaysia = country("Malaysia")	
Malta = country("Malta")	
Mexico = country("Mexico")	
Montenegro = country("Montenegro")	
Monaco = country("Monaco")	
Namibia	= country("Namibia")
Netherlands	= country("Netherlands")
New_Zealand = country("New_Zealand")
Nepal = country("Nepal")
Nigiria = country("Nigiria")
Norway = country("Norway")
North_Macedonia = country("North_Macedonia")
Oman = country("Oman")
Panama = country("Panama")
Paraguay = country("Paraguay")
Peru = country("Peru")
Phillipines = country("Phillipines")
Puerto_Rico = country("Puerto_Rico")
Poland = country("Poland")
Portugal = country("Portugal")
Qatar = country("Qatar")	
Russia = country("Russia")	
Ruanda = country("Ruanda")	
Romania	= country("Romania")
Sweden = country("Sweden")	
Senegal = country("Senegal")	
Serbia = country("Serbia")	
Slovakia = country("Slovakia")	
Slovenia = country("Slovenia")	
South_Africa = country("South_Africa")
South_Korea = country("South_Korea")
Spain = country("Spain")	
Sri_Lanka = country("Sri_Lanka")
Swizerland = country("Swizerland")
Taiwan = country("Taiwan")
Thailand = country("Thailand")
Tunisia = country("Tunisia")
Türkiye = country("Türkiye")
UAE = country("UAE")
Uganda = country("Uganda")
Ukraine = country("Ukraine")
United_Kingdom = country("United_Kingdom")
Uruguay = country("Uruquay")
USA = country("USA")
Vietnam = country("Vietnam")

def main():
  while True:
        menu()
        Auswahl = int(input("Was möchtest du ausführen?"))
        match Auswahl:
           case 1:
              land_input = input("Gebe dein Land ein: ").strip().lower()  # Benutzerinput in Kleinbuchstaben
              found_land = None
              for c in CountryList:
                if c.country.lower() == land_input:
                  found_land = c
                  break

              if not found_land:
                print("Land nicht gefunden") 
                main()
              found_land.camount += 1
              score =  int(input("Gebe deinen Score an "))
              found_land.Durschnitt(score)
              menu2()
              A =  int(input("Was möchtest du ausführen?"))
              match A:
                 case 1:
                    get = True
                 case 2: 
                    get = False
              if get:
                 found_land.cget += 1
              print("Eingabe erfolgreich")

           case 2:
               land_input = input("Gebe dein Land ein: ").strip().lower()  # Benutzerinput in Kleinbuchstaben
               found_land = None
               for c in CountryList:
                if c.country.lower() == land_input:
                  found_land = c
                  break

               if not found_land:
                print("Land nicht gefunden")  
                main()
                
               print(found_land)

           case 3:
              Speichern()
           case 4:
              reset()
              
if __name__ == "__main__":   
   main()   



