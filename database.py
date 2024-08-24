import pymongo
import os
def load_data():
    try:
        access_key = os.environ['mongodb_convo_ai']
        client = pymongo.MongoClient(access_key)

        mydb = client.assignment1

        news = mydb.news
        jobs = mydb.jobs
        last_update = mydb.last_update

        print("Connection Established Successfully!!")
    except:
        print("Couldnt establish connection...")
        return None, None, None

    print("Retrieving the data...")
    try:
        news_data = list(news.find())
        jobs_data = list(jobs.find())
        last_update = list(last_update.find())
    except:
        print("Data Retrieval Failed!!")
        return None, None, None
    print("Data Retrieval Successfull!!")
    return news_data, jobs_data, last_update
