from autostereogram.converter import StereogramConverter
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

converter = StereogramConverter()
source_image = Image.open("inputs/cube.jpg")

# A. black and white.
depth_map = np.array(source_image, dtype=float)
result = converter.convert_depth_to_stereogram(depth_map).astype(np.uint8)
Image.fromarray(result).save("outputs/demo.jpg")

# B. Random color
rgb_texture = np.random.randint(low=0, high=255, size=(100,100, 3), dtype=int)
result = converter.convert_depth_to_stereogram_with_rgb_texture(
    depth_map,
    rgb_texture,
    draw_helper_dots=True,
    ).astype(np.uint8)
Image.fromarray(result).save("outputs/demo_rgb_random.jpg")


# B. RGB image texture
rgb_texture = np.array(Image.open("textures/colors_2.jpg")).astype(int)
result = converter.convert_depth_to_stereogram_with_rgb_texture(
    depth_map,
    rgb_texture,
    draw_helper_dots=True,
    ).astype(np.uint8)
Image.fromarray(result).save("outputs/demo_rgb_image.jpg")
