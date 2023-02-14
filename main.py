print("What is your file name")
filename = input()


class filename:
    def __init__(self):
      self.filedetails = {'name': '','streetname':'','phonenumber':''}

    def setname(self, name):
      self.filedetails['name'] = name

    def setstreetname(self, streetname):
      self.filedetails['streetname'] = str(streetname)

    def setphonenumber(self, phonenumber):
      self.filedetails['phonenumber'] = str(phonenumber)
  
    def displayfile(self):
      print("")
      print(f"{self.filedetails['name']}, {self.filedetails['streetname']}, {self.filedetails['phonenumber']} ")
      print("")



def main():
    
  input_name = input("Please enter your name: ")
  input_streetname = input("Please enter your street name: ")
  input_phonenumber = input("Please enter your phone number: ")
  new_file = filename()
  new_file.setname(input_name)
  new_file.setstreetname(input_streetname)
  new_file.setphonenumber(input_phonenumber)
  new_file.displayfile()

main()

main()