#modul zawierarajacy klasy
import ex_903_1

#modul pobierajacy dane
import ex_903_2 as get_user_data


imie = get_user_data.get_first_name()

kacper = ex_903_1.User(imie, 'turek', 'pi33966', 'devopsAdmin')
kacper.greet_user()
kacper.describe_user()
