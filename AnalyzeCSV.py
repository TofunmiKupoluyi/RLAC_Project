import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim()


def getAfricanSentiment(pathToCSVFile):
    csvFile = csv.reader(open(pathToCSVFile,"r", encoding='latin-1'), dialect='excel')
    numberFromAfrica = 0
    totalSentiment = 0
    averageAfricanSentiment = 0
    for i in csvFile:
        if("Africa" in i[1] or (i[1]=="Not Available")):
            totalSentiment = totalSentiment+float(i[2])
            numberFromAfrica = numberFromAfrica+1

    averageAfricanSentiment = totalSentiment/numberFromAfrica
    print(averageAfricanSentiment*100)
    return averageAfricanSentiment*-100, totalSentiment, numberFromAfrica

def getDiasporaSentiment(pathToCSVFile):
    csvFile = csv.reader(open(pathToCSVFile,"r", encoding='latin-1'), dialect='excel')
    numberFromDiaspora = 0
    totalSentiment = 0
    averageDiasporaSentiment = 0
    for i in csvFile:
        if(not ("Africa" in i[1]) and not(i[1]==' location' or i[1]=='Not Available')):
            # if(geolocator.geocode(i[1])):
            #     rawResponse=geolocator.geocode(i[1], language='en').raw
            #     location = geolocator.reverse([rawResponse['lat'], rawResponse['lon']], language='en')
            #     print(location.raw['address']['country'])
            totalSentiment = totalSentiment+float(i[2])
            numberFromDiaspora = numberFromDiaspora+1

    averageDiasporaSentiment = totalSentiment/numberFromDiaspora
    print(averageDiasporaSentiment*100)
    return averageDiasporaSentiment*-100, totalSentiment, numberFromDiaspora

