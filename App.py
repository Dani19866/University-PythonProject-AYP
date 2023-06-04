# Utils
from utils.colors import HeadersMessages, DefaultMessages, InformationMessages
from utils.api import Api, ApiBackUp, OrganizerApi

# Managements
from managemetns.restaurants import Restaurants
from managemetns.races import Races, Races_and_teams

# Panel
from user.panel import UserPanel
from admin.panel import AdminPanel

# Vars
colorHeaders = HeadersMessages()
colorMessages = InformationMessages()
defaultMessages = DefaultMessages()
api = Api()
apiBackUp = ApiBackUp()
organizerApi = OrganizerApi()
adminPanel = AdminPanel()


class AutomaticFunctions:
    # Races and teams managements
    sraces_and_teams = None

    # JSON Documents
    pilots = []
    constructs = []
    races = []
    circuits = []

    # Panels
    userPanel = None
    adminPanel = None
    restaurants = None
    racesMenu = None

    # Ready
    def requestAPI(self):
        timeLoop = True
        count = 0

        while timeLoop:
            try:
                self.pilots = api.GetPilots()
                self.constructs = api.GetConstructs()
                self.races = api.GetRaces()
                self.userPanel = UserPanel(self.races)
                self.restaurants = Restaurants(self.races)

                timeLoop = False

            except Exception as e:
                count += 1
                colorMessages.errorMessage(
                    f"Verifique conexión a internet. Intento número: {count}/3")

                if count == 3:
                    colorMessages.succesMessage(
                        "Recuperando datos del último BackUp...")
                    self.pilots = apiBackUp.GetPilots()
                    self.constructs = apiBackUp.GetConstructs()
                    self.races = apiBackUp.GetRaces()
                    self.userPanel = UserPanel(self.races)
                    self.restaurants = Restaurants(self.races)

                    timeLoop = False

    # Ready
    def organizerAPI(self):
        self.pilots = organizerApi.organizerPilots(self.pilots)
        self.constructs = organizerApi.organizerConstructs(
            self.constructs, self.pilots)
        self.circuits = organizerApi.organizerCircuits(self.races)
        self.races = organizerApi.organizerRaces(self.races)

    # Ready
    def organizerRestaurants(self):
        self.restaurants.organizer()

    # Ready
    def organizerRacesTeams(self):
        self.racesMenu = Races(self.constructs, self.pilots, self.races, self.circuits)

        self.races_and_teams = Races_and_teams(self.constructs, self.pilots, self.races, self.circuits)
        self.races_and_teams.createDocument()
        self.races_and_teams.saveValues()

class App(AutomaticFunctions):
    # Ready
    def __automaticAlgorithm(self):
        self.requestAPI()
        self.organizerAPI()
        self.organizerRestaurants()
        self.organizerRacesTeams()
        colorHeaders.title(
            "Sistema para gestión de carreras 2023 de Fórmula 1 (BETA)")
        colorMessages.information("Iniciando...")

    # Ready
    def __clientPanel(self):
        """
            Funciones:
                - Comprar entrada
                - Comprar productos
                - Filtro de competidores
        """

        colorMessages.succesMessage("Acceso a panel de usuario concedido")

        menuLoop = True
        while menuLoop:
            colorHeaders.title("Por favor, seleccione una opción")
            colorHeaders.option("0: Salir del panel de usuario")
            colorHeaders.option("1: Comprar entrada")
            colorHeaders.option("2: Comprar productos (Restaurants)")
            colorHeaders.option("3: Filtrar información de las carreras")
            option = input(colorHeaders.inputMode("Opción a elegir (0/1/2): "))

            match option:
                # READY: Exit
                case "0":
                    menuLoop = False

                # READY: Buy ticket
                case "1":
                    self.userPanel.buyTicket()

                # READY: Buy product
                case "2":
                    self.restaurants.buyProducts()

                # READY: Filter menu of races information
                case "3":
                    self.racesMenu.filterMenu()

                # READY: Control errors
                case _:
                    defaultMessages.errorSelection()

    # ONLY GRAPHIC FUNCTION
    def __adminPanel(self):
        colorMessages.succesMessage(
            "Acceso a panel de administrador concedido (MODO BETA: Sin password actualmente)")

        menuLoop = True
        while menuLoop:
            colorHeaders.title("Por favor, seleccione una opción")
            colorHeaders.option("0: Salir del panel de administrador")
            colorHeaders.option("1: Ver estadísticas")
            colorHeaders.option("2: Verificar ticket")
            colorHeaders.option("3: Terminar carrera")
            colorHeaders.option("4: Terminar temporada")

            option = input(colorHeaders.inputMode("Opción a elegir (0/1/2): "))

            match option:
                # READY: Close menu
                case "0":
                    menuLoop = False

                # Show stadistics menu
                case "1":
                    adminPanel.stadistics()

                # READY: Verify ticket
                case "2":
                    adminPanel.verifyTicket()

                # READY: Finish race
                case "3":
                    self.racesMenu.finishRace()

                # READY: Finish season
                case "4":
                    self.racesMenu.finishSeason()

                # Error control
                case _:
                    defaultMessages.errorSelection()

    # READY
    def start(self):
        self.__automaticAlgorithm()

        menuLoop = True
        while menuLoop:
            colorHeaders.title("Por favor, seleccione el panel que desee")
            colorHeaders.option("0: Salir del sistema")
            colorHeaders.option("1: Panel usuario")
            colorHeaders.option("2: Panel administrador")
            option = input(colorHeaders.inputMode("Opción a elegir (0/1/2): "))

            match option:
                # Exit
                case "0":
                    colorHeaders.title("Cerrando sistema...")
                    menuLoop = False

                # Client menu
                case "1":
                    self.__clientPanel()

                # Admin menu
                case "2":
                    self.__adminPanel()

                # Control errors
                case _:
                    colorMessages.errorMessage(
                        "Selección errónea! Por favor inténtelo de nuevo")