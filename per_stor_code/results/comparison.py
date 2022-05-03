from scipy.fftpack import diff


first =  [0.925146,0.929707,0.934653,0.939652,0.944285,0.949694,0.954928,0.960172,0.965246,0.969399]
second = [0.926258,0.930777,0.935397,0.940346,0.945273,0.949990,0.955119,0.959174,0.963596,0.967796]

standard_first = [0.000403, 0.004908, 0.008933, 0.012677, 0.016639, 0.020944, 0.025104, 0.029322, 0.033331, 0.037871]
standard_second = [0.003278, 0.008569, 0.012635, 0.016696, 0.020835, 0.025159, 0.029384, 0.033894, 0.038464, 0.043005]

ave_list = [37.000403,37.004908,37.008933,37.012677,37.016639,37.020944,37.025104,37.029322,37.033331,37.037871]
def local():
    diff_sum = 0
    for i in range(10):
        diff_sum += second[i] - first[i]
    return diff_sum

def standard():
    diff_sum = 0
    for i in range(10):
        diff_sum += standard_second[i] - standard_first[i]
    return diff_sum

def average():
    diff_sum = 0
    for i in range(10):
        diff_sum += ave_list[i]
    return diff_sum / 10

print("AVERAGE DIFFERENCE IS: ", local()/10, " milliseconds")
print("AVERAGE DIFFERENCE IS: ", standard()/10, " milliseconds")
print("AVERAGE OF AVE_LIST: ", average())
test = 37.000403 + 0.019013199999996
print(test)