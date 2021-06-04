#!/usr/bin/env python

import csv
import glob


def getDistrictDVMap(fname):
    """
    Returns a list of tuples with the following DV data per district.
    e.g
    (state_id, district_id, name, dv_val)
    """
    with open(fname) as stateCSV:
        results = []
        reader = csv.DictReader(stateCSV)
        state_id = 0
        district_id = 0
        name = ""
        print("Trying file:" + fname)
        try:
            for row in reader:
                if row.get("3") and row["3"].strip() != "":
                    name = row["3"].strip()
                    state_id = row["1"].strip()
                    district_id = row["2"].strip()
                if row["4"] == "2011":
                    results.append(
                        (state_id, district_id, name, float(row["7"])))
        except Exception as e:
            print("Exception :" + str(e))
            return results
    return results


def cleanAllCSVs(dir):
    csvs = glob.glob(dir + '/*.csv')
    for csvf in csvs:
        if "cleaned" in csvf:
            continue
        with open(csvf) as inp, open("cleaned" + csvf, "w") as out:
            for x in range(4):
                next(inp)
            for line in inp:
                out.write(line)


def combineResultsFromAllStates(cleanedDir):
    results = []
    csvs = glob.glob(cleanedDir + "/*.csv")
    for csvf in csvs:
        result = getDistrictDVMap(csvf)
        results.extend(result)
    return results


def writeOutCombinedCSV(results, fname):
    with open(fname, "w") as outcsv:
        writer = csv.writer(outcsv, delimiter=",")
        writer.writerow(["state_id", "district_id", "name", "dv_val_2011"])
        for r in results:
            writer.writerow(r)


if __name__ == "__main__":
    cleanAllCSVs("files")
    results = combineResultsFromAllStates("cleanedfiles")
    writeOutCombinedCSV(results, "dv_2011_districts.csv")
