# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(*args:str)-> dict:
  """pick random, numbers annd determine the maximum,minimum,avarage and sum of the numbers

  Args:
      *args (list): collection of numbers provided by the user

  Returns:
      dict: max,min,avarage and sum apired with their values
  """
  collection = list(args)

  #sort the collection
  collection.sort()

  max_num = collection[-1]
  min_num = collection[0]
  sum = 0
  for num in collection:
    sum += num
  avarage = round((sum/len(collection)),2)

  values = {"max_num": max_num,"min_num":min_num,"sum":sum,"avarage":avarage}

  return values

ans = stats(8,9,6,7,4,3,2,18,2,89,76,54)

for key,value in ans.items():
  print(f"{key}:{value}")


