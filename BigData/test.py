from flask import Flask, render_template
import pandas as pd
import csv

with open('tableA.csv', 'r', encoding="utf8") as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        print(line)
