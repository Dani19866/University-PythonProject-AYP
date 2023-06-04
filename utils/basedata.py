import json
import random
from utils.colors import DefaultMessages, HeadersMessages, InformationMessages

colorHeaders = HeadersMessages()
colorMessages = InformationMessages()
defaultMessages = DefaultMessages()


class Database:
    ticketsPath = "database/tickets.json"
    resultsPath = "database/info/results.json"

    # For seasons and pilots algorithm
    structSeason = {
        "data": None,
        "state": None,
        "podium": None,
        "rounds": []
    }

    # Only client
    def updateClient(self, listClients: list):
        with open(self.ticketsPath, "w") as file:
            json.dump(listClients, file)

    def saveClient(self, client: dict):
        with open(self.ticketsPath, "r") as file:
            jsonDocument = json.load(file)

        jsonDocument.append(client)
        self.__updateFileClient(jsonDocument)

    def __updateFileClient(self, data: list):
        with open(self.ticketsPath, "w") as file:
            json.dump(data, file)

    # Only winner pilot
    def savePilot(self, pilot: str, podium: str):
        # 1. Extract json
        with open(self.resultsPath, "r") as file:
            jsonDocument = json.load(file)

        # 2. CONDITION: Verify len of document, if no exist any data, create a firts season. If exist seasons, only update a actual season or create a new season
        if len(jsonDocument) == 0:
            # CREATE A SEASON
            randomYear = str(random.randint(2023, 2024))
            randomMonth = str(random.randint(1, 12))
            randomDay = str(random.randint(1, 28))
            date = f"{randomDay}-{randomMonth}-{randomYear}"

            newSeason = {"data": date, "state": "running",
                         "podium": podium, "rounds": [pilot]}
            self.structSeason.update(newSeason)

            # 2.1 Save in json
            self.__updateFilePilotWinner([self.structSeason])

        else:
            createSeason = True
            
            # Verify season in running
            for season in jsonDocument:
                stateSeason = season.get("state")
                roundsSeason = len(season.get("rounds"))
                dateSeason = season.get("data")
                podiumSeason = season.get("podium")

                
                if stateSeason == "running":
                    createSeason = False
                    
                    # Verify last round
                    lastRound = 0
                    for ignore in season.get("rounds"):
                        lastRound += 1
                        
                    # !23: Keep adding
                    if lastRound != 23:
                        season["rounds"].append(pilot)
                        
                        # Verify to close sesion after adding
                        verify = lastRound + 1
                        if verify == 23:
                            season["state"] = "finished"
                            self.__stadistics(season, dateSeason, podiumSeason)
                            self.__updateFilePilotWinner(jsonDocument)
                        else:
                            self.__updateFilePilotWinner(jsonDocument)
                        
                    else:
                        season["state"] = "finished"
                        self.__stadistics(season, dateSeason, podiumSeason)
                        self.__updateFilePilotWinner(jsonDocument)

            # CONDITION: Create a season
            if createSeason:
                randomYear = str(random.randint(2023, 2024))
                randomMonth = str(random.randint(1, 12))
                randomDay = str(random.randint(1, 28))
                date = f"{randomDay}-{randomMonth}-{randomYear}"

                newSeason = {"data": date, "state": "running","podium": podium, "rounds": [pilot]}
                self.structSeason.update(newSeason)
                jsonDocument.append(self.structSeason)
                self.__updateFilePilotWinner(jsonDocument)
                    
    def __stadistics(self, season: list, dateSeason: str, podiumSeason: str):
        colorMessages.information(f"Temporada {dateSeason} finalizada! Carrera realizada en {podiumSeason}")
        pilots = {}
        race = 1
        
        # 1 Calculate pilot winner with points
        for x in season.get("rounds"):
            if x not in pilots:
                pilots[x] = self.__pilotPoint(race)

            else:
                pilots[x] += self.__pilotPoint(race)
        result, val = 0, ''
        for i, j in pilots.items():
            if result < j:
                result = j
                val = i
        colorMessages.information(f"El piloto con más puntos es: {val} con {result} puntos!")
        
        with open("database/info/constructs.json", "r") as file:
            constructs = json.load(file)
            teams = {}

            # 2.2.3.1 Search pilots in her constructs
            for construct in constructs:
                pilotsConstructs = construct.get("pilots")
                nameConstruct = construct.get("name")

                for pilotConstruct in pilotsConstructs:

                    # 2.2.3.1.1 Search pilots in pilots point
                    for pilotName in pilots:
                        points = pilots[pilotName]

                        # Compareer
                        if pilotName == pilotConstruct:
                            if nameConstruct not in teams:
                                teams[nameConstruct] = 0
                                teams[nameConstruct] += points

                            else:
                                teams[nameConstruct] += points

            # 2.2.3.2 Calculate points
            result, val = 0, ''
            for i, j in teams.items():
                if result < j:
                    result = j
                    val = i

            # 2.2.3.3 Show results
            colorMessages.information(f"El constructor con más puntos es: {val} con {result} puntos!")
    
    def __updateFilePilotWinner(self, data: list):
        with open(self.resultsPath, "w") as file:
            json.dump(data, file)

    def __pilotPoint(self, position: int):
        position = int(position)

        match position:
            case 1:
                return 25

            case 2:
                return 18

            case 3:
                return 15

            case 4:
                return 12

            case 5:
                return 10

            case 6:
                return 8

            case 7:
                return 6

            case 8:
                return 4

            case 9:
                return 2

            case 10:
                return 1

        return int(position)
