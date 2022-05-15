import csv
from prettytable import PrettyTable

FILE = "currencies22.csv"

def parse_csv():
	data = []
	file = open(FILE,"r")
	tabl = csv.reader(file, delimiter = ";")
	
	for dvi in tabl:
		element = {"name":dvi[0],"market_cap":dvi[1],"price":dvi[2]}
		data.append(element)
	return data

def search(data, key):
	findItems = []

	for item in data:
		if item.get("name").lower().startswith(key.lower()):
			findItems.append(item)

	return findItems

def print_data(data):
	table = PrettyTable()

	table.field_names = ["Наименование", "Рыночная капитализация", "Стоимость 1 ед. в долларах"]

	for element in data:
		table.add_row([element["name"], element["market_cap"], element["price"]])
	print(table)


def main():
	vst = []
	key = ""
	vst = parse_csv()
	print_data(vst)
	key = input("Введите название криптовалюты > ")
	search(vst, key)
	vsk = search(vst, key)
	if len(vsk) == 0:
		print("По запросу ничего не найдено.")
	else:
		print("По запросу найдено:")
		print_data(vsk)

if __name__ == "__main__":
	main()
