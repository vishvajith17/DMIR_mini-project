from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json, re
import codecs
import unicodedata
import datetime
# import queries

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'lyrics123'

def createIndex():
    settings = {
        "settings": {
            "index":{
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis" :{
                "analyzer":{
                    "sinhala-analyzer":{
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter":["edge_ngram_custom_filter"]
                    }
                },
                "filter" : {
                    "edge_ngram_custom_filter":{
                        "type": "edge_ngram",
                        "min_gram" : 2,
                        "max_gram" : 50,
                        "side" : "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                    "title": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "lyrics": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "artist": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "lyricist": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "music": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "genre": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "metaphors": {
                        "properties": {
                            "lyrics_part": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "meaning": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "source_domain": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "target_domain": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            }
                        }
                    }
            }
        }
    }
    result = client.indices.create(index=INDEX , body =settings)
    print (result)

def read_all_songs():
    with open('./data/songs_lyrics_corpus.json', 'r', encoding='utf8') as f:
        tra_songs = json.loads(f.read())
        results_list = [a for num, a in enumerate(tra_songs) if a not in tra_songs[num + 1:]]
        return results_list

def genData(song_array):
    for song in song_array:

        title = song["title_si"]
        #song_lyrics = clean_function(song["song_lyrics"])
        artist = song["artist"]
        lyricist = song["writer"]
        music = song["music"]
        genre = song["genre"]
        lyrics = song["lyrics"]
        metaphors = song["metaphor"]
        
        yield {
            "_index": INDEX,
            "_source": {
                "title": title,
                "artist": artist,
                "lyricist": lyricist,
                "music": music,
                "genre": genre,
                "lyrics": lyrics,
                "metaphors": metaphors
            },
        }
        



createIndex()
all_songs = read_all_songs()
# print(all_songs[0]['metaphors'][0])
# print(len(all_songs))
# genData(all_songs)
#print(genData)
helpers.bulk(client,genData(all_songs))