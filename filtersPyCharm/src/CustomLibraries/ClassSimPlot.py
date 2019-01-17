# This class fournishes methods to plot your simulation relevant data
import matplotlib.pyplot as plt
plt.ion()
# import time

class SimPlot:

    # Constructor method
    # -- Input
    #   - filterType: 1 for KF, 2 for EKF, 3 for PF
    def __init__(self, filterType):

        # Instantiating useful variables
        self.ax = [None]
        self.fig = [None]
        self.lines = [None]

        # Instantiating the correctly filter plot style
        if filterType == 1:
            self.kf_initiate()
        elif filterType == 2:
            self.ekf_initiate()
        elif filterType == 3:
            self.pf_initiate()
        else:
            print('SimPlot constructed with unknown arguments.')

    # ===== Method - Kalman filter plot initiation
    def kf_initiate(self):

        # self.fig[0] = plt.figure()
        #
        # self.ax[0] = self.fig[0].add_subplot(1, 1, 1)
        #
        # # defining some plot characteristics

        # # self.ax[0].set_xlim(-6, 6)
        # # self.ax[0].set_ylim(-6, 6)
        # self.ax[0].grid(True)
        #
        # # Displays the plot
        # self.fig[0].show()

        # creating the figure
        self.fig[0] = plt.figure()

        # creating the axes region
        self.ax[0] = self.fig[0].add_subplot(1, 1, 1)

        # defining some plot parameters
        self.ax[0].set_xlim(-6, 6)
        self.ax[0].set_ylim(-6, 6)
        self.ax[0].set_xlabel('pos x [m]')
        self.ax[0].set_ylabel('pos y [m]')
        self.ax[0].set_title('Kalman Filter')
        self.ax[0].grid(True)

        # creating robot real position line
        self.lines[0], = self.ax[0].plot([], [], '--r')

        # creating measurement plot line
        self.lines.extend(self.ax[0].plot([], [], 'og'))

        # creating estimated plot line
        self.lines.extend(self.ax[0].plot([], [], '-b'))

    def kf_draw(self, x_real, x_estimated, z_t):

        # plots the received arrays

        # ploting the real robot real path
        # self.ax[0].plot(x_real[:, 0], x_real[:, 1], '-r')

        # plotting the robot estimated path
        # self.ax[0].plot(x_estimated[:, 0], x_estimated[:, 1], '-b')

        # plotting the sensor reading
        # self.ax[0].plot(z_t[0], z_t[1], marker='o', markersize='3', color='green')

        # displays the plot
        # self.fig[0].show()

        # plt.pause(0.05)

        # updating  robot_realposition plot
        self.lines[0].set_xdata(x_real[:, 0])
        self.lines[0].set_ydata(x_real[:, 1])

        # updating reading plot
        self.lines[1].set_xdata(z_t[0])
        self.lines[1].set_ydata(z_t[1])

        # updating estimation plot
        self.lines[2].set_xdata(x_estimated[:, 0])
        self.lines[2].set_ydata(x_estimated[:, 1])

        # self.ax[0].relim()
        # self.ax[0].autoscale_view()

        # updating the figure
        self.fig[0].canvas.draw()
        self.fig[0].canvas.flush_events()

        plt.pause(0.05)

# for class testing purposes
if __name__ == '__main__':

    test = SimPlot(1)

    a = input('Press any button to close the figure')