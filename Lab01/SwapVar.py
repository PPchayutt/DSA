def convert_string_to_tuples(text_in):
  values = text_in.strip('()').split(', ')
  real_tup = tuple(map(float, values))
  convert = f"({real_tup[1]}, {real_tup[0]})"
  values2 = convert.strip('()').split(', ')
  print(tuple(map(float, values2)))
laongdao_data = convert_string_to_tuples(input())
