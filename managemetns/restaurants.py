from utils.colors import DefaultMessages, HeadersMessages, InformationMessages
from utils.basedata import Database
import os, random, json as j

defaultMessages = DefaultMessages()
colorHeaders = HeadersMessages()
colorMessages = InformationMessages()
database = Database()

class Product:
    age = 0                     # For filter of age
    id = 0                      # For perfect number
    shoppingCar = []            # For save products
    costs = 0
    
    # READY
    def _verifyPerfectNumber(self):
        suma = 0

        for i in range(1, self.id):
            if (self.id % (i) == 0):
                suma += (i)

        if self.id == suma:
            return True

        else:
            return False
    
    # READY
    def __showProducts(self):
        path = "database/products.json"
        
        # 1 Read json
        with open(path, "r") as file:
            jsonDocument = j.load(file)
    
        # 2 Show products
        colorMessages.information("A continuación, se muestrans los restaurantes con sus productos")
        for productDict in jsonDocument:
            productName = productDict.get("name")
            productType = productDict.get("type")
            productPrice = productDict.get("price")
            
            if productType == "alcoholic":
                if self.age > 18:
                    colorHeaders.text(f"     Product: {productName} | Tipo: {productType} | Precio: {productPrice}$")
            else:
                colorHeaders.text(f"     Product: {productName} | Tipo: {productType} | Precio: {productPrice}$")
    
    # READY
    def __selectProducts(self):
        # Select products
        control = True
        while control:
            colorHeaders.subTittle("Por favor seleccione una opción")
            colorHeaders.option("1: Añadir producto")
            colorHeaders.option("2: Ir a pagar")
            
            selection = input( colorHeaders.inputMode("Seleccione una opción (1/2): ") )
            
            match selection:
                # Add product & keep buying
                case "1":
                    p = input(colorHeaders.inputMode("Escriba correctamente el producto: "))
                    path = "database/products.json"
        
                    # 1 Read json
                    with open(path, "r") as file:
                        jsonDocument = j.load(file)
                
                    # 2 Find product
                    finded = False
                    for productDict in jsonDocument:
                        productName = productDict.get("name")
                        productPrice = productDict.get("price")
                        
                        # 2.2 Compareer product
                        if productName == p:
                            colorMessages.succesMessage("Producto añadido con éxito!")
                            data = {"productName": productName, "price": productPrice}
                            self.shoppingCar.append(data)
                            finded = True
                            
                    # 2 CONTROL ERROR
                    if finded == False:
                        colorMessages.errorMessage("Producto no encontrado! Por favor escriba bien el nombre")
                        
                # Go to buy
                case "2":
                    control = False
                    
                # CONTROL ERROR
                case _:
                    defaultMessages.errorSelection()
    
    # READY
    def __calculateCosts(self):
        for item in self.shoppingCar:
            self.costs += int(float(item.get("price")))
    
    # READY
    def __utilGetCosts(self):
        control = True
        while control:
            colorHeaders.subTittle("Seleccione una opción")
            colorHeaders.option("1: Confirmar compra de productos")
            colorHeaders.option("2: Cancela")
            
            selection = input(colorHeaders.inputMode("Seleccione una opción (1/2): "))
            
            match selection:
                # Confirm buy
                case "1":
                    colorMessages.succesMessage("Compra procesada con éxito!")
                    return True
                
                # Cancel
                case "2":
                    colorMessages.information("Compra cancelada!")
                    return False
                
                # CONTROL ERRORS
                case _:
                    defaultMessages.errorSelection()
    
    # READY
    def __init__(self, age: int, id: int) -> None:
        self.age = age
        self.id = id
        
        # 1. Show products
        self.__showProducts()
        
        # 2. Select products
        self.__selectProducts()

        # 3. Calculate costs: getCosts()
        self.__calculateCosts()
    
    # READY
    def getCosts(self):
        # 1 Sale
        if self._verifyPerfectNumber():
            sale = self.costs * 0.15
            self.costs = self.costs - sale
            colorMessages.information(f"Su costo total es de {self.costs}$")
            
            return self.__utilGetCosts()
                    
        # No sale
        else:
            colorMessages.information(f"Su costo total es de {self.costs}$")
            return self.__utilGetCosts()

class BuyProducts:
    age = 0
    id = 0
    
    # READY
    def __verify(self):
        check = True
        tries = 0
        
        while check:
            # 1. Request ID
            try:
                id = int(input(colorHeaders.inputMode("Ingrese su cédula por favor: ")))
                
                # 2. Verify ticket
                path = "database/tickets.json"
                
                # 2.1 Extract data of clients
                with open(path, "r") as file:
                    jsonDocument = j.load(file)
                
                # 2.2 Search ID's
                clientCheck = False
                for client in jsonDocument:
                    # 2.2.1 Search id in ticket.json to compareer
                    idCompareer = int(client.get("basicInformation").get("id"))
                    
                    if idCompareer == id:
                        clientCheck = True
                        
                        # 2.2.2 Verify ticket VIP
                        verifyTicket = client.get("ticketInformation").get("ticket")
                        if verifyTicket != "general":
                            self.id = id
                            self.age = client.get("basicInformation").get("age")
                            
                            return True
                        
                        # 2.2.2 CONTROL ERROR: No has VIP
                        else:
                            colorMessages.errorMessage("Usted no es VIP")
                            return False
                
                # 2.2 CONTROL ERROR: No ticket with her ID
                if clientCheck == False:
                    colorMessages.errorMessage("Usted no tiene ningún boleto asignado")
                    return False
                
            # CONTROL ERROR: Invalid ID
            except ValueError:
                tries += 1
                colorMessages.errorMessage(f"Valor inválido! Intento {tries}/3")
                
                if tries == 3:
                    check = False
                    return False

    # READY
    def __getID(self):
        return self.id
    
    # READY
    def __getAge(self):
        return self.age

    # ====================================
    def __addInTickets(self, shoppingCar: list, costs: int, id: int):
        path = "database/tickets.json"
        
        # 1. Extract json
        with open(path, "r") as file:
            jsonDocument = j.load(file)
        
        # 2. Find client
        for client in jsonDocument:
            idClient = client.get("basicInformation").get("id")
            
            # 2.2 Client founded
            if idClient == id:
                
                # Add products to json
                for products in shoppingCar:
                    productName = products.get("productName")
                    productPrice = products.get("price")
                    
                    client["productsInformation"]["products"].append(productName)
                    client["productsInformation"]["totalSpend"] += int( float(productPrice) )
                    print(f"{productName} | {productPrice}")
            
        # 3. Save data
        database.updateClient(jsonDocument)
        
    def __restInventory(self, shoppingCar: list):
        path = "database/products.json"
                

    # ====================================
    def __algorithm(self):
        # CONDITION: Verify ID and Ticket VIP
        verify = self.__verify()
        
        if verify != False:
            # # Obtail all information of product to buy
            product = Product(self.age, self.id)
        
            # # 3. Confirm buy. CONDITION: confirm, add to tickets.json product & rest products in products.json
            if product.getCosts():
                
                # 3.1 Add products in tickets.json
                self.__addInTickets(product.shoppingCar, product.costs, product.id)
                
                # 3.2 Rest products in products.json
                self.__restInventory(product.shoppingCar)
        
        # CONTROL ERROR
        else:
            pass
    
    def buyProducts(self):
        colorMessages.information("Solo puede comprar 1 producto del mismo, es decir, no puede pedir por ejemplo 2 hamburguesas. No será contado si es así")
        self.__algorithm()

class OrganizerProducts:
    racesJSON = None
    productsPath = "database/products.json"
    
    # READY
    def __init__(self, races: list) -> None:
        self.racesJSON = races
    
    # READY
    def organizer(self):
        # 1. Verify if exist products.json
        exists = os.path.exists(self.productsPath)
        if exists == False:
            values = []
            
            # Search in races
            for race in self.racesJSON:
                
                # Filter for restaurants
                restaurantsArray = race.get("restaurants")
                
                # Show all restaurants of restaurantsArray
                for restaurant in restaurantsArray:
                    productsRestaurants = restaurant.get("items")
                    
                    for product in productsRestaurants:
                        nameProduct = product.get("name")
                        typeProduct = product.get("type").split(":")[1]
                        priceProduct = product.get("price")
                        quantityProduct = random.randint(50, 200)
                        
                        json = { "name": nameProduct, "type": typeProduct, "price": priceProduct, "quantity": quantityProduct }
                        values.append(json)
            
            seen = set()
            new_l = []
            
            for d in values:
                t = tuple(d.items())
                if t not in seen:
                    seen.add(t)
                    new_l.append(d)
            
            with open(self.productsPath, "w") as file:
                j.dump(values, file)
                
            exit(123123123)

class Restaurants(OrganizerProducts, BuyProducts):
    def __init__(self, races: list) -> None:
        super().__init__(races)