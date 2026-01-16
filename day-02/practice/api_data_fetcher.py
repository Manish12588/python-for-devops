#We have Day02 Assignment inside this file

import requests  #Install the request library using pip install requests command
import json

api_url = "https://dog.ceo/api/breeds/list/all"

def get_details_of_dog(dog_breeds):
    response = requests.get(url=api_url)    #Calling the API with GET request method

    for key, value in response.json().items():
        if key == "message":
            if value.get(dog_breeds):                           #Here we are check the provided breed in available value DISC.
                breed_information = value.get(dog_breeds)       #Storing the breed information in variable and returning it at the end  
            else:
                print("Please provide the value from available breed ('african','australian','bakharwal','mastiff','mountain').")
    return breed_information
                                        

dog_breeds = input("Please provide the dog breeds eg. ('african','australian','bakharwal','mastiff','mountain'): ")
breed_information = get_details_of_dog(dog_breeds)
print(type(breed_information))
print(breed_information)   #Print the information of breed.


#Writing the captured breed information in JSON file
#with open("output.json","w") as file:
#    json.dump(breed_information,file,indent=4)

#Another way to write a JSON file like open, write and close
file = open("output.json","w")
json.dump(breed_information,file,indent=4)
file.close()   