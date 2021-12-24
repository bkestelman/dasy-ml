# synthetic-data
Generate synthetic data with desired statistical properties. Intended for machine learning research.

## Introduction
When researching machine learning algorithms, we often want to know how they behave on data with specific properties. For example: linearly separable, correlated, isotropic, etc. This library aims to provide functionality to construct synthetic datasets with any desired statistical properties, so researchers can easily study how algorithms respond to different types of data. 

Why is this useful for machine learning research compared to using existing datasets?
- Existing datasets may lack certain statistical properties you want to test your algorithm against.
- You may not have enough information about where an existing dataset comes from. For example, is it IID?
- You may want to test against many different types of data. 
- You may want to arbitrarily adjust the size of the dataset. 

Note: this is not a library for adding synthetic data to an existing dataset - there are already many other libraries that do this. 

## DataGenerators and Labelers 
The core of synthetic-data are DataGenerators and Labelers. 

DataGenerators sample inputs X from the feature-space. 

Labelers take inputs X and assign labels y to them. 

These are very general classes. The procedure for creating X typically involves sampling from some probability distribution. Assigning labels may be a deterministic or probabilistic function. Each x or y may be created independently but does not have to be, for example if created through a Markov process.

## Discussion of Kinds of Data

### Independent vs. Non-Independent Data

### Time-Series Data

### Data for Classification Problems

#### Deterministic vs. Probabilistic Labels
If for any given input x, the label must always be a specific value, then the labels are deterministic. In other words, the label y=f(x), where f is a pure function. Typically, y is encoded as a one-hot vector. 

On the other hand, if a given input x may be assigned different labels, then labels are probabilistic. Here, y is drawn from the possible classes according to some probability distribution p(x), representing the probability of each class for the given input. 

Theoretically, it is possible to achieve 100% accuracy on a deterministic classification problem. This is impossible in a probabilistic classification problem. 

#### Noisy Labels

#### Linearly Separable Data

### Data for Regression Problems


