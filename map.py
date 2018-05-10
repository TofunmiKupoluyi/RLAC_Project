import geopandas as gpd
import AnalyzeCSV as analysis

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world = world[['continent', 'geometry']]

continents = world.dissolve(by='continent')
continents['polarity']=analysis.getDiasporaSentiment('tweets-csv.csv')[0]
continents['polarity'][1]=0
continents['polarity'][7]=0
continents.loc[:,('polarity')][0] = analysis.getAfricanSentiment('tweets-csv.csv')[0]

print(continents)
continents.plot(column='polarity', cmap='OrRd')

import matplotlib.pyplot as plt
plt.show()
