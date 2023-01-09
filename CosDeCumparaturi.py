import os

class CosDeCumparaturi:
    def __init__(self, lista_de_produse, pret_dict, stoc_dict, buget, nume):

        self.lista_de_produse = lista_de_produse
        self.pret_dict = pret_dict
        self.stoc_dict = stoc_dict
        self.suma_produse, self.produsele_in_buget = CosDeCumparaturi.produse_adaugate(self, int(buget))

        self.nume = nume

    def produse_adaugate(self, buget):
        """
        calculam suma tuturor produselor care se afla in stoc si intra in bugetul persoanei.
        Cream un dictionar cu produul:cantitatea pe care persoana si-a permis-o
        :param buget:
        :return:
        """
        produse_cumparate = {}
        suma_produselor = 0
        buget_depasit = False
        for item in self.lista_de_produse:

            if not buget_depasit:

                for _ in range(int(item[item.find(',') + 1::])):

                    if suma_produselor + int(self.pret_dict[item[0:item.find(',')]]) < buget:

                        if self.stoc_dict[item[0:item.find(',')]] != 0:

                            suma_produselor += int(self.pret_dict[item[0:item.find(',')]])
                            try:
                                produse_cumparate[item[0:item.find(',')]] += 1
                            except KeyError:
                                produse_cumparate[item[0:item.find(',')]] = 1
                            self.stoc_dict[item[0:item.find(',')]] -= 1

                        else:
                            break

                    else:
                        buget_depasit = True
                        break

        return suma_produselor, produse_cumparate

    def scade_pedusele_cumparate_din_stoc(self, file):
        """
        luam stocul de produse, dupa ce o persoana a cumparat ceva, si suprasscriem informatile existente cu
        cantitatea de produse cu informatia noua
        :param file:
        :return:
        """
        with open(file, 'w') as fw:
            for k, v in self.stoc_dict.items():
                fw.write(f"{k},{self.stoc_dict[k]},{self.pret_dict[k]}\n")



    def elibereaza_bon(self):
        """
        scriem intrun fiser text care se afla in folderul BonuriFiscale (daca nu exusita un fiser se creaza automat)
        ce, cat si la ce pret a cumparat persoana respectiva alimentele

        printam informatile pentru a vedea ce am scris in fisiere
        :return:
        """
        main_path = os.getcwd()
        os.chdir('BonurileFiscale')

        bon = ['BON FISCAL'] + \
              [f"{k},{v},{v * self.pret_dict[k]} lei" for k, v in self.produsele_in_buget.items()] + \
              [f"PRET TOTAL,{self.suma_produse} lei"]
        print(f'\nBonul persoanei cu numele {self.nume}')
        with open(f'bon_fiscal_{self.nume}', 'w') as fw:
            for item in bon:

                fw.write(f"{item}\n")
                print(item)
        print("")

        os.chdir(main_path)






