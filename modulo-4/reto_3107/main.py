from Clase import *

completo_italiano = Italiano()
completo_italiano_2 = Italiano(ingredientes=["chucrut", "americana","tomate","palta","mayo casera"], proteina="Vienesa Sureña", tamaño=25)
completo_al_plato = AlPlato()
ass = Italiano(tipo="As", proteina="carne")

#completo_italiano.colocar_ingredientes(completo_italiano.proteina, completo_italiano.ingredientes).colocar_adereso().servir()
completo_al_plato.colocar_ingredientes(completo_al_plato.proteina, completo_al_plato.ingredientes).colocar_adereso().servir()
completo_italiano_2.colocar_ingredientes(completo_italiano_2.proteina, completo_italiano_2.ingredientes).colocar_adereso().servir()
ass.colocar_ingredientes(ass.proteina, ass.ingredientes).colocar_adereso().servir()