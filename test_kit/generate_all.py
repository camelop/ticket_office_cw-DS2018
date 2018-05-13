import os
for i in range(1,100):
  if os.path.exists(str(i)+'.in'):
    command =  "cat {}.in >> all.in && echo \"\\n\" >> all.in ".format(str(i))
    print(command)
    os.system(command)
  else:
    break

