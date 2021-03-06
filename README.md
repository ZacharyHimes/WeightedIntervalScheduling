# WeightedIntervalScheduling
 Project Devoper: Zachary Himes
 
 # Description:  
 Given a CSV file with lists of jobs in the format of {Starttime, Endtime, Duration}, the program can compute the best sequence of jobs with the most return of constant work hours. It outputs a nicely formatted list of the individual jobs and their corresponding information, along with the sorted CSV containing all jobs for reference. 
 
 # User Manual:
 To run this you should just be able to pull the repository and run it in IDLE (pythons, built in IDE). I utilized Python 3.9, with the Pycharm IDE from Jetbrains if you wish to do the same, if the file is not reading in terminal or Pycahrm then **youll NEED to run it in IDLE**, see https://www.python.org/downloads/ to download IDLE/python if you do not already have it. Make sure all CSV files are in the same folder as the main.py file. When you run the program, when prompted, enter the names of the three CSV files I have provided to test. 
 
 # Details of the Implementation:
This algorithm time complexity is analyzed as follows: Sorting by finish time:  O(n log n), Computing p[]:  O(n) after sorting. ComputeOpt(j):  each invocation takes O(1) time and either returns an existing value M[j] or stores a new value into M[j] and makes at most two recursive calls. So the overall run time since we are caching the recursive calls instead of letting them reside on the call stack is O(n). The piece of this that makes it a dynamic algorithm is that it goes through and computes values that we can use later. For instance, the list P[] is a prime example, as it computes the largest index that is not incompatible for every index or job in the list. This lets us recursively always go to the next sequentially compatible job.

# Testing explanation:
 I have three CSV files attached, two of which are pulled directily from the power point slides. The third is a randomly generated job list that can be used for additional testing.  
 ### Job.csv's visual represenation is as follows:
 <img width="1208" alt="JOBCSV-Example" src="https://user-images.githubusercontent.com/48925673/111559840-8005e180-874e-11eb-817c-640b263c30b1.png">  
As you can see the most profitable sequence of jobs based on weight is going to be Jobs {1, 3, 5} as labled on the diagram, which equates to a total weight of 9.

### Job2.csv's visual represenation is as follows:
<img width="1206" alt="Screen Shot 2021-03-17 at 6 42 54 PM" src="https://user-images.githubusercontent.com/48925673/111560850-a7f64480-8750-11eb-87ae-083ea09581c6.png">
As you can see the most profitable sequence of jobs based on weight is going to be Jobs {3,7} as labled on the diagram, which equates to a total weight of 10.  

### Job3.csv    
Most effecient string of colabrative jobs will be Jobs:    
* {7,10,3}      
* {6,7,1}    
* {4,6,2}   
* {2,4,2}   
* {0,2,2}  

## Running Screen Shots:  
### Job1.csv output:
![Job1 output](https://user-images.githubusercontent.com/48925673/111563800-e04c5180-8755-11eb-9352-d48abcd25ec6.png)
### Job2.csv output:
![Job2 output](https://user-images.githubusercontent.com/48925673/111563879-040f9780-8756-11eb-8a8d-ec365dc0333b.png)
### Job3.csv output:
![Job3 output](https://user-images.githubusercontent.com/48925673/111563911-138ee080-8756-11eb-9c48-ced9af07ee0d.png)

