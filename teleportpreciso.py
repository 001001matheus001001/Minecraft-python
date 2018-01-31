# Conectar ao Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# String para variaveis de 3D

x = input("localização desejada para x ")
y = input("localização desejada para y ")
z = input("localização desejada para z ")

# Mudar a posição do jogador

mc.player.setPos(x, y, z)

print("Fim de locomoção ->", x, y ,z)