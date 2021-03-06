import numpy

"""configuration in the form

f = float, [0, 1]
i = int, [0, 255]
b = binary

config = {
    'r': [f, i, i, b]
    'g': [f, i, i, b]
    'b': [f, i, i, b]
    'k': [f, i, i, b]
}

where in each channel the __ element is:
0th: magnitude
1st: lower bound
2nd: upper bound
3rd: binarization

"""
channels = ['r','g','b','k']

def apply_luts(image, configuration):

    for i in range(3):
        lut = generate_lut(*configuration[channels[i]])
        image[:,:,i] = lut[image[:,:,i]]
    
    return image

def generate_lut(magnitude, lowerBound, upperBound, binarize=False):
    slope = ((upperBound - lowerBound) / 255.) * magnitude
    lut = numpy.asarray([x * slope for x in range(255)])
    
    if binarize:
        lut = numpy.where(lut > 128, 255, 0)

    lut = numpy.clip(lut, 0, 254)

    return lut

channel_l = ['red','green','blue']
channel_d = {'red':["mag_r", "upper_r", "lower_r", "binary_r"],
    'blue': ["mag_b", "upper_b", "lower_b", "binary_b"],
    'green': ["mag_g", "upper_g", "lower_g", "binary_g"],
    'black':["mag_k", "upper_k", "lower_k", "binary_k"]}

def apply_qt_luts(image, config):
    #return image
    #for i, key in enumerate(channel_l):
    #    lut = generate_lut((config[key][channel_d[key][0]]) / 100., config[key][channel_d[key][1]], config[key][channel_d[key][0]], bool(config[key][channel_d[key][0]]))
    m = config["black"]["mag_k"] / 100. 
    l = config["black"]["lower_k"]
    u = config["black"]["upper_k"]
    lut = numpy.asarray([(u - l)*x*m for x in range(255)]).astype(int)
    image = lut[image]

    return image