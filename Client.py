class Client:
    def __init__(self, buget, lista_de_produse, pret_dict, name):

        self.buget = buget
        self.lista_de_produse = lista_de_produse
        self.pret_dict = pret_dict
        self.name = name

    def suma_de_achitat(self):
        """
        calculam suma totala a produselor folosind dictionarul produs:pret

        folosind exceptie pentruc ca este posibil ca alimentul sa nu existe in repertoriul magazinelor
        :return:
        """
        suma_totala = 0
        for item in self.lista_de_produse:
            try:

                suma_totala += int(self.pret_dict[item[0:item.find(",")]]) * int(item[item.find(",") + 1::])
            except:
                print(f"i{item[0:item.find(',')]} nu exista in stocul nostru")
        return suma_totala

