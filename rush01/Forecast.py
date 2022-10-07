import pickle
import numpy as np

class Forecast:
    """
    Predicting the rating or the class
    """
    list_of_ingredients = list()
    rating = 0.0
    rating_cat = 0
    text = ""
    text_cat = ""
    
    def __init__(self, list_of_ingredients):
        """
        Put any fields here that you think you will need.
        """
        self.list_of_ingredients = list_of_ingredients
  
    def preprocess(self):
        """
        This method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.
        """
        with open("./data/epi_r_short.csv", 'r') as fin:
            header = dict.fromkeys(fin.readline().strip().split(','), 0)

        del header["title"]
        del header["rating"]
        del header[""]
        for i in header:
            for j in self.list_of_ingredients:
                if (i == j):
                    header[i] = 1
        
        return [header[i] for i in header]
        
    def predict_rating(self):
        """
        This method returns the rating for the list of ingredients using the regression model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating and gives a recommendation as in the example above.
        """
        with open("./data/finalized_regression.sav", 'rb') as fin:
            regr = pickle.loads(fin.read())
        vector = self.preprocess()
        rating = regr.predict(vector)
        
        if round(rating) < 2:
            text = "Bad idea to mix this ingredients!"
        elif round(rating) < 4:
            text = "The idea to mix this ingredients is so-so."
        else:
            text = "It's a great idea to cook something with this ingridients."

        self.rating = rating
        self.text = text
        
        return rating, text
        
    def predict_rating_category(self):
        """
        This method returns the rating category for the list of ingredients using the classification model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating category and gives a recommendation as in the example above.
        """
        with open("./data/finalized_classifier.sav", 'rb') as fin:
            clsfctr = pickle.loads(fin.read())
        vector = self.preprocess()
        vector = np.array(vector).reshape((1, -1))
      
        rating_cat = clsfctr.predict(vector)
        
        if rating_cat < 2:
            text_cat = "Bad idea to mix this ingredients!"
        elif rating_cat < 4:
            text_cat = "The idea to mix this ingredients is so-so."
        else:
            text_cat = "It's a great idea to cook something with this ingridients."

        self.rating_cat = rating_cat
        self.text_cat = text_cat
        
        return rating_cat, text_cat
    