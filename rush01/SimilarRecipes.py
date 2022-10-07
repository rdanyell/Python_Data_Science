import pandas as pd 
import requests
import time
from bs4 import BeautifulSoup

class SimilarRecipes:
    """
    Recommending similar recipes with additional information
    """
    def __init__(self, list_of_ingredients):
        """
        Put any here fields that you think you will need.
        """    
        df = pd.read_csv('data/epi_r_short.csv')
        self.ingredients = list_of_ingredients
        df_filter = df
        for ing in list_of_ingredients:
            df_filter = df_filter[df_filter[ing] == 1]
        if df_filter.shape == 0:
            self.filter = None
        else:
            self.filter = df_filter

    def find_all(self):
        """
        This method returns a list of indexes of the recipes that contain the given list of ingredients. If there is no recipe that contains all the ingredients, handle it.
        """
        if self.filter is None:
            return None
        return self.filter
    
    def get_recipe(self, recipe):
        url_epic = 'https://www.epicurious.com/search/' + recipe.replace(' ', '%20')
        resp = requests.get(url_epic, time.sleep(3))
        if resp.status_code != 200:
            return None
        data = resp.text
        soup = BeautifulSoup(data, 'lxml')
        for a in soup.find_all('a', href=True):
            if '/recipes/food/views/' in a['href']:
                return 'https://www.epicurious.com' + str(a['href'])

    def top_similar(self, n):
        """
        This method returns a text formatted as in the example above with title, rating, and URL. Before that, it finds top-n most similar recipes by the number of additional ingredients that are required in the recipes using indexes from the find_all method. The most similar is the one that does not require any other ingredients. Next is the one that requires only one, etc. If it requires 5 more ingredients, do not return those recipes.
        """
        filter = self.filter
        filter['extra_num'] = filter.iloc[:,3:].sum(axis=1, ) - len(self.ingredients)
        topn = filter.sort_values(by='rating', ascending=False).iloc[:n+1,:]
        if topn.shape[0] == 0:
            print("There are no recipes with these ingridients in our base.")

        URL = []
        text_with_recipes = ''  
        for i in range (topn.shape[0]): 
            title = topn.iloc[i].title
            rating = topn.iloc[i].rating
            URL = SimilarRecipes.get_recipe(self, title) 
            if (URL):
                text_with_recipes += f'-  {title}, rating: {rating}, URL: {URL}\n'
        return text_with_recipes
    