import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PIL import Image

class Initialize:

      def __init__(self, image_link):
            self.image = Image.open(image_link)
            self.fig, self.ax = plt.subplots(1,1)
            self.grid_exsit = False

      def plot_grid(self, dark_image=False):
            self.grid_count = 10
            self.width, self.height = self.image.size

            self.grid_width_interval = int(np.linspace(0, self.width, self.grid_count)[1] - np.linspace(0, self.width, self.grid_count)[0])
            self.grid_height_interval = int(np.linspace(0, self.height, self.grid_count)[1] - np.linspace(0, self.width, self.grid_count)[0])
            print(self.grid_height_interval)

            self.ax.set_xticks(np.arange(0, self.width, self.grid_width_interval))
            self.ax.set_yticks(np.arange(0, self.height, self.grid_height_interval))

            print(len(np.arange(0, self.width, self.grid_width_interval)))

            if dark_image:
                  plt.grid(color="white", linestyle="-")
            else:
                  plt.grid(color="black", linestyle="-")

            self.ax.imshow(self.image)
            print(self.ax)
            self.grid_exsit = True
            plt.show()
            return self.image

      def tighten(self):

            if self.grid_exsit == False:
                  raise AttributeError("Image has not been initialized.")

            self.grid_height_interval = self.grid_height_interval // 10
            self.grid_width_interval = self.grid_width_interval // 10

            self.ax.set_xticks(np.arange(0, self.width, self.grid_width_interval))
            self.ax.set_yticks(np.arange(0, self.height, self.grid_height_interval))

            print(self.ax)
            print(len(np.arange(0, self.width, self.grid_width_interval)))
            print(self.grid_height_interval)

            self.ax.imshow(self.image)
            plt.grid(color="black", linestyle="-")
            # self.ax.clear()
            # self.ax = self.ax
            # self.image = plt.gcf()
            # self.plot_grid()
            plt.show()
            # tightened = plt.gcf()
            # tightened.show()

            # with plt.ion():
            #       fig2 = plt.figure()
            #       fig2.show()
            # self.fig.canvas.draw()
            # plt.show()


id_image = Initialize("sample.jpg")
id_image.plot_grid()
id_image.tighten()
# plt.show()