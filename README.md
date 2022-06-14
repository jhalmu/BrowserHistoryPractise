# BROWSER HISTORY. Visualised. 
### Scary thing or not.

Started: 27.5.2022

I could start this from scratch fetching information on browser but not now. Next parts (not included yet) are more interesting. Working with Data analysis is the thing.  

GOAL: Visualise your browser data as you browse. Add categories for domains so yo do not have to show actual domain if there going to be implementations for public use. Charts and Pies, and if possible, some French/Freedom fries. Main goal: Know where you have been...  

### Journal
28.5.2022
- Finded way to manipulate browser_history's interesting data-stream. I wanted to cut urls to have only domains. Cleaned date-data 'cos I could. Succeed with domain-thing after hard "my way" trying. Tuples and strings, fun.
- This uses Firefox as The Browser as it is anyway. But using another browsers ok too, see footnote *) 

3.6.2022
- Started to add FastApi, but not yet. Saved that for another project. New idea is start new cloud postgres database so my I can show world wide what I am browsing. Thinking [hasura](hasura.io) and of course that that...

6.6.2022
- Added FastApi and figurded out finally (stackover..). Still missing things. But there is now one for chart.js via jinja2 and one as an api. Information is kind of boring, so it vill take much that I figure (oh, pun) out what is best way to show this data: time and www address.

14.6.2022
- I ditch this project for now. This was good practice for more interesting data. If you want't to start this up, main.py is the file. Make first csv-file from your own Firefox browser-history. Instructions in browserdata.py. Astually you might not need csv, because df includes same data than you export. Haven't tried. 

14.4.2022
- Here I am, same days evning. Can't stop before I learn this. I trimmed time-part so no it shows time to day. Maeby now some pivot things working better.  


## TODO
- [X] Data-stream
- [ ] Basic pivoting strategies
- [ ] Visualisation 1 aka basic plotting
- [ ] Server based functionalities. Have link to show your history in browser
- [ ] Postgress database in docker 
- [ ] and Postgess in the cloud 
- [ ] Helper db-tables for masking www adresses aka making categories 
- [ ] Dockerize
- [ ] Starting The End Product(s) project
- [X] API
- [ ] Mobile App
- [ ] Desktop App
- [ ] Have trip to Space with Elon

- [ ] Clean env 


*) This project is started based on [samyak](https://pypi.org/user/samyak/)'s + contributors in [Browser History](https://pypi.org/project/browser-history/)

## REQUIREMENTS
# Because freeze and conda makes hard requirements files nowdays when there is M1 and other machines

- browser-history
- pandas
- uvicorn
- fastapi 
- dash w/ extras  