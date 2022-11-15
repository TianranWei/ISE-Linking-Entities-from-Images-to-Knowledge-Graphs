import logging

import pandas as pd




logger = logging.getLogger(__name__)
class StringMatcher():
    
    def __init__(self) -> None:
        self.df = pd.read_csv("/Users/twei/workplace/ISE-workplace/ISE-Linking-Entities-from-Images-to-Knowledge-Graphs/src/data/dbpedia_classes.csv")
    
    def match_string(self, string:str) -> pd.DataFrame:
        """method that gives us the dbpedia class to a given string
        OBS: the string needs the be the same as the label of the class
        TODO: find pattern that allows upper/lowercase differences if necessary
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
    
a = StringMatcher()
print(a.match_string("zoo"))
