import requests
from bs4 import BeautifulSoup
import mysql.connector  


conn = mysql.connector.connect(
    host="localhost",       
    user="root",  
    password="Sandy@410", 
    database="imdb_movies" 
)
cursor = conn.cursor()

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    Movies = soup.find('ul', class_="ipc-metadata-list").find_all("li")

    for movie in Movies:
        Title = movie.find('div', class_="ipc-title").h3.text
        Movie_details = movie.find('div', class_="sc-d5ea4b9d-6 hBxwRe cli-title-metadata").find_all("span")

        Release_Year = Movie_details[0].text
        Duration = Movie_details[1].text
        Rating = Movie_details[2].text
        IMDb_Score = movie.find('span', class_="ipc-rating-star--rating").text
        Number_of_Votes = movie.find('span', class_="ipc-rating-star--voteCount").text

        #print(Title, Release_Year, Duration, Rating, IMDb_Score, Number_of_Votes)

        cursor.execute("""
            INSERT INTO movies (title, release_year, duration, rating, imdb_score, number_of_votes)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (Title, Release_Year, Duration, Rating, IMDb_Score, Number_of_Votes))

    conn.commit()
    print("Data inserted into MySQL successfully!")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
