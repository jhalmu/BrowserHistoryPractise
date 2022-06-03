# BROWSER HISTORY. Visualised. 
### Scary thing or not.

Started: 27.5.2022

I could start this from scratch fetching information on browser but not now. Next parts (not included yet) are more interesting. Working with Data analysis is the thing.  

GOAL: Visualise your browser data as you browse. Add categories for domains so yo do not have to show actual domain if there going to be implementations for public use. Charts and Pies, and if possible, some Frenc/Freedom fries. Main goal: Know where you have been...  

### Journal
28.5.2022
- Finded way to manipulate browser_history's interesting data-stream. I wanted to cut urls to have only domains. Cleaned date-data 'cos I could. Succeed with domain-thing after hard "my way" trying. Tuples and strings, fun.
- This uses Firefox as The Browser as it is anyway. But using another browsers ok too, see footnote *) 

3.6.2022
- Started to add FastApi, but not yet. Saved that for another project. New idea is start new cloud postgres database so my I can show world wide what I am browsing. Thinking [hasura](hasura.io) and of course that that...


## TODO
- [X] Data-stream
- [ ] Basic pivoting strategies
- [ ] Visualisation 1 aka basic plotting
- [ ] Server based functionalities. Have link to show your history in browser
- [ ] Dockerize
- [ ] Starting The End Product(s) project
- [ ] API
- [ ] Mobile App
- [ ] Desktop App
- [ ] Have trip to Space with Elon

- [ ] Clean env 


*) This project is started based on [samyak](https://pypi.org/user/samyak/)'s + contributors in [Browser History](https://pypi.org/project/browser-history/)

## REQUIREMENTS
# Because freeze and conda makes hard requirements files nowdays when there is M1 and other machines

- browser-history
- pandas   