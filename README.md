<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __biciMAD-worker Ironhack Project Module 1__

biciMAD-worker provides biciMAD workers with an optimized route between the high and low populated biciMAD stations with the aim of solving one of the biggest problems of the platform: the redistribution of bikes along the different stations. 

## **Additional info:**

The app will ask the worker for three inputs:

1. **What district have you been assigned today?** The input here will be one of the 21 districts that exist in Madrid (f.e. 20). 

2. **Is this your initial route? If not, enter your actual coordinates:** The input here will be either "yes", in which case the route will start in the EMT Central (where the vans are stored) or a list of coordinates provided to them by the app (usually when the worker is assigned another district because they have completed their first). In this case, the route will take as a start point the coordinates provided. 

3. **Is your van empty or full?** The input here will be either "empty" or "full", depending of the status of the last station visited by the worker on the route. If the last station was a high populated one, the worker will have to take the spare bikes on the van and will start the next route with them, and so the first stop of the next route will be a low populated station. On the contrary, if the last station was a low populated one, the worker will have an empty van and so the first stop of the next route will be a high populated station. The same will happen if it is the first route of said worker.












 


 

