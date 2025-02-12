<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __biciMAD-worker Ironhack Project Module 1__

biciMAD-worker provides an optimized route between high and low-populated biciMAD stations, aiming to solve one of the platform's biggest problems: the **redistribution** of bikes among various stations.

![Captura de pantalla 2023-11-22 a las 16 35 55](https://github.com/silviluliuma/ih_datamadpt0923_project_m1/assets/138609959/4add47cd-53ff-4b07-9463-e03914177fd5)


## **Status**

biciMAD-worker is python based project for the Ironhack Data Analysis Bootcamp (Madrid 2023)

## **Additional info:**

This app utilizes the biciMAD API to gather **real-time information** about biciMAD stations. It employs a function to consistently calculate the nearest low or high-populated station, depending on the route's characteristics and input from the worker.

The app prompts the worker for three inputs:

**1. What district have you been assigned today?** The worker inputs one of the 21 districts in Madrid, for example, 20.

**2. Is this your initial route? If not, enter your current coordinates:** The worker responds with either "yes," starting the route at EMT Central, or provides a list of coordinates received from the app, typically when reassigned to a different district. In the latter case, the route begins at the specified coordinates.

**3. Is your van empty or full?** The worker selects either "empty" or "full," based on the last station visited. If the last station was high-populated, the worker loads spare bikes onto the van, and the first stop of the next route is a low-populated station. Conversely, if the last station was low-populated, the worker starts the next route with an empty van, and the first stop is a high-populated station. The same applies to the worker's first route.

<img width="587" alt="Captura de pantalla 2023-11-22 a las 19 25 08" src="https://github.com/silviluliuma/ih_datamadpt0923_project_m1/assets/138609959/39526901-5afb-4be3-a587-70e537db7455">


## **Tablet of contents**

```

└── project
    ├── __wip__
    ├── data
        └──maps (biciMAD-worker)
            └──ROUTE_MAP_20_DISTRICT.html
            └──ROUTE_MAP_21_DISTRICT.html
        ├── raw 
            └──bicimad_stations.csv
            └──bicipark_stations.csv
        ├── results 
            └──BICIMAD_ONE_RESULT.csv
            └──BICIMAD_PARKING_RESULT.csv
    ├── modules
        └──api.py 
        └──argparse_route.py (biciMAD-worker)
        └──argparse.py 
        └──functions.py 
        └──route.py (biciMAD-worker)
    ├── notebooks
        ├── dev_api.ipynb
        └── dev_bicimad.ipynb
        └── dev_bicipark.ipynb
        └── dev_notebook.ipynb
        └── dev_occupation.ipynb (biciMAD-worker)
        └── dev_route.ipynb (biciMAD-worker)
    ├── .env 
    └── .gitignore
    └── LICENSE
    └── main.py
    └── README.md
    └── route_main.py (biciMAD-worker)

```
## **Technical information**

You can use the code of biciMAD-worker, as long as you give **autorship credits**. 

Please, clone this GitHub repository to your local machine.

You will need to install the following:

    * Pandas
    * Requests
    * Json
    * [Folium](https://python-visualization.github.io/folium/latest/getting_started.html)
    * [Openrouteservice](https://openrouteservice.org/)
    * Geopy

## **Inspiration**

This project addresses the frequent complaints from biciMAD users concerning the **uneven distribution** of bikes among the stations. Throughout the workday, stations near business areas tend to become completely full due to people cycling to work, while stations in residential areas are left empty. This initiative is not only an attempt to resolve user issues but also **aims to enhance the working conditions for the employees involved**.

## **Things to improve**

In the future, the project will need to consider the **current capacity of the van**. If the van is entirely empty, the app should exclusively search for high-populated stations. If the van has bikes but still has space, the app could search for both high and low-populated stations. However, if the van is completely full, the app should focus solely on low-populated stations. The status of the van should be updated with every interaction, contributing to the continuous optimization of the route.

Also, it would be nice to use the spectacular **VROOM project** (https://github.com/VROOM-Project/vroom), which has an awesome optimization route system that allows pickups and deliveries and takes into account the time used by each worker to complete their tasks. This would offer a whole new set of possibilities.

## **Contact**

You can contact me here: valeromsilvia@gmail.com

![tumblr_otvsbuaaRF1vha0yxo5_r1_250](https://github.com/silviluliuma/ih_datamadpt0923_project_m1/assets/138609959/f597f7de-0741-4079-a9ac-a94b92359e8a)
