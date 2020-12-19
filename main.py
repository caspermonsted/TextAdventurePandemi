from pathlib import Path
from os import system, name
import sys
import time #Imports a module to add a pause

def main():
    # laver dict med kapitler i folder vha folder_dir
    kapitel_list = folder_dir(kapitler)
    kapitel_dict = {}

    for path in kapitel_list:
        fil_navn = path.split('\\')[1]
        kapitel_navn = fil_navn.split('.')[0]
        kapitel_dict[kapitel_navn] = path

    routes_dict = {
        'intro':                        ['statsminister_start','forsker_start', 'almindelig_start'],
        'forsker_start':                ['forsker_ven', 'forsker_overveje', 'forsker_genoverveje'],
        'forsker_ven':                  ['mangler', 'forsker_hospital', 'forsker_bange_for_smitte'],
        'forsker_overveje':             ['forsker_aere', 'b', 'forsker_aere'],
        'forsker_genoverveje':          ['forsker_bange_for_smitte', 'b', 'forsker_aere'],
        'forsker_aere':                 [],
        'forsker_bange_for_smitte':     [],
        'forsker_hospital':             ['forsker_interview','forsker_slut_hospital','forsker_slut_hospital'],
        'forsker_slut_hospital':        [],
        'forsker_interview':            [],
        'statsminister_start':          ['statsminister_1000indlagte', 'statsminister_fest', 'statsminister_fest'],
        'statsminister_1000indlagte':   ['statsminister_kæledyr', 'statsminister_alledøde', 'statsminister_stemtud'],
        'statsminister_fest':           ['statsminister_alledøde', 'statsminister_kæledyr', 'statsminister_stemtud'],
        'statsminister_stemtud':        [],
        'statsminister_alledøde':       [],
        'statsminister_kæledyr':        ['statsminister_afliver_kæledyr', 'b', 'statsminister_alle døde'],
        'statsminister_afliver_kæledyr':[],
        'statsminister_vaccine ':       ['statsminister_forkert_vaccine','statsminister_vaccine_angst', 'statsminister_vaccine_angst'],
        'statsminister_forkert_vaccine': [],
        'statsminister_vaccine_angst':  ['statsminister_vundet', 'statsminister_ingen_vaccineret', 'statsminister_ingen_vaccineret'],
        'statsminister_vundet':         [],
        'statsminister_ingen_vaccineret':[]
    }

    svar_a = ["A", "a"]
    svar_b = ["B", "b"]
    svar_c = ["C", "c"]
    svar = [svar_a, svar_b, svar_c]

    kapitel = 'intro'
    cont = 1
    while cont == 1:
        print_blanks(10)
        laes_kapitel(kapitel, kapitel_dict)
        print_blanks(3)
        options = len(routes_dict[kapitel])
        if options > 1:
            valg_txt = input("Skriv dit svar her: ")
            print_blanks(10)
            valg = valg_konvert(valg_txt, svar)
            next = routes_dict[kapitel]
            kapitel = next[valg]
            options = len(routes_dict[kapitel])
        else:
            cont = 0
            print("SLUT")

def print_blanks(rows):
    for row in range(rows):
        print("")

def valg_konvert(valg_txt, svar):
    if valg_txt in svar[0]:
        valg = 0
    elif valg_txt in svar[1]:
        valg = 1
    elif valg_txt in svar[2]:
        valg =2
    else:
        print(muligheder)
        laes_kapitel('intro', kapitel_dict)
    return valg

def laes_kapitel(kapitel, kapitel_dict):
    """printer kapitel"""
    indhold = open(kapitel_dict[kapitel], "r").read()

    print(indhold)

def folder_dir(folder):
    """ Return list of filenames in folder including path. """
    entries_list = []
    pathlist = Path(folder).rglob('**/*')
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        # print(path_in_str)
        entries_list.append(path_in_str)
    return entries_list


if __name__ == '__main__':
    main()
