# Proiect practic
### Python Fundamentals

---

Folosind conceptele pe care le-am invatat in cursul de Python Fundamentals, vom
scrie o aplicatie care sa implementeze un sistem de gestionare al operatiilor dintr-un magazin
alimentar.

---

Pentru realizarea proiectului vor fi necesare urmatoarele clase:
**Client:**
Atribute
- Buget
- Lista de produse
Metode
- plateste(de_achitat)
**Produs:**
Atribute
- Nume
- Stoc
- Pret
**CosDeCumparaturi:**
Atribute
- Lista de produse
Metode
- elibereaza_bon() -> Elibereaza bonul, sub forma unui fișier text, cu numele
produsului, cantitatea și prețul, iar la final, prețul final.
- adauga_produs(produs, cantitate)

---

Produsele magazinului alimentar se vor citit dintr-un fișier de tip text, alături de preț
și stoc, separate printr-o virgulă, pe câte o linie sub forma:
<nume_produs>,<stoc>,<pret>

![This is an image](https://lh3.googleusercontent.com/KKf4VRT-LdtolBDqTk6YEW0fZnKRgetxNDeaoihBhs-9Pv8mK0x59ITX3MbwHB8oW7qsA5lJtVUNr0KLXq0vzJg-NEKbynUylfSSWl9qy6GZOEV_sJJbZ1fys0nu-Bv8-3FaylM4KipJ7COKNYUXRm5hBXSB3ZvrEusGRVDaUlnQ6MSQSlY5NofbU6AzVib5cdgvM9AgO5kB_u5sXk6m7DjnR9nCvRP1Rm15kvluRNzg7htNnQP5GjuL7OZXfMTU3tGXpyuQ5AClwG6gFiON2-V9eSIHTOBCuTvP55XOyTGM0Uo6xcUeZmQ1ahqta31O-nOQAF9-It0JVFRkAntXdbymtXXTGVmM4Awdg0_lwZGy974pFlTSNgctoFsKoWAHPQqINPOLfPkGMVsLaV_Mx7SgKBZK9Uatq1ELUthgzYrZVw7sV9D_7kp2GnuSADU36CMtiOChOg4LCejBQyOz1TIO6bXtPfnxffQ_Dwzxbu_y-neQUcLB0u0OzeDwvQcUQs8fnCYntlYwxxhenRQJ-WCS0KvmKZQ72O9YIFVi3_GAy3kKPHy6jidmd-BNBsNq2IKAF5LVgF-0AiPGFqBfEtCSH53lZVksjyyGAR4ccKFJklHw8Hd59dUBqWo6SYtCIsrWL69aYUKjOiCKuvGjAZXiFP2HVJ45rzfyOMFeI9o9G7_4wC520saJCoipRd_zMqLErHgbuMxEOm_McRhREYrKJbRpLjcZ5un-CMPlGwJtPWZXKXMRRfGIvfZpQealTc6gXFLi0G-Jfgz-LsGfWMsvHBFU2yV2GcobmGVrsEHueyPIio4gZC7I3bfjV1_D-oAi5pK52_yfWhaUJRYwHKTG-XrgR6tjAxhL392_S2V0rZ6YAne1gqXOVAyjGKjIv8eZJph4RBNhaJ-2wipEXNp-k8TnWcrBAzEfosBohrQqzw=w232-h210-no?authuser=0)

---

Aplicația va primi, ca argumente în linia de comandă, atât numele fișierului text care
conține lista cu produsele pe care magazinul le are pe stoc, cât și numele unui folder care
conține un număr de fișiere reprezentând listele de cumpărături ale clienților.

---

Listele de cumpărături vor conține, pe prima linie, un număr reprezentând bugetul
clientului respective, iar pe liniile următoare (1..N), o listă cu produse și cantitatea dorită:
<nume_produs>,<cantitate>.

![This is an image](https://lh3.googleusercontent.com/Cl0wJf3hazxScSBNoMah8ufs-544VTHlobLEuLgVm-0ITTkxlzb7g0ooWG0kImJXA-7BiTnkbzHMoL7q7BsOrckOMnOZr0N5QDC2s7zG-nizpiFaiN-8TaOS5M_aTYLSn51dN1p64Qs4BUiHQkwNm3EQ77BQxNs9-1ujt4t4vncdbmwz4673Z7-cxIge99uISnaMgs08pulJotVE4ut3Zw2s2LsSK7ENy_5GEqrZ0-LlMxmDPytD04RELE-VQSWHKv-c8fKRPf3NTS5z6pv2LN7k_HVJIjiCA12voBEFSKz2XiwGUs6s-yLjURfGs0jXseHegF-oDB5x3Wgv8g0JZx4ToOYS0rmMOZNevOqUrbOeKhuT_I7VM2YrOCdcdL-Iv08CcDXyHe0xTiOUkNpc2rlXntE78_yS0TeUbiXL6sFvrvhrKyIuBioPAi66i-bSzBdu0PLvMEzQURKizuXrHMECdUgxcRm9SC-EoCnZz6xp-Kr_0yNpU_KGnk8bQ9MdC57o14E5sNTYiYEQxZk92JokqRDK4P3oLYHc34X3rWKJlopavSOSw_KP-aCC2OzsAeR9awbBaGXTPopo9Q15OzRSfbOI5EzK2cUbp5U8u8qNCqd1Y0FU5hB4OxSi0RKtGXGOEuOD3JOdUaIZMDPvQcoTuyWjB0qLXgLDmQP9buS8ot1SPJ_GrwPmVVMMfcaGlE-4lH6shK_0ykl-7lhGy4FvSUAj4_9oW3DV-Xq9qKBzuG-QJefNvETZzGkDAXX8Zq1RIBlovRwcMlYK3Zok8aW5yFuSSkFQVBiJ-gi8xfVAcaF6Tlp0XY5c6d3PvqBaYQLhI9h2a3ZPzIuMWQGjvxjyJnGluo-6zEz8SbHW3XsG2lJdrMU6ZLd5yfzh0KEffuHsf8OzdZstsMi6cnRXJ5Lrk0mXuM74DgCKUr1WT7giNw=w217-h221-no?authuser=0)

---

Fiecare clasă trebuie scrisă într-un fișier separat, iar fișierul ce va fi executat va avea
numele magazin.py. In magazin.py vom stabili, pe baza fisierului text cu produse, stocul
magazinului, dar si vom procesa fiecare lista de cumparaturi, actualizand, in timp real, stocul
magazinului.

---

Lista de produse va fi procesata secvential, iar produsele pe care clientul nu si le
permite vor fi pastrate in stocul magazinului.

---

La final, in functie de produse, cantitatea si bugetul pe care fiecare client il are, se va
scrie intr-un fisier, sub forma de bon fiscal, pe cate un rand nou:
<nume_produs>,<cantitate>,<pret_produs*cantitate> Lei,
iar la final pretul total:
PRET TOTAL,<pret_total>

![This is an image](https://lh3.googleusercontent.com/AvvCFQLrz2JHlBvCdiMGz4XAwG9L4Jo3gg31XEg2d9wHoU3i8RV2HRUHzeyRa_Lhwq9yI6nu-ZijXuGLCMETCy06xK_LhLN1vB1l1DPif4Ns0ifjE442n9-KxNIizEwWEHr9RCYHgfN77JVL4QHzmdm7rbrJVKxsB7hwEq472yrIQXx4Yzv4EK6SENq0tIsJA8rb2Jh6HQEgFs3bF7e8EeyKFeVmU4asvXympw5Q_eI8_yRDglGb0Huvpol2O9lflAyKgiKDLBh6q5Ndba8sPnx5eUTf4RNLUvs5vFzHBY7gV5dsf1fykBt_OYqbIHmftm2WGKfjI_blYurjZ8Jg0_qQoig5t6tyRhriRSb6CCWS73Pb6shb6X2oP_NarNkYaVLPxftBwyDx0s7xI10IWTRBkE0tLE7Xnsb_x7d3rluhwlFmyQfi-zCAuL6kZL9eSHt_OlrM-u2Nda_6JagmHfzP6_ulZkvz4ZgfuXBaMMPOYPNZXzR2P3rUvs1rliX2-7mvTYhERRVvzNhJnBMvDVmxcbd41aiH8oXgq3A7nK7ubM7w4ZuZnnEXuOSuHbo4n6rOt3TW0ce9TGxG0nS3VHJCigUtOYbQIb8rdraKWN2etx0dHW_A9DtG9LOREBs8R9M1EWMAPfEqqITi9c4tw0y2M6mskJgLJYEYOJqt2Nw3SstPKDq8xQkl5wHc-q9MFYHohGXDpKIYnC1Fx6ujVkENkXNrZlmf9y-nMZVNXcH5itj59cz--X4BwGCJJviWPU4-O1j8bLs_lDqZm5tiIssyiaugHQt2zrVqDa4ZoS1ewpgI9L8zhL5PTD2PYcAUKP8yyooh2lZszgBV1y3XMOpRi9VqL-HwrfgjvXWTf-hABQW4ijIdGJnnaV9vN9yuTMDW446lY7YaC9KNKHOY34tFz4-Esm-TxpYbHOEFgllE_Q=w229-h179-no?authuser=0)