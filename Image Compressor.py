#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from matplotlib import pyplot
import matplotlib as mpl
from sklearn.cluster import KMeans

#image to compress goes here
image_to_read = 'face.jpg'
A = mpl.image.imread(image_to_read)
A = A.astype(float)

#Number of clusters (or colors) you want to compress with
K = 8

#Divide by 255 to normalize features
A /= 255
#Reshape the image to have RGB values as features for each pixel
X = A.reshape(-1, 3)

#Initializing KMeans model and fitting to data
kmeans = KMeans(n_clusters=K, random_state=0).fit(X)
X_recovered = kmeans.cluster_centers_[kmeans.labels_, :].reshape(A.shape)

# Display the original image, rescale back by 255
fig, ax = pyplot.subplots(2, 1, figsize=(16, 8))
A = A*255.0
#Need to convert back to integers if image is a jpeg
if image_to_read[-3] == 'j':
    A = A.astype(np.uint8)
ax[0].imshow(A)
ax[0].set_title('Original')
ax[0].grid(False)
ax[0].set_axis_off()

# Display compressed image, rescale back by 255
X_recovered = X_recovered*255.0
#Need to convert back to integers if image is a jpeg
if image_to_read[-3] == 'j':
    X_recovered = X_recovered.astype(np.uint8)
ax[1].imshow(X_recovered)
ax[1].set_title('Compressed, with %d colors' % K)
ax[1].grid(False)
ax[1].set_axis_off()


# In[ ]:





# In[ ]:




