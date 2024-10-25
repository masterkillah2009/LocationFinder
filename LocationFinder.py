import phonenumbers
import socket
from ip2geotools.databases.noncommercial import DbIpCity 
from phonenumbers import geocoder 
from phonenumbers import carrier  
from phonenumbers import timezone


def findlocationbyip(ip_address):
                  location = DbIpCity.get(ip_address, api_key="free")
                  print(f"IP Address: {ip_address}")
                  print(f"Location: {location.city}, {location.region}, {location.country}")
                  print(f"Coordinates: Longitude: {location.longitude}, Latitude: {location.latitude}")
        
def findlocationbynumber(number):
                      phone = phonenumbers.parse(number)

                      carrier_name = carrier.name_for_number(phone, "en")
                      if carrier_name:
                                print("Carrier:", carrier_name)
                      else:
                                print("Carrier: Not available")

                      region = geocoder.description_for_number(phone, "en")
                      if region:
                                print("Region:", region)
                      else:
                                print("Region: Not available")
                        
                      time_zone = timezone.time_zones_for_number(phone)
                      if time_zone:
                                print(f"Timezone: {time_zone}")
                        
                      else:
                         print("Timezone: Not Available")
            

                    

                

                    

while True:
            
            print("--------WELCOME TO LOCATIONFINDER--------")
            print("1. Find Location By IP")
            print("2. Find Location By Phone Number")
            print("3. Get Location Fron URL")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                  ip_address = input("Enter your IP Address: ")
                  print(findlocationbyip(ip_address))
                 
            
            elif choice == "2":
                   number = input("Enter your phone number: ")
                   print(findlocationbynumber(number))

            
            elif choice == "3":
                  try:
                    url = input("Enter a url: ")
                    ip_address = socket.gethostbyname(url)
                    print(findlocationbyip(ip_address))
                  except:
                        print("Try a different URL or connect to the internet.")
            
            elif choice == "4":
                 exit()
      
      
            else:
             continue



          