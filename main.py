##############################################################################
#                                                                            #                       
#   argparse — Parser for command-line options, arguments and sub-commands   #     
#                                                                            #
#   Ironhack Data Part Time --> Sep-2023                                    #
#                                                                            #
##############################################################################


# import library

import modules.prog as pr
import pandas as pd
import requests 
import modules.funciones as fn 


def main (): 
    instalaciones_df = fn.instalaciones()
    bicipark_df = fn.bicipark_final(instalaciones_df)
    #print('bicipark created')
    bicimad_df = fn.bicimad_final(instalaciones_df)
    #print(bicimad_df.columns)
    if pr.parser().application.upper() == 'BICIMAD':
        nearest_df =fn.nearest(instalaciones_df,bicimad_df)

    elif pr.parser().application.upper() == 'BICIPARK':    
        nearest_df =fn.nearest(instalaciones_df,bicipark_df)
    #print(nearest_df)
    if pr.parser().location != None:
        instalacion = pr.fuzzyWuzzy_func(nearest_df,pr.parser().location)
        print("DataFrame filtrado con fuzzywuzzy:")
        print(instalacion)
        filtered_df = nearest_df.loc[nearest_df['place'] == instalacion ]  
        print(filtered_df)    
    else:
        print(nearest_df)    

    return
    
if __name__ == '__main__':
    main ()