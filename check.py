 # api_key ='AIzaSyAu1vpmfXxqJ1sVpTQu-27Y36qu0KrCt3M'
        # url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
        # for iter in range(len(x)):
        #     source = (x[iter][0],x[iter][1])
        #     for iter2 in range(len(x)):
        #         dest = (x[iter2][0],x[iter2][1])
        #         r = requests.get(url + 'origins = ' +str(source[0])+","+str(source[1]) +'&destinations = ' + str(dest[0])+","+str(dest[1]) +'&key = ' + api_key+'&callback=?') 
        #         print(r.json())    
        
        # var rad = function(y) {
        #     return y * Math.PI / 180;
        # };

        # var getDistance = function(p1, p2) {
        #     var R = 6378137; 
        #     var dLat = rad(p2.lat() - p1.lat());
        #     var dLong = rad(p2.lng() - p1.lng());
        #     var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        #     Math.cos(rad(p1.lat())) * Math.cos(rad(p2.lat())) *
        #     Math.sin(dLong / 2) * Math.sin(dLong / 2);
        #     var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        #     var d = R * c;
        #     return d; // returns the distance in meter
        # };

        
      
        print("*****************************************************************")   
        for iter1 in range(len(x)):
            # source = (x[iter1][0],x[iter1][1])
            for iter2 in range(len(x)):

                R = 6373.0

                lat1 = x[iter1][0];
                lon1 = x[iter1][1];
                lat2 = x[iter2][0];
                lon2 = x[iter2][1];

                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = R * c

                print( distance)

                