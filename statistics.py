from typing import List
Vector = List[float]

def mean(x: Vector) -> float:
  return sum(x)/len(x)

def de_mean(x: Vector) -> Vector:
  x_bar = mean(x)
  return [d - x_bar for d in x]

def dot(x: Vector, y: Vector) -> float:
  assert len(x) == len(y)
  return sum([d*e for d, e in zip(x, y)])

def variance(x, y=None) -> float:
  if y is None: y = x
  #assert type(x) == Vector
  #assert type(y) == Vector
  assert len(x) == len(y)

  return dot(de_mean(x), de_mean(y)) / (len(x) -1)

def deviation(x, y=None) -> float:
  return variance(x, y)**(1/2)

def correlation(x: Vector, y: Vector) -> float:
  x_dev = deviation(x)
  y_dev = deviation(y)
  covariance = variance(x, y)
  if x_dev > 0 and y_dev > 0:
    return covariance / x_dev / y_dev
  else:
    return 0

if __name__=="__main__":
  assert dot([1,2,3], [4,5,6]) == 32
  test_data1 = [1,2,3,4,5,6]
  test_data2 = [d+1 for d in test_data1]
  test_data3 = [-1*d for d in test_data1]
  assert correlation(test_data1, test_data2) == 1
  assert correlation(test_data1, test_data3) == -1
