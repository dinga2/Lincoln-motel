import csv
import os

# The django script needs to initialize the django configuration first
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_booking_sys.settings")
django.setup()

from app.models import Hotel, Country, City, HotelChain, HotelBrand

hotels_file = 'hotels.csv'
hotels_img_file = 'hotel_img.csv'


def import_hotel():
    with open(hotels_file, 'r') as f:
        rv = csv.reader(f)  # Using the CSV module to read CSV files
        header = rv.__next__()
        for row in rv:
            # Assemble CSV data into a dictionary for easy future use
            hotel_data = {header[i]: row[i] for i in range(len(row))}
            # Using get_ Or_ The create method retrieves the object, otherwise it is created.
            country, _ = Country.objects.get_or_create(
                name=hotel_data['country'],
                defaults={
                    'country_code': hotel_data['countrycode']
                }
            )
            city, _ = City.objects.get_or_create(
                name=hotel_data['city'],
                defaults={
                    'country': country
                }
            )

            # Create or update hotel objects
            hotel, _ = Hotel.objects.update_or_create(
                name=hotel_data['name'],
                defaults={
                    'address': hotel_data['address'],
                    'email': hotel_data['email'],
                    'website': hotel_data['website'],
                    'tel': hotel_data['tel'],
                    'postcode': hotel_data['postcode'],
                    'latitude': hotel_data['latitude'],
                    'longitude': hotel_data['longitude'],
                    'star': hotel_data['star'],
                    'city': city,

                }
            )
            if hotel_data['chainname']:
                chain, _ = HotelChain.objects.get_or_create(
                    name=hotel_data['chainname']
                )
                hotel.chain = chain

            if hotel_data['brandname']:
                brand, _ = HotelBrand.objects.get_or_create(
                    name=hotel_data['brandname']
                )
                hotel.brand = brand

            hotel.save()

if __name__ == '__main__':
    import_hotel()
