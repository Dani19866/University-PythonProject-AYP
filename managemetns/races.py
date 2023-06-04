import os
import json
import random
from utils.colors import DefaultMessages, HeadersMessages, InformationMessages
from utils.api import OrganizerApi
from utils.basedata import Database

colorHeaders = HeadersMessages()
colorMessages = InformationMessages()
defaultMessages = DefaultMessages()
organizerApi = OrganizerApi()
database = Database()


class Races_and_teams:
    # Paths
    paths = ["database/info/pilots.json", "database/info/constructs.json",
             "database/info/races.json", "database/info/circuits.json", "database/info/results.json"]

    constructs = []
    pilots = []
    races = []
    circuits = []

    def __init__(self, constructs: list, pilots: list, races: list, circuits: list) -> None:
        self.constructs = constructs
        self.pilots = pilots
        self.races = races
        self.circuits = circuits

    def createDocument(self):
        exists = os.path.exists("database/info")

        # 1. Verify exist folder
        if exists:
            # 1.1 Verify exists documents
            for path in self.paths:
                exists = os.path.exists(path)

                if exists == False:
                    with open(path, "w") as file:
                        file.write("[]")

        # CONTROL ERROR: Create a folder & documents
        else:
            # CONTROL ERROR: Create a folder
            os.mkdir("database/info")

            # CONTROL ERROR: Create a documents
            for path in self.paths:
                with open(path, "w") as file:
                    file.write("[]")

    def saveValues(self):
        paths = ["database/info/pilots.json", "database/info/constructs.json",
                 "database/info/races.json", "database/info/circuits.json"]

        # 1. Save data of pilots
        with open(paths[0], "w") as file:
            json.dump(self.pilots, file)

        # # 2. Save data of constructs
        with open(paths[1], "w") as file:
            json.dump(self.constructs, file)

        # 3. Save data of races
        with open(paths[2], "w") as file:
            json.dump(self.races, file)

        # 4. Save data of circuits
        with open(paths[3], "w") as file:
            json.dump(self.circuits, file)


class FinishRace:
    # For create a season
    randomPodium = None
    randomPilot = None

    def __saveData(self):
        database.savePilot(self.randomPilot, self.randomPodium)

    def algorithmRace(self, circuits: list, pilots: list):
        # 1. Select random podium
        self.randomPodium = circuits[random.randint(
            0, len(circuits) - 1)].get("name")

        # 2. Select random pilot winner
        x = random.randint(0, len(pilots) - 1)
        self.randomPilot = pilots[x].get(
            "name") + " " + pilots[x].get("lastname")

        # 3. Show succes message
        colorMessages.succesMessage(
            f"{self.randomPilot} ha ganado la carrera!")

        # 4. Save in results.json
        self.__saveData()


class FinishSeason:
    # For finish a season
    randomPilot = None
    randomPodium = None

    def algorithSeason(self, circuits: list, pilots: list):
        path = "database/info/results.json"

        with open(path, "r") as file:
            jsonDocument = json.load(file)
            lastRace = len(jsonDocument) - 1

            # ERROR BECAUSE NO HAVE LEN
            try:
                race = jsonDocument[lastRace]

                # 1. For finish a season
                if race.get("state") == "running":
                    rounds = len(race.get("rounds"))

                    while rounds < 23:
                        self.randomPodium = circuits[random.randint(
                            0, len(circuits) - 1)].get("name")
                        x = random.randint(0, len(pilots) - 1)
                        self.randomPilot = pilots[x].get(
                            "name") + " " + pilots[x].get("lastname")

                        rounds += 1
                        database.savePilot(self.randomPilot, self.randomPodium)

                # 2. For create and finish season
                else:
                    rounds = 0

                    while rounds < 23:
                        self.randomPodium = circuits[random.randint(
                            0, len(circuits) - 1)].get("name")
                        x = random.randint(0, len(pilots) - 1)
                        self.randomPilot = pilots[x].get(
                            "name") + " " + pilots[x].get("lastname")

                        rounds += 1
                        database.savePilot(self.randomPilot, self.randomPodium)
            except:
                rounds = 1

                while rounds < 23:
                    self.randomPodium = circuits[random.randint(
                        0, len(circuits) - 1)].get("name")
                    x = random.randint(0, len(pilots) - 1)
                    self.randomPilot = pilots[x].get(
                        "name") + " " + pilots[x].get("lastname")

                    rounds += 1
                    database.savePilot(self.randomPilot, self.randomPodium)


class Races(FinishRace, FinishSeason):
    constructs = []
    pilots = []
    races = []
    circuits = []

    def __init__(self, constructs: list, pilots: list, races: list, circuits: list) -> None:
        self.constructs = constructs
        self.pilots = pilots
        self.races = races
        self.circuits = circuits

    # Ready
    def __filterNationality(self):
        values = {}

        for construct in self.constructs:
            nationalityTeam = construct.get("nationality")
            teamName = construct.get("name")

            if nationalityTeam not in values:
                values[nationalityTeam] = []
                values[nationalityTeam].append(teamName)
            else:
                values[nationalityTeam].append(teamName)

        for x in values:
            # Nationality
            colorHeaders.text(x.upper())

            # Teams in nationality
            for team in values[x]:
                colorHeaders.text(f"    {team}")

    # Ready
    def __filterPilotsConstructs(self):
        for construct in self.constructs:
            teamName = construct.get("name")
            pilots = construct.get("pilots")
            colorHeaders.text(teamName)

            for pilot in pilots:
                colorHeaders.text(f"    {pilot}")

    # Ready
    def __filterRacesForCC(self):
        values = {}

        for race in self.races:
            nameRace = race.get("name")
            countryRace = race.get("country")

            if countryRace not in values:
                values[countryRace] = []
                values[countryRace].append(nameRace)
            else:
                values[countryRace].append(nameRace)

        for x in values:
            # Country
            colorHeaders.text(x.upper())

            # Races in country
            for race in values[x]:
                colorHeaders.text(f"    {race}")

    # Ready
    def __filterAllRacesIM(self):
        values = {}

        for race in self.races:
            dateRace = race.get("date")[0:7]
            nameRace = race.get("name")

            if dateRace not in values:
                values[dateRace] = []
                values[dateRace].append(nameRace)
            else:
                values[dateRace].append(nameRace)

        for x in values:
            # Date
            colorHeaders.text(x.upper())

            # Races in date
            for race in values[x]:
                colorHeaders.text(f"    {race}")

    # =========================================================================
    # Ready
    def filterMenu(self):
        menuLoop = True
        while menuLoop:
            colorHeaders.subTittle(
                "Búsqueda de carreras a través de los siguientes filtros")
            colorHeaders.option("0: Salir del menú de filtros")
            colorHeaders.option("1: Constructores (Por nacionalidad)")
            colorHeaders.option("2: Pilotos por constructores")
            colorHeaders.option("3: Carreras por país del circuito")
            colorHeaders.option("4: Todas las carreras ocurridas en 1 mes")

            option = input(colorHeaders.inputMode(
                "Seleccione una opción (1/2/3/4/5): "))

            match option:
                # Exit menu
                case "0":
                    menuLoop = False

                # Constructs x nationality
                case "1":
                    self.__filterNationality()

                # Pilots x constructs
                case "2":
                    self.__filterPilotsConstructs()

                # Races x circuit country
                case "3":
                    self.__filterRacesForCC()

                # All races in month
                case "4":
                    self.__filterAllRacesIM()

                # CONTROL ERROR
                case _:
                    defaultMessages.errorSelection()

    # ######
    def finishRace(self):
        self.algorithmRace(self.circuits, self.pilots)

    # ######
    def finishSeason(self):
        self.algorithSeason(self.circuits, self.pilots)
