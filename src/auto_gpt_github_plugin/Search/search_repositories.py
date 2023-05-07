import os
import requests
import dotenv
import pandas as pd

class Search():

    url = 'https://api.github.com/'
    
    def sort_by():
        sorts = ['stars', 'forks', 'help-wanted-issues', 'updated']
        sort_by = sorts[0]
        return sort_by
    
    def language():
        language = 'python'
        language = 'language:${language}'
        return language
    
    def text_match():
        text_match = pd.read_csv('text_match.txt')
        texts = [text_match]
        text = "_".join(texts)
        return text
    
    def execute_search():
        ## This query searches for repositories with the match_text in the name, the description, or the README. 

        language = language()
        search_type = search_type()
        text_match = text_match()
        sort_by = sort_by()
        header = 'accept:application/vnd.github+json'
        search = '${url}${search_type}?q=${text_match}+${language}s&sort=${sort_by}'
        
        return requests.get(header,search).json()