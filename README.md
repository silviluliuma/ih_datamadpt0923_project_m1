<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __biciMAD-worker Ironhack Project Module 1__

biciMAD-worker provides biciMAD workers with an optimized route between the high and low populated biciMAD stations with the aim of solving one of the biggest problems of the platform: the redistribution of bikes along the different stations. 

## **Status**

biciMAD-worker is project for the Ironhack Data Analysis Bootcamp (Madrid 2023)

## **Additional info:**

This apps uses the biciMAD API to take real-time information about the biciMAD stations and uses a function to repeatedly calculate the nearest low or high populated station (depending on the particularities of the route and the inputs from the worker).

The app will ask the worker for three inputs:

1. **What district have you been assigned today?** The input here will be one of the 21 districts that exist in Madrid (f.e. 20). 

2. **Is this your initial route? If not, enter your actual coordinates:** The input here will be either "yes", in which case the route will start in the EMT Central (where the vans are stored) or a list of coordinates provided to them by the app (usually when the worker is assigned another district because they have completed their first). In this case, the route will take as a start point the coordinates provided. 

3. **Is your van empty or full?** The input here will be either "empty" or "full", depending of the status of the last station visited by the worker on the route. If the last station was a high populated one, the worker will have to take the spare bikes on the van and will start the next route with them, and so the first stop of the next route will be a low populated station. On the contrary, if the last station was a low populated one, the worker will have an empty van and so the first stop of the next route will be a high populated station. The same will happen if it is the first route of said worker.

## **Tablet of contents**

```

└── project
    ├── __wip__
    ├── data
    ├── maps #maps generated with the app as an example
        └──ROUTE_MAP_20_DISTRICT.html
        └──ROUTE_MAP_21_DISTRICT.html
    ├── raw #raw data corresponding to the main challenge of the project (not biciMAD-worker)
        └──bicimad_stations.csv
        └──bicipark_stations.csv
    ├── results #results corresponding to the main challenge of the project (not biciMAD-worker)
        └──BICIMAD_ONE_RESULT.csv
        └──BICIMAD_PARKING_RESULT.csv
    ├── modules
        └──api.py #module corresponding to the main challenge of the project (not biciMAD-worker)
        └──argparse_route.py
        └──argparse.py #module corresponding to the main challenge of the project (not biciMAD-worker)
        └──functions.py # module corresponding to the main challenge of the project (not biciMAD-worker)
        └──route.py
    ├── notebooks
    │   ├── dev_api.ipynb
    │   └── dev_bicimad.ipynb
        └── dev_bicipark.ipynb
        └── dev_notebook.ipynb
        └── dev_occupation.ipynb
        └── dev_route.ipynb
    ├── .env
    │  
    └── .gitignore
    └── LICENSE
    └── main.py
    └── README.md
    └── route_main.py

```
## **Technical information**

You can use the code of biciMAD-worker, as long as you give autorship credits. 

You have to clone this github repository in your local. 

You will need to install the following:

    -Pandas
    -Requests
    -Json
    -Folium
    -Openrouteservice
    -Geopy

## **Inspiration**

This project arises from the existing complaints from the biciMAD users regarding the redistribution of bikes along the stations. During the workday, stations close to business areas use to be completely full (people go to work cycling), leaving the station of the residential areas empty. This is an attempt, not only to solve the users problem, but also to solve and improve the workers situation.

## **Things to improve**

In the future, the project would need to take in consideration the actual capacity of the van. If the van is completely empty, then the app should only search for high populated stations. If the van has bikes but there is still space, then the app could search for both high and low populated stations. At least, if the van is completely full, the app should only search for low populated stations. The status of the van should be updated with every interaction. This would improve the optimization of the route.

## **Contact**

You can contact me here: valeromsilvia@gmail.com














 


 

