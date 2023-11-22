<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __biciMAD-worker Ironhack Project Module 1__

biciMAD-worker provides biciMAD workers with an optimized route between the high and low populated biciMAD stations with the aim of solving one of the biggest problems of the platform: the redistribution of bikes along the different stations. 

![Captura de pantalla 2023-11-22 a las 16 35 55](https://github.com/silviluliuma/ih_datamadpt0923_project_m1/assets/138609959/8ca0cfad-55d2-4b60-a1d0-b1d4dafc7dd4)


## **Additional info:**

The app will ask the worker for three inputs:

1. **What district have you been assigned today?** The input here will be one of the 21 districts that exist in Madrid (f.e. 20). 

2. **Is this your initial route? If not, enter your actual coordinates:** The input here will be either "yes", in which case the route will start in the EMT Central (where the vans are stored) or a list of coordinates provided to them by the app (usually when the worker is assigned another district because they have completed their first). In this case, the route will take as a start point the coordinates provided. 

3. **Is your van empty or full?** The input here will be either "empty" or "full", depending of the status of the last station visited by the worker on the route. If the last station was a high populated one, the worker will have to take the spare bikes on the van and will start the next route with them, and so the first stop of the next route will be a low populated station. On the contrary, if the last station was a low populated one, the worker will have an empty van and so the first stop of the next route will be a high populated station. The same will happen if it is the first route of said worker.

<img width="587" alt="Captura de pantalla 2023-11-22 a las 19 25 08" src="https://github.com/silviluliuma/ih_datamadpt0923_project_m1/assets/138609959/368e3454-06ef-4397-a403-bf19a183100f">


## **Main Challenge:**

You must create a Python App (**Data Pipeline**) that allow their potential users to find the nearest BiciMAD station to a set of places of interest using the methods included in the module `geo_calculations.py`. The output table should look similar to:

| Place of interest | Type of place (*) | Place address | BiciMAD station | Station location |
|---------|----------|-------|------------|----------|
| Auditorio Carmen Laforet (Ciudad Lineal)   | Centros Culturales | Calle Jazmin, 46 | Legazpi | Calle Bolívar, 3 |
| Centro Comunitario Casino de la Reina | Centros municipales de enseñanzas artísticas | Calle Casino, 3 | Chamartin | Calle Rodríguez Jaén, 40 |
| ...     | ...            | ...        | ...      | ...        |
> __(*)__ This correspond to the type of place assigned to you. 


**Your project must meet the following requirements:**

- It must be contained in a GitHub repository which includes a README file that explains the aim and content of your code. You may follow the structure suggested [here](https://github.com/potacho/data-project-template).

- __It must create, at least, a `.csv` file including the requested table (i.e. Main Challenge).__ Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 

- It must provide, at least, two options for the final user to select when executing using `argparse`: **(1)** To get the table for every 'Place of interest' included in the dataset (or a set of them), **(2)** To get the table for a specific 'Place of interest' imputed by the user.


**Additionally:**

- You must prepare a 4 minutes presentation (ppt, canva, etc.) to explain your project (Instructors will provide further details about the content of the presentation).

- The last slide of your presentation must include your candidate for the **'Ironhack Data Code Beauty Pageant'**. 


---

### **Bonus 1:**

You may include in your table the availability of bikes in each station.

---

### **Bonus 2:**

You may improve the usability of your app by using [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/).

---

### **Bonus 3:**

Feel free to enrich your output data with any data you may find relevant (e.g.: wiki info for every place of interest) or connect to the [BiciMAD API](https://mobilitylabs.emtmadrid.es/) and update bikes availability realtime or find a better way to calculate distances...there's no limit!!!

--- 


## **Project Main Stack**

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.9/library/argparse.html)












 


 

