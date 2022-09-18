import requests
import environ
import pprint
import json
import asyncio  
import aiohttp

from api.models import BatchRunModel
from django.core.cache import cache

env = environ.Env();

def get_results(word):
    res = requests.post(
        env("RAPI_URL"),
        data = {
            "text" : word
        },
        headers={
            "X-RapidAPI-Key" : env("RAPI_KEY")
        }
    )
    return json.loads(res.content)['categories']


def fetch_and_store_keywords(queries, batch_id):

    print(f"\n\nFetching categories for Batch Run : {batch_id}")

    results = {}

    def print_iter(iter, word):
        print(f"Fetched result for query[{iter}] - {word}")

    async def getResponse(session, index, word):

        cache_result = cache.get(word)

        if(cache_result != None):
            results[index] = cache_result
            print_iter(index, word);
            return
        
        async with session.post(env("RAPI_URL"),data = {"text" : word},headers={"X-RapidAPI-Key" : env("RAPI_KEY")}, ssl=False) as response:

            categories = json.loads((await response.text()))

            if(categories["categories"]): categories = categories["categories"]
            else: categories = []

            cache.set(word, categories)
            
            results[index] = categories
            print_iter(index, word);
            

    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = [getResponse(session, i, w) for i, w in enumerate(queries)] # create list of tasks
            await asyncio.gather(*tasks) # execute them in concurrent manner

    asyncio.new_event_loop().run_until_complete(main())

    print(f"Obtained all results for Batch Run : {batch_id}\n\n")

    BatchRunModel.objects.filter(id=batch_id).update(results = json.dumps(results), done=True);

                    


