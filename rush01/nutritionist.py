import sys
from SimilarRecipes import *
from Forecast import *
from NutritionFacts import *
import warnings


def main():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments!")
    ingridients = sys.argv[1:]
    ingridients_clean = []
    for ingr in ingridients:
        if ingr[-1] == ',':
            ingr = ingr.rstrip(',')
            ingridients_clean.append(ingr)
        else:
            ingridients_clean.append(ingr)
    df = pd.read_csv('data/epi_r_short.csv')
    names = list(df.columns)[3:]
    for ing in ingridients_clean:
        if ing not in names:
            print('Ingridient ' + ing + ' is not found in base')
            exit()

    print('I. OUR FORECAST')
    print("There are two methods of forecasting. Choose the one you like!")
    rgr = Forecast(ingridients_clean)
    rgr.predict_rating()
    rgr.predict_rating_category()
    print(rgr.rating, " -  ", rgr.text)
    print(rgr.rating_cat, " -  ", rgr.text_cat)
    print("\n")
    print('II. NUTRITION FACTS')
    
    nf = NutritionFacts(ingridients_clean)
    nf.nutrients_norm()
    nf.printer(nf.retrieve())
    
    print('III. TOP-3 SIMILAR RECIPES')
    sr = SimilarRecipes(ingridients_clean)
    print(sr.top_similar(3))

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
         