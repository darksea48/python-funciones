# main
from Persona import Persona as p
import Tamagotchi as t
import TipoTamagotchi as tt

douglas = p("Douglas", "Suárez")
douglas.obtener_tamagotchi()
douglas.tamagotchi[0].presentarse()
douglas.jugar_con_tamagotchi(douglas.tamagotchi[0]).darle_comida(douglas.tamagotchi[0]).consultar_datos(douglas.tamagotchi[0])
douglas.curarlo(douglas.tamagotchi[0])