#  Conectar ao Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# String para variaveis de 3D

bloco = input("Numero do bloco desejado:")

x = input("localização desejada para: x ")
y = input("localização desejada para: y ")
z = input("localização desejada para: z ")

mc.setBlock(x, y, z, bloco)

print("Fim de script obs: cria 1 bloco por vez ! ")