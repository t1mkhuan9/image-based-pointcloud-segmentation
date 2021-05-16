import os
import pykitti
import cv2
import numpy as np

from preparation.dataset import generate, delete
from projection.project import points_to_image_project
from visualisation.image import show_image, plot_point_on_image

# The Path to the downloaded odometry file
calibration = os.path.join(os.path.pardir, "dataset", "calibration")
color = os.path.join(os.path.pardir, "dataset", "color")
velodyne = os.path.join(os.path.pardir, "dataset", "velodyne")
label = os.path.join(os.path.pardir, "dataset", "label")

# The path of the dateset
dataset = os.path.join(os.path.abspath(os.path.curdir), "dataset")

# Field of view
v_fov = (-24.9, 2.0)
h_fov = (-45, 45)

if __name__ == '__main__':
    if not os.path.exists(dataset):
        generate(dataset, calibration=calibration, color=color, velodyne=velodyne, label=label)

    seq = pykitti.odometry(dataset, "00")
    index = 0

    img = np.array(seq.get_cam2(index))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    xyz_selected, xy_projected = points_to_image_project(seq, index, v_fov, h_fov)

    show_image("Projected Image", plot_point_on_image(img, xyz_selected, xy_projected))

