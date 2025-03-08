import requests

type_of_stuff = input("Would you like to encode or decode data? (Reply with encode/decode) ").strip().lower()

if type_of_stuff == "encode":
   text_to_encode = input("What would you like to encode? ")
   new_str = ""

   for char in text_to_encode:
       if char != " ":
          new_str  += char
       else:
          new_str += "%20"
   encode_data = requests.get(f"https://networkcalc.com/api/encoder/{new_str}?encoding=base64").json()
   print("Encoded: "+ encode_data["encoded"])
else:
   text_to_decode = input("What would you like to decode? ")
   encode_data = requests.get(f"https://networkcalc.com/api/encoder/{text_to_decode}?encoding=base64&decode=true").json()
   print("Decoded: "+ encode_data["decoded"])
