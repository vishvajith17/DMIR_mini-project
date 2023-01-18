import json

#best_fields
def multi_match_agg_best(query, fields=['title','lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Title Filter": {
				"terms": {
					"field": "title.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			},
            "Album Filter": {
				"terms": {
					"field": "album.keyword",
					"size": 10
				}
			},
            "Metaphor Filter": {
				"terms": {
					"field": "metaphor.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_best(query, sort_num, fields=['title','lyrics']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"year": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Title Filter": {
				"terms": {
					"field": "title.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			},
            "Album Filter": {
				"terms": {
					"field": "album.keyword",
					"size": 10
				}
			},
            "Metaphor Filter": {
				"terms": {
					"field": "metaphor.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

#cross_filds
def multi_match_agg_cross(query, fields=['title','lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Title Filter": {
				"terms": {
					"field": "title.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			},
            "Album Filter": {
				"terms": {
					"field": "album.keyword",
					"size": 10
				}
			},
            "Metaphor Filter": {
				"terms": {
					"field": "metaphor.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_year_range(query, year, fields=['year']):
	q = {
		"sort": [
			{"year": {"order": "desc"}},
		],
		"query": {
			# "multi_match": {
			# 	"query": query,
			# 	"fields": fields,
			# 	"operator": 'or',
			# 	"type": "cross_fields"
			# },
            "range": {
                "year": {
                    "gte": year[0],
                    "lt": year[1]
                }
            }
		},
		"aggs": {
			"Title Filter": {
				"terms": {
					"field": "title.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			},
            "Album Filter": {
				"terms": {
					"field": "album.keyword",
					"size": 10
				}
			},
            "Metaphor Filter": {
				"terms": {
					"field": "metaphor.keyword",
					"size": 10
				}
			}
            # "Year Filter": {
			#  	"terms": {
			#  		"field": "year.keyword",
			#  		"size": 10
			#  	}
			# }
		}
	}
	q = json.dumps(q)
	return q

def multi_match_agg_single_year(query, fields=['title','lyrics']):
	q = {
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			# "Title Filter": {
			# 	"terms": {
			# 		"field": "title.keyword",
			# 		"size": 10
			# 	}
			# },
			# "Lyricist Filter": {
			# 	"terms": {
			# 		"field": "lyricist.keyword",
			# 		"size": 10
			# 	}
			# },
			# "Artist Filter": {
			# 	"terms": {
			# 		"field": "artist.keyword",
			# 		"size": 10
			# 	}
			# },
			# "Lyrics Filter": {
			# 	"terms": {
			# 		"field": "lyrics.keyword",
			# 		"size": 10
			# 	}
			# },
            # "Album Filter": {
			# 	"terms": {
			# 		"field": "album.keyword",
			# 		"size": 10
			# 	}
			# },
            # "Metaphor Filter": {
			# 	"terms": {
			# 		"field": "metaphor.keyword",
			# 		"size": 10
			# 	}
			# }
            #"Year Filter": {
			#	"terms": {
			#		"field": "year.keyword",
			#		"size": 10
			#	}
			#}
		}
	}

	q = json.dumps(q)
	return q


# def multi_match_agg_sort_cross(query, year, fields=['year']):
# 	q = {
# 		"sort": [
# 			{"year": {"order": "desc"}},
# 		],
# 		"query": {
# 			"multi_match": {
# 				"query": query,
# 				"fields": fields,
# 				"operator": 'or',
# 				"type": "cross_fields"
# 			},
#             "range": {
#                 "published_date": {
#                     "gte": year[0],
#                     "lt": year[1]
#                 }
#             }
# 		},
# 		"aggs": {
# 			"Title Filter": {
# 				"terms": {
# 					"field": "title.keyword",
# 					"size": 10
# 				}
# 			},
# 			"Lyricist Filter": {
# 				"terms": {
# 					"field": "lyricist.keyword",
# 					"size": 10
# 				}
# 			},
# 			"Artist Filter": {
# 				"terms": {
# 					"field": "artist.keyword",
# 					"size": 10
# 				}
# 			},
# 			"Lyrics Filter": {
# 				"terms": {
# 					"field": "lyrics.keyword",
# 					"size": 10
# 				}
# 			},
#             "Album Filter": {
# 				"terms": {
# 					"field": "album.keyword",
# 					"size": 10
# 				}
# 			},
#             "Metaphor Filter": {
# 				"terms": {
# 					"field": "metaphor.keyword",
# 					"size": 10
# 				}
# 			}
#             # "Year Filter": {
# 			#  	"terms": {
# 			#  		"field": "year.keyword",
# 			#  		"size": 10
# 			#  	}
# 			# }
# 		}
# 	}
# 	q = json.dumps(q)
# 	return q


#phrase_filds
def multi_match_agg_phrase(query, fields=['title','song_lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Title Filter": {
				"terms": {
					"field": "title.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			},
            "Album Filter": {
				"terms": {
					"field": "album.keyword",
					"size": 10
				}
			},
            "Metaphor Filter": {
				"terms": {
					"field": "metaphor.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_phrase(query, sort_num, fields=['title','song_lyrics']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"year": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Title Filter": {
				"terms": {
					"field": "title.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			},
            "Album Filter": {
				"terms": {
					"field": "album.keyword",
					"size": 10
				}
			},
            "Metaphor Filter": {
				"terms": {
					"field": "metaphor.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

