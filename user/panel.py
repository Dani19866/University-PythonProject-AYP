import string, secrets
from utils.colors import DefaultMessages, HeadersMessages, InformationMessages
from utils.basedata import Database
from managemetns.restaurants import Restaurants

defaultMessages = DefaultMessages()
colorHeaders = HeadersMessages()
colorMessages = InformationMessages()
database = Database()
# restaurants = Restaurants()

class ClientProperties:
    # Verify sell to save in database
    succesful = True
    
    # Properties of client
    name = None
    age = None
    id = None
    ticket = None
    costs = None
    race = None
    seat = None
    code = None
    quantity = None
    raceRef = None
    assistance = False
    
    def requestName(self):
        control = True
        while control:
            try:
                x = str(input(colorHeaders.inputMode("Nombre y apellido: ")))
                return x

            except ValueError:
                colorMessages.errorMessage(
                    "Valor inválido! Por favor inténtelo de nuevo")

    def requestID(self):
        control = True
        while control:
            try:
                x = int(input(colorHeaders.inputMode("Cédula de identidad: ")))
                return x

            except ValueError:
                colorMessages.errorMessage(
                    "Valor inválido! Por favor verifique su cédula")

    def requestAge(self):
        control = True
        while control:
            try:
                x = int(input(colorHeaders.inputMode("Edad: ")))

                if x >= 1 and x <= 99:
                    return x

                else:
                    colorMessages.errorMessage(
                        "Valor inválido! Por favor verifique su edad")

            except ValueError:
                colorMessages.errorMessage(
                    "Valor inválido! Por favor verifique su edad")

    def automaticCode(self):
        letters = string.ascii_letters
        digits = string.digits
        alphabet = letters + digits

        pwd_length = 8
        pwd = ''

        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        return pwd

    def requestTickets(self):
        colorHeaders.subTittle("Tickets disponibles")
        colorHeaders.text("1: GENERAL 150$")
        colorHeaders.text("2: VIP 340$")

        check = True
        while check:
            option = input(colorHeaders.inputMode(
                "Seleccione una opción (1/2): "))

            match option:
                case "1":
                    check = False
                    return "general"

                case "2":
                    check = False
                    return "vip"

                case _:
                    colorMessages.errorMessage(
                        "Selección inválida, inténtelo de nuevo")

    def requestTotalCost(self):
        check = True
        while check:
            try:
                x = int(input(colorHeaders.inputMode("Tickets a comprar: ")))

                if x > 0:
                    self.quantity = x
                    check = False
                else:
                    colorMessages.errorMessage(
                        "Valor inválido! por favor inténtelo de nuevo")

            except ValueError:
                colorMessages.errorMessage(
                    "Valor inválido! por favor inténtelo de nuevo")

        colorHeaders.subTittle("Calculando el costo total...")

        # ------------------------> Sale <------------------------
        saleCheck = True
        a = ""
        b = ""
        count = 0

        for i in str(self.id):
            # Starting pattern
            if a == "" and b == "":
                a = i
            elif a != "" and b == "":
                b = i

            # Compareer
            else:
                if (count % 2) == 0:
                    count = 1
                    if i != a:
                        saleCheck = False
                else:
                    count = 0
                    if i != b:
                        saleCheck = False
        # ------------------------> Sale <------------------------
        # Total costs: si es general: 150$
        if self.ticket == "general":
            # Si el id es ondulado: 50% de descuento
            if saleCheck:
                self.subTotal = 75 * self.quantity
                self.sale = "Aplica. Costo original: 150$ sin IVA"
                self.iva = self.subTotal * 0.16
                self.total = round(self.subTotal * 1.16)

                data = {
                    "subtotal": self.subTotal,
                    "sale": self.sale,
                    "IVA": self.iva,
                    "total": self.total
                }

                return data

            else:
                self.subTotal = 150 * self.quantity
                self.iva = self.subTotal * 0.16
                self.total = round(self.subTotal * 1.16)

                data = {
                    "subtotal": self.subTotal,
                    "sale": "No aplica",
                    "IVA": self.iva,
                    "total": self.total
                }

                return data

        # Total costs: Si es vip: 340
        else:
            # Si el id es ondulado: 50% de descuento
            if saleCheck:
                self.subTotal = 170 * self.quantity
                self.sale = "Aplica. Costo original: 340$ sin IVA"
                self.iva = self.subTotal * 0.16
                self.total = round(self.subTotal * 1.16)

                data = {
                    "subtotal": self.subTotal,
                    "sale": self.sale,
                    "IVA": self.iva,
                    "total": self.total
                }

                return data

            else:
                self.subTotal = 340 * self.quantity
                self.iva = self.subTotal * 0.16

                self.total = round(self.subTotal * 1.16)

                data = {
                    "subtotal": self.subTotal,
                    "sale": "No aplica",
                    "IVA": self.iva,
                    "total": self.total
                }

                return data

    def requestRace(self):
        colorHeaders.subTittle("Carreras disponibles: ")
        
        # Show information of races
        for race in self.racesJSON:
            raceName = race.get("name")
            raceID = race.get("circuit").get("circuitId")
            colorHeaders.text(f"{raceName} | REF '{raceID}'")
            
        # Select races
        check = True
        while check:
            choose = input(colorHeaders.inputMode("Carrera a seleccionar (Por referencia): "))
            
            # Find race
            for race in self.racesJSON:
                raceID = race.get("circuit").get("circuitId")
                raceName = race.get("name")
                
                # Compareer
                if raceID == choose:
                    # Close verification
                    check = False
                    
                    # Automatic information
                    self.raceRef = raceID
                    return raceName
        
            # Control errors
            colorMessages.errorMessage("Carrera no encontrada!")
     
    def requestSeats(self):
        colorHeaders.subTittle("Carreras disponibles: ")
        values = []
        
        # Show information of races
        for race in self.racesJSON:
            raceID = race.get("circuit").get("circuitId")
            ticketsMap = race.get("map")
            
            # Find race
            if raceID == self.raceRef:
                
                # With type ticket, show seats
                tickets = ticketsMap.get(self.ticket)
                colorHeaders.text(f"Filas: {tickets[0]} | Columna: {tickets[1]}")     
                
                # Select fila
                check = True
                while check:
                    try:
                        x = int(
                            input(colorHeaders.inputMode("Seleccionar fila: ")))

                        if x >= 1 and x <= tickets[0]:
                            values.append(x)
                            check = False

                        else:
                            colorMessages.errorMessage("Fila inválida!")

                    except ValueError:
                        colorMessages.errorMessage("Fila inválida!")   
            
                # Select column
                check = True
                while check:
                    try:
                        x = int(input(colorHeaders.inputMode(
                            "Seleccionar columna: ")))

                        if x >= 1 and x <= tickets[1]:
                            values.append(x)
                            check = False

                        else:
                            colorMessages.errorMessage("Columna inválida!")

                    except ValueError:
                        colorMessages.errorMessage("columna inválida!")
        
        return values
        
    def __init__(self, races: list) -> None:
        self.racesJSON = races

        # Automatic information
        self.code = self.automaticCode()
        self.quantity = None
        self.raceRef = None
        self.assistance = False

        # Basic information
        self.name = self.requestName()
        self.age = self.requestAge()
        self.id = self.requestID()
        self.ticket = self.requestTickets()
        self.costs = self.requestTotalCost()

        # Ticket information
        self.race = self.requestRace()
        self.seat = self.requestSeats()
    
