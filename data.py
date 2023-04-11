
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:35:44 2023

@author: asma
"""
from pathlib import Path
import pandas as pd 
import scipy 
import scipy.sparse


#Define a function to load the csv file that contains the userID and the artistID 
#that the user has listened to and the number of times of the listens

def load_user_artist_file (user_artists_file: Path)-> scipy.sparse.csr_matrix:
    #define a dataframe to load the csv by pandas
    user_artist_df = pd.read_csv('/home/asma/Downloads/Melody Generation/music recommender last.fm/musiccollaborativefiltering-main/lastfmdata/user_artists.dat', sep='\t')
    user_artist_df.set_index(['userID', 'artistID'], inplace= True)
    coo = scipy.sparse.coo_matrix(
        
        (
            user_artist_df.weight.astype(float),
            (
               user_artist_df.index.get_level_values(0),
               user_artist_df.index.get_level_values(1)
                )
            )
        
        
        )
    
    return coo.tocsr()

#Function (2): we will need to retrieve artist name
#(A)Define an empty dataframe to store the content of the csv that has the artists names
#(B) Empty the content from csv to empty fataframe
#(c) retrieve artist name with their unique 'id'

class ArtistNameRetriever:
    
    def __init__ (self):
     self._artist_df = None
    
    def artist_file_loader(self, artist_file:Path):
     artist_df_load= pd.read_csv(artist_file, sep='\t')
     artist_df_load = artist_df_load.set_index('id')
     self._artist_df = artist_df_load

    def artist_name_retriever(self, artist_id:int)->str:
     return self._artist_df.loc[artist_id, "name"]
     


# to test the functions, we implement this script:
    
if __name__ == '__main__':
    retrieve_artist = ArtistNameRetriever()
    retrieve_artist.artist_file_loader(Path('/home/asma/Downloads/Melody Generation/music recommender last.fm/musiccollaborativefiltering-main/lastfmdata/artists.dat'))
    artist = retrieve_artist.artist_name_retriever(5)
    print (artist)
    
    
    '''user_artist_file_loader = load_user_artist_file(Path('/home/asma/Downloads/Melody Generation/music recommender last.fm/musiccollaborativefiltering-main/lastfmdata/user_artists.dat')
     )
    
print (user_artist_file_loader) '''                                            
                                                    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    