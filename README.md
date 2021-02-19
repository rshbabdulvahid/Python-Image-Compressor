# Python-Image-Compressor

An image compressor built in python using the sci-kit learn package, with matplotlib to retrieve RGB features from each pixel of image and to display
the images. 

The goal of this project was to compress either a PNG or JPEG image, depending on the format of the input image. In order to do this, KMeans clustering was
used: each data point is one pixel of the image, and the three dimensions of each data point correlate to their RGB values.
The user can enter in a value for 'K' to choose how many clusters the KMeans model will cluster the data points into: this correlates to how many shades of
color are desired in the final compressed image.

The actual compression is done using the KMeans model in sklearn, and the full image is recovered by examining the label that each data point received, the coordinates
of each of these labels (displayed in cluster_centers_), and then reshaping this array of labeled data points to the original format of the input image. The image can
then, finally, be displayed using pyplot.

Note that all compression is done after converting the image's RGB values to floats. For a JPEG image, the new data points corresponding to cluster centers are
recast to integers before the image is displayed by pyplot.

A sample compression on an image found online is shown below.


![Alt text](https://github.com/rshbabdulvahid/Python-Image-Compressor/blob/master/Compression.PNG)
