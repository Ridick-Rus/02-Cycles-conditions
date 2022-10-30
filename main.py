drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro",
              "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3",
              "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

# в drone по очереди попадает каждый дрон из списка drone_list
CORRECT_COMPANY_LIST = {
    "dji": "DJI",
    "autel": "Autel",
    "parrot": "Parrot",
    "ryze": "Ryze",
    "eachine": "Eachine"
}

index = -1
for drone in drone_list:
    index += 1
    drone_data = drone.split(' ')
    try:
        drone_data[0] = CORRECT_COMPANY_LIST[drone_data[0].lower()]
    except:
        raise Exception("Undefined company_name, check CORRECT_COMPANY_LIST")
    drone_list[index] = ' '.join(drone_data)
    print(drone_list[index])
# TODO1
# выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество.
# учтите, что:
# 1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
# 2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel
print("Введите название компании производителя")
chosen_company = input()

for drone in drone_list:
    drone_data = drone.split(' ')
    company_name = drone_data[0]
    drone_name = drone_data[1:]
    if chosen_company.lower() == company_name.lower():
        print(company_name, ' '.join(drone_name))

# TODO2
# подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
drone_amount = {"DJI": 0, "Autel": 0, "Parrot": 0, "Ryze": 0, "Eachine": 0}
for drone in drone_list:
    company_name = drone.split(' ')[0]
    drone_amount[company_name] += 1

for key, value in drone_amount.items():
    print("{0}: {1}".format(key, value))

# TODO3
# выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество.
# сделайте то же самое для всех дронов, которые не нужно регистрировать
# для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
# как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

need_register_drones = []
dont_need_register_drones = []
for drone, weight in zip(drone_list, drone_weight_list):
    if weight > 150:
        need_register_drones.append(drone)
    else:
        dont_need_register_drones.append(drone)

print("\nЭтих дронов необходимо зарегистрировать")
for drone in need_register_drones:
    print(drone)
print(len(need_register_drones))

print("\nЭтих дронов не нужно регистрировать")
for drone in dont_need_register_drones:
    print(drone)
print(len(dont_need_register_drones))

# TODO4
# для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
# высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
# помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

for drone, weight in zip(drone_list, drone_weight_list):

    #print("Введите высоту")
    height = 100

    city_check = ""
    while city_check not in ["Д", "н"]:
        #print("Летите ли вы над населённым пунктом?[Д/н]")
        city_check = "Д"
    if city_check == "Д": city_check = True

    close_zone_check = ""
    while close_zone_check not in ["Д", "н"]:
        #print("Вы находитесь в закрытой зоне? [Д/н]")
        close_zone_check = "н"
    if close_zone_check == "Д": close_zone_check = True

    view_check = ""
    while view_check not in ["Д", "н"]:
        #print("Вы находитесь в прямой видимости? [Д/н]")
        view_check = "Д"
    if view_check == "н": view_check = True

    if (height > 150) or (city_check and weight > 150) or close_zone_check == True or view_check == True:
        print("Для дрона {0} нужно согласование".format(drone))
    else:
        print("Для дрона {0} не нужно согласование".format(drone))
# TODO5*
# модифицируйте решение задания TODO1:
# теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
# например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
# производители те же: DJI, Autel, Parrot, Ryze, Eachine
