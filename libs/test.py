# here define a dict
enc_array = {
  "a":"_|",
  "b":"_",
  "and so on"
}

test_string = 'aaa'

def conv(s):
  out = []
  for _ in s:
    if _ in enc_array:
      out.append(_)
    else:
      print('Unkown character')

print(conv(test_string))