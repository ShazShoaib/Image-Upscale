from PIL import Image
from math import floor

def input_image(file='input.png'):
    # Open the image file
    image = Image.open(file)

    # Convert the image to RGB mode if it's not already
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Get the width and height of the image
    width, height = image.size

    # Create a 2D list to store the RGB tuples
    rgb_list = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    # Iterate over the pixels and store the RGB values in the list
    for y in range(height):
        for x in range(width):
            rgb_list[y][x] = image.getpixel((x, y))

    return rgb_list

def render_image(rgb_list, output_file='output.png'):
    # Create a new image with the specified width and height
    image = Image.new("RGB", (len(rgb_list[0]), len(rgb_list)))

    # Create a pixel access object to modify the image pixels
    pixels = image.load()

    # Iterate over the RGB tuples and set the corresponding pixels in the image
    for y in range(len(rgb_list)):
        for x in range(len(rgb_list[0])):
            rgb = rgb_list[y][x]
            pixels[x,y] = rgb

    # Save the image to the output file
    image.save(output_file)


def interpolate_cols(pixels2D):
    interpolated = []
    for i in range(len(pixels2D)-1,-1,-1):
        interpolated_col = []
        for j in range(len(pixels2D[0])-1,-1,-1):
            interpolated_col.insert(0, pixels2D[i][j])
            rgb = floor((pixels2D[i][j-1][0] + pixels2D[i][j][0])/2),floor((pixels2D[i][j-1][1] + pixels2D[i][j][1])/2),floor((pixels2D[i][j-1][2] + pixels2D[i][j][2])/2)
            interpolated_col.insert(0,rgb)
        del interpolated_col[0]
        interpolated.insert(0,interpolated_col)

    return interpolated

def interpolate_rows(pixels2D):
    interpolated = []
    for i in range(len(pixels2D) - 1):
        interpolated_row = []
        for j in range(len(pixels2D[0])):
            rgb =  ((pixels2D[i][j][0] + pixels2D[i+1][j][0]) // 2,
                    (pixels2D[i][j][1] + pixels2D[i+1][j][1]) // 2,
                    (pixels2D[i][j][2] + pixels2D[i+1][j][2]) // 2)
            interpolated_row.append(rgb)
        interpolated.append(pixels2D[i])
        interpolated.append(interpolated_row)

    interpolated.append(pixels2D[-1])
    return interpolated

def interpolate(RGB_list):
    return (interpolate_cols(interpolate_rows(RGB_list)))


#----public static void main(String[] args){----------------------------------------------------------------------------}
rgb_list = [
    [(190, 0, 64), (190, 0, 123), (190,123,123), (190,190,123)],
    [(255, 0, 64), (255, 0, 123), (255,123,123), (255,190,123)],
    [(255, 123, 64), (255, 190, 123), (255,220,123), (255,230,123)],
    [(255,190, 64), (255, 200, 150), (255,220,190), (255,240,200)]
]

#rgb_list = input_image('input.bmp')
#render_image(rgb_list)
#upscaled_image = bilinear('output2.png','output2.png')

rgb_list = input_image('input.bmp')
render_image(rgb_list)
render_image(interpolate(rgb_list),'output.png')