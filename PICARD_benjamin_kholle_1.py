#!/usr/bin/python3.6
#Title : PICARD_benjamin_khôlle_1.py
#Date : 24/11/2108
#Description : Programme/Utilitaire capable d'opérations simple sur une liste d'entier dans un fichier au format csv
#Author : Benjamin Picard

import argparse
import csv
from statistics import mean

##option##
parser = argparse.ArgumentParser()
parser.add_argument("-l", action="store_true", help="Display de la liste")
parser.add_argument("-a", nargs="+", help="Permet d'jouter des valeurs à la liste")
parser.add_argument("-c",  action="store_true", help="Fais un delete all")
parser.add_argument("-s", action="store_true", help="")
parser.add_argument("--max", action="store_true", help="Display Max")
parser.add_argument("--min", action="store_true", help="Display Min")
parser.add_argument("--moy", action="store_true", help="Display Moy")
parser.add_argument("--sum", action="store_true", help="Display Sum")
parser.add_argument("-t", action="store_true", help="Display par ordre croissant")
parser.add_argument("--desc", action="store_true", help="Display par ordre décroissant.")
args = parser.parse_args()

example = []

def displayExampleCsv():
    with open("./example.csv", "r") as file_csv:
        csv_reader = csv.reader(file_csv)
        for ligne in  csv_reader:
            for i in range(0, len(ligne)):
               example.append(ligne[i])
	
def writeCsv(value):
    with open("./example.csv", "w") as file_csv:
        csv_write = csv.writer(file_csv)
        csv_write.writerow(value)

def contentList():
    displayExampleCsv()
    for row in example:
        print(row)

def ajoutElement(value):
    example.append(value)

def deleteAll():
    displayExampleCsv()
    while len(example) > 0:
        del example[0]
    writeCsv(example)

def Max():
    displayExampleCsv()
    example_max = [int(n) for n in example]
    value_max = max(example_max)
    print(value_max)

def Min():
    displayExampleCsv()
    example_min = [int(n) for n in example]
    value_min = min(example_min)
    print(value_min)  

def getAverageValue():
    displayExampleCsv()
    example_moy = [int(n) for n in example]
    value_average = mean(example_moy)
    print(value_average)
	
def getSumValue():
    displayExampleCsv()
    example_sum = [int(n) for n in example]
    value_sum = sum(example_sum)
    print(value_sum)

def exampleCroissant():
    displayExampleCsv()
    example_croissant = [int(n) for n in example]
    example_croissant.sort()
    writeCsv(example_croissant)
	
def exampleDecroissant():
    displayExampleCsv()
    example_decroissant = [int(n) for n in example]
    example_decroissant.sort(reverse = True)
    writeCsv(example_decroissant)

if args.l:
    contentList()

elif args.a:
    displayExampleCsv()
    for num in args.a:
        ajoutElement(num)
    writeCsv(example)

elif args.c:
    deleteAll()
	
elif args.s:
    if args.max:
        Max()
    elif args.min:
        Min()
    elif args.moy:
        getAverageValue()
    elif args.sum:
        getSumValue()
	
elif args.t:
    if args.desc:
        exampleDecroissant()
    else:
        exampleCroissant()

