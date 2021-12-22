# Password classification
##Goal
The task was to classify password strength (3 classes: weak, medium, strong) using data from 000webhost leak that is available
online.

### The model performance
After experimenting with models (file PasswordClassificationExperiments.ipynb), XGBoostCLassifier was chosen as final decision, which gave the best AUC score 0.9994 (other metrics of that and other models can be found in notebook).

### How to predict classes of your data
1.Clone the repository
    
`git clone --recurse-submodules https://github.com/OvsiienkoVladyslava/password_classification.git`  

2.Make sure that you fulfill all the requirements in requirements.txt
 
`pip install -r requirements.txt`

3.Classifier can be run on most data formats (e.g. .txt). 
Each password must start on a new line in source file, like below:   
   
source.txt:       
password1                              
adskd123                        
67fdfj

4.Parameters:    
--source  - path to the file with passwords;   
--save-file - 1 - save file of predictions in 'save-path' (file name will be'predictions.csv'), 0 - print predictions in terminal;   
--save-path - where to save results, e.g. D:/results (without / in the end!), default path is '.'.

Example (save results in project directory):     
`$ python classify.py --source source.txt --save-file 1 `
