import logging

import pandas as pd




logger = logging.getLogger(__name__)
class StringMatcher():
    
    def __init__(self) -> None:
        self.df = pd.read_csv("data/raw/dbpedia_classes.csv")
    
    def match_exact_string(self, string:str) -> pd.DataFrame:
        """method that gives us the dbpedia class to a given string
        Args:
            string (str): the class we are looking for
        Returns:
            pd.DataFrame: returns a DataFrame with the corresponding classes from dbpedia
        """        
        output = pd.DataFrame()
        if self.df['label'].eq(string).any():
            df = self.df[self.df['label'] == string]['class']
            output = pd.DataFrame(df)
            output = output.reset_index(drop=True)           
        else:
            logger.info("Couldnt find matching string to: {string}")
        return output    
    
    def match_lowercase_exact_string(self, string:str) -> pd.DataFrame:
        output = pd.DataFrame()
        if self.df['label'].eq(string.lower()).any():
            df = self.df[self.df['label'] == string]['class']
            output = pd.DataFrame(df)
            output = output.reset_index(drop=True)           
        else:
            logger.info("Couldnt find matching string to: {string}")
        return output
      
a = StringMatcher()
print(a.match_exact_string("zoo"))
