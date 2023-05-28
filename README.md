# Building-a-Recommender-System
The Movie Recommender System allows users to input a movie (with the release year) and receive several recommendations that are close in rating with that movie.

## Installation

No installation needed.

## Usage

Import CSVs that include movie titles and movie ratings on 0.0-5.0 scale. I used the files movies.csv and ratings.csv obtained from ml-latest-small.

```python
import numpy as np
import pandas as pd

# Creating the recommender system encouraging user input.
foobar.pluralize('word')

while True:
    entrance = input("Would you like to look up movie ratings? Enter 'Y' to continue or any key to exit: ")
    # The loop will run if the user inputs 'Y' and accepts lowercase y as well. Anything else breaks the loop.
    if entrance.upper() == 'Y':
        # Movie input.
        input_movie = input("Please enter which movie you would like the ratings for. Be sure to enter the year: ")
        # If the movie is in the set, it will generate a list. If it is not, it will prompt a user to input another movie.
        if input_movie in movies_df['title'].tolist():
            # Used previous code but created a new data frame with it.
            correlations1 = df_new.corrwith(df_new[input_movie])
            recommend1 = pd.DataFrame(correlations1,columns=['Correlation'])
            recommend1.dropna(inplace=True)
            recommend1 = recommend1.join(avg_ratings['Total Ratings'])
            recc1 = recommend1[recommend1['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()
            recc1 = recc1.merge(movies_df,on='title', how='left')
            print(recc1.head(10))
        else:
            print("That movie is not in the dataset. Please try again.")
    else:
        print("Thank you for using the Movie Recommender System!")
        break
```
