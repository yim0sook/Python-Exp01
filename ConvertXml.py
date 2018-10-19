from xml.dom import minidom

xmldoc = minidom.parse("kml.kml")  # this line read whole xml document kml.kml ( kml is after ?xml tag name)

kml = xmldoc.getElementsByTagName("kml")[0]  # retuns the list of all tags matched with kml tag name, 0 is to get the first element

document = kml.getElementsByTagName("Document")[0] # to get the Document tag under knml tag, use the exact tag name

placemarks = document.getElementsByTagName("Placemark")   #extract DOM objects

for placemark in placemarks:
    desc = placemark.getElementsByTagName("description")[0].firstChild.data  # to get the descriptoin tag
                                                   # firstChild.data give all data under description tag
    lst = desc.split(":")  # split the data by : lst[0] before : lst[1] after :
    population = int(lst[1].split("<")[0])
    coords = placemark.getElementsByTagName("coordinates")[0].fisrtChild.data # to get the latitude
    lst2 = coords.split(",")
    longitude = float(lst2[0])
    latitude = float(lst2[1])

    cityName = placemark.getElementsByTagName("name")[0].firstChild.data

    print(cityName +  ":", -longitude, latitude, population)


