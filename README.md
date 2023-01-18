# DMIR_mini-project
Data Mining &amp; Information Retrieval_Mini Project - Building Text Corpus and Search Application


---How to Run the Application---
install elastic search and setup in port 9200
install elasticsearch_dsl using pip
install flask using pip
install plugin inside the elastic search  using bin/elasticsearch-plugin install analysis-icu
Run index-creat.py
Run main.py
visit http://127.0.0.1:5000/ and enjoy!!!

IR_Project-Song_Search_Engine
Song Search Engine using ElasticSearch and Python for IR Project(CS4642)

Getting Start

Setting up the Environment
    Download and Install the ElasticSearch
    Install the ICU_Tokenizer plugin on the ElasticSearch
    Install the python3 with pip3
    Running the Project
    First start the ElasticSearch locally on port 9200.
    Then run index_creation.py file to create the index and insert data.
    Next run the main.py to start the search engine
    Then visit http://localhost:5000/ for see the user interface.
    Finally add your search query in the search box for searching.

File Structure
data - Folder contains both scraped data and translatd data with python code used for translation
    templates - Folder contains Html user interface of the search engine
    index_creation.py - Python code for index creating and data inserting
    search_function.py - Python code use for process search query
    advanced_queries.py - Elastic Search queries

title - Song title in both Sinhala and English languages
song_lyrics - Song lyrics in Sinhala
artist - Singer's name in Sinhala
lyricist - writer's name in Sinhala
music - Musician's name in Sinhala
genre - Song type in Sinhala
metaphore - Metaphores

Basic Functionalities
It supports searching by the title, artist name, writer name, composer name, or using the part of the lyrics.(Faceted Query)
eg : රිද්ම කුවේණියේ, Akuru Maki Nehe – අකුරු මැකී නෑ, රන් ටිකිරි සිනා

Search Engine can identify synonyms related to specific fields like ගයපු(artist), ලියපු(lyricist), සංගීත(music) and search based on the identified fields
eg : එච්.ආර්.ජෝතිපාල ගයපු සින්දු, ලුෂන් බුලත්සිංහල ලියූ සින්දු, එච්.එම්. ජයවර්ධන සංගීතවත් කල ගී

Search Engine also support to the query phrases which is a mix of Sinhala and English languages.
eg : එච්.ආර්.ජෝතිපාල songs

