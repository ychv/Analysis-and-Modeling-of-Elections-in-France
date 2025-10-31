import pandas as pd

path = "../Data/data_merged_20250922.parquet" # path to Data file (in repo parent folder)

# data = pd.read_parquet(path,engine='fastparquet')
# print(data)

def importCommuneData(postcode,feature_list = None): # Create a datapoint for a specific commune by merging all the available data on this commune

    path = "../Data/data_merged_20250922.parquet" # path to Data file (in repo parent folder)
    col = None
    if feature_list is not None:
        col = ["codecommune"] + feature_list

    sel = [("codecommune","==",str(postcode))]
    data = pd.read_parquet(path,engine='pyarrow',columns = col,filters=sel)

    return data

    # path = "../Data/" # path to Data folder (in repo parent folder)
    # vect = pd.DataFrame({'code' : postcode},index=[0])

    # # Age
    # folder_path = path + 'Age_csv/'
    # data = pd.read_csv(folder_path + 'agesexcommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'menagescommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Alphabetisation
    # file_path = path + 'Alphabetisation_csv/alphabetisationcommunes.csv'
    # data = pd.read_csv(file_path,index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Capital Immobilier
    # folder_path = path + 'Capital_immobilier_csv/'
    # data = pd.read_csv(folder_path + 'basesfiscalescommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'capitalimmobiliercommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)
    
    # data = pd.read_csv(folder_path + 'isfcommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'terrescommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Catégories socio professionnelles
    # folder_path = path + 'CSP_csv/'
    # data = pd.read_csv(folder_path + 'crimesdelitscommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)
    
    # data = pd.read_csv(folder_path + 'cspcommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'empfoncommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'emploicommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'rsacommunes.csv', index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Diplomes
    # file_path = path + 'Diplomes_csv/diplomescommunes.csv'
    # data = pd.read_csv(file_path,index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Enseignement privé et religion

    # # Législatives

    # # Nationalités
    # folder_path = path + 'Nationalites_csv/'
    # data = pd.read_csv(folder_path + 'etrangerscommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # data = pd.read_csv(folder_path + 'naticommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)
    
    # # Présidentielles

    # # Propriétaires
    # file_path = path + 'Proprietaires_csv/proprietairescommunes.csv'
    # data = pd.read_csv(file_path,index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Referundum

    # # Revenus
    # folder_path = path + 'Revenus_csv/'
    # data = pd.read_csv(folder_path + 'pibcommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)
    
    # data = pd.read_csv(folder_path + 'revcommunes.csv',index_col=False)
    # data = data.loc[data['codecommune'] == postcode]
    # vect = pd.concat([vect, data[[key for key in data.columns if key not in ['dep', 'nomdep', 'nomcommune']]]],axis=1)

    # # Taille communes et agglomération


    # return vect