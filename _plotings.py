import os

import matplotlib.pyplot as plt
import numpy as np

import math
import vfs
import pandas as pd

COLORS = [
    ""
]

os.makedirs(f"{vfs.RESULTS_FOLDER}charts/", exist_ok=True)

colors = [
    "darkred",
    "lightgreen",
    "b",
    "g",
    "r",
    "black"
]


def run_ploting(company: str):
    # _run_example(company,company_name)
    _run_ploting(company)


def _run_example(company: str):
    X = np.arange(0, math.pi * 2, 0.05)
    y = np.sin(X)
    z = np.cos(X)

    plt.plot(X, y, color='r', label='sin')
    plt.plot(X, z, color='g', label='cos')

    plt.xlabel("Angle")
    plt.ylabel("Magnitude")
    plt.title("Sine and Cosine functions")

    plt.legend()
    plt.savefig(f"{vfs.RESULTS_FOLDER}charts/{company}.png", format="png")
    plt.close()


def _run_ploting(company: str):
    company_folder = f"{vfs.COMPANIES_FOLDER}{company}/"

    data = []

    for file in os.listdir(company_folder):
        df = pd.read_csv(f"{company_folder}/{file}")
        column_data = df["Low"]
        x = range(0, len(column_data))

        data.append([x, column_data, file])

    index = 0
    for i in data:
        plt.plot(i[0], i[1], color=colors[index], label=i[2])
        index += 1

    plt.title(f'{company} 2021 - 2022 - 2023')
    plt.xlabel('Days')
    plt.ylabel('Value')
    plt.legend()
    plt.savefig(f"{vfs.RESULTS_FOLDER}charts/{company}.png", format="png")
    plt.close()
