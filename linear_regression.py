import numpy as np
import pandas



def normalize_features(df):
    """
    Normalize the features in the data set.
    """
    mu = df.mean()
    sigma = df.std()
    
    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                         "not be normalized. Please do not include features with only a single value " + \
                         "in your model.")
    df_normalized = (df - df.mean()) / df.std()

    return df_normalized



def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    """
    
    m = len(values)
    
    for i in range(num_iterations):
    
        predicted_values = np.nan_to_num(np.dot(features,theta))
        
        theta = theta - (float(alpha)/float(m))*np.dot((predicted_values - values),features)
        theta = np.nan_to_num(theta)
        # your code here
    return theta

def predictions(dataframe):
    
    # Select Features (try different features!)
    features = dataframe[['Pclass', 'Age', 'Fare', 'SibSp']]
    
    # Add SEX to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['Sex'], prefix='unit')
    features = features.join(dummy_units)
    # Values
    
    values = dataframe['Survived']
    m = len(values)
    
    
    features = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)
    
    # Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to change this value
    num_iterations = 100 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent= gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    


    predictions = np.nan_to_num(np.dot((features_array),(theta_gradient_descent)))
    return predictions
    
dataframe = pandas.read_csv("C:\\Users\\Keshav Vinayak Jha\\Desktop\\Programs\\UdacityResources\\titanic_data.csv")
p= predictions(dataframe)
values = np.array(dataframe['Survived'])
for i in xrange(len(p)):
    if(p[i] > 1):
        p[i] = 1
    if(p[i] < 0):
        p[i] = 0
    p[i] = "%.2f" % p[i]

k = values - p


m = 0
for i in k:
    if i < 0:
        i = (-1)*i
        
    m += i
m = 1-m/len(k)
print "this model was able to predict survival of a passenger to a {}% accuracy".format(m*100)
