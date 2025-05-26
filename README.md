# 🧭 LocationFinder

> A Python-based tool to find geographic information from IP addresses, phone numbers, and website URLs. Perfect for OSINT enthusiasts, cyber curious minds, or anyone who just wants to flex on data.

## 🚀 Features

- 🌍 Find geographic location from an **IP address**
- 📱 Extract region, timezone, and carrier from a **phone number**
- 🌐 Convert a **URL to IP**, then geolocate it
- 📟 CLI-based interface for smooth command-line action
- 🔄 Infinite loop until the user exits (because quitting is for the weak... or the done)

## 🧪 Requirements

Before running, install the dependencies:

pip install phonenumbers ip2geotools

How it works:

# IP Lookup
findlocationbyip("8.8.8.8")

# Phone Number Lookup
findlocationbynumber("+14155552671")

# URL Lookup
socket.gethostbyname("example.com") ➜ IP ➜ Location

Usage:
Run the program using: python LocationFinder.py

Menu:

--------WELCOME TO LOCATIONFINDER--------
1. Find Location By IP
2. Find Location By Phone Number
3. Get Location From URL
4. Exit

Example Output:
IP Address: 8.8.8.8
Location: Mountain View, California, US
Coordinates: Longitude: -122.0838, Latitude: 37.386

Carrier: Verizon
Region: California
Timezone: ('America/Los_Angeles',)

Disclaimers:
Location accuracy depends on the public databases used.

This tool is for educational and informational purposes only. Don’t be sketchy.

If something breaks, check your internet connection or input validity.

When inputting a phone number, always include the country code. For example, +260....... 
Doing so helps the program to identify the country from the number came by performing a look up in a public database

Things to add/modify in the future:
- Error handling
- GUI with animations and user-friendly navigation
- Export any results to a file for later use
- Batch processing to handle multiple inputs


Author: Kevin Hamusute(masterkillah2009) Have any queries? Email me using hamusutekevin@gmail.com 

HAPPY HACKING! STAY CURIOUS


