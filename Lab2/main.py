from company import AirlineCompany

def main():
    company = AirlineCompany()
    company.load_from_file('data/planes.json')

    print("\n--- Общая информация ---")
    print(f"Пассажировместимость: {company.total_passenger_capacity()}")
    print(f"Грузоподъемность: {company.total_cargo_capacity()} тонн")

    print("\n--- Сортировка по дальности ---")
    for plane in company.sort_by_range():
        print(plane)

    print("\n--- Поиск по расходу топлива (от 2000 до 5000 Л/ч) ---")
    for plane in company.find_by_fuel_consumption(2000, 5000):
        print(plane)

if __name__ == "__main__":
    main()
