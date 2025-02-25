import requests
from bs4 import BeautifulSoup
import pandas, openpyxl


excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Movie Details"
sheet.append(["Title", "Release Year", "Duration", "Rating", "IMDb Score", "Number of Votes"])

url="https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
    response= requests.get(url, headers=headers)
    soup= BeautifulSoup(response.text,'html.parser')
    #print(soup)
    Movies=soup.find('ul',class_="ipc-metadata-list").find_all("li")

    for movie in Movies:
       # print(Movies)
        Title=movie.find('div', class_="ipc-title").h3.text
        Movie_details = movie.find('div', class_="sc-d5ea4b9d-6 hBxwRe cli-title-metadata").find_all("span")
        Release_Year=Movie_details[0].text
        Duration=Movie_details[1].text
        Rating =Movie_details[2].text
        IMDb_Score=movie.find('span', class_="ipc-rating-star--rating").text
        Number_of_Votes=movie.find('span', class_="ipc-rating-star--voteCount").text #.replace('(',"")
        #People_rated=People_rated.replace(')',"")
        print(Title,Release_Year,Duration,Rating ,IMDb_Score,Number_of_Votes)
        sheet.append([Title,Release_Year,Duration,Rating ,IMDb_Score,Number_of_Votes])
except Exception as e:
    print(e)

excel.save("IMDB Movie list.csv")
print("Excel file created successfully")