from dataImport import *

feature_list = ['pvoteppar','pvotepvoteG','pvotepvoteC','pvotepvoteD','agesexcommunes/perage_rank']

data = importCommuneData(95625,feature_list)

print(data)