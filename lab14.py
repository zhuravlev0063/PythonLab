import xml.etree.ElementTree as ET

# Загрузка OSM-файла
osm_file = r"C:\Users\zhura\Desktop\9.osm"  # Убедитесь, что файл находится в той же директории

# Словарь для аптек
pharmacies = []
round_the_clock_pharmacies = 0

# Чтение и обработка файла
tree = ET.parse(osm_file)
root = tree.getroot()

# Итерация по узлам для поиска аптек
for element in root.findall(".//node"):
    tags = {tag.attrib['k']: tag.attrib['v'] for tag in element.findall("tag")}

    # Проверяем, является ли объект аптекой
    if tags.get("amenity") == "pharmacy":
        pharmacies.append(tags.get("name", "Unknown Pharmacy"))

        # Проверяем, работает ли аптека круглосуточно
        if tags.get("opening_hours") == "24/7":
            round_the_clock_pharmacies += 1

# Удаление дубликатов и сортировка списка аптек
pharmacies = sorted(set(pharmacies))

# Вывод результатов
print(f"Количество аптек: {len(pharmacies)}")
print("Список аптек в алфавитном порядке:")
for pharmacy in pharmacies:
    print(pharmacy)

print(f"Количество круглосуточных аптек: {round_the_clock_pharmacies}")