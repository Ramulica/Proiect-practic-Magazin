import os

from Client import Client
from Produs import Produs
from CosDeCumparaturi import CosDeCumparaturi


def citeste_fisierul(file):
    """
    citim fisierul txt si returnam o lista cu liniile di acesta
    :param file:
    :return:
    """

    with open(file, "r") as fr:
        content = fr.readlines()
    return [item.strip() for item in content]


def adauga_produsele_citite_in_stocul_magazinului(content):
    """
    cream o lista cu toate produsele din magazin, punandule atributele citite din fierul text

    transformam stringul(linia din text) intr-o lista separand (split) item-ele la fiecare virgula.
    Folosind clasa Produs, creem o lista cu produse

    :param content:
    :return:
    """

    lista_stoc_magazin = []
    for item in content:
        atribute = item.split(",")
        lista_stoc_magazin.append(Produs(atribute[0], atribute[1], atribute[2]))
    return lista_stoc_magazin


def dictionar_produs_pret(produse):
    """
    facem 2 dictionare :
    dictionar cu produs:stoc
    dictionar cu produs:pret

    pentru fiecare produs din lista il adaugam in cele 2 dictionare (key) cu valorile pret(1) si stoc(2) (value)

    :return:
    """

    dict_p = {}  # dictionar cu produs:pret
    dict_s = {}    # dictionar cu produs:stoc
    for item in produse:
        dict_p[item.nume] = int(item.pret)
        dict_s[item.nume] = int(item.stoc)

    return dict_p, dict_s


def toate_listele_de_cumparaturi_buget(clienti_folder):
    """

    cream o lista cu toti clientii, punandule atributele citite din fierele cu listele de cumpatraturi

    luam datele din dictionarul produs:pret si citim datele din fiserele txt cu listele de cumparaturi (acestea sunt
    atributele clasei Client
    Folosind clasa Client, creem o lista cu toti clientii

    :param clienti_folder:
    :return:
    """

    lista_de_liste_cumparaturi = []
    dict_produs_pret = dictionar_produs_pret(adauga_produsele_citite_in_stocul_magazinului(citeste_fisierul('produse.txt')))[0]
    main_path = os.getcwd()
    os.chdir(clienti_folder)
    for item in os.listdir():
        content = citeste_fisierul(item)

        lista_de_liste_cumparaturi.append(Client(content[0], content[1::], dict_produs_pret,
                                                 item[item.rfind('_') + 1:item.rfind('.')]))
    os.chdir(main_path)
    return lista_de_liste_cumparaturi

print(f'acestea sun fiserele si folderele disponibile:\n{os.listdir()}\n')

fiser_produse = input('Care este fiserul in care se afla produsele: ')
folder_clenti = input('\nCare este folderul in care se afla listele clientiilor: ')

produse_din_magazin = adauga_produsele_citite_in_stocul_magazinului(citeste_fisierul(fiser_produse))
listele_de_clienti = toate_listele_de_cumparaturi_buget(folder_clenti)
produse_pret, produse_stoc = dictionar_produs_pret(adauga_produsele_citite_in_stocul_magazinului(citeste_fisierul(fiser_produse)))
lista_cos_de_cumparaturi = [CosDeCumparaturi(item.lista_de_produse, produse_pret, produse_stoc, item.buget, item.name)
                            for item in listele_de_clienti]
print('\n\033[38;5;226mAcestia sunt clientii magazinelui si ce au cumparat\033[0m\n')
for item in lista_cos_de_cumparaturi:
    CosDeCumparaturi.elibereaza_bon(item)
    CosDeCumparaturi.scade_pedusele_cumparate_din_stoc(item, fiser_produse)





