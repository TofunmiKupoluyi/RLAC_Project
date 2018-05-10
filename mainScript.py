import requests, base64, AnalyzeCorpusSentiment, csv


def writeToFile(tweet, location, entities, sentiment):
    fileOutput = csv.writer(open("tweets-csv.csv", "a"))
    fileOutput.writerow([tweet, location, entities, sentiment])

def analyzeEntities(entities):
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
    entityArray = []
    for entity in entities.entities:
        if(entity.type== 1 or entity.type== 2 or entity.type == 4):
            entityArray.append(entity.name)
    return entityArray
def main():
    # OAUTH PARAMETERS
    consumerKey = b'[YOUR_CONSUMER_KEY]'
    consumerSecret = b'[YOUR_CONSUMER_SECRET]
    encodedKeyB64 = base64.b64encode(consumerKey+b":"+consumerSecret)
    encodedKeyToString = str(encodedKeyB64)[2:len(str(encodedKeyB64))-1]
    headers = {'Authorization': "Basic "+encodedKeyToString, 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
    payload = {'grant_type': 'client_credentials'}

    # OAUTH TOKEN
    r = requests.post("https://api.twitter.com/oauth2/token", headers=headers, data=payload)
    accessToken = r.json()['access_token']
    currentLatestTweet = ""
    while(True):
        # SEARCH

        headers ={'Authorization': 'Bearer '+accessToken}
        r = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=buhari&tweet_mode=extended&result_type=recent", headers=headers)
        try:
            topStatus = r.json()['statuses'][0]
            print(topStatus)
            if('retweeted_status' in topStatus):
                fullText = topStatus['retweeted_status']['full_text']
            else:
                fullText = r.json()['statuses'][0]['full_text']
            
            
            
            if not (fullText == currentLatestTweet):
                currentLatestTweet = fullText
                if(topStatus['user']['time_zone']):
                    location = topStatus['user']['time_zone']
                else:
                    location= "Not Available"
                

                # sentimentCall = requests.post("http://text-processing.com/api/sentiment/", data={'text': fullText})
                # print(sentimentCall.json())
                print(topStatus['user']['time_zone'])
                writeToFile(fullText, location, str(AnalyzeCorpusSentiment.analyze(fullText)[0].document_sentiment.score), analyzeEntities(AnalyzeCorpusSentiment.analyze(fullText)[1]))
                
        except:
            pass
        

        

main()