class Client(ClientProperties):
    def __init__(self, races: list) -> None:
        super().__init__(races)
        self.confirmPurcharse()
            
    def confirmPurcharse(self):
        # Menu to process purcharse
        check = True
        while check:
            colorMessages.information(f"Estimado {self.name} su costo total es { self.costs.get('total') }$")
            colorHeaders.option("1: Para continuar con la compra")
            colorHeaders.option("2: Para cancelar la compra")

            selection = input(colorHeaders.inputMode("Seleccione una opción (1/2): "))
            
            match selection:
                    # COMPRAR
                    case "1":
                        colorMessages.succesMessage(f"Compra hecha con éxito! Su código secreto es: {self.code}, si lo pierde no va a poder entrar a la carrera")
                        check = False

                    # CANCELAR
                    case "2":
                        colorMessages.succesMessage("Compra CANCELADA")
                        self.succesful = False
                        check = False

                    # CONTROL DE ERRORES
                    case _:
                        colorMessages.errorMessage("Selección errónea! Por favor intente de nuevo")
    
    def getInfo(self):
        data = {
            "basicInformation": {
                "name": self.name,
                "age": self.age,
                "id": self.id
            },
            "ticketInformation": {
                "code": self.code,
                "race": self.race,
                "ticket": self.ticket,
                "seat": self.seat,
                "raceRef": self.raceRef,
                "quantity": self.quantity,
                "costs": self.costs,
                "assistance": self.assistance
            },
            "productsInformation": {
                "totalSpend": 0,
                "products": []
            }
        }
        return data

class UserPanel:
    # All data of races: Circuits, Restaurants, etc
    racesDocument = None
    
    def __init__(self, races: list) -> None:
        self.racesDocument = races
    
    def buyTicket(self):
        # INFORMATION
        colorMessages.information("Solo puede comprar entradas 1 vez. Si ya hizo una compra van a ver errores con sus entradas, si pasa esto contacte con atención al cliente")
        
        # 1. Create a client json document
        client = Client(self.racesDocument)
        
        # 2. Buy: Save in database
        if client.succesful:
            database.saveClient(client.getInfo())
    
    def buyProduct(self):
        # restaurants.buyProducts()
        pass