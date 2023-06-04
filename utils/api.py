import requests 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

# Only to organizer API Information
class OrganizerApi:
  def organizerPilots(self, pilots: list):
        values = []
        
        for pilot in pilots:
            data = {'name': pilot['firstName'], 'lastname': pilot['lastName'], 'birthday': pilot['dateOfBirth'],
                    'nationality': pilot['nationality'], 'number': pilot['permanentNumber'], 'refTeam': pilot['team']}
            values.append(data)
            
        return values
    
  def organizerConstructs(self, constructList: list, pilots: list):
      values = []
      
      for construct in constructList:
          data = {'name': construct['name'], 'id': construct['id'],
                  'nationality': construct['nationality'], 'pilots': [], 'points': 0}
          values.append(data)
      
      # Add pilotsRef in her construct
      for construct in values:
          construct_refPilot = construct['id']
          
          for pilot in pilots:
              pilot_refTeam = pilot['refTeam']
              pilot_fullname = pilot['name'] + ' ' + pilot['lastname']
              
              if construct_refPilot == pilot_refTeam:
                  construct['pilots'].append(pilot_fullname)
                  
      return values
  
  def organizerCircuits(self, races: list):
      values = []
      
      for circuit in races:
          data = {
              'name': circuit['circuit']['name'],
              'country': circuit['circuit']['location']['country'],
              'locality': circuit['circuit']['location']['locality'],
              'coords': {
                  'lat': circuit['circuit']['location']['lat'],
                  'long': circuit['circuit']['location']['long']
              }
          }
          values.append(data)
  
      return values
  
  def organizerRaces(self, races: list):
      values = []
      
      for race in races:
          data = {
              'name': race['name'],
              'round': race['round'],
              'date': race['date'],
              'circuit': race['circuit']['name'],
              'podium': race['circuit']['name'],
              'country': race['circuit']['location']['country'],
              'ref': race['circuit']['circuitId'],
              'seats': race['map']
          }
          values.append(data)
      
      return values

# Only to request to URL for received JSON Document for the information
class Api:
    def __Request(self, url: str):
        res = requests.get(url= url, timeout= 1, verify=False)
        return json.loads(res.text)
        
    def GetPilots(self):
        url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json"
        return self.__Request(url)
    
    def GetConstructs(self):
        url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json"
        return self.__Request(url)
    
    def GetRaces(self):
        url = "https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json"
        return self.__Request(url)

# To work with last information of API
class ApiBackUp:
    def GetPilots(self):
        values = '''[
  {
    "id": "albon",
    "permanentNumber": "23",
    "code": "ALB",
    "team": "williams",
    "firstName": "Alexander",
    "lastName": "Albon",
    "dateOfBirth": "1996-03-23",
    "nationality": "Thai"
  },
  {
    "id": "alonso",
    "permanentNumber": "14",
    "code": "ALO",
    "team": "aston_martin",
    "firstName": "Fernando",
    "lastName": "Alonso",
    "dateOfBirth": "1981-07-29",
    "nationality": "Spanish"
  },
  {
    "id": "bottas",
    "permanentNumber": "77",
    "code": "BOT",
    "team": "alfa",
    "firstName": "Valtteri",
    "lastName": "Bottas",
    "dateOfBirth": "1989-08-28",
    "nationality": "Finnish"
  },
  {
    "id": "de_vries",
    "permanentNumber": "45",
    "code": "DEV",
    "team": "alphatauri",
    "firstName": "Nyck",
    "lastName": "de Vries",
    "dateOfBirth": "1995-02-06",
    "nationality": "Dutch"
  },
  {
    "id": "gasly",
    "permanentNumber": "10",
    "code": "GAS",
    "team": "alpine",
    "firstName": "Pierre",
    "lastName": "Gasly",
    "dateOfBirth": "1996-02-07",
    "nationality": "French"
  },
  {
    "id": "hamilton",
    "permanentNumber": "44",
    "code": "HAM",
    "team": "mercedes",
    "firstName": "Lewis",
    "lastName": "Hamilton",
    "dateOfBirth": "1985-01-07",
    "nationality": "British"
  },
  {
    "id": "hulkenberg",
    "permanentNumber": "27",
    "code": "HUL",
    "team": "haas",
    "firstName": "Nico",
    "lastName": "Hülkenberg",
    "dateOfBirth": "1987-08-19",
    "nationality": "German"
  },
  {
    "id": "leclerc",
    "permanentNumber": "16",
    "code": "LEC",
    "team": "ferrari",
    "firstName": "Charles",
    "lastName": "Leclerc",
    "dateOfBirth": "1997-10-16",
    "nationality": "Monegasque"
  },
  {
    "id": "kevin_magnussen",
    "permanentNumber": "20",
    "code": "MAG",
    "team": "haas",
    "firstName": "Kevin",
    "lastName": "Magnussen",
    "dateOfBirth": "1992-10-05",
    "nationality": "Danish"
  },
  {
    "id": "norris",
    "permanentNumber": "4",
    "code": "NOR",
    "team": "mclaren",
    "firstName": "Lando",
    "lastName": "Norris",
    "dateOfBirth": "1999-11-13",
    "nationality": "British"
  },
  {
    "id": "ocon",
    "permanentNumber": "31",
    "code": "OCO",
    "team": "alpine",
    "firstName": "Esteban",
    "lastName": "Ocon",
    "dateOfBirth": "1996-09-17",
    "nationality": "French"
  },
  {
    "id": "perez",
    "permanentNumber": "11",
    "code": "PER",
    "team": "red_bull",
    "firstName": "Sergio",
    "lastName": "Pérez",
    "dateOfBirth": "1990-01-26",
    "nationality": "Mexican"
  },
  {
    "id": "piastri",
    "permanentNumber": "81",
    "code": "PIA",
    "team": "mclaren",
    "firstName": "Oscar",
    "lastName": "Piastri",
    "dateOfBirth": "2001-04-06",
    "nationality": "Australian"
  },
  {
    "id": "russell",
    "permanentNumber": "63",
    "code": "RUS",
    "team": "mercedes",
    "firstName": "George",
    "lastName": "Russell",
    "dateOfBirth": "1998-02-15",
    "nationality": "British"
  },
  {
    "id": "sainz",
    "permanentNumber": "55",
    "code": "SAI",
    "team": "ferrari",
    "firstName": "Carlos",
    "lastName": "Sainz",
    "dateOfBirth": "1994-09-01",
    "nationality": "Spanish"
  },
  {
    "id": "sargeant",
    "permanentNumber": "2",
    "code": "SAR",
    "team": "williams",
    "firstName": "Logan",
    "lastName": "Sargeant",
    "dateOfBirth": "2000-12-31",
    "nationality": "American"
  },
  {
    "id": "stroll",
    "permanentNumber": "18",
    "code": "STR",
    "team": "aston_martin",
    "firstName": "Lance",
    "lastName": "Stroll",
    "dateOfBirth": "1998-10-29",
    "nationality": "Canadian"
  },
  {
    "id": "tsunoda",
    "permanentNumber": "22",
    "code": "TSU",
    "team": "alphatauri",
    "firstName": "Yuki",
    "lastName": "Tsunoda",
    "dateOfBirth": "2000-05-11",
    "nationality": "Japanese"
  },
  {
    "id": "max_verstappen",
    "permanentNumber": "33",
    "code": "VER",
    "team": "red_bull",
    "firstName": "Max",
    "lastName": "Verstappen",
    "dateOfBirth": "1997-09-30",
    "nationality": "Dutch"
  },
  {
    "id": "zhou",
    "permanentNumber": "24",
    "code": "ZHO",
    "team": "alfa",
    "firstName": "Guanyu",
    "lastName": "Zhou",
    "dateOfBirth": "1999-05-30",
    "nationality": "Chinese"
  }
]'''
        return json.loads(values)
    
    def GetConstructs(self):
        values = '''[
  {
    "id": "alfa",
    "name": "Alfa Romeo",
    "nationality": "Swiss"
  },
  {
    "id": "alphatauri",
    "name": "AlphaTauri",
    "nationality": "Italian"
  },
  {
    "id": "alpine",
    "name": "Alpine F1 Team",
    "nationality": "French"
  },
  {
    "id": "aston_martin",
    "name": "Aston Martin",
    "nationality": "British"
  },
  {
    "id": "ferrari",
    "name": "Ferrari",
    "nationality": "Italian"
  },
  {
    "id": "haas",
    "name": "Haas F1 Team",
    "nationality": "American"
  },
  {
    "id": "mclaren",

    "name": "McLaren",
    "nationality": "British"
  },
  {
    "id": "mercedes",
    "name": "Mercedes",
    "nationality": "German"
  },
  {
    "id": "red_bull",
    "name": "Red Bull",
    "nationality": "Austrian"
  },
  {
    "id": "williams",
    "name": "Williams",
    "nationality": "British"
  }
]'''
        return json.loads(values)
    
    def GetRaces(self):
        values = '''[
  {
    "round": "1",
    "name": "Bahrain Grand Prix",
    "circuit": {
      "circuitId": "bahrain",
      "name": "Bahrain International Circuit",
      "location": {
        "lat": 26.0325,
        "long": 50.5106,
        "locality": "Sakhir",
        "country": "Bahrain"
      }
    },
    "date": "2023-03-05",
    "restaurants": [
      {
        "name": "Soria y Rael",
        "items": [
          {
            "name": "ullam voluptas corporis",
            "type": "drink:alcoholic",
            "price": "736.00"
          },
          {
            "name": "officia porro eos",
            "type": "food:restaurant",
            "price": "822.00"
          },
          {
            "name": "facilis tenetur nesciunt",
            "type": "drink:alcoholic",
            "price": "164.00"
          },
          {
            "name": "doloremque perferendis debitis",
            "type": "drink:alcoholic",
            "price": "582.00"
          },
          {
            "name": "temporibus placeat iste",
            "type": "food:fast",
            "price": "381.00"
          },
          {
            "name": "minus in quasi",
            "type": "food:fast",
            "price": "130.00"
          },
          {
            "name": "molestias repudiandae ratione",
            "type": "food:fast",
            "price": "35.00"
          },
          {
            "name": "laborum blanditiis possimus",
            "type": "drink:alcoholic",
            "price": "496.00"
          },
          {
            "name": "debitis impedit consequuntur",
            "type": "drink:not-alcoholic",
            "price": "263.00"
          },
          {
            "name": "ipsa dolor repellat",
            "type": "drink:not-alcoholic",
            "price": "936.00"
          },
          {
            "name": "et incidunt iusto",
            "type": "food:restaurant",
            "price": "563.00"
          },
          {
            "name": "reprehenderit pariatur impedit",
            "type": "drink:not-alcoholic",
            "price": "229.00"
          },
          {
            "name": "exercitationem laudantium quia",
            "type": "food:fast",
            "price": "870.00"
          }
        ]
      }
    ],
    "map": {
      "general": [1, 6],
      "vip": [1, 1]
    }
  },
  {
    "round": "2",
    "name": "Saudi Arabian Grand Prix",
    "circuit": {
      "circuitId": "jeddah",
      "name": "Jeddah Corniche Circuit",
      "Location": {
        "lat": 21.6319,
        "long": 39.1044,
        "locality": "Jeddah",
        "country": "Saudi Arabia"
      },
      "location": {
        "lat": 21.6319,
        "long": 39.1044,
        "locality": "Jeddah",
        "country": "Saudi Arabia"
      }
    },
    "date": "2023-03-19",
    "restaurants": [
      {
        "name": "Soto e Hijos",
        "items": [
          {
            "name": "tempora laboriosam omnis",
            "type": "drink:not-alcoholic",
            "price": "110.00"
          },
          {
            "name": "quisquam eaque cumque",
            "type": "food:fast",
            "price": "314.00"
          },
          {
            "name": "quos quasi in",
            "type": "drink:not-alcoholic",
            "price": "446.00"
          },
          {
            "name": "numquam placeat numquam",
            "type": "drink:alcoholic",
            "price": "521.00"
          },
          {
            "name": "magni inventore hic",
            "type": "drink:alcoholic",
            "price": "353.00"
          },
          {
            "name": "quam eum ad",
            "type": "food:fast",
            "price": "345.00"
          },
          {
            "name": "illum eum occaecati",
            "type": "food:fast",
            "price": "674.00"
          },
          {
            "name": "quae atque magnam",
            "type": "food:restaurant",
            "price": "687.00"
          }
        ]
      }
    ],
    "map": {
      "general": [3, 6],
      "vip": [1, 7]
    }
  },
  {
    "round": "3",
    "name": "Australian Grand Prix",
    "circuit": {
      "circuitId": "albert_park",
      "name": "Albert Park Grand Prix Circuit",
      "Location": {
        "lat": -37.8497,
        "long": 144.968,
        "locality": "Melbourne",
        "country": "Australia"
      },
      "location": {
        "lat": -37.8497,
        "long": 144.968,
        "locality": "Melbourne",
        "country": "Australia"
      }
    },
    "date": "2023-04-02",
    "restaurants": [
      {
        "name": "Menéndez y Olivera",
        "items": [
          {
            "name": "tenetur vitae voluptas",
            "type": "drink:alcoholic",
            "price": "121.00"
          },
          {
            "name": "in eius voluptatum",
            "type": "food:fast",
            "price": "438.00"
          },
          {
            "name": "enim odio quasi",
            "type": "food:restaurant",
            "price": "676.00"
          },
          {
            "name": "quis nam natus",
            "type": "food:fast",
            "price": "60.00"
          },
          {
            "name": "earum explicabo eius",
            "type": "food:fast",
            "price": "992.00"
          },
          {
            "name": "dolore rem libero",
            "type": "drink:alcoholic",
            "price": "571.00"
          },
          {
            "name": "iusto itaque dolorum",
            "type": "food:fast",
            "price": "859.00"
          },
          {
            "name": "tempora blanditiis minus",
            "type": "drink:not-alcoholic",
            "price": "925.00"
          },
          {
            "name": "unde maiores sapiente",
            "type": "drink:not-alcoholic",
            "price": "311.00"
          },
          {
            "name": "repudiandae distinctio error",
            "type": "drink:alcoholic",
            "price": "246.00"
          },
          {
            "name": "hic velit sint",
            "type": "food:restaurant",
            "price": "3.00"
          },
          {
            "name": "iste praesentium necessitatibus",
            "type": "drink:alcoholic",
            "price": "653.00"
          }
        ]
      },
      {
        "name": "Puente Hermanos",
        "items": [
          {
            "name": "ratione recusandae praesentium",
            "type": "food:fast",
            "price": "759.00"
          },
          {
            "name": "numquam molestiae corporis",
            "type": "food:fast",
            "price": "714.00"
          },
          {
            "name": "quod corporis rerum",
            "type": "drink:alcoholic",
            "price": "453.00"
          },
          {
            "name": "impedit facere nisi",
            "type": "food:restaurant",
            "price": "264.00"
          },
          {
            "name": "explicabo earum ducimus",
            "type": "food:restaurant",
            "price": "402.00"
          },
          {
            "name": "quidem debitis aliquam",
            "type": "food:restaurant",
            "price": "593.00"
          },
          {
            "name": "magni sapiente placeat",
            "type": "food:fast",
            "price": "621.00"
          },
          {
            "name": "voluptatum nemo nesciunt",
            "type": "food:restaurant",
            "price": "815.00"
          },
          {
            "name": "harum assumenda quae",
            "type": "drink:not-alcoholic",
            "price": "913.00"
          },
          {
            "name": "exercitationem eveniet culpa",
            "type": "food:fast",
            "price": "790.00"
          }
        ]
      },
      {
        "name": "Alonzo Gaytán S.L.",
        "items": [
          {
            "name": "magni ut animi",
            "type": "food:restaurant",
            "price": "256.00"
          },
          {
            "name": "rem quia placeat",
            "type": "drink:not-alcoholic",
            "price": "116.00"
          },
          {
            "name": "itaque dolores expedita",
            "type": "drink:not-alcoholic",
            "price": "820.00"
          },
          {
            "name": "eos consequatur officia",
            "type": "food:fast",
            "price": "407.00"
          },
          {
            "name": "vel officia itaque",
            "type": "food:restaurant",
            "price": "347.00"
          },
          {
            "name": "inventore quibusdam ratione",
            "type": "drink:not-alcoholic",
            "price": "924.00"
          },
          {
            "name": "quam quidem rerum",
            "type": "drink:not-alcoholic",
            "price": "850.00"
          },
          {
            "name": "explicabo provident accusantium",
            "type": "drink:not-alcoholic",
            "price": "953.00"
          },
          {
            "name": "sequi recusandae harum",
            "type": "drink:not-alcoholic",
            "price": "345.00"
          }
        ]
      },
      {
        "name": "Sedillo Caraballo S.L.",
        "items": [
          {
            "name": "explicabo molestiae necessitatibus",
            "type": "drink:alcoholic",
            "price": "816.00"
          },
          {
            "name": "incidunt necessitatibus illum",
            "type": "food:restaurant",
            "price": "934.00"
          },
          {
            "name": "adipisci ducimus adipisci",
            "type": "drink:not-alcoholic",
            "price": "927.00"
          },
          {
            "name": "porro alias repellendus",
            "type": "drink:alcoholic",
            "price": "982.00"
          },
          {
            "name": "doloremque aliquid explicabo",
            "type": "food:fast",
            "price": "219.00"
          },
          {
            "name": "odio accusamus quidem",
            "type": "drink:not-alcoholic",
            "price": "282.00"
          }
        ]
      },
      {
        "name": "Armas Hermanos",
        "items": [
          {
            "name": "ullam sit illo",
            "type": "drink:not-alcoholic",
            "price": "948.00"
          },
          {
            "name": "aliquid inventore eveniet",
            "type": "drink:alcoholic",
            "price": "600.00"
          },
          {
            "name": "nesciunt vel itaque",
            "type": "drink:not-alcoholic",
            "price": "234.00"
          },
          {
            "name": "ex neque consequatur",
            "type": "drink:alcoholic",
            "price": "946.00"
          },
          {
            "name": "natus sequi porro",
            "type": "food:restaurant",
            "price": "816.00"
          },
          {
            "name": "quisquam aspernatur ex",
            "type": "drink:not-alcoholic",
            "price": "977.00"
          },
          {
            "name": "ab ut exercitationem",
            "type": "food:fast",
            "price": "55.00"
          },
          {
            "name": "fugit itaque exercitationem",
            "type": "drink:alcoholic",
            "price": "519.00"
          },
          {
            "name": "iusto natus fugit",
            "type": "food:fast",
            "price": "252.00"
          },
          {
            "name": "aliquam veniam dolor",
            "type": "food:fast",
            "price": "931.00"
          },
          {
            "name": "laboriosam vel dolorum",
            "type": "food:fast",
            "price": "217.00"
          },
          {
            "name": "tempora et pariatur",
            "type": "drink:alcoholic",
            "price": "914.00"
          },
          {
            "name": "accusamus rerum quaerat",
            "type": "drink:not-alcoholic",
            "price": "12.00"
          },
          {
            "name": "deleniti dignissimos libero",
            "type": "food:fast",
            "price": "584.00"
          }
        ]
      },
      {
        "name": "Guillén, Banda y Grijalva Asociados",
        "items": [
          {
            "name": "earum officiis culpa",
            "type": "drink:not-alcoholic",
            "price": "798.00"
          },
          {
            "name": "laudantium aperiam quisquam",
            "type": "drink:alcoholic",
            "price": "228.00"
          },
          {
            "name": "culpa blanditiis voluptatum",
            "type": "drink:not-alcoholic",
            "price": "874.00"
          }
        ]
      },
      {
        "name": "Sierra Gastélum e Hijos",
        "items": [
          {
            "name": "sunt blanditiis velit",
            "type": "drink:alcoholic",
            "price": "888.00"
          },
          {
            "name": "ea ducimus ipsum",
            "type": "drink:alcoholic",
            "price": "530.00"
          },
          {
            "name": "quis ex delectus",
            "type": "food:fast",
            "price": "824.00"
          },
          {
            "name": "nesciunt vitae saepe",
            "type": "food:restaurant",
            "price": "470.00"
          },
          {
            "name": "velit ad id",
            "type": "food:fast",
            "price": "724.00"
          }
        ]
      },
      {
        "name": "Coronado Covarrubias S.L.",
        "items": [
          {
            "name": "distinctio iusto autem",
            "type": "food:fast",
            "price": "627.00"
          },
          {
            "name": "harum in aliquid",
            "type": "food:restaurant",
            "price": "22.00"
          },
          {
            "name": "recusandae eaque ea",
            "type": "food:restaurant",
            "price": "529.00"
          }
        ]
      }
    ],
    "map": {
      "general": [4, 2],
      "vip": [1, 3]
    }
  },
  {
    "round": "4",
    "name": "Azerbaijan Grand Prix",
    "circuit": {
      "circuitId": "baku",
      "name": "Baku City Circuit",
      "Location": {
        "lat": 40.3725,
        "long": 49.8533,
        "locality": "Baku",
        "country": "Azerbaijan"
      },
      "location": {
        "lat": 40.3725,
        "long": 49.8533,
        "locality": "Baku",
        "country": "Azerbaijan"
      }
    },
    "date": "2023-04-30",
    "restaurants": [
      {
        "name": "Cardona Hermanos",
        "items": [
          {
            "name": "nulla doloribus itaque",
            "type": "drink:alcoholic",
            "price": "275.00"
          },
          {
            "name": "aliquam repudiandae excepturi",
            "type": "food:restaurant",
            "price": "883.00"
          },
          {
            "name": "consequuntur commodi ipsum",
            "type": "food:fast",
            "price": "182.00"
          },
          {
            "name": "consequuntur voluptate velit",
            "type": "food:fast",
            "price": "926.00"
          },
          {
            "name": "delectus facilis officiis",
            "type": "drink:not-alcoholic",
            "price": "753.00"
          },
          {
            "name": "labore sequi tempora",
            "type": "food:fast",
            "price": "768.00"
          },
          {
            "name": "alias earum debitis",
            "type": "food:restaurant",
            "price": "909.00"
          },
          {
            "name": "reiciendis recusandae exercitationem",
            "type": "food:restaurant",
            "price": "334.00"
          },
          {
            "name": "quisquam sequi possimus",
            "type": "drink:alcoholic",
            "price": "331.00"
          },
          {
            "name": "facere in nihil",
            "type": "food:fast",
            "price": "288.00"
          },
          {
            "name": "voluptates vero cupiditate",
            "type": "drink:not-alcoholic",
            "price": "79.00"
          },
          {
            "name": "esse ipsum maiores",
            "type": "drink:alcoholic",
            "price": "821.00"
          },
          {
            "name": "sint enim necessitatibus",
            "type": "food:restaurant",
            "price": "599.00"
          },
          {
            "name": "atque quo earum",
            "type": "food:restaurant",
            "price": "673.00"
          }
        ]
      },
      {
        "name": "Adame Hermanos",
        "items": [
          {
            "name": "corporis corporis fuga",
            "type": "drink:not-alcoholic",
            "price": "927.00"
          },
          {
            "name": "reiciendis odio rerum",
            "type": "food:fast",
            "price": "412.00"
          },
          {
            "name": "aspernatur iure nihil",
            "type": "food:fast",
            "price": "991.00"
          },
          {
            "name": "in deleniti perferendis",
            "type": "drink:alcoholic",
            "price": "34.00"
          },
          {
            "name": "magni dolore est",
            "type": "food:fast",
            "price": "967.00"
          },
          {
            "name": "quasi sequi voluptate",
            "type": "drink:alcoholic",
            "price": "550.00"
          },
          {
            "name": "perspiciatis error accusantium",
            "type": "drink:alcoholic",
            "price": "740.00"
          },
          {
            "name": "quisquam amet debitis",
            "type": "food:fast",
            "price": "980.00"
          },
          {
            "name": "aliquid quibusdam facilis",
            "type": "drink:alcoholic",
            "price": "770.00"
          },
          {
            "name": "quas in cumque",
            "type": "drink:alcoholic",
            "price": "809.00"
          },
          {
            "name": "nesciunt ipsa amet",
            "type": "food:restaurant",
            "price": "406.00"
          },
          {
            "name": "hic quisquam iste",
            "type": "drink:alcoholic",
            "price": "357.00"
          }
        ]
      },
      {
        "name": "Cornejo, Rangel y Delapaz Asociados",
        "items": [
          {
            "name": "hic dignissimos explicabo",
            "type": "food:restaurant",
            "price": "1.00"
          },
          {
            "name": "molestiae nihil maiores",
            "type": "food:fast",
            "price": "490.00"
          },
          {
            "name": "a omnis ipsa",
            "type": "food:restaurant",
            "price": "813.00"
          }
        ]
      },
      {
        "name": "Quesada S.L.",
        "items": [
          {
            "name": "velit nam adipisci",
            "type": "drink:alcoholic",
            "price": "594.00"
          },
          {
            "name": "expedita exercitationem aut",
            "type": "food:restaurant",
            "price": "321.00"
          },
          {
            "name": "nisi quo deleniti",
            "type": "food:fast",
            "price": "877.00"
          },
          {
            "name": "quia at qui",
            "type": "food:restaurant",
            "price": "241.00"
          },
          {
            "name": "consequuntur ea animi",
            "type": "food:fast",
            "price": "60.00"
          },
          {
            "name": "voluptatibus eum officia",
            "type": "food:fast",
            "price": "637.00"
          },
          {
            "name": "odit eos quisquam",
            "type": "food:fast",
            "price": "356.00"
          }
        ]
      },
      {
        "name": "Cornejo S.L.",
        "items": []
      },
      {
        "name": "Araña Rivera S.A.",
        "items": [
          {
            "name": "magnam rerum assumenda",
            "type": "food:restaurant",
            "price": "822.00"
          },
          {
            "name": "a rem dolor",
            "type": "drink:not-alcoholic",
            "price": "305.00"
          },
          {
            "name": "et eum dolorem",
            "type": "drink:not-alcoholic",
            "price": "842.00"
          },
          {
            "name": "eum fugit est",
            "type": "drink:not-alcoholic",
            "price": "802.00"
          },
          {
            "name": "quae facilis alias",
            "type": "drink:not-alcoholic",
            "price": "800.00"
          },
          {
            "name": "recusandae fugit ex",
            "type": "food:fast",
            "price": "769.00"
          },
          {
            "name": "corporis suscipit praesentium",
            "type": "food:fast",
            "price": "191.00"
          },
          {
            "name": "nesciunt voluptatum aut",
            "type": "food:restaurant",
            "price": "163.00"
          },
          {
            "name": "quos nisi vitae",
            "type": "food:fast",
            "price": "308.00"
          }
        ]
      },
      {
        "name": "Carrasquillo Carreón Hermanos",
        "items": [
          {
            "name": "eligendi provident harum",
            "type": "food:fast",
            "price": "392.00"
          },
          {
            "name": "neque itaque reiciendis",
            "type": "drink:alcoholic",
            "price": "390.00"
          },
          {
            "name": "dolores minima repudiandae",
            "type": "food:fast",
            "price": "49.00"
          },
          {
            "name": "maxime modi at",
            "type": "drink:not-alcoholic",
            "price": "591.00"
          },
          {
            "name": "quibusdam maiores dignissimos",
            "type": "food:restaurant",
            "price": "178.00"
          },
          {
            "name": "porro adipisci suscipit",
            "type": "drink:alcoholic",
            "price": "760.00"
          }
        ]
      },
      {
        "name": "Mejía Espinal S.L.",
        "items": [
          {
            "name": "voluptatum consectetur ut",
            "type": "food:restaurant",
            "price": "783.00"
          }
        ]
      },
      {
        "name": "Perea, Berríos y Cardona Asociados",
        "items": [
          {
            "name": "alias quis tempore",
            "type": "food:restaurant",
            "price": "815.00"
          },
          {
            "name": "quidem eveniet unde",
            "type": "drink:not-alcoholic",
            "price": "967.00"
          }
        ]
      }
    ],
    "map": {
      "general": [7, 5],
      "vip": [5, 2]
    }
  },
  {
    "round": "5",
    "name": "Miami Grand Prix",
    "circuit": {
      "circuitId": "miami",
      "name": "Miami International Autodrome",
      "Location": {
        "lat": 25.9581,
        "long": -80.2389,
        "locality": "Miami",
        "country": "USA"
      },
      "location": {
        "lat": 25.9581,
        "long": -80.2389,
        "locality": "Miami",
        "country": "USA"
      }
    },
    "date": "2023-05-07",
    "restaurants": [],
    "map": {
      "general": [7, 3],
      "vip": [7, 3]
    }
  },
  {
    "round": "6",
    "name": "Emilia Romagna Grand Prix",
    "circuit": {
      "circuitId": "imola",
      "name": "Autodromo Enzo e Dino Ferrari",
      "Location": {
        "lat": 44.3439,
        "long": 11.7167,
        "locality": "Imola",
        "country": "Italy"
      },
      "location": {
        "lat": 44.3439,
        "long": 11.7167,
        "locality": "Imola",
        "country": "Italy"
      }
    },
    "date": "2023-05-21",
    "restaurants": [
      {
        "name": "Barajas, Menéndez y Ledesma Asociados",
        "items": [
          {
            "name": "est totam nisi",
            "type": "food:fast",
            "price": "693.00"
          },
          {
            "name": "eligendi aliquam provident",
            "type": "food:fast",
            "price": "967.00"
          },
          {
            "name": "velit perferendis corrupti",
            "type": "food:fast",
            "price": "623.00"
          },
          {
            "name": "modi laboriosam ut",
            "type": "food:restaurant",
            "price": "114.00"
          }
        ]
      },
      {
        "name": "Dávila Córdova Hermanos",
        "items": []
      },
      {
        "name": "Méndez y Villa",
        "items": [
          {
            "name": "saepe culpa fugit",
            "type": "drink:not-alcoholic",
            "price": "458.00"
          },
          {
            "name": "quae illum hic",
            "type": "food:fast",
            "price": "745.00"
          },
          {
            "name": "rerum harum saepe",
            "type": "food:fast",
            "price": "58.00"
          },
          {
            "name": "quae laboriosam a",
            "type": "drink:not-alcoholic",
            "price": "252.00"
          },
          {
            "name": "illum laborum incidunt",
            "type": "drink:not-alcoholic",
            "price": "607.00"
          },
          {
            "name": "laudantium optio pariatur",
            "type": "food:fast",
            "price": "768.00"
          },
          {
            "name": "corporis cupiditate adipisci",
            "type": "food:restaurant",
            "price": "267.00"
          },
          {
            "name": "harum aperiam veritatis",
            "type": "food:restaurant",
            "price": "893.00"
          },
          {
            "name": "earum ipsa provident",
            "type": "drink:alcoholic",
            "price": "1000.00"
          },
          {
            "name": "ducimus consequuntur aspernatur",
            "type": "food:fast",
            "price": "31.00"
          },
          {
            "name": "iure ex laboriosam",
            "type": "food:restaurant",
            "price": "820.00"
          },
          {
            "name": "incidunt ipsum maxime",
            "type": "food:restaurant",
            "price": "6.00"
          }
        ]
      },
      {
        "name": "Rubio y Banda",
        "items": [
          {
            "name": "eligendi natus magni",
            "type": "drink:alcoholic",
            "price": "202.00"
          },
          {
            "name": "architecto maxime ipsa",
            "type": "food:fast",
            "price": "931.00"
          },
          {
            "name": "perferendis architecto ut",
            "type": "food:fast",
            "price": "929.00"
          },
          {
            "name": "nostrum eos unde",
            "type": "food:restaurant",
            "price": "755.00"
          },
          {
            "name": "aspernatur quaerat mollitia",
            "type": "drink:not-alcoholic",
            "price": "970.00"
          },
          {
            "name": "voluptas voluptates laudantium",
            "type": "food:fast",
            "price": "403.00"
          }
        ]
      },
      {
        "name": "Polanco Hermanos",
        "items": [
          {
            "name": "laborum magnam odio",
            "type": "drink:not-alcoholic",
            "price": "397.00"
          },
          {
            "name": "possimus et tempore",
            "type": "food:restaurant",
            "price": "617.00"
          },
          {
            "name": "aperiam facere recusandae",
            "type": "food:fast",
            "price": "562.00"
          },
          {
            "name": "quos dolores repudiandae",
            "type": "food:restaurant",
            "price": "963.00"
          }
        ]
      },
      {
        "name": "Nevárez, García y Cortés Asociados",
        "items": [
          {
            "name": "nihil distinctio ipsam",
            "type": "food:restaurant",
            "price": "687.00"
          },
          {
            "name": "praesentium fuga quaerat",
            "type": "food:restaurant",
            "price": "990.00"
          },
          {
            "name": "eligendi commodi excepturi",
            "type": "food:restaurant",
            "price": "209.00"
          },
          {
            "name": "numquam velit distinctio",
            "type": "drink:not-alcoholic",
            "price": "869.00"
          },
          {
            "name": "quo earum libero",
            "type": "drink:not-alcoholic",
            "price": "662.00"
          },
          {
            "name": "totam tempora voluptatibus",
            "type": "food:fast",
            "price": "101.00"
          },
          {
            "name": "officiis similique sint",
            "type": "drink:not-alcoholic",
            "price": "927.00"
          }
        ]
      },
      {
        "name": "Tapia e Hijos",
        "items": [
          {
            "name": "magni sit iure",
            "type": "food:restaurant",
            "price": "264.00"
          }
        ]
      },
      {
        "name": "Gámez, Gurule y Valadez Asociados",
        "items": [
          {
            "name": "autem tempore nemo",
            "type": "food:restaurant",
            "price": "967.00"
          },
          {
            "name": "sapiente modi at",
            "type": "food:restaurant",
            "price": "754.00"
          },
          {
            "name": "quae quibusdam deserunt",
            "type": "food:fast",
            "price": "274.00"
          },
          {
            "name": "labore architecto recusandae",
            "type": "drink:not-alcoholic",
            "price": "299.00"
          },
          {
            "name": "non veniam non",
            "type": "drink:not-alcoholic",
            "price": "918.00"
          },
          {
            "name": "maiores asperiores saepe",
            "type": "food:fast",
            "price": "251.00"
          },
          {
            "name": "inventore inventore consequatur",
            "type": "food:fast",
            "price": "849.00"
          },
          {
            "name": "atque cumque id",
            "type": "drink:not-alcoholic",
            "price": "452.00"
          },
          {
            "name": "ab libero beatae",
            "type": "food:restaurant",
            "price": "317.00"
          },
          {
            "name": "nulla deleniti incidunt",
            "type": "food:fast",
            "price": "291.00"
          }
        ]
      },
      {
        "name": "Espinal Rosales e Hijos",
        "items": [
          {
            "name": "assumenda excepturi pariatur",
            "type": "drink:not-alcoholic",
            "price": "642.00"
          },
          {
            "name": "veniam mollitia animi",
            "type": "food:fast",
            "price": "485.00"
          },
          {
            "name": "fugiat at quasi",
            "type": "food:restaurant",
            "price": "545.00"
          },
          {
            "name": "nemo ipsam pariatur",
            "type": "drink:alcoholic",
            "price": "583.00"
          },
          {
            "name": "voluptatibus ipsa inventore",
            "type": "drink:not-alcoholic",
            "price": "690.00"
          },
          {
            "name": "quos veniam cumque",
            "type": "food:fast",
            "price": "319.00"
          }
        ]
      }
    ],
    "map": {
      "general": [2, 3],
      "vip": [6, 2]
    }
  },
  {
    "round": "7",
    "name": "Monaco Grand Prix",
    "circuit": {
      "circuitId": "monaco",
      "name": "Circuit de Monaco",
      "Location": {
        "lat": 43.7347,
        "long": 7.42056,
        "locality": "Monte-Carlo",
        "country": "Monaco"
      },
      "location": {
        "lat": 43.7347,
        "long": 7.42056,
        "locality": "Monte-Carlo",
        "country": "Monaco"
      }
    },
    "date": "2023-05-28",
    "restaurants": [
      {
        "name": "Vela, Mares y Ortega Asociados",
        "items": [
          {
            "name": "consequuntur repudiandae sunt",
            "type": "drink:alcoholic",
            "price": "900.00"
          },
          {
            "name": "vitae repudiandae quia",
            "type": "food:fast",
            "price": "341.00"
          },
          {
            "name": "facere nesciunt deserunt",
            "type": "food:fast",
            "price": "414.00"
          },
          {
            "name": "quis enim voluptatibus",
            "type": "food:restaurant",
            "price": "940.00"
          },
          {
            "name": "impedit explicabo facilis",
            "type": "drink:alcoholic",
            "price": "514.00"
          },
          {
            "name": "similique soluta dolores",
            "type": "drink:alcoholic",
            "price": "886.00"
          },
          {
            "name": "libero dignissimos ab",
            "type": "food:fast",
            "price": "185.00"
          },
          {
            "name": "nesciunt vitae aliquid",
            "type": "drink:alcoholic",
            "price": "795.00"
          },
          {
            "name": "veritatis voluptatibus adipisci",
            "type": "food:restaurant",
            "price": "811.00"
          },
          {
            "name": "et quidem fugit",
            "type": "drink:alcoholic",
            "price": "927.00"
          },
          {
            "name": "quae non quo",
            "type": "drink:alcoholic",
            "price": "387.00"
          },
          {
            "name": "corrupti mollitia aliquam",
            "type": "food:restaurant",
            "price": "637.00"
          }
        ]
      },
      {
        "name": "Briseño y Murillo",
        "items": [
          {
            "name": "voluptate quis necessitatibus",
            "type": "food:restaurant",
            "price": "975.00"
          },
          {
            "name": "quidem corrupti possimus",
            "type": "drink:not-alcoholic",
            "price": "380.00"
          },
          {
            "name": "quos esse similique",
            "type": "drink:alcoholic",
            "price": "312.00"
          },
          {
            "name": "pariatur nostrum doloribus",
            "type": "food:fast",
            "price": "325.00"
          },
          {
            "name": "asperiores cum veniam",
            "type": "drink:alcoholic",
            "price": "207.00"
          },
          {
            "name": "laboriosam consectetur quidem",
            "type": "food:restaurant",
            "price": "584.00"
          },
          {
            "name": "vitae quaerat quia",
            "type": "food:fast",
            "price": "659.00"
          }
        ]
      },
      {
        "name": "Collazo Hermanos",
        "items": [
          {
            "name": "aliquid excepturi laborum",
            "type": "drink:alcoholic",
            "price": "868.00"
          },
          {
            "name": "error optio illo",
            "type": "food:restaurant",
            "price": "968.00"
          },
          {
            "name": "at natus quam",
            "type": "food:restaurant",
            "price": "562.00"
          },
          {
            "name": "consectetur delectus consequuntur",
            "type": "food:fast",
            "price": "380.00"
          },
          {
            "name": "eveniet sunt fugiat",
            "type": "drink:alcoholic",
            "price": "113.00"
          },
          {
            "name": "ipsum perferendis similique",
            "type": "drink:alcoholic",
            "price": "738.00"
          },
          {
            "name": "in vero quaerat",
            "type": "food:fast",
            "price": "814.00"
          },
          {
            "name": "doloremque necessitatibus possimus",
            "type": "drink:not-alcoholic",
            "price": "601.00"
          }
        ]
      },
      {
        "name": "Almanza, Toledo y Girón Asociados",
        "items": []
      }
    ],
    "map": {
      "general": [5, 8],
      "vip": [1, 6]
    }
  },
  {
    "round": "8",
    "name": "Spanish Grand Prix",
    "circuit": {
      "circuitId": "catalunya",
      "name": "Circuit de Barcelona-Catalunya",
      "Location": {
        "lat": 41.57,
        "long": 2.26111,
        "locality": "Montmeló",
        "country": "Spain"
      },
      "location": {
        "lat": 41.57,
        "long": 2.26111,
        "locality": "Montmeló",
        "country": "Spain"
      }
    },
    "date": "2023-06-04",
    "restaurants": [],
    "map": {
      "general": [1, 7],
      "vip": [3, 2]
    }
  },
  {
    "round": "9",
    "name": "Canadian Grand Prix",
    "circuit": {
      "circuitId": "villeneuve",
      "name": "Circuit Gilles Villeneuve",
      "Location": {
        "lat": 45.5,
        "long": -73.5228,
        "locality": "Montreal",
        "country": "Canada"
      },
      "location": {
        "lat": 45.5,
        "long": -73.5228,
        "locality": "Montreal",
        "country": "Canada"
      }
    },
    "date": "2023-06-18",
    "restaurants": [
      {
        "name": "Páez y Garrido",
        "items": [
          {
            "name": "in voluptatibus quisquam",
            "type": "drink:not-alcoholic",
            "price": "617.00"
          }
        ]
      }
    ],
    "map": {
      "general": [8, 1],
      "vip": [6, 5]
    }
  },
  {
    "round": "10",
    "name": "Austrian Grand Prix",
    "circuit": {
      "circuitId": "red_bull_ring",
      "name": "Red Bull Ring",
      "Location": {
        "lat": 47.2197,
        "long": 14.7647,
        "locality": "Spielberg",
        "country": "Austria"
      },
      "location": {
        "lat": 47.2197,
        "long": 14.7647,
        "locality": "Spielberg",
        "country": "Austria"
      }
    },
    "date": "2023-07-02",
    "restaurants": [
      {
        "name": "Tovar y Tórrez",
        "items": [
          {
            "name": "fugit porro perspiciatis",
            "type": "food:restaurant",
            "price": "897.00"
          },
          {
            "name": "totam eaque asperiores",
            "type": "food:fast",
            "price": "456.00"
          },
          {
            "name": "nulla corporis minima",
            "type": "food:restaurant",
            "price": "899.00"
          }
        ]
      },
      {
        "name": "Aranda y Burgos",
        "items": [
          {
            "name": "facilis reprehenderit quibusdam",
            "type": "food:fast",
            "price": "661.00"
          },
          {
            "name": "molestiae id asperiores",
            "type": "food:restaurant",
            "price": "427.00"
          },
          {
            "name": "rerum a recusandae",
            "type": "drink:not-alcoholic",
            "price": "312.00"
          },
          {
            "name": "neque vitae quam",
            "type": "food:fast",
            "price": "582.00"
          },
          {
            "name": "illum quo impedit",
            "type": "food:fast",
            "price": "14.00"
          },
          {
            "name": "quaerat minus ullam",
            "type": "drink:not-alcoholic",
            "price": "437.00"
          },
          {
            "name": "quos dolores perspiciatis",
            "type": "food:restaurant",
            "price": "77.00"
          },
          {
            "name": "repudiandae distinctio fuga",
            "type": "drink:not-alcoholic",
            "price": "487.00"
          },
          {
            "name": "corporis quo deleniti",
            "type": "food:restaurant",
            "price": "563.00"
          },
          {
            "name": "amet doloribus repellendus",
            "type": "drink:alcoholic",
            "price": "336.00"
          },
          {
            "name": "repellat quibusdam in",
            "type": "drink:alcoholic",
            "price": "590.00"
          },
          {
            "name": "tenetur quis hic",
            "type": "drink:not-alcoholic",
            "price": "100.00"
          }
        ]
      },
      {
        "name": "Navarro y Saavedra",
        "items": [
          {
            "name": "assumenda nulla labore",
            "type": "food:restaurant",
            "price": "569.00"
          },
          {
            "name": "autem id esse",
            "type": "drink:alcoholic",
            "price": "664.00"
          },
          {
            "name": "dolor nihil molestias",
            "type": "food:fast",
            "price": "337.00"
          },
          {
            "name": "laudantium molestiae expedita",
            "type": "drink:not-alcoholic",
            "price": "732.00"
          }
        ]
      },
      {
        "name": "Jaimes y Angulo",
        "items": [
          {
            "name": "magni cupiditate alias",
            "type": "food:restaurant",
            "price": "67.00"
          },
          {
            "name": "possimus quas soluta",
            "type": "drink:alcoholic",
            "price": "498.00"
          }
        ]
      },
      {
        "name": "Laboy Barrios Hermanos",
        "items": [
          {
            "name": "odio accusamus iure",
            "type": "food:fast",
            "price": "806.00"
          },
          {
            "name": "porro eius laudantium",
            "type": "food:fast",
            "price": "738.00"
          },
          {
            "name": "dicta harum voluptate",
            "type": "food:fast",
            "price": "799.00"
          },
          {
            "name": "earum atque porro",
            "type": "food:fast",
            "price": "927.00"
          },
          {
            "name": "minus doloribus fugiat",
            "type": "food:restaurant",
            "price": "938.00"
          }
        ]
      },
      {
        "name": "Balderas Pizarro S.L.",
        "items": [
          {
            "name": "eius quis cum",
            "type": "drink:not-alcoholic",
            "price": "405.00"
          },
          {
            "name": "expedita eius tempora",
            "type": "food:restaurant",
            "price": "80.00"
          },
          {
            "name": "officia earum consequatur",
            "type": "drink:alcoholic",
            "price": "922.00"
          },
          {
            "name": "illum blanditiis quo",
            "type": "food:restaurant",
            "price": "629.00"
          },
          {
            "name": "in expedita sint",
            "type": "drink:alcoholic",
            "price": "50.00"
          },
          {
            "name": "nobis facilis et",
            "type": "drink:alcoholic",
            "price": "934.00"
          },
          {
            "name": "asperiores suscipit dolorum",
            "type": "drink:not-alcoholic",
            "price": "676.00"
          }
        ]
      },
      {
        "name": "Holguín S.A.",
        "items": [
          {
            "name": "assumenda voluptatum adipisci",
            "type": "food:restaurant",
            "price": "39.00"
          },
          {
            "name": "ex ex quibusdam",
            "type": "drink:not-alcoholic",
            "price": "559.00"
          },
          {
            "name": "dolores reprehenderit eaque",
            "type": "food:restaurant",
            "price": "578.00"
          },
          {
            "name": "accusamus in animi",
            "type": "drink:not-alcoholic",
            "price": "887.00"
          },
          {
            "name": "libero voluptas ut",
            "type": "food:restaurant",
            "price": "354.00"
          },
          {
            "name": "maxime vel odio",
            "type": "drink:alcoholic",
            "price": "949.00"
          }
        ]
      },
      {
        "name": "Sisneros S.A.",
        "items": [
          {
            "name": "illum nihil expedita",
            "type": "drink:alcoholic",
            "price": "802.00"
          },
          {
            "name": "molestiae quo eligendi",
            "type": "food:fast",
            "price": "633.00"
          },
          {
            "name": "dolore praesentium quos",
            "type": "food:fast",
            "price": "620.00"
          },
          {
            "name": "laborum magnam repellat",
            "type": "food:restaurant",
            "price": "172.00"
          },
          {
            "name": "et optio hic",
            "type": "drink:alcoholic",
            "price": "565.00"
          },
          {
            "name": "expedita atque consequuntur",
            "type": "drink:alcoholic",
            "price": "597.00"
          },
          {
            "name": "mollitia temporibus odio",
            "type": "drink:alcoholic",
            "price": "973.00"
          },
          {
            "name": "deleniti doloribus placeat",
            "type": "drink:alcoholic",
            "price": "948.00"
          },
          {
            "name": "aut doloribus id",
            "type": "drink:alcoholic",
            "price": "31.00"
          },
          {
            "name": "animi consequatur impedit",
            "type": "food:fast",
            "price": "803.00"
          }
        ]
      },
      {
        "name": "Calderón S.A.",
        "items": [
          {
            "name": "eaque amet laborum",
            "type": "drink:not-alcoholic",
            "price": "253.00"
          },
          {
            "name": "ut laborum tenetur",
            "type": "drink:not-alcoholic",
            "price": "875.00"
          },
          {
            "name": "in laudantium sed",
            "type": "drink:not-alcoholic",
            "price": "11.00"
          },
          {
            "name": "omnis quisquam ad",
            "type": "food:restaurant",
            "price": "615.00"
          },
          {
            "name": "accusantium ipsa sed",
            "type": "food:restaurant",
            "price": "131.00"
          },
          {
            "name": "pariatur delectus libero",
            "type": "food:restaurant",
            "price": "229.00"
          },
          {
            "name": "qui nulla minima",
            "type": "food:fast",
            "price": "895.00"
          },
          {
            "name": "nemo voluptates sint",
            "type": "food:fast",
            "price": "197.00"
          },
          {
            "name": "tempore dolorum repellendus",
            "type": "food:fast",
            "price": "112.00"
          },
          {
            "name": "eos recusandae nihil",
            "type": "food:fast",
            "price": "731.00"
          },
          {
            "name": "rerum alias soluta",
            "type": "drink:not-alcoholic",
            "price": "279.00"
          },
          {
            "name": "soluta blanditiis officia",
            "type": "food:fast",
            "price": "689.00"
          }
        ]
      }
    ],
    "map": {
      "general": [7, 8],
      "vip": [2, 3]
    }
  },
  {
    "round": "11",
    "name": "British Grand Prix",
    "circuit": {
      "circuitId": "silverstone",
      "name": "Silverstone Circuit",
      "Location": {
        "lat": 52.0786,
        "long": -1.01694,
        "locality": "Silverstone",
        "country": "UK"
      },
      "location": {
        "lat": 52.0786,
        "long": -1.01694,
        "locality": "Silverstone",
        "country": "UK"
      }
    },
    "date": "2023-07-09",
    "restaurants": [
      {
        "name": "Rincón, Sanabria y Marroquín Asociados",
        "items": [
          {
            "name": "facere quas doloribus",
            "type": "drink:alcoholic",
            "price": "881.00"
          },
          {
            "name": "quod odit dolor",
            "type": "food:fast",
            "price": "648.00"
          },
          {
            "name": "sunt eligendi alias",
            "type": "drink:alcoholic",
            "price": "822.00"
          },
          {
            "name": "numquam libero rem",
            "type": "food:restaurant",
            "price": "35.00"
          },
          {
            "name": "sit soluta natus",
            "type": "food:fast",
            "price": "75.00"
          },
          {
            "name": "autem nihil architecto",
            "type": "food:restaurant",
            "price": "151.00"
          },
          {
            "name": "et reprehenderit fuga",
            "type": "food:restaurant",
            "price": "806.00"
          },
          {
            "name": "non accusantium reiciendis",
            "type": "food:fast",
            "price": "40.00"
          },
          {
            "name": "reprehenderit reprehenderit suscipit",
            "type": "food:restaurant",
            "price": "152.00"
          },
          {
            "name": "tempore tempore placeat",
            "type": "food:restaurant",
            "price": "808.00"
          }
        ]
      },
      {
        "name": "Pizarro, Armas y Longoria Asociados",
        "items": []
      },
      {
        "name": "Ulibarri Hermanos",
        "items": [
          {
            "name": "nam tempore ducimus",
            "type": "food:fast",
            "price": "625.00"
          },
          {
            "name": "et officiis iure",
            "type": "drink:not-alcoholic",
            "price": "267.00"
          },
          {
            "name": "libero accusantium laboriosam",
            "type": "food:restaurant",
            "price": "523.00"
          },
          {
            "name": "doloribus mollitia recusandae",
            "type": "food:restaurant",
            "price": "449.00"
          },
          {
            "name": "incidunt molestiae eius",
            "type": "drink:alcoholic",
            "price": "1.00"
          },
          {
            "name": "eum maiores incidunt",
            "type": "food:restaurant",
            "price": "96.00"
          },
          {
            "name": "voluptate nulla qui",
            "type": "drink:alcoholic",
            "price": "470.00"
          },
          {
            "name": "est officia quae",
            "type": "food:fast",
            "price": "226.00"
          },
          {
            "name": "deleniti cum animi",
            "type": "food:fast",
            "price": "19.00"
          },
          {
            "name": "iusto quibusdam accusantium",
            "type": "drink:not-alcoholic",
            "price": "722.00"
          },
          {
            "name": "recusandae molestias voluptas",
            "type": "drink:not-alcoholic",
            "price": "230.00"
          },
          {
            "name": "veniam ut magnam",
            "type": "food:fast",
            "price": "564.00"
          }
        ]
      },
      {
        "name": "Puente y Serna",
        "items": [
          {
            "name": "nulla a quos",
            "type": "food:restaurant",
            "price": "163.00"
          },
          {
            "name": "in beatae deleniti",
            "type": "drink:not-alcoholic",
            "price": "381.00"
          }
        ]
      },
      {
        "name": "Calvillo Hermanos",
        "items": [
          {
            "name": "quia iusto sint",
            "type": "drink:not-alcoholic",
            "price": "870.00"
          },
          {
            "name": "laborum earum aspernatur",
            "type": "food:restaurant",
            "price": "235.00"
          },
          {
            "name": "quo repudiandae illum",
            "type": "food:fast",
            "price": "536.00"
          }
        ]
      },
      {
        "name": "Molina y Regalado",
        "items": [
          {
            "name": "omnis a atque",
            "type": "food:restaurant",
            "price": "127.00"
          },
          {
            "name": "modi eveniet corporis",
            "type": "drink:alcoholic",
            "price": "100.00"
          },
          {
            "name": "voluptatem deserunt eos",
            "type": "food:fast",
            "price": "164.00"
          },
          {
            "name": "doloribus ex commodi",
            "type": "food:restaurant",
            "price": "396.00"
          },
          {
            "name": "tempore expedita reiciendis",
            "type": "drink:not-alcoholic",
            "price": "347.00"
          },
          {
            "name": "reprehenderit mollitia dicta",
            "type": "drink:not-alcoholic",
            "price": "800.00"
          },
          {
            "name": "nulla repudiandae rem",
            "type": "drink:not-alcoholic",
            "price": "114.00"
          },
          {
            "name": "mollitia molestiae animi",
            "type": "food:fast",
            "price": "970.00"
          },
          {
            "name": "tempora explicabo doloribus",
            "type": "food:fast",
            "price": "168.00"
          }
        ]
      },
      {
        "name": "Alaníz, Camarillo y Palacios Asociados",
        "items": [
          {
            "name": "iusto voluptates saepe",
            "type": "drink:alcoholic",
            "price": "849.00"
          },
          {
            "name": "explicabo nobis sequi",
            "type": "drink:not-alcoholic",
            "price": "454.00"
          },
          {
            "name": "veritatis quod aspernatur",
            "type": "drink:alcoholic",
            "price": "432.00"
          },
          {
            "name": "illo voluptate consequatur",
            "type": "drink:not-alcoholic",
            "price": "757.00"
          },
          {
            "name": "incidunt soluta alias",
            "type": "food:fast",
            "price": "557.00"
          },
          {
            "name": "sit architecto quos",
            "type": "food:restaurant",
            "price": "806.00"
          },
          {
            "name": "maxime tempore architecto",
            "type": "food:restaurant",
            "price": "724.00"
          },
          {
            "name": "doloremque pariatur temporibus",
            "type": "food:restaurant",
            "price": "41.00"
          }
        ]
      },
      {
        "name": "Rosario Holguín S.L.",
        "items": [
          {
            "name": "maxime nam quos",
            "type": "drink:alcoholic",
            "price": "797.00"
          },
          {
            "name": "earum laboriosam quia",
            "type": "drink:alcoholic",
            "price": "570.00"
          },
          {
            "name": "libero dolore dolores",
            "type": "drink:alcoholic",
            "price": "862.00"
          },
          {
            "name": "nesciunt laborum iusto",
            "type": "drink:alcoholic",
            "price": "866.00"
          },
          {
            "name": "harum quod atque",
            "type": "drink:not-alcoholic",
            "price": "528.00"
          },
          {
            "name": "a exercitationem modi",
            "type": "drink:alcoholic",
            "price": "207.00"
          },
          {
            "name": "rerum veniam itaque",
            "type": "drink:not-alcoholic",
            "price": "102.00"
          },
          {
            "name": "sunt facere quasi",
            "type": "drink:alcoholic",
            "price": "86.00"
          },
          {
            "name": "neque vero ipsam",
            "type": "drink:not-alcoholic",
            "price": "993.00"
          },
          {
            "name": "fugit temporibus alias",
            "type": "food:fast",
            "price": "824.00"
          },
          {
            "name": "provident necessitatibus et",
            "type": "drink:alcoholic",
            "price": "564.00"
          },
          {
            "name": "enim necessitatibus aut",
            "type": "drink:not-alcoholic",
            "price": "108.00"
          },
          {
            "name": "accusamus sapiente nesciunt",
            "type": "drink:alcoholic",
            "price": "462.00"
          }
        ]
      }
    ],
    "map": {
      "general": [7, 3],
      "vip": [5, 2]
    }
  },
  {
    "round": "12",
    "name": "Hungarian Grand Prix",
    "circuit": {
      "circuitId": "hungaroring",
      "name": "Hungaroring",
      "Location": {
        "lat": 47.5789,
        "long": 19.2486,
        "locality": "Budapest",
        "country": "Hungary"
      },
      "location": {
        "lat": 47.5789,
        "long": 19.2486,
        "locality": "Budapest",
        "country": "Hungary"
      }
    },
    "date": "2023-07-23",
    "restaurants": [
      {
        "name": "Polanco Vera Hermanos",
        "items": [
          {
            "name": "magni animi quam",
            "type": "food:fast",
            "price": "747.00"
          },
          {
            "name": "eum reiciendis cumque",
            "type": "drink:alcoholic",
            "price": "591.00"
          },
          {
            "name": "aut veritatis quidem",
            "type": "food:restaurant",
            "price": "13.00"
          },
          {
            "name": "ut incidunt rem",
            "type": "food:restaurant",
            "price": "805.00"
          },
          {
            "name": "numquam sapiente ratione",
            "type": "drink:not-alcoholic",
            "price": "396.00"
          },
          {
            "name": "magnam eaque porro",
            "type": "drink:alcoholic",
            "price": "147.00"
          },
          {
            "name": "explicabo modi ullam",
            "type": "food:restaurant",
            "price": "848.00"
          },
          {
            "name": "ut ullam consequatur",
            "type": "food:fast",
            "price": "108.00"
          }
        ]
      },
      {
        "name": "Ocasio y Armenta",
        "items": [
          {
            "name": "consequatur a eligendi",
            "type": "food:fast",
            "price": "794.00"
          },
          {
            "name": "quidem adipisci nulla",
            "type": "drink:alcoholic",
            "price": "505.00"
          },
          {
            "name": "architecto nulla non",
            "type": "drink:not-alcoholic",
            "price": "546.00"
          },
          {
            "name": "laboriosam dicta minus",
            "type": "drink:not-alcoholic",
            "price": "543.00"
          },
          {
            "name": "totam facere minima",
            "type": "food:restaurant",
            "price": "29.00"
          },
          {
            "name": "incidunt nobis distinctio",
            "type": "drink:alcoholic",
            "price": "499.00"
          }
        ]
      },
      {
        "name": "Altamirano Figueroa S.L.",
        "items": [
          {
            "name": "qui necessitatibus deserunt",
            "type": "drink:alcoholic",
            "price": "374.00"
          },
          {
            "name": "saepe vero iusto",
            "type": "food:restaurant",
            "price": "94.00"
          },
          {
            "name": "numquam ipsa aliquid",
            "type": "drink:alcoholic",
            "price": "432.00"
          },
          {
            "name": "quam voluptatibus iusto",
            "type": "food:restaurant",
            "price": "323.00"
          },
          {
            "name": "eligendi dolore quia",
            "type": "food:restaurant",
            "price": "141.00"
          },
          {
            "name": "maxime dignissimos nam",
            "type": "drink:not-alcoholic",
            "price": "734.00"
          },
          {
            "name": "iure earum tenetur",
            "type": "drink:alcoholic",
            "price": "386.00"
          }
        ]
      },
      {
        "name": "Cano, Elizondo y Balderas Asociados",
        "items": [
          {
            "name": "labore autem sunt",
            "type": "drink:alcoholic",
            "price": "615.00"
          },
          {
            "name": "aspernatur eum voluptatibus",
            "type": "food:restaurant",
            "price": "282.00"
          },
          {
            "name": "odit doloribus eveniet",
            "type": "drink:alcoholic",
            "price": "843.00"
          },
          {
            "name": "cumque nulla libero",
            "type": "food:restaurant",
            "price": "114.00"
          },
          {
            "name": "a pariatur doloribus",
            "type": "food:restaurant",
            "price": "629.00"
          },
          {
            "name": "aspernatur iste molestiae",
            "type": "drink:alcoholic",
            "price": "45.00"
          },
          {
            "name": "atque quos ea",
            "type": "drink:alcoholic",
            "price": "182.00"
          },
          {
            "name": "sunt non eius",
            "type": "food:fast",
            "price": "461.00"
          }
        ]
      }
    ],
    "map": {
      "general": [7, 6],
      "vip": [1, 8]
    }
  },
  {
    "round": "13",
    "name": "Belgian Grand Prix",
    "circuit": {
      "circuitId": "spa",
      "name": "Circuit de Spa-Francorchamps",
      "Location": {
        "lat": 50.4372,
        "long": 5.97139,
        "locality": "Spa",
        "country": "Belgium"
      },
      "location": {
        "lat": 50.4372,
        "long": 5.97139,
        "locality": "Spa",
        "country": "Belgium"
      }
    },
    "date": "2023-07-30",
    "restaurants": [],
    "map": {
      "general": [1, 3],
      "vip": [4, 7]
    }
  },
  {
    "round": "14",
    "name": "Dutch Grand Prix",
    "circuit": {
      "circuitId": "zandvoort",
      "name": "Circuit Park Zandvoort",
      "Location": {
        "lat": 52.3888,
        "long": 4.54092,
        "locality": "Zandvoort",
        "country": "Netherlands"
      },
      "location": {
        "lat": 52.3888,
        "long": 4.54092,
        "locality": "Zandvoort",
        "country": "Netherlands"
      }
    },
    "date": "2023-08-27",
    "restaurants": [],
    "map": {
      "general": [8, 3],
      "vip": [4, 6]
    }
  },
  {
    "round": "15",
    "name": "Italian Grand Prix",
    "circuit": {
      "circuitId": "monza",
      "name": "Autodromo Nazionale di Monza",
      "Location": {
        "lat": 45.6156,
        "long": 9.28111,
        "locality": "Monza",
        "country": "Italy"
      },
      "location": {
        "lat": 45.6156,
        "long": 9.28111,
        "locality": "Monza",
        "country": "Italy"
      }
    },
    "date": "2023-09-03",
    "restaurants": [
      {
        "name": "Zarate S.A.",
        "items": [
          {
            "name": "labore quas repellendus",
            "type": "food:fast",
            "price": "999.00"
          }
        ]
      },
      {
        "name": "Olivares y Vega",
        "items": [
          {
            "name": "animi cumque repellendus",
            "type": "drink:alcoholic",
            "price": "133.00"
          },
          {
            "name": "reiciendis animi unde",
            "type": "drink:not-alcoholic",
            "price": "381.00"
          },
          {
            "name": "ad in a",
            "type": "drink:alcoholic",
            "price": "791.00"
          }
        ]
      },
      {
        "name": "Cárdenas, Alfaro y Mireles Asociados",
        "items": [
          {
            "name": "labore quis autem",
            "type": "food:restaurant",
            "price": "476.00"
          },
          {
            "name": "incidunt sunt iure",
            "type": "food:restaurant",
            "price": "129.00"
          },
          {
            "name": "atque minus magnam",
            "type": "drink:alcoholic",
            "price": "943.00"
          },
          {
            "name": "sunt vero eos",
            "type": "food:fast",
            "price": "693.00"
          },
          {
            "name": "quo voluptates sapiente",
            "type": "food:fast",
            "price": "139.00"
          },
          {
            "name": "facere ipsa facilis",
            "type": "food:restaurant",
            "price": "43.00"
          },
          {
            "name": "ex eligendi harum",
            "type": "drink:alcoholic",
            "price": "522.00"
          },
          {
            "name": "ipsam incidunt voluptatum",
            "type": "food:restaurant",
            "price": "970.00"
          },
          {
            "name": "maiores sapiente tenetur",
            "type": "drink:not-alcoholic",
            "price": "3.00"
          }
        ]
      }
    ],
    "map": {
      "general": [4, 8],
      "vip": [1, 1]
    }
  },
  {
    "round": "16",
    "name": "Singapore Grand Prix",
    "circuit": {
      "circuitId": "marina_bay",
      "name": "Marina Bay Street Circuit",
      "Location": {
        "lat": 1.2914,
        "long": 103.864,
        "locality": "Marina Bay",
        "country": "Singapore"
      },
      "location": {
        "lat": 1.2914,
        "long": 103.864,
        "locality": "Marina Bay",
        "country": "Singapore"
      }
    },
    "date": "2023-09-17",
    "restaurants": [
      {
        "name": "Negrete, Romo y Esquibel Asociados",
        "items": [
          {
            "name": "voluptate ipsa exercitationem",
            "type": "food:restaurant",
            "price": "728.00"
          },
          {
            "name": "fugit quia laudantium",
            "type": "food:fast",
            "price": "716.00"
          },
          {
            "name": "quidem error commodi",
            "type": "drink:not-alcoholic",
            "price": "974.00"
          },
          {
            "name": "architecto laudantium corporis",
            "type": "food:fast",
            "price": "689.00"
          },
          {
            "name": "sequi nulla occaecati",
            "type": "food:fast",
            "price": "821.00"
          },
          {
            "name": "possimus aperiam velit",
            "type": "food:restaurant",
            "price": "751.00"
          },
          {
            "name": "totam officiis quo",
            "type": "food:restaurant",
            "price": "629.00"
          },
          {
            "name": "vel doloribus maiores",
            "type": "drink:alcoholic",
            "price": "428.00"
          },
          {
            "name": "voluptates blanditiis tempora",
            "type": "drink:alcoholic",
            "price": "272.00"
          },
          {
            "name": "maxime dicta ipsum",
            "type": "food:restaurant",
            "price": "822.00"
          },
          {
            "name": "officiis accusantium illo",
            "type": "food:restaurant",
            "price": "517.00"
          }
        ]
      },
      {
        "name": "Guzmán Preciado S.A.",
        "items": [
          {
            "name": "voluptatem mollitia dolorum",
            "type": "food:fast",
            "price": "771.00"
          }
        ]
      },
      {
        "name": "Castellanos y Vallejo",
        "items": [
          {
            "name": "incidunt nesciunt quas",
            "type": "drink:alcoholic",
            "price": "345.00"
          },
          {
            "name": "nesciunt dolorem dolorem",
            "type": "drink:not-alcoholic",
            "price": "186.00"
          }
        ]
      },
      {
        "name": "Lira Hermanos",
        "items": [
          {
            "name": "sequi quo nulla",
            "type": "food:fast",
            "price": "704.00"
          },
          {
            "name": "maxime dolorem officia",
            "type": "food:restaurant",
            "price": "807.00"
          },
          {
            "name": "cum dolorum maxime",
            "type": "drink:not-alcoholic",
            "price": "464.00"
          },
          {
            "name": "exercitationem perferendis voluptatem",
            "type": "drink:alcoholic",
            "price": "972.00"
          }
        ]
      },
      {
        "name": "Barraza Rosario S.L.",
        "items": [
          {
            "name": "id consectetur quo",
            "type": "food:fast",
            "price": "160.00"
          },
          {
            "name": "odio similique neque",
            "type": "food:restaurant",
            "price": "415.00"
          },
          {
            "name": "iste assumenda aspernatur",
            "type": "food:fast",
            "price": "734.00"
          },
          {
            "name": "ea maiores ad",
            "type": "food:fast",
            "price": "605.00"
          },
          {
            "name": "dolorum quis quaerat",
            "type": "drink:alcoholic",
            "price": "160.00"
          },
          {
            "name": "ad ipsa consectetur",
            "type": "drink:alcoholic",
            "price": "20.00"
          },
          {
            "name": "ut molestias non",
            "type": "food:fast",
            "price": "558.00"
          },
          {
            "name": "iure veritatis veniam",
            "type": "drink:not-alcoholic",
            "price": "307.00"
          },
          {
            "name": "repellendus ut fugit",
            "type": "food:restaurant",
            "price": "169.00"
          }
        ]
      },
      {
        "name": "Lovato S.L.",
        "items": [
          {
            "name": "optio molestias sint",
            "type": "drink:not-alcoholic",
            "price": "667.00"
          },
          {
            "name": "ab tempore veritatis",
            "type": "drink:alcoholic",
            "price": "796.00"
          },
          {
            "name": "asperiores earum voluptatem",
            "type": "drink:not-alcoholic",
            "price": "598.00"
          },
          {
            "name": "eum optio ullam",
            "type": "food:fast",
            "price": "123.00"
          },
          {
            "name": "id distinctio doloribus",
            "type": "drink:not-alcoholic",
            "price": "467.00"
          },
          {
            "name": "voluptatum voluptates exercitationem",
            "type": "drink:alcoholic",
            "price": "239.00"
          },
          {
            "name": "labore veritatis aliquam",
            "type": "food:fast",
            "price": "968.00"
          },
          {
            "name": "repellat voluptates eos",
            "type": "food:restaurant",
            "price": "570.00"
          },
          {
            "name": "quod ab expedita",
            "type": "drink:not-alcoholic",
            "price": "760.00"
          },
          {
            "name": "accusamus tempore aliquam",
            "type": "drink:alcoholic",
            "price": "393.00"
          }
        ]
      },
      {
        "name": "Villegas, Anaya y Palomino Asociados",
        "items": []
      }
    ],
    "map": {
      "general": [8, 4],
      "vip": [7, 4]
    }
  },
  {
    "round": "17",
    "name": "Japanese Grand Prix",
    "circuit": {
      "circuitId": "suzuka",
      "name": "Suzuka Circuit",
      "Location": {
        "lat": 34.8431,
        "long": 136.541,
        "locality": "Suzuka",
        "country": "Japan"
      },
      "location": {
        "lat": 34.8431,
        "long": 136.541,
        "locality": "Suzuka",
        "country": "Japan"
      }
    },
    "date": "2023-09-24",
    "restaurants": [],
    "map": {
      "general": [3, 4],
      "vip": [5, 1]
    }
  },
  {
    "round": "18",
    "name": "Qatar Grand Prix",
    "circuit": {
      "circuitId": "losail",
      "name": "Losail International Circuit",
      "Location": {
        "lat": 25.49,
        "long": 51.4542,
        "locality": "Al Daayen",
        "country": "Qatar"
      },
      "location": {
        "lat": 25.49,
        "long": 51.4542,
        "locality": "Al Daayen",
        "country": "Qatar"
      }
    },
    "date": "2023-10-08",
    "restaurants": [
      {
        "name": "Haro, Gómez y Valle Asociados",
        "items": [
          {
            "name": "inventore nemo molestias",
            "type": "food:restaurant",
            "price": "870.00"
          },
          {
            "name": "necessitatibus placeat sed",
            "type": "drink:not-alcoholic",
            "price": "374.00"
          }
        ]
      },
      {
        "name": "Fernández S.A.",
        "items": [
          {
            "name": "consequuntur sit quis",
            "type": "drink:alcoholic",
            "price": "489.00"
          }
        ]
      },
      {
        "name": "Alva, Lucero y Puente Asociados",
        "items": []
      },
      {
        "name": "Cano y Polanco",
        "items": [
          {
            "name": "porro excepturi quo",
            "type": "food:restaurant",
            "price": "51.00"
          },
          {
            "name": "architecto aperiam impedit",
            "type": "drink:not-alcoholic",
            "price": "549.00"
          }
        ]
      },
      {
        "name": "Garica Baeza S.A.",
        "items": [
          {
            "name": "enim quia itaque",
            "type": "food:restaurant",
            "price": "827.00"
          },
          {
            "name": "iusto quae ea",
            "type": "food:fast",
            "price": "610.00"
          }
        ]
      }
    ],
    "map": {
      "general": [9, 2],
      "vip": [5, 2]
    }
  },
  {
    "round": "19",
    "name": "United States Grand Prix",
    "circuit": {
      "circuitId": "americas",
      "name": "Circuit of the Americas",
      "Location": {
        "lat": 30.1328,
        "long": -97.6411,
        "locality": "Austin",
        "country": "USA"
      },
      "location": {
        "lat": 30.1328,
        "long": -97.6411,
        "locality": "Austin",
        "country": "USA"
      }
    },
    "date": "2023-10-22",
    "restaurants": [
      {
        "name": "Fajardo, Samaniego y Carrillo Asociados",
        "items": [
          {
            "name": "sit illo ad",
            "type": "food:restaurant",
            "price": "500.00"
          },
          {
            "name": "occaecati voluptas maiores",
            "type": "food:restaurant",
            "price": "5.00"
          },
          {
            "name": "magni occaecati esse",
            "type": "food:fast",
            "price": "709.00"
          },
          {
            "name": "illo voluptas at",
            "type": "food:fast",
            "price": "825.00"
          },
          {
            "name": "sapiente tenetur dolorem",
            "type": "drink:alcoholic",
            "price": "890.00"
          },
          {
            "name": "totam repellat laboriosam",
            "type": "drink:not-alcoholic",
            "price": "160.00"
          },
          {
            "name": "ipsam nesciunt esse",
            "type": "food:restaurant",
            "price": "982.00"
          },
          {
            "name": "nemo id quia",
            "type": "food:restaurant",
            "price": "46.00"
          },
          {
            "name": "esse quos numquam",
            "type": "food:fast",
            "price": "101.00"
          },
          {
            "name": "sint quasi placeat",
            "type": "food:fast",
            "price": "390.00"
          }
        ]
      }
    ],
    "map": {
      "general": [3, 3],
      "vip": [6, 7]
    }
  },
  {
    "round": "20",
    "name": "Mexico City Grand Prix",
    "circuit": {
      "circuitId": "rodriguez",
      "name": "Autódromo Hermanos Rodríguez",
      "Location": {
        "lat": 19.4042,
        "long": -99.0907,
        "locality": "Mexico City",
        "country": "Mexico"
      },
      "location": {
        "lat": 19.4042,
        "long": -99.0907,
        "locality": "Mexico City",
        "country": "Mexico"
      }
    },
    "date": "2023-10-29",
    "restaurants": [
      {
        "name": "Cedillo y Vargas",
        "items": [
          {
            "name": "libero voluptates rem",
            "type": "food:restaurant",
            "price": "583.00"
          },
          {
            "name": "tenetur quisquam distinctio",
            "type": "food:restaurant",
            "price": "209.00"
          },
          {
            "name": "a deleniti sed",
            "type": "food:restaurant",
            "price": "86.00"
          },
          {
            "name": "aliquid tempore ullam",
            "type": "drink:not-alcoholic",
            "price": "484.00"
          },
          {
            "name": "labore fugiat repellat",
            "type": "food:fast",
            "price": "7.00"
          },
          {
            "name": "aut minus accusantium",
            "type": "food:restaurant",
            "price": "589.00"
          }
        ]
      },
      {
        "name": "Murillo y Serrano",
        "items": [
          {
            "name": "ipsam repudiandae iure",
            "type": "food:fast",
            "price": "179.00"
          }
        ]
      },
      {
        "name": "Portillo y Adorno",
        "items": [
          {
            "name": "itaque neque distinctio",
            "type": "food:fast",
            "price": "19.00"
          },
          {
            "name": "corporis sunt eaque",
            "type": "food:restaurant",
            "price": "441.00"
          },
          {
            "name": "officia assumenda tempora",
            "type": "food:fast",
            "price": "418.00"
          }
        ]
      },
      {
        "name": "Godínez y Barela",
        "items": [
          {
            "name": "voluptatibus et maiores",
            "type": "food:fast",
            "price": "392.00"
          },
          {
            "name": "repellat enim earum",
            "type": "food:restaurant",
            "price": "92.00"
          },
          {
            "name": "doloremque at tenetur",
            "type": "food:restaurant",
            "price": "959.00"
          }
        ]
      },
      {
        "name": "Acuña, Almanza y Zaragoza Asociados",
        "items": [
          {
            "name": "repellendus odit soluta",
            "type": "drink:not-alcoholic",
            "price": "556.00"
          },
          {
            "name": "sequi omnis doloribus",
            "type": "food:restaurant",
            "price": "119.00"
          },
          {
            "name": "doloribus maiores atque",
            "type": "drink:alcoholic",
            "price": "902.00"
          },
          {
            "name": "minus illo unde",
            "type": "food:restaurant",
            "price": "978.00"
          }
        ]
      },
      {
        "name": "Heredia y Alva",
        "items": [
          {
            "name": "itaque numquam necessitatibus",
            "type": "drink:not-alcoholic",
            "price": "292.00"
          },
          {
            "name": "rem ducimus perferendis",
            "type": "food:restaurant",
            "price": "877.00"
          },
          {
            "name": "libero ex tenetur",
            "type": "drink:not-alcoholic",
            "price": "122.00"
          },
          {
            "name": "amet mollitia unde",
            "type": "food:restaurant",
            "price": "370.00"
          },
          {
            "name": "commodi ipsa vero",
            "type": "food:fast",
            "price": "570.00"
          },
          {
            "name": "mollitia sequi iste",
            "type": "drink:alcoholic",
            "price": "613.00"
          }
        ]
      }
    ],
    "map": {
      "general": [3, 1],
      "vip": [1, 7]
    }
  },
  {
    "round": "21",
    "name": "São Paulo Grand Prix",
    "circuit": {
      "circuitId": "interlagos",
      "name": "Autódromo José Carlos Pace",
      "Location": {
        "lat": -23.7036,
        "long": -46.6997,
        "locality": "São Paulo",
        "country": "Brazil"
      },
      "location": {
        "lat": -23.7036,
        "long": -46.6997,
        "locality": "São Paulo",
        "country": "Brazil"
      }
    },
    "date": "2023-11-05",
    "restaurants": [
      {
        "name": "Verdugo Quintero S.L.",
        "items": [
          {
            "name": "impedit laborum mollitia",
            "type": "food:fast",
            "price": "571.00"
          },
          {
            "name": "enim eveniet magni",
            "type": "food:fast",
            "price": "305.00"
          },
          {
            "name": "accusantium alias quod",
            "type": "food:fast",
            "price": "577.00"
          },
          {
            "name": "voluptatem voluptatum rem",
            "type": "drink:not-alcoholic",
            "price": "421.00"
          },
          {
            "name": "nulla ipsa voluptatum",
            "type": "drink:not-alcoholic",
            "price": "538.00"
          },
          {
            "name": "earum quae beatae",
            "type": "food:fast",
            "price": "386.00"
          },
          {
            "name": "voluptatibus necessitatibus animi",
            "type": "drink:alcoholic",
            "price": "460.00"
          },
          {
            "name": "consequuntur consequuntur doloribus",
            "type": "drink:not-alcoholic",
            "price": "551.00"
          },
          {
            "name": "aut ea nobis",
            "type": "food:fast",
            "price": "831.00"
          },
          {
            "name": "voluptate voluptates voluptatum",
            "type": "drink:alcoholic",
            "price": "758.00"
          },
          {
            "name": "dicta exercitationem voluptatem",
            "type": "drink:alcoholic",
            "price": "399.00"
          },
          {
            "name": "voluptatum harum dicta",
            "type": "food:restaurant",
            "price": "194.00"
          },
          {
            "name": "et veniam facere",
            "type": "food:restaurant",
            "price": "940.00"
          }
        ]
      },
      {
        "name": "Aguirre y Hinojosa",
        "items": [
          {
            "name": "nihil distinctio omnis",
            "type": "drink:alcoholic",
            "price": "329.00"
          },
          {
            "name": "maiores officia magnam",
            "type": "drink:alcoholic",
            "price": "307.00"
          },
          {
            "name": "libero non sapiente",
            "type": "food:restaurant",
            "price": "415.00"
          },
          {
            "name": "ex repellendus voluptates",
            "type": "food:restaurant",
            "price": "349.00"
          },
          {
            "name": "voluptatibus quisquam tempore",
            "type": "food:fast",
            "price": "203.00"
          }
        ]
      },
      {
        "name": "Velasco, Calvillo y Ruíz Asociados",
        "items": [
          {
            "name": "laborum necessitatibus esse",
            "type": "drink:alcoholic",
            "price": "501.00"
          },
          {
            "name": "laboriosam exercitationem quisquam",
            "type": "drink:not-alcoholic",
            "price": "990.00"
          },
          {
            "name": "in odio quae",
            "type": "drink:not-alcoholic",
            "price": "967.00"
          },
          {
            "name": "repellat incidunt autem",
            "type": "food:fast",
            "price": "621.00"
          },
          {
            "name": "quibusdam esse possimus",
            "type": "food:restaurant",
            "price": "357.00"
          },
          {
            "name": "odio itaque fugit",
            "type": "drink:not-alcoholic",
            "price": "265.00"
          },
          {
            "name": "provident cupiditate esse",
            "type": "food:restaurant",
            "price": "677.00"
          },
          {
            "name": "omnis qui libero",
            "type": "food:fast",
            "price": "229.00"
          },
          {
            "name": "vel totam laborum",
            "type": "drink:not-alcoholic",
            "price": "924.00"
          }
        ]
      },
      {
        "name": "Prado S.A.",
        "items": [
          {
            "name": "excepturi commodi dicta",
            "type": "drink:alcoholic",
            "price": "226.00"
          },
          {
            "name": "porro qui tenetur",
            "type": "drink:not-alcoholic",
            "price": "701.00"
          },
          {
            "name": "asperiores aut dolore",
            "type": "drink:alcoholic",
            "price": "746.00"
          },
          {
            "name": "illo corrupti fugiat",
            "type": "food:fast",
            "price": "136.00"
          }
        ]
      },
      {
        "name": "Bermúdez y Velasco",
        "items": [
          {
            "name": "aperiam quod id",
            "type": "drink:alcoholic",
            "price": "608.00"
          },
          {
            "name": "tempore reiciendis voluptates",
            "type": "food:fast",
            "price": "377.00"
          },
          {
            "name": "mollitia molestias nihil",
            "type": "food:restaurant",
            "price": "231.00"
          },
          {
            "name": "dolorem optio omnis",
            "type": "drink:alcoholic",
            "price": "454.00"
          },
          {
            "name": "aliquam odit incidunt",
            "type": "drink:alcoholic",
            "price": "893.00"
          },
          {
            "name": "saepe eveniet natus",
            "type": "drink:not-alcoholic",
            "price": "566.00"
          },
          {
            "name": "non ut omnis",
            "type": "food:restaurant",
            "price": "259.00"
          },
          {
            "name": "voluptatibus consectetur laborum",
            "type": "food:restaurant",
            "price": "715.00"
          },
          {
            "name": "repudiandae eos repellendus",
            "type": "food:fast",
            "price": "228.00"
          },
          {
            "name": "necessitatibus earum excepturi",
            "type": "drink:not-alcoholic",
            "price": "555.00"
          },
          {
            "name": "maxime unde asperiores",
            "type": "food:fast",
            "price": "897.00"
          },
          {
            "name": "fugit ullam sequi",
            "type": "food:fast",
            "price": "918.00"
          },
          {
            "name": "distinctio suscipit deserunt",
            "type": "food:restaurant",
            "price": "3.00"
          },
          {
            "name": "consequatur tempore natus",
            "type": "food:fast",
            "price": "578.00"
          }
        ]
      },
      {
        "name": "Gutiérrez, Sánchez y Guzmán Asociados",
        "items": [
          {
            "name": "itaque hic quae",
            "type": "food:fast",
            "price": "760.00"
          },
          {
            "name": "quidem minus voluptate",
            "type": "food:fast",
            "price": "442.00"
          },
          {
            "name": "cum est iure",
            "type": "food:restaurant",
            "price": "288.00"
          },
          {
            "name": "ipsam voluptatem laudantium",
            "type": "food:restaurant",
            "price": "814.00"
          },
          {
            "name": "tempore quis quis",
            "type": "drink:alcoholic",
            "price": "619.00"
          }
        ]
      },
      {
        "name": "Urías, Tirado y Vela Asociados",
        "items": [
          {
            "name": "cumque recusandae sed",
            "type": "food:fast",
            "price": "16.00"
          },
          {
            "name": "totam itaque nihil",
            "type": "drink:not-alcoholic",
            "price": "185.00"
          },
          {
            "name": "recusandae dolorem eveniet",
            "type": "drink:alcoholic",
            "price": "54.00"
          },
          {
            "name": "consequatur incidunt dignissimos",
            "type": "food:restaurant",
            "price": "46.00"
          },
          {
            "name": "architecto voluptatum nostrum",
            "type": "food:fast",
            "price": "8.00"
          },
          {
            "name": "excepturi totam repellendus",
            "type": "drink:not-alcoholic",
            "price": "708.00"
          },
          {
            "name": "officia adipisci quod",
            "type": "drink:not-alcoholic",
            "price": "504.00"
          },
          {
            "name": "quae repellat facere",
            "type": "food:fast",
            "price": "581.00"
          },
          {
            "name": "et neque amet",
            "type": "food:restaurant",
            "price": "479.00"
          },
          {
            "name": "vitae illum voluptate",
            "type": "food:fast",
            "price": "224.00"
          },
          {
            "name": "repudiandae tenetur atque",
            "type": "food:restaurant",
            "price": "905.00"
          },
          {
            "name": "alias consequatur necessitatibus",
            "type": "drink:alcoholic",
            "price": "387.00"
          },
          {
            "name": "iusto optio quasi",
            "type": "drink:not-alcoholic",
            "price": "646.00"
          },
          {
            "name": "libero ipsam natus",
            "type": "drink:alcoholic",
            "price": "598.00"
          }
        ]
      },
      {
        "name": "Barreto S.L.",
        "items": [
          {
            "name": "libero recusandae deserunt",
            "type": "food:restaurant",
            "price": "259.00"
          },
          {
            "name": "rem aut minima",
            "type": "food:fast",
            "price": "81.00"
          },
          {
            "name": "eius totam natus",
            "type": "drink:not-alcoholic",
            "price": "812.00"
          },
          {
            "name": "dicta impedit nobis",
            "type": "drink:not-alcoholic",
            "price": "704.00"
          },
          {
            "name": "sit excepturi debitis",
            "type": "food:fast",
            "price": "54.00"
          },
          {
            "name": "voluptatibus tempora odit",
            "type": "drink:not-alcoholic",
            "price": "742.00"
          }
        ]
      }
    ],
    "map": {
      "general": [2, 1],
      "vip": [4, 7]
    }
  },
  {
    "round": "22",
    "name": "Las Vegas Grand Prix",
    "circuit": {
      "circuitId": "vegas",
      "name": "Las Vegas Strip Street Circuit",
      "Location": {
        "lat": 36.1147,
        "long": -115.173,
        "locality": "Las Vegas",
        "country": "United States"
      },
      "location": {
        "lat": 36.1147,
        "long": -115.173,
        "locality": "Las Vegas",
        "country": "United States"
      }
    },
    "date": "2023-11-19",
    "restaurants": [
      {
        "name": "Matías, Nájera y Riojas Asociados",
        "items": [
          {
            "name": "molestias aut et",
            "type": "drink:alcoholic",
            "price": "703.00"
          },
          {
            "name": "laborum quaerat in",
            "type": "food:restaurant",
            "price": "254.00"
          },
          {
            "name": "voluptatum excepturi quod",
            "type": "drink:alcoholic",
            "price": "623.00"
          },
          {
            "name": "minima voluptates quisquam",
            "type": "food:restaurant",
            "price": "311.00"
          }
        ]
      },
      {
        "name": "Vigil Casanova S.A.",
        "items": []
      },
      {
        "name": "Guerrero y Galindo",
        "items": [
          {
            "name": "autem voluptates nisi",
            "type": "food:restaurant",
            "price": "24.00"
          },
          {
            "name": "magnam quaerat itaque",
            "type": "food:restaurant",
            "price": "73.00"
          },
          {
            "name": "enim ducimus cumque",
            "type": "food:restaurant",
            "price": "756.00"
          },
          {
            "name": "doloremque voluptate fugit",
            "type": "drink:alcoholic",
            "price": "147.00"
          },
          {
            "name": "distinctio soluta quae",
            "type": "food:fast",
            "price": "265.00"
          },
          {
            "name": "aut quia vel",
            "type": "drink:alcoholic",
            "price": "193.00"
          },
          {
            "name": "recusandae aperiam atque",
            "type": "drink:alcoholic",
            "price": "786.00"
          },
          {
            "name": "corporis sequi consectetur",
            "type": "drink:not-alcoholic",
            "price": "175.00"
          },
          {
            "name": "eum dolorum natus",
            "type": "food:restaurant",
            "price": "229.00"
          },
          {
            "name": "occaecati quibusdam tempore",
            "type": "food:fast",
            "price": "127.00"
          },
          {
            "name": "quod voluptatum excepturi",
            "type": "food:restaurant",
            "price": "990.00"
          },
          {
            "name": "accusamus alias vero",
            "type": "food:restaurant",
            "price": "259.00"
          }
        ]
      },
      {
        "name": "Camarillo, Fernández y Arellano Asociados",
        "items": []
      },
      {
        "name": "Cazares S.A.",
        "items": [
          {
            "name": "vero repellat dolores",
            "type": "drink:alcoholic",
            "price": "503.00"
          },
          {
            "name": "labore consequuntur modi",
            "type": "food:fast",
            "price": "32.00"
          },
          {
            "name": "repudiandae ducimus sapiente",
            "type": "food:restaurant",
            "price": "135.00"
          },
          {
            "name": "ullam modi nulla",
            "type": "food:restaurant",
            "price": "36.00"
          },
          {
            "name": "quisquam quis quae",
            "type": "food:restaurant",
            "price": "24.00"
          },
          {
            "name": "natus ab voluptatum",
            "type": "drink:not-alcoholic",
            "price": "15.00"
          }
        ]
      },
      {
        "name": "Quintero, Bernal y Salcido Asociados",
        "items": [
          {
            "name": "explicabo cupiditate fugiat",
            "type": "drink:alcoholic",
            "price": "452.00"
          },
          {
            "name": "accusamus delectus blanditiis",
            "type": "food:restaurant",
            "price": "675.00"
          },
          {
            "name": "ab voluptate rerum",
            "type": "drink:not-alcoholic",
            "price": "732.00"
          },
          {
            "name": "unde aliquam necessitatibus",
            "type": "food:restaurant",
            "price": "374.00"
          },
          {
            "name": "voluptatem repellendus dignissimos",
            "type": "drink:alcoholic",
            "price": "656.00"
          },
          {
            "name": "eveniet aspernatur fuga",
            "type": "food:restaurant",
            "price": "872.00"
          },
          {
            "name": "blanditiis facere consequuntur",
            "type": "drink:alcoholic",
            "price": "917.00"
          },
          {
            "name": "dicta molestiae unde",
            "type": "drink:not-alcoholic",
            "price": "473.00"
          },
          {
            "name": "aut dolore enim",
            "type": "food:fast",
            "price": "18.00"
          },
          {
            "name": "cupiditate molestiae velit",
            "type": "food:fast",
            "price": "948.00"
          },
          {
            "name": "ex voluptas libero",
            "type": "food:restaurant",
            "price": "912.00"
          }
        ]
      },
      {
        "name": "Aragón S.A.",
        "items": [
          {
            "name": "facere eius quidem",
            "type": "drink:alcoholic",
            "price": "61.00"
          },
          {
            "name": "nemo odio impedit",
            "type": "drink:alcoholic",
            "price": "902.00"
          },
          {
            "name": "ab voluptates aspernatur",
            "type": "drink:alcoholic",
            "price": "399.00"
          },
          {
            "name": "cupiditate animi deleniti",
            "type": "drink:not-alcoholic",
            "price": "364.00"
          },
          {
            "name": "placeat reiciendis placeat",
            "type": "food:fast",
            "price": "488.00"
          },
          {
            "name": "labore odit rem",
            "type": "food:restaurant",
            "price": "367.00"
          },
          {
            "name": "minus odit nobis",
            "type": "drink:not-alcoholic",
            "price": "505.00"
          },
          {
            "name": "consectetur alias inventore",
            "type": "food:fast",
            "price": "661.00"
          },
          {
            "name": "modi suscipit commodi",
            "type": "food:restaurant",
            "price": "380.00"
          },
          {
            "name": "distinctio eligendi possimus",
            "type": "drink:not-alcoholic",
            "price": "298.00"
          },
          {
            "name": "nobis quos amet",
            "type": "food:fast",
            "price": "60.00"
          },
          {
            "name": "voluptatem iure accusamus",
            "type": "food:restaurant",
            "price": "804.00"
          },
          {
            "name": "itaque aperiam quidem",
            "type": "drink:not-alcoholic",
            "price": "607.00"
          },
          {
            "name": "corrupti quae et",
            "type": "food:fast",
            "price": "705.00"
          }
        ]
      },
      {
        "name": "Fajardo y Palomino",
        "items": [
          {
            "name": "id vero porro",
            "type": "drink:not-alcoholic",
            "price": "642.00"
          }
        ]
      }
    ],
    "map": {
      "general": [6, 1],
      "vip": [1, 7]
    }
  },
  {
    "round": "23",
    "name": "Abu Dhabi Grand Prix",
    "circuit": {
      "circuitId": "yas_marina",
      "name": "Yas Marina Circuit",
      "Location": {
        "lat": 24.4672,
        "long": 54.6031,
        "locality": "Abu Dhabi",
        "country": "UAE"
      },
      "location": {
        "lat": 24.4672,
        "long": 54.6031,
        "locality": "Abu Dhabi",
        "country": "UAE"
      }
    },
    "date": "2023-11-26",
    "restaurants": [
      {
        "name": "Saucedo Solorzano e Hijos",
        "items": [
          {
            "name": "quam officia tempora",
            "type": "drink:alcoholic",
            "price": "389.00"
          },
          {
            "name": "adipisci corporis nesciunt",
            "type": "food:restaurant",
            "price": "304.00"
          },
          {
            "name": "omnis eaque consequatur",
            "type": "drink:alcoholic",
            "price": "111.00"
          },
          {
            "name": "nam illo distinctio",
            "type": "food:fast",
            "price": "334.00"
          },
          {
            "name": "eligendi laborum inventore",
            "type": "food:fast",
            "price": "677.00"
          },
          {
            "name": "ipsam voluptates quaerat",
            "type": "drink:not-alcoholic",
            "price": "502.00"
          },
          {
            "name": "itaque laborum repellat",
            "type": "food:restaurant",
            "price": "697.00"
          },
          {
            "name": "minima optio nihil",
            "type": "food:restaurant",
            "price": "971.00"
          },
          {
            "name": "perferendis aut enim",
            "type": "food:restaurant",
            "price": "561.00"
          },
          {
            "name": "asperiores nostrum dolor",
            "type": "food:fast",
            "price": "337.00"
          },
          {
            "name": "fugiat repudiandae ipsum",
            "type": "food:fast",
            "price": "714.00"
          },
          {
            "name": "esse suscipit hic",
            "type": "food:fast",
            "price": "287.00"
          },
          {
            "name": "officia mollitia praesentium",
            "type": "drink:not-alcoholic",
            "price": "923.00"
          }
        ]
      }
    ],
    "map": {
      "general": [8, 3],
      "vip": [2, 9]
    }
  }
]'''
        return json.loads(values)