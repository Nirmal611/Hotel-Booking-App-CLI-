import pandas as pd

df = pd.read_csv('hotels.csv')

df1 = pd.read_csv('users.csv')

df2 = pd.read_csv('booker.csv')

class User:
    def __init__(self, name, birth_year, user_id):
        self.name = name
        self.birth_year = birth_year
        self.user_id = user_id

    def get_name(self):
        return self.name.upper()

    def age(self, current_year=2024):
        age = current_year - self.birth_year
        return age


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id

    def book(self, user_id):
        df.loc[df['id'] == self.hotel_id,'available'] = 'no'
        df.to_csv('hotels.csv', index=False)
        df2.loc[df2['hotel_id']==self.hotel_id , 'user_id'] = user_id
        df2.to_csv('booker.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id,'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    def clearbooking(self):
        df2.loc[df2['hotel_id'] == self.hotel_id, 'user_id'] = 0
        df.loc[df['id'] == self.hotel_id , 'available'] = 'yes'
        df2.to_csv('booker.csv',index=False)
        df.to_csv('hotels.csv',index=False)

class Spa(Hotel):
    def __init__(self,hotel_id,spa='no'):
        super().__init__(hotel_id)
        self.spa = spa



