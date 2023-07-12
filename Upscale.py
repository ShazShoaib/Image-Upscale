from PIL import Image
from math import floor

def get_color_list():
    rgb_list = []
    for i in range(255):
        Row = []
        for j in range(255):
            Row.append((i,0,j))
        rgb_list.append(Row)
    return rgb_list

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

def upscale(pixels2D):
    pixel_pos = []
    for i in range(len(pixels2D)):
        for j in range(len(pixels2D[0])):
            pixel = pixels2D[i][j]
            for c in range(3):
                for k in range(3):
                    pixel_pos.append((pixel,(i-1+c,j-1+k)))


    for i in range(len(pixels2D)):
        for j in range(len(pixels2D[0])):
            for pair in pixel_pos:
                pixel = pair[0]
                pos = pair[1]
                num = 0
                sum = []
                if pos == (i,j):
                    num = num + 1
                    sum.append(pixel)
                if num == 0:
                    continue
                avgR = 0
                avgG = 0
                avgB = 0
                for val in sum:
                    avgR = avgR + val[0]
                    avgG = avgG + val[1]
                    avgB = avgB + val[2]
                avgR = avgR // num
                avgG = avgG // num
                avgB = avgB // num
                pixels2D[i][j] = (avgR,avgG,avgB)
            print(i,j)
        render_image(pixels2D,'temp.png')
    return pixels2D

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

def interpolateGUI(image_path,iterations):
    rgb_list = input_image(image_path)
    for i in range(iterations):
        render_image(interpolate(rgb_list),image_path)
        rgb_list = input_image(image_path)
        print("Iteration Complete :" + str(i+1) + " / " + str(iterations))

#rgb_list = input_image('OP.jpeg')

#render_image(rgb_list)
#render_image(upscale(rgb_list),'output2.png')
#for i in range(5):
#    render_image(interpolate(rgb_list),'output3.png')
#    rgb_list = input_image('output3.png')