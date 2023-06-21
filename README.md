# Image-Upscale
a basic image upscaler using Python PIL

# Algorithm
The algorithm works by taking the average between pixels, this is done vertically and horizontally. \
Example:

[000][100][200]\
[050][150][250]\
[000][150][250]

=>

[000][050][100][150][200]\
[050][100][150][200][250]\
[000][075][150][200][250]

=>

[000][050][100][150][200]\
[025][075][125][175][225]\
[050][100][150][200][250]\
[025][087][150][200][250]\
[000][075][150][200][250]
