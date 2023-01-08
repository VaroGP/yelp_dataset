<div align="center">
<a href="https://example.com"><img src="https://localmarketinginstitute.com/wp-content/uploads/2020/03/yelp-reviews.png" alt="Yelp" width="842"/></a>

Machine Learning
==============================

Yelp Dataset Analysis
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Project Organization</a>
        <li><a href="#description">Description</a></li>
    </li>
    <li>
      <a href="#authors">Authors</a>
        <li><a href="#github-link">Github link</a></li>
    </li>
  </ol>
</details>

## Project Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │    │  
    │    └── restaurants
    │    │  
    │    └── reviews
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── html               <- Generated analysis as HTML.
    │
    ├── env                <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │    │  
    │    └── Preprocessor.py
    │
    └── end.


## Description

In this proyect, we have analysed the Yelp dataset in order to select 2 business lines.
To achieve this goal, we have performed the following steps:

Steps Yelp Anlaysis
------------
    ├── 01 - Data Extraction            <- Extraction of the 5 tables from Yelp (Json to Dataframe)
    │               │  
    │               └── Bussines
    │               │  
    │               └── Reviews
    │               │  
    │               └── Users
    │               │  
    │               └── Tips
    │               │  
    │               └── Checkin
    │
    ├── 02 - EDA                       <- Exploratory Data Analysis of the tables
    │
    ├── 03 - First Business Model      <- Selection of the first business line and model generation.
    │               │  
    │               └── Model Selection
    │               │  
    │               └── Tunning
    │               │  
    │               └── Explicability
    │
    ├── 04 - Second Business Model     <- Selection of the second business line and model generation.
    │               │  
    │               └── Model Selection
    │               │  
    │               └── Tunning
    │               │  
    │               └── Explicability
    └── end.

## Authors
-------
* Jorge Plaza Yuste: jorge.plaza@cunef.edu \
* Álvaro Gómez Pérez: alvaro.gomezperez@cunef.edu

## Github link
------
Available at https://github.com/JorgePlazaJPY
Available at https://github.com/VaroGP
