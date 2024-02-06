import csv
import pandas


def main():
    # with open("day-25-weather_data.csv") as data_file:
    #     data = data_file.readlines()
    #     print(data)
    #
    # with open("day-25-weather_data.csv") as data_file:
    #     data = csv.reader(data_file)
    #     temperature = [int(row[1]) for row in data if row[1] != "temp"]
    #
    # print(temperature)
    #
    # data = pandas.read_csv("day-25-weather_data.csv")
    # print(data["temp"])
    #
    data = pandas.read_csv("day-25-weather_data.csv")
    # data_dict = data.to_dict()
    # print(data_dict)
    #
    # temp_list = data["temp"].to_list()
    # print(temp_list)
    #
    # print(data["temp"].mean())
    # print(data["temp"].max())
    #
    # Get data in columns
    # print(data["condition"])
    # print(data.condition)
    #
    # Get data in rows
    # print(data[data.day == "Monday"])
    # print(data[data.temp == data.temp.max()])
    #
    # monday = data[data.day == "Monday"]
    # print(monday.temp[0] * 9/5 + 32)

    # Create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("day-25-new_data.csv")


if __name__ == "__main__":
    main()
