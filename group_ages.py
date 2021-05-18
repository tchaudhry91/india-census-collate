#!/usr/bin/env python3
import sys
import csv


def build_grouped_csv(fname):
    district_dict = {}
    with open(fname) as csvfile:
        with open("grouped-" + fname, "w") as csvout:
            fieldnames = ['state', 'district', 'name',
                          'age', 'persons', 'males', 'females']
            writer = csv.DictWriter(csvout, fieldnames=fieldnames)
            writer.writeheader()
            reader = csv.DictReader(csvfile)
            for row in reader:
                state = row.get("state")
                district = row.get("district")
                name = row.get("name")
                age = row.get("age")
                persons = row.get("persons")
                males = row.get("males")
                females = row.get("females")
                if district in district_dict:
                    try:
                        age = int(age)
                    except ValueError:
                        continue
                    try:
                        if age >= 18 and age < 45:
                            district_dict[district]["persons"]["18-44"] += int(
                                persons)
                            district_dict[district]["males"]["18-44"] += int(
                                males)
                            district_dict[district]["females"]["18-44"] += int(
                                females)
                        if age >= 45 and age < 60:
                            district_dict[district]["persons"]["45-59"] += int(
                                persons)
                            district_dict[district]["males"]["45-59"] += int(
                                males)
                            district_dict[district]["females"]["45-59"] += int(
                                females)
                        if age >= 60:
                            district_dict[district]["persons"]["60+"] += int(
                                persons)
                            district_dict[district]["males"]["60+"] += int(
                                males)
                            district_dict[district]["females"]["60+"] += int(
                                females)
                    except:
                        print("Found an error while working on " +
                              state + ": " + district)
                else:
                    district_dict[district] = {
                        "state": state,
                        "name": name,
                        "persons": {
                            "18-44": 0,
                            "45-59": 0,
                            "60+": 0,
                        },
                        "males": {
                            "18-44": 0,
                            "45-59": 0,
                            "60+": 0,
                        },
                        "females": {
                            "18-44": 0,
                            "45-59": 0,
                            "60+": 0,
                        }
                    }
            # Write CSV now
            for d, v in district_dict.items():
                writer.writerow(
                    {
                        "state": v.get("state"),
                        "district": d,
                        "name": v.get("name"),
                        "age": "18-44",
                        "persons": v.get("persons").get("18-44"),
                        "males": v.get("males").get("18-44"),
                        "females": v.get("females").get("18-44"),
                    }
                )
                writer.writerow(
                    {
                        "state": v.get("state"),
                        "district": d,
                        "name": v.get("name"),
                        "age": "45-59",
                        "persons": v.get("persons").get("45-59"),
                        "males": v.get("males").get("45-59"),
                        "females": v.get("females").get("45-59"),
                    }
                )
                writer.writerow(
                    {
                        "state": v.get("state"),
                        "district": d,
                        "name": v.get("name"),
                        "age": "60+",
                        "persons": v.get("persons").get("60+"),
                        "males": v.get("males").get("60+"),
                        "females": v.get("females").get("60+"),
                    }
                )


def main(args):
    input_file = args[0]
    build_grouped_csv(input_file)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
