import numpy as np
import argparse
import sys

def arg_parse():
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file', dest = 'data_file', required = True, help = 'input raw data in one column')
  parser.add_argument('-d', '--dimension', dest = 'dims', nargs = '+', type = int, required = True, help = 'dimension of data array')
  parser.add_argument('-x', '--axis', dest = 'ave_axis', type = int, required = True, help = 'the dimension along which to average')
  parser.add_argument('-v', '--verbose', action = 'store_true', help = 'print data matrix before averaging')
  args = parser.parse_args()
  return args.data_file, args.dims, args.ave_axis, args.verbose

if __name__== "__main__":
  data_file, dims, ave_axis, verbose = arg_parse();

  with open(data_file) as f:
    data = f.read().split('\n')

  del data[-1]
  data = [np.double(x) for x in data]
  print "Length of data: " + str(len(data))
  data = np.array(data)
  shape = dims
  data_mat = data.reshape(shape)
  if verbose:
    print data_mat
  ave = np.mean(data_mat, axis = ave_axis)
  stddev = np.std(data_mat, axis = ave_axis)

  print "Average:"
  if len(ave.shape) > 2:
    for n in ave:
      np.savetxt(sys.stdout, n, fmt = '%.7f')
      print ''
  else:
    np.savetxt(sys.stdout, ave, fmt = '%.7f')

  print "Standard deviation:"
  if len(ave.shape) > 2:
    for n in stddev:
      np.savetxt(sys.stdout, n, fmt = '%-6s')
      print ''
  else:
    np.savetxt(sys.stdout, stddev, fmt = '%-6s')
