## 3 methods to create numpy ndarray
1. python list to ndarray
```
a = [1,2,3]
x = np.array(a)
```

2. Using numpy function
```
x = np.arange(11)   # create 0 to 10
```

3. Read data from file
```
x = np.loadtxt('1.csv', delimiter=',', skiprows=1, usecols=(0, 1, 4), unpack=False)

col1, col2, col5 = np.loadtxt('1.csv', delimiter=',', skiprows=1, usecols=(0, 1, 4), unpack=True)
```

## Index and slice

## Random
```
np.random.seed(19680801)

x = np.random.randn(1000)  # creat 1000 random numbers

x = np.random.normal(0, 1, 1024) # create 1024 numbers, mean is 0 , sd is 1

x = np.linspace(-10, 10, 100)    # 100 numbers between -10 to 10
```

## Functions
```
    y = np.sort(x)     # create a sorted array
    x.sort()           # x is sorted
```
