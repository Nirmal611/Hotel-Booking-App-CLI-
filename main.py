import pandas as pd
from hotelclasses import User,Hotel

df = pd.read_csv('hotels.csv')
print(df)
df1 = pd.read_csv('users.csv')
print(df1)

user_id = int(input('Enter your id or enter 0 to register'))
if user_id == 0:
    user_id = df1.shape[0]+1
    name = input('Enter your name')
    birthyear = int(input('Enter your birth year'))
    user = User(name=name,birth_year=birthyear,user_id=user_id)
    new_user = {'user_id' : user_id,'name' : name,'birthyear' : birthyear}
    df1.loc[len(df1)] = new_user
    df1.to_csv('users.csv',index=False)

else:
    existing_user = df1.loc[df1['user_id']==user_id]
    name = existing_user['name'].squeeze()
    birthyear = existing_user['birthyear'].squeeze()
    name = existing_user['name'].squeeze()
    user = User(name=name, birth_year=birthyear, user_id=user_id)

while True:
    hotel_id = int(input('Enter the Hotel ID : '))
    hotel = Hotel(hotel_id=hotel_id)

    if hotel.available():
        hotel.book(user_id=user_id)
        print('hotel booked')
        break
    else :
        print('sorry that hotel has been booked !')