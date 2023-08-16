# -*- coding: UTF-8 -*-

import os
import imageio


def create_gif(image_list, gif_name, suffix=".png"):
    frames = []
    for image_name in image_list:
        if image_name.endswith(suffix):
            print(image_name)
            frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, "GIF", duration=1, loop=0)

    return


def main():
    data_root = "./images/visualization_flow"
    image_list = [f"{data_root}/{img}" for img in sorted(os.listdir(data_root))]
    gif_name = "./images/openscene-flow.gif"
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()
