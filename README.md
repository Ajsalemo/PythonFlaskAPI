# PythonFlaskAPI

### A small REST API that exposes data about BMW M performance models

https://pythonflaskapi.azurewebsites.net/

<br>

![Imgur](https://i.imgur.com/gDUvK1b.png)

## Routes
### /api/v1/cars/all - 
#### Retrieve all cars 

#### JSON Format - Array of Objects:

     {
        "all_cars": [
              {
                  "Body": "Coupe",
                  "Displacement": "3.5-litre",
                  "Engine_Type": "l6",
                  "Model": "M1",
                  "Power": "273 hp",
                  "Production": "1978-1981",
                  "Production_Number": "453",
                  "Type": "E26",
                  "id": 1
              },
              {
                ....
              },
              {
                ....
              }
           ]
        }

<br>

      
### /api/v1/cars/all_models - 
#### Retrieve all models prefixed with the year, such as "2006-2010 M3"

#### JSON Format - Array:

       {
          "all_models": [
              "1978-1981 M1",
              "1980-1984 M535i",
              "1984-1989 M635CSi",
              ....
              ...
              ..
            ]
        }
        
<br>

### /api/v1/cars/model_types - 
#### All generation types - ex. "E46" or "E60"

#### JSON Format - Array:

       {
          "all_models": [
            "E26",
            "E12",
            "E24",
            ....
            ...
            ..
          ]
        }
        
<br>
        
### /api/v1/cars/models/<model> - 
#### Specify a model information to retrieve, where <model> is the string based parameter - ex. /api/v1/cars/models/m3
  
#### JSON Format - Array of Objects - if multiple matching values are returned, they will be in the form of an Array of Objects:
  
       {
           "model": [
                {
                  "Body": "Coupe, Convertible",
                  "Engine_Type": "l4",
                  "Model": "M3",
                  "Power": "191 hp to 234 hp",
                  "Production_Number": "17,184 (Coupe); 786 (Convertible)",
                  "Type": "E30",
                  "Year": "1986-1991",
                  "id": 6
                },
                {
                    "Body": "Sedan with 4 doors; Coupe; Convertible",
                    "Engine_Type": "l6",
                    "Model": "M3",
                    "Power": "240 hp to 316 hp",
                    "Production_Number": "71,242",
                    "Type": "E36",
                    "Year": "1992-1999",
                    "id": 9
                },
                {
                  ...
                }
              ]
          }
  
### /api/v1/cars/types/<gen_type> - 
#### Specify a model type to retrieve, where <gen_type> is the generation - ex. /api/v1/cars/types/e60 

#### JSON Format - Array of Objects - if multiple matching values are returned, they will be in the form of an Array of Objects:

       {
          "type": [
            {
              "Body": "Coupe; Convertible",
              "Engine_Type": "l6; V8",
              "Model": "M3",
              "Power": "337 hp to 374 hp",
              "Production_Number": "85,744",
              "Type": "E46",
              "Year": "2000-2006",
              "id": 12
            },
            {
              ...
            }
          ]
       }
       
<br>     
       
       
### /api/v1/cars/<int:id> - 
#### Specify a model type by ID - where <int:id> is an integer based parameter - ex. /api/v1/cars/2
#### JSON Format - Object:

      {
          "response": [
            {
                "Body": "Sedan with 4 doors",
                "Engine_Type": "l6",
                "Model": "M535i",
                "Power": "215 hp",
                "Production_Number": "1,410",
                "Type": "E12",
                "Year": "1980-1984",
                "id": 2
            }
          ]
        }
      
<br> 

