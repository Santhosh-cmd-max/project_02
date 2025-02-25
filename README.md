# 🎬 IMDb Top Movies Scraper  
A Python project that scrapes IMDb's **Top 25 Movies** and exports the data to **Excel and MySQL**.  


## 📌 Project Overview  
This project collects movie details from IMDb's **Top 25 Movies List** and allows exporting data to:  
✅ **Excel (`IMDB Movie list.csv`)**  
✅ **MySQL Database (`web-db.sql`)**  

Extracted movie details:  
- **Movie Title**  
- **Release Year**  
- **Duration**  
- **Rating (PG, R, etc.)**  
- **IMDb Score**  
- **Number of Votes**  

---

## 🛠 Files in the Repository  

| File Name             | Description |
|----------------------|-------------|
| `web.py`            | Python script to scrape IMDb and export data to Excel. |
| `web-db.py`         | Python script to scrape IMDb and insert data into MySQL. |
| `web-db.sql`        | SQL script to create the **`movies`** table in MySQL. |
| `IMDB Movie list.csv` | Exported IMDb movie data (Excel format). |
| `README.md`         | Project documentation. |
