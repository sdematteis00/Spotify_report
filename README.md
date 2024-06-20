<h1> Spotify Analysis</h1>

<h2>Introduction</h2>
This repository contains an analysis of a public Spotify dataset. The analysis includes information about the most popular artists, tracks, and albums, as well as listening trends over time.
<br />

<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Excel</b>
- <b>PowerBI</b>

<h2>Database Used </h2>

- [Spotify Dataset](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download&select=spotify-2023.csv)

<h2>Methodology</h2>
The analysis was conducted in several stages:

- <b> Database Cleaning in Excel: </b>
  - I imported the Spotify dataset into Excel.
  - I removed any duplicate or incomplete records.
  - I formatted the data consistently.

- <b> Creating Album URL Column with Python: </b>
  - I used a Python script to extract album IDs from each track.
  - I utilized the Spotify API to retrieve album URLs from the IDs.
  - I added a new column to the dataset containing the album URLs.

- <b> Analysis in Power BI: </b>
  - I imported the dataset into Power BI.
  - I created visualizations to explore the data, such as bar charts and line chart.
  - I created calculated measures to gain deeper insights from the analysis, such as:
    - Average number of listens per album
    - Album popularity over time
  - I used filters and slicers to analyze the data in more detail.

<h2>Program walk-through:</h2>
<img src="https://i.imgur.com/FzltZIy.png">


<img src="http://ecopas.altervista.org/ezgif.com-video-to-gif-converter.gif">

<img src="http://ecopas.altervista.org/Video3.gif">
