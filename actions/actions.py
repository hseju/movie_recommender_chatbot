# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .app import get_movies
import pandas as pd
import pickle


movies_df = pd.read_csv("movies_df.csv", encoding="unicode_escape", index_col=0)
posters_df = pd.read_csv("Posters.csv",encoding="unicode_escape", index_col=0)

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        result =get_movies(tracker.get_slot('movie'))
        print(result)
        get_imdb_score = posters_df[posters_df['title'].isin(result)]['IMDB Score'].to_list()
        get_poster = posters_df[posters_df['title'].isin(result)]['Poster'].to_list()

        print(get_imdb_score)
        print(get_poster)
        output = ""
        for items in result:
            output = output + items + f"\n"
            
        # dispatcher.utter_message(text=str(output)+ f"\n")
      

        movie_carousel = {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [{
                "title": result[0],
                "subtitle": "IMDb: " + str(get_imdb_score[0]),
                "image_url": get_poster[0],
                "buttons": [{
                    "title": result[0],
                    "url": "http://link.url",
                    "type": "web_url"
                },
                    {
                        "title": "Description",
                        "type": "postback",
                        "payload": "/greet"
                    }
                ]
            },
                {
                    "title": result[1],
                    "subtitle": "IMDb: " + str(get_imdb_score[1]),
                    "image_url": get_poster[1],
                    "buttons": [{
                        "title": result[1],
                        "url": "http://link.url",
                        "type": "web_url"
                    },
                        {
                            "title": "Description",
                            "type": "postback",
                            "payload": "/greet"
                        }
                    ]
                },

                {
                    "title": result[2],
                    "subtitle": "IMDb: " + str(get_imdb_score[2]),
                    "image_url": get_poster[2],
                    "buttons": [{
                        "title": result[2],
                        "url": "http://link.url",
                        "type": "web_url"
                    },
                        {
                            "title": "Description",
                            "type": "postback",
                            "payload": "/greet"
                        }
                    ]
                },


                {
                    "title": result[3],
                    "subtitle": "IMDb: " + str(get_imdb_score[3]),
                    "image_url": get_poster[3],
                    "buttons": [{
                        "title":  result[3],
                        "url": "http://link.url",
                        "type": "web_url"
                    },
                        {
                            "title": "postback name",
                            "type": "postback",
                            "payload": "/greet"
                        }
                    ]
                },


                {
                    "title": result[4],
                    "subtitle": "IMDb: " + str(get_imdb_score[4]),
                    "image_url": get_poster[4],
                    "buttons": [{
                        "title": "Link name",
                        "url": "http://link.url",
                        "type": "web_url"
                    },
                        {
                            "title": "postback name",
                            "type": "postback",
                            "payload": "/greet"
                        }
                    ]
                }


               
            ]
        }
    }
        dispatcher.utter_message(attachment=movie_carousel)

          
        dispatcher.utter_message(text="Did you find it helpful?")

        return []
