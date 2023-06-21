# Image-Upscale
a basic image upscaler using Python PIL

# Algorithm
The algorithm works by taking the average between pixels, this is done vertically and horizontally. \
Example:\
                                                  [  0][ 50][100][150][200]\
[  0][100][200]     [  0][ 50][100][150][200]     [ 25][ 75][125][175][225]\
[ 50][150][250] =>  [ 50][100][150][200][250] =>  [ 50][100][150][200][250]\
[  0][150][250]     [  0][075][150][200][250]     [ 25][ 87][150][200][250]\
                                                  [  0][ 75][150][200][250]\
                                                  
                                                  
