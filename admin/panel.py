import json
from utils.basedata import Database
from utils.colors import DefaultMessages, HeadersMessages, InformationMessages

colorHeaders = HeadersMessages()
colorMessages = InformationMessages()
defaultMessages = DefaultMessages()

database = Database()


class StadisticsFunctions:
    tickets = None
    products = None

    def __init__(self) -> None:
        ticketsPath = "database/tickets.json"
        productsPath = "database/products.json"

        try:
            # 1. Tickets
            with open(ticketsPath, "r") as file:
                self.tickets = json.load(file)

            # 2. Products
            with open(productsPath, "r") as file:
                self.products = json.load(file)
        except:
            colorMessages.information("Archivos reseteados! Por favor inicie de nuevo el programa")

    # READY
    def averageSpend(self):
        totalTicketsVIP = 0
        totalSpendPersonsVIP = 0
        totalPersonsVIP = 0

        for client in self.tickets:
            verifyVIP = client.get("ticketInformation").get("ticket")
            if verifyVIP == "vip":
                totalPersonsVIP += 1
                totalTicketsVIP += int(client.get(
                    "ticketInformation").get("costs").get("total"))
                totalSpendPersonsVIP += int(client.get(
                    "productsInformation").get("totalSpend"))

        average = (totalTicketsVIP + totalSpendPersonsVIP) / totalPersonsVIP
        colorMessages.information(
            f"El promedio de gastos de personas VIP fue {round(average)}$!")

        # For stadistics
        return average

    # READY
    def assistanceTable(self):
        values = {}

        for client in self.tickets:
            nameRace = client.get("ticketInformation").get("race")
            assistance = bool(client.get(
                "ticketInformation").get("assistance"))

            if assistance:
                if nameRace not in values:
                    values[nameRace] = 0
                    values[nameRace] += 1
                else:
                    values[nameRace] += 1

        # Top 3 clients that buy more tickets
        valuesSorted = sorted(values, key=values.get, reverse=True)
        rank = 1
        for race in valuesSorted:
            colorHeaders.text(f"{rank}. {race}")
            rank += 1

        # For stadistics
        return valuesSorted

    # READY
    def mostAssistanceRace(self):
        values = {}

        for client in self.tickets:
            nameRace = client.get("ticketInformation").get("race")
            assistance = bool(client.get(
                "ticketInformation").get("assistance"))

            if assistance:
                if nameRace not in values:
                    values[nameRace] = 0
                    values[nameRace] += 1
                else:
                    values[nameRace] += 1

        # Choose the race of most tickets solds
        result, val = 0, ''
        for i, j in values.items():
            if result < j:
                result = j
                val = i

        # Result
        colorMessages.information(
            f"La carrera más asistida fue {val} con {result} personas asistidas!")

        # For stadistics
        return result

    # READY
    def mostSoldOut(self):
        values = {}

        for client in self.tickets:
            nameRace = client.get("ticketInformation").get("race")
            tickets = client.get("ticketInformation").get("quantity")

            if nameRace not in values:
                values[nameRace] = 0
                values[nameRace] += tickets
            else:
                values[nameRace] += tickets

        # Choose the race of most tickets solds
        result, val = 0, ''
        for i, j in values.items():
            if result < j:
                result = j
                val = i

        # Result
        colorMessages.information(
            f"La carrera más vendida fue {val} con {result} tickets vendidos!")

        # For stadistics
        return result

    # READY
    def top3ClientsMostBuyTickets(self):
        values = {}

        for client in self.tickets:
            nameClient = client.get("basicInformation").get("name")
            tickets = client.get("ticketInformation").get("quantity")

            if nameClient not in values:
                values[nameClient] = 0
                values[nameClient] += tickets
            else:
                values[nameClient] += tickets

        # Top 3 clients that buy more tickets
        valuesSorted = sorted(values, key=values.get, reverse=True)
        colorMessages.information(
            f"Los clientes que más compraron tickets fueron {valuesSorted[0]}, {valuesSorted[1]} y {valuesSorted[2]} comprando {values[valuesSorted[0]]}, {values[valuesSorted[1]]} y {values[valuesSorted[2]]}")

        # For stadistics
        return valuesSorted

    # READY
    def top3ProductsMostSell(self):
        values = {}

        for client in self.tickets:
            products = client.get("productsInformation").get("products")
            
            for product in products:
                
                if product not in values:
                    values[product] = 0
                    values[product] += 1
                else:
                    values[product] += 1


        # Top 3 products that buy more
        valuesSorted = sorted(values, key=values.get, reverse=True)
        try:
            colorMessages.information(f"Los 3 productos más vendidos fueron {valuesSorted[0]}, {valuesSorted[1]} y {valuesSorted[2]}, pidiendo {values[valuesSorted[0]]}, {values[valuesSorted[1]]} y {values[valuesSorted[2]]} cantidades")
        
        except:
            
            # Top 2 products that buy more
            try:
                colorMessages.information(f"Los 2 productos más vendidos fueron {valuesSorted[0]} y {valuesSorted[1]}, pidiendo {values[valuesSorted[0]]} y {values[valuesSorted[1]]} cantidades")
        
            except:
                
                # Top products that buy more
                try:
                    colorMessages.information(f"El producto más vendidos fue {valuesSorted[0]}, pidiendo {values[valuesSorted[0]]} cantidades")
        
                # No products selled
                except:
                    colorMessages.information(f"No hay productos vendidos!")
        
        # For stadistics
        return valuesSorted

    # ##############################
    def graphic(self):
        pass
    # ##############################

class AdminPanel(StadisticsFunctions):
    # READY
    def verifyTicket(self):
        path = "database/tickets.json"

        menuLoop = True
        tries = 0
        while menuLoop:
            # 1. Request SECRET CODE
            secretCode = input(colorHeaders.inputMode(
                "Por favor, introduce el código del ticket: "))

            # 2. Extract information of tickets.json
            with open(path, "r") as file:
                jsonDocument = json.load(file)

            # 3. Check code
            exists = False
            for client in jsonDocument:
                code = client.get("ticketInformation").get("code")
                status = bool(client.get(
                    "ticketInformation").get("assistance"))

                # 3.1 Compareer codes
                if code == secretCode and status == False:
                    exists = True

                    # 3.1.1 Change value
                    client["ticketInformation"]["assistance"] = True

                    # 3.1.2 Update changes
                    database.updateClient(jsonDocument)
                    menuLoop = False

            # 3. CONTROL ERROR: Code no exist
            if exists == False:
                tries += 1
                colorMessages.errorMessage(
                    f"El código no existe o ya ha sido usado! Intento {tries}/3")

                if tries == 3:
                    menuLoop = False

    def stadistics(self):
        menuLoop = True
        while menuLoop:
            colorHeaders.title("Por favor, seleccione una opción")
            colorHeaders.option("0: Salir del menú")
            colorHeaders.option(
                "1: Promedio de gasto de un VIP en una carrera (ticket + restaurant)")
            colorHeaders.option(
                "2: Mostrar tabla de asistencia de las carreras (mejor a peor)")
            colorHeaders.option("3: Carrera con más asistencia")
            colorHeaders.option("4: Carrera con mayor boletos vendidos")
            colorHeaders.option(
                "5: Top 3 productos más vendidos en el restaurante")
            colorHeaders.option("6: Top 3 clientes que más compraron boletos")
            colorHeaders.option("7: Gráfico con estadísticas")

            option = input(colorHeaders.inputMode(
                "Opción a elegir (1/2/3/4/5/6/7/0): "))

            match option:
                # Exit menu
                case "0":
                    menuLoop = False

                # Average of spent of VIP client in a race (ticket + restaurant)
                case "1":
                    self.averageSpend()

                # Show table from high to low assistance. Showing: RACE NAME | TEAM NAME | CIRCUIT | TICKETS SALES | PERSONS ASSISTANCE | ASSISTANCE/SALE RELATION
                case "2":
                    self.assistanceTable()

                # Race with most assistance
                case "3":
                    self.mostAssistanceRace()

                # Race with the most tickets solds
                case "4":
                    self.mostSoldOut()

                # Top 3 products most sell in restaurants
                case "5":
                    self.top3ProductsMostSell()

                # Top 3 clients that buy more tickets
                case "6":
                    self.top3ClientsMostBuyTickets()

                # Graphic with stadistics (mathplotlib o Bokeh)
                case "7":
                    self.graphic()

                # CONTROL ERROR
                case _:
                    defaultMessages.errorSelection()
