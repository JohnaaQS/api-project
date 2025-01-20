import functies as api
import re

while True :
    print("\n_______________________________________________________________")
    print("welkom bij het keuzemenu")
    print("____________________________________________________________")
    print("1. Bekijk alle wijken.")
    print("2. Zoek informatie over een specifieke wijk.")
    print("3. Geef straatcriminaliteit op basis van locatie.")
    print("4. Bekijk alle politiediensten.")
    print("5. Stop en zoek incidenten.")
    print("6. Stop het programma.")
    keuze = input("\nMaak een keuze: ")
    print("_______________________________________________________________")
        
    if keuze == "1":
        wijken = api.neighbourhoods()
        if "error" in wijken:
            print(wijken["error"])
        else:
            print("\nOverzicht van wijken in Leicestershire:")
            print("_______________________________________________________________")
            for wijk in wijken:
                print(f"Naam: {wijk['name']:30} | Code: {wijk['id']}")
            print("_______________________________________________________________")

    elif keuze == "2":
        code = input("geef een wijkcode in (bv.'NC04'): ")
        wijk_info = api.specificneighbourhood(code)
        if "name" in wijk_info and "description" in wijk_info:
            naam = wijk_info["name"]
            beschrijving = wijk_info["description"]
            beschrijving = re.sub(r"<.*?>", "", beschrijving)
            print(f"Informatie over wijk '{naam}':")
            print(beschrijving)
        else:
            print("Geen informatie beschikbaar voor deze wijk.")
        
    elif keuze == "3":
        crimes = api.street_crimes()