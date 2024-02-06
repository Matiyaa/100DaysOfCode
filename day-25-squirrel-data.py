import pandas


def main():
    data = pandas.read_csv("day-25-Squirrel_Data.csv")
    data_frame = pandas.DataFrame(data)
    count_data = data_frame["Primary Fur Color"].value_counts()
    count_data.to_csv("day-25-squirrel_count.csv")


if __name__ == "__main__":
    main()