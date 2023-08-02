import re
import pdb  #pdb.set_trace()
import time

def ask_user():
  print("Have you run the command 'shasum -a 256 /path/to/your/iso/file'\nto return a 256-bit confirmation hash?")
  time.sleep(1)
  return input("Y/n? ")

def match(sha_hash, iso_img):
  file = open('./SHA256SUMS.txt')

  for l in file:
    strings = re.split(' ', l)
    hash = strings[0]
    iso = strings[2].replace('\n','')

    if re.match(iso, iso_img):
      print("Matching ISO Found! Checking SHA...")
      if re.match(hash, sha_hash):
        print("SHA256 Match: Your ISO image file is valid.")
        print(l)
        print("SHA256SUM check complete.")
        break
      else:
        print("SHA256 key assigned to ISO does not match the input value.\nHere are some options:\n\r- Check that your SHA key was input correctly\n\r- Ensure your ISO was obtained from a trusted source\n\r- Contact the distribution creators for further assistance")
    else:
      print("ISO filename not found\nHere are some options:\n\r- Check that your ISO Filename was input correctly/as downloaded from the official site\n\r- Ensure your ISO was obtained from a trusted source\n\r- Contact the distribution creators for further assistance")

