def get_lat_long(place):

    if str(type(place)) == "<class 'str'>":
        import googlemaps
        gmaps = googlemaps.Client(key='AIzaSyDqtbRTxXbZhbNYah370N1_S6Be_2Y_mlc')

        geocode_result = gmaps.geocode(place)

        if geocode_result != []:

            return(geocode_result[0]['geometry']['location'])
        else:
            return({'lat': None, 'lng': None})
