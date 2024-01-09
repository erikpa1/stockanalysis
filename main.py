import os
import yfinance as yf

from _plotings import run_ploting

# define the ticker symbol

import vfs

periods = [
    ['2019', '2019-1-1', '2020-1-1'],
    ['2020', '2020-1-1', '2021-1-1'],
    ['2021', '2021-1-1', '2022-1-1'],
    ['2022', '2022-1-1', '2023-1-1'],
    ['2023', '2023-1-1', '2024-1-1'],
    ['2024', '2024-1-1', '2025-1-1']
]

companies = [
    ["TWO", "TwoHarbors"],
    ["MMM", "3M"],
    ["O", "RealtyIncome"],
    ["NFG", "NationalFuelGas"],
    ["PFE", "Pfizer"],
    ["DIS", "WaltDisney"],
    ["LUV", "SouthewstAirlines"],
    ["IMO", "ImperialOil"],
    ["SSL", "Sasol"],
    ["JMIA", "Jumia"],
    ["SBSW", "SibanyeStillwater"],
    ["GM", "GeneralMotors"],
    ["TGT", "Target"],
    ["TV", "GrupoTelevisa"],
    ["BBY", "BestBuy"],
    ["TSCO", "TractorSupplyCompany"],
    ["POR", "PortlandGeneral"],
    ["CSCO", "Cisco"],
    ["LOGI", "Logitech"],
    ["MDT", "Medtronic"],
    ["T", "AT&T"],
    ["IBM", "IBM"],
    ["AAT", "AmericanAssets"],
    ["APAM", "ArtisanPartners"],
    ["PBF", "PBFEnergy"],
    ["BAM", "BrookfieldAssetManagement"],
    ["KHC", "KraftHeinz"],
]

os.makedirs(f"{vfs.RESULTS_FOLDER}", exist_ok=True)
os.makedirs(f"{vfs.COMPANIES_FOLDER}", exist_ok=True)

for company in companies:

    for period in periods:
        os.makedirs(f"{vfs.COMPANIES_FOLDER}{company[1]}/", exist_ok=True)

        tickerData = yf.Ticker(company[0])
        tickerDf = tickerData.history(period='1d', start=period[1], end=period[2])
        lowFieldData = tickerDf['Low']

        path = f'{vfs.COMPANIES_FOLDER}{company[1]}/{period[0]}.csv'

        lowFieldData.to_csv(path, index=False)

    run_ploting(company[1])
