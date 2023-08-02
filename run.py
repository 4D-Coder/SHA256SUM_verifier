import time
import shasum_matcher
import pdb  #pdb.set_trace()

try:
  print("Before you proceed, please confirm:")
  time.sleep(1)

  while True:
    response = shasum_matcher.ask_user()

    if response.lower() == 'y':
      sha_hash = input("Please input hash key: ")
      iso_img = input("Please input iso filename: ")
      print("Searching local directory for 'SHA256SUMS.txt' file...")

      try:
        shasum_matcher.match(sha_hash, iso_img)
      except FileNotFoundError:
        print("File does not exist or has the incorrect name.\nCheck directory and try again.")

      break
    elif response.lower() == 'n':
      print("\nPlease run the command:\n'shasum -a 256 /path/to/your/iso/file'\nand then try again.")
      break
    elif response.lower() != 'n' or response.lower() != 'y':
      print("\nPlease enter a valid input.\n")
      time.sleep(1)
except KeyboardInterrupt:
  quit = input("Would you like to exit the program?")
