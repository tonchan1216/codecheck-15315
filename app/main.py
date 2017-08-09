def main(argv):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
  if len(argv) == 0:
  	argv = ['']

  for i, v in enumerate(argv):
  	if v == "World":
  		print('Hello World!')
  	elif len(v) == 0 and isinstance(v, str):
  		print('Hello!')
  	elif v == 'codecheck':
  		print('Hello codecheck!')
  	elif v == '織田信長':
  		print('Hello 織田信長!')
  	else:
  		print('printing:' + v)