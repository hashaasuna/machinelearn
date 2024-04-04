import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
import io
import urllib, base64
from rest_framework.decorators import api_view

@api_view(['GET'])
def firstml(request):
    rng = np.random.RandomState(1)
    x = 8 * rng.rand(50)
    y = np.sin(x) + 0.1 * rng.randn(50)

    #Create single dimension
    x= x[:,np.newaxis]
    y= y[:,np.newaxis]

    inds = x.ravel().argsort()  # Sort x values and get index    
    x = x.ravel()[inds].reshape(-1,1)
    y = y[inds] #Sort y according to x sorted index

    print(x.shape)
    print(y.shape)

    #Plot
    plt.scatter(x,y)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
import io
import urllib, base64
from rest_framework.decorators import api_view

def firstml(request):
    rng = np.random.RandomState(1)
    x = 8 * rng.rand(50)
    y = np.sin(x) + 0.1 * rng.randn(50)

    #Create single dimension
    x= x[:,np.newaxis]
    y= y[:,np.newaxis]

    inds = x.ravel().argsort()  # Sort x values and get index    
    x = x.ravel()[inds].reshape(-1,1)
    y = y[inds] #Sort y according to x sorted index

    print(x.shape)
    print(y.shape)

    #Plot
    plt.scatter(x,y)
    fig = plt.gcf()
    plt.close()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'matplot.html',{'data':uri})

def analyz(request):
    return render(request, 'analyzing.html')