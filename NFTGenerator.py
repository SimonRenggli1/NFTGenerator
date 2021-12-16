# Import all things to import
import random
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection

# Set how many NFTs you want to create
amount = int(input("How Many NFTs you wanna make? "))
# All the Colors the NFT can vary
color= ["yellow", "black", "blue", "green", "red", "cyan", "magenta", "white"]
loop = int(1)
# Enter the loop
while loop <= amount:
  random_number = random.randint(1, 999999)
# Define the f1 and f2
  def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
  def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
  g = GenerativeImage(f1,f2)
# Generate the Image
  g.generate()
# Define a Random color defined above to the image
  g.plot(color=random.choice(color), bgcolor="black", projection=Projection.POLAR)
  g.seed
# Send the Image to your nft.storage inventory
  g.nft_storage(api_key = 'Your nft.storage api')
  {'status': True, 'message': 'Everything seems good'}
# Print a Message to see how many NFT it generated
  print("Finished the " + str(loop) + " NFT")
  loop = loop + 1