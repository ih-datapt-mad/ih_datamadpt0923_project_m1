import argparse
import pandas as pd
from fuzzywuzzy import fuzz, process

#DEFINO LA CLASE PARA LUEGO DECIDIR EXCEPCIONES PERSONALIZADAS
#CUANDO BICIMAD NO EXISTE TE DEVUELVE TU ERROR
class MyExceptionClass_UndefinedApplication(Exception):
    pass

 #DEFINIMOS LA FUNCION FUZZY, CON EL ARGUMENTO DF COMPLETO Y EL LUGAR DE PLACE
def fuzzyWuzzy_func(final_df_bici, user_place):
    sitios_interes = final_df_bici['place'].tolist() #DEL DF FINAL TOMAMOS PLACE Y LA PARSEAMOS A LIST, EXTRACTONE USA STRINGS
    #DEVUELVE DEL SITIOS_INTERES LA INSTALACION QUE MEJOR METRICA TENGA, UTILIZANDO EL PARTIAL RATIO
    (match, score) = process.extractOne(user_place, sitios_interes, scorer=fuzz.partial_ratio, score_cutoff=20) #EXTRACTONE LIST SITIOS INTERES) / ARG PLACE (USER_PLACE)  
    #USA UN UMBRAL DE UN 20% (AQUELLAS QUE DEVUELVAN UNA METRICA POR DEBAJO DEL 20% NO SE TENDRAN EN CUENTA)
    return match

def choice(place, final_df_bici):
    print(f"The nearest bici station is {final_df_bici[final_df_bici['place']==place]['station_address'].iloc[0]}")
    print(f"The bici station is located at: {final_df_bici[final_df_bici['place']==place]['distance'].iloc[0]} metros")

def parser():
    parser = argparse.ArgumentParser(description='This app is to find the nearest bici station using BICIMAD or BICIPARK data')
    parser.add_argument('-a', '--application', help='Choose between BICIMAD or BICIPARK', required=True)
    parser.add_argument('-l','--location', help= 'Choose specific location')
    args = parser.parse_args()
    return args

    user_app = args.application.upper()
    user_place = args.location

    if user_app == "BICIMAD":
        final_df_bici = pd.read_csv('./data/bicimad_data.csv')

    elif user_app == "BICIPARK":
        final_df_bici = pd.read_csv('bicipark_data.csv')
    else:
        raise MyExceptionClass_UndefinedApplication("No has elegido una aplicación correcta! Vuelve a ejecutar y selecciona entre BICIMAD o BICIPARK!")

    if user_place is None:
        print(final_df_bici)
        raise MyExceptionClass_UndefinedLocation("No has elegido una localización correcta! Vuelve a ejecutar!")

    (match, score) = fuzzyWuzzy_func(final_df_bici, user_place)
    print("El Centro deportivo que más se asemeja a la dirección introducida es {}.Se ha elegido con un ratio del {}% ".format(match, score))
    choice(match, final_df_bici)


#PROCESO DE LA FUNCION
