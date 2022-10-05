# Defining the arguments that we want to use in Grid Search along  
# with the list of values that we want to try out  
from tkinter import Y

learnRate = [0.001, 0.02, 0.2]
dropoutRate = [0.0, 0.2, 0.4]
batchSize = [10, 20, 30]
epochs = [1, 5, 10]

# Making a dictionary of the grid search parameters  
paramgrid = {'learnRate': learnRate, 'dropoutRate': dropoutRate, 'batch_size': batchSize, 'epochs': epochs}

# Building and fitting the GridSearchCV  
def GridSearchCV(estimator, param_grid, cv, verbose):
    pass


class KFold:
    pass


mygrid = GridSearchCV(estimator=GridSearchCV, param_grid=paramgrid, cv=KFold(random_state=None), verbose=10)


class X_stdized:
    pass


gridresults = mygrid.fit(X_stdized, Y)

# Summarizing the results in a readable format  
print("Best: " + gridresults.best_score_ + " using " + gridresults.best_params_)

means = gridresults.cv_results_['mean_test_score']
stds = gridresults.cv_results_['std_test_score']
params = gridresults.cv_results_['params']

for mean, stdev, param in zip(means, stds, params):
    print(mean + "(" + stdev + ")" + " with: " + param)  
