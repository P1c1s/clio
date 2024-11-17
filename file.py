def write():
  
  a = "Mario"
  b = "Pinlo" 

  with open('DB_data.dat', 'a') as f:
    for i in range(2):
      f.write('{} {}\n'.format(a,b,))

def read():
  with open('DB_data.dat', 'r') as f:
      line = f.readline()

      while line:
          data.append(line.split(' '))
          line = f.readline()
  print(data)


