import pandas as pd
from hotelclasses import User,Hotel

df = pd.read_csv('hotels.csv')

df1 = pd.read_csv('users.csv')

df2 = pd.read_csv('booker.csv')

hotel_id = int(input('Enter Hotel ID or enter 0 to register : '))

if hotel_id==0:
    hotel_id = df.shape[0]+1
    hotel_name = input('Enter hotel name : ')
    address = input('Enter hotel address : ')
    new_hotel = {'id':hotel_id, 'hotel_name':hotel_name, 'address': address, 'available':'yes'}
    df.loc[len(df)] = new_hotel
    print(df.loc[len(df)-1])
    df.to_csv('hotels.csv', index=False)
    hotel = Hotel(hotel_id=hotel_id)
    print('Successfully registered ! ')
    print('Your hotel ID is : '+str(hotel_id))
else :
    hotel = Hotel(hotel_id=hotel_id)

while True :
    choice = int(input('To Edit Hotel details Enter 1 '
                       '\nTo view booking status Enter 2'
                       '\nTo clear booking Enter 3 '
                       '\nTo exit enter 4 \n'))
    match choice:
        case 1 :
            hotel_name = input('Enter hotel name : ')
            address = input('Enter hotel address : ')
            df.loc[df['id'] == hotel_id, 'hotel_name'] = hotel_name
            df.loc[df['id'] == hotel_id, 'address'] = address
            df.to_csv('hotels.csv',index=False)
            df = pd.read_csv('hotels.csv')

        case 2 :
            availability = df.loc[df['id'] == hotel_id, 'available'].squeeze()
            if availability == 'yes':
                print('Hotel is not booked by anyone')
            else :
                print('Hotel is booked')
                booked_user = df2.loc[df2['hotel_id'] == hotel_id, 'user_id'].squeeze()
                booked_user = df1.loc[df1['user_id'] == booked_user]
                print('Name : ' + booked_user['name'].squeeze() +
                      '\nBirth Year : ' + str(booked_user['birthyear'].squeeze()))

        case 3 :
                hotel.clearbooking()
                df = pd.read_csv('hotels.csv')
                df2 = pd.read_csv('booker.csv')

        case 4 :
            break

