import psycopg2

PSQL_HOST = 'localhost'
PSQL_PORT = '5432'
PSQL_USER = 'postgres'
PSQL_PASS = ''
PSQL_DB = 'postgres'

connection_address = """
host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
connection = psycopg2.connect(connection_address)

cursor = connection.cursor()

population = "SELECT * FROM poblacion;"
income = "SELECT * FROM ingresos;"
cursor.execute(population)
population_values = cursor.fetchall()
cursor.execute(income)
income_values = cursor.fetchall()

cursor.close()
connection.close()

pib_per_capita = []

def Pib_per_capita(population, income):
    for tupl in population:
        year = tupl[1]
        for ingres in income:
            second_year = ingres[1]
            if year == second_year:
                result = int(ingres[2]) /tupl[2]
                pib_per_capita.append(result)
    return pib_per_capita

def Big_less(info):
    biggest_value = 0 
    smallest_value = info[1]
    for value in info:
        if value > biggest_value:
            biggest_value = value
        else:
            pass
        
        if value < smallest_value:
            smallest_value = value
        else:
            pass

    return [biggest_value, smallest_value]

def Population_increment(poblacion, j = int):
    i = 1
    poblation_diferencies = []
    first_data = poblacion[0]
    first_poblation = first_data[j]
    for count in poblacion:
        actual_poblation = count[j]
        try:
            future_data = poblacion[i]
        except:
            pass
        men = future_data[j] 
        subtraction = men - actual_poblation
        poblation_diferencies.append(subtraction)
        i += 1
    poblation_diferencies.remove(0)
    return poblation_diferencies

def Man_and_woman_comparison(poblacion):
    more_men = False
    for info in poblacion:
        if info[3] > info[4]:
            more_men = True
        else:
            pass
    return more_men

def Searching(info, more_less):
    max_ubi = info.index(more_less[0])
    min_ubi = info.index(more_less[1])
    maxi = int(more_less[0])
    minu = int(more_less[1])
    data_max = income_values[max_ubi]
    data_minu = income_values[min_ubi]
    year_max = int(data_max[1])
    year_min = int(data_minu[1])

    return [maxi, minu, year_max, year_min]


if __name__ == '__main__':
    pib_per_cap = Pib_per_capita(population_values, income_values)
    more_less = Big_less(pib_per_cap)
    men_changes = Population_increment(population_values, 3)
    more_less_man = Big_less(men_changes)
    women_changes = Population_increment(population_values, 4)
    more_less_woman = Big_less(women_changes)
    total_changes = Population_increment(population_values, 2)
    more_less_total = Big_less(total_changes)
    more_men = Man_and_woman_comparison(population_values)

    search_pib = Searching(pib_per_cap, more_less)
    search_man = Searching(men_changes, more_less_man)
    search_woman = Searching(women_changes, more_less_woman)
    search_total = Searching(total_changes, more_less_total)
    print('en México el maximo pib per capita que ha habido ha sido en el año de', int(search_pib[2]),'con un ingreso de', int(search_pib[0]), 'por persona y el menor fue en el año de', int(search_pib[3]), 'con un total de', int(search_pib[1]), 'por persona')
    print('en México el maximo aumento de hombres en la poblacion fue de', int(search_man[0]),'en el año de', int(search_man[2]), 'y el menor aumento fue de', int(search_man[1]), 'en el año de ', int(search_man[3]))
    print('en México el maximo aumento de mujeres en la poblacion fue de', int(search_woman[0]),'en el año de', int(search_woman[2]), 'y el menor aumento fue de', int(search_woman[1]), 'en el año de ', int(search_woman[3]))
    print('en México el maximo aumento total en la poblacion fue de', int(search_total[0]),'en el año de', int(search_total[2]), 'y el menor aumento fue de', int(search_total[1]), 'en el año de ', int(search_total[3]))
    print('otro dato que podemos sacar es que en México segun estos datos desde el año de 1960 residen mas mjeres que hombres en el pais')