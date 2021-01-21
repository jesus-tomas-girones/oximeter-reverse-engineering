# Transforma el fchero de log en varios ficheros csv
import re
regex = re.compile(r".*: (\d*); ([a-f0-9 ]*)")

def analyze():
  array = []
  # Extrae las tramas del fichero de log y las almacena en array
  with open('Log2 FastBLE FRO200.txt') as file:
    for line in file:
      results = regex.match(line)
      time = results[1]
      rem = results[2]
      while len(rem)>0:
        length = int(rem[3:5],16)
        trama = rem[0:length*3-1]
        rem = rem[length*3:]
        array.append((int(time), trama))
  # Crea dos ficheros csv según el tipo de trama
  with open('output_80_2.csv', "w") as out80,  open("output_81_2.csv","w") as out81,  open("output_other_2.csv","w") as out_other:
    for item in array:
      if(item[1][6:8] == "80"):
        out80.write(f"{item[0]},{item[1]},{int(item[1][9:11],16)},{int(item[1][12:14],16)},{int(item[1][15:17],16)}\n")
      elif(item[1][6:8] == "81"):
        out81.write(f"{item[0]},{item[1]},{int(item[1][9:11],16)},{int(item[1][12:14],16)},{int(item[1][15:17],16)},{int(item[1][18:20],16)},{int(item[1][21:23],16)},{int(item[1][24:26],16)},{int(item[1][27:29],16)},{int(item[1][30:32],16)}\n")
      else:
        out_other.write(f"{item[0]},{item[1]}\n")

if __name__ == "__main__":
  analyze()
