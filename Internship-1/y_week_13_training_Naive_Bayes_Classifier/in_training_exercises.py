# Write a python function that computes the probability of an instance provided an array.
def calculateProbability(x, list):
  probability = list.count(x) / len(list) * 100
  return probability

sampleList = [32, 3, 23, 23, 50, 23]
print(calculateProbability(23, sampleList))



# Write a python function that computes probability of two consecutive events with replacement and without replacement
def calculateProbabilityWithReplacement(x, y, list):
  x_prob = list.count(x) / len(list)
  y_prob = list.count(y) / len(list)
  joint_prob = x_prob * y_prob # Independent events, multiplication rule
  return joint_prob


def calculateProbabilityWithOutReplacement(x, y, list):
  x_prob = list.count(x) / len(list)
  list.remove(x)
  y_prob = list.count(y) / len(list)
  joint_prob = x_prob * y_prob
  return joint_prob


sampleList = [32, 3, 23, 23, 50, 23]
print(calculateProbabilityWithReplacement(23, 50, sampleList))
print(calculateProbabilityWithOutReplacement(23, 50, sampleList))
