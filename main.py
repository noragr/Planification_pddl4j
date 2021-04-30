# This is a sample Python script.
from matplotlib import pyplot as plt


def plotBlocksworld():
    # blocksworld

    x_data_HSP = [11,14,12,9,13,15,10,8,7,5,6,1,2,4,3]
    y_data_HSP = [1.06,0.57,0.48,0.41,0.36,0.33,0.29,0.18,0.18,0.18,0.17,0.16,0.15,0.15,0.14]
    y_steps_HSP = [22,20,20,20,18,16,20,10,12,10,16,6,10,12,6]

    y_data_SAT = [0.49,1.9,0.17,0.1,0.44,0.18,0.07,0.04,0.02,0.02,0.05,60.01,0.02,0.02,0.01]
    y_steps_SAT = [22,20,20,20,18,16,20,10,12,10,16,6,10,12,6]
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax2= fig.add_subplot(1,2,2)
    ax1.plot(x_data_HSP, y_data_HSP, label='HSP')
    ax1.plot(x_data_HSP, y_data_SAT, label='SAT')
    ax2.plot(x_data_HSP, y_steps_HSP, label='HSP')
    ax2.plot(x_data_HSP, y_steps_SAT, label='SAT')
    ax1.set_xlabel("Problem number")
    ax1.set_ylabel("Time in seconds")
    ax1.set_title('Blocksworld, time')
    ax2.set_xlabel("Problem number")
    ax2.set_ylabel("Number of steps")
    ax2.set_title('Blocksworld, number of steps')
    ax1.legend()
    ax2.legend()

    plt.show()

def plotDepot():
    # depot

    x_data_HSP = [15,14,12,11,9,8,6,5,4,10,3,13,7,2,1]
    y_data_HSP = [0,0,0,0,0,0,0,0,8.02,3.49,2.95,2.37,1.37,0.2,0.2]
    y_data_SAT = [0,0,0,0,0,0,0,0,0,15.74,4.21,9.93,2.20,0.1,0.1]
    y_steps_HSP =[0,0,0,0,0,0,0,0,30,25,29,25,21,15,10]
    y_steps_SAT = [0,0,0,0,0,0,0,0,0,25,29,25,21,15,10]
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.plot(x_data_HSP, y_data_HSP, label='HSP')
    ax1.plot(x_data_HSP, y_data_SAT, label='SAT')
    ax2.plot(x_data_HSP, y_steps_HSP, label='HSP')
    ax2.plot(x_data_HSP, y_steps_SAT, label='SAT')
    ax1.set_xlabel("Problem number")
    ax1.set_ylabel("Time in seconds")
    ax1.set_title('Depot, time')
    ax2.set_xlabel("Problem number")
    ax2.set_ylabel("Number of steps")
    ax2.set_title('Depot, number of steps')
    ax1.legend()
    ax2.legend()

    plt.show()

def plotGripper():
    # depot

    x_data_HSP = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    y_data_HSP = [0,0,0,0,0,0,0,0,0,0,13.97,4.94,1.15,0.38,0.23]
    y_data_SAT = [0,0,0,0,0,0,0,0,0,0,17.48,3.98,2.36,0.23,0.07]
    y_steps_HSP = [0,0,0,0,0,0,0,0,0,0,35,29,23,17,11]
    y_steps_SAT = [0,0,0,0,0,0,0,0,0,0,35,29,23,17,11]
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.plot(x_data_HSP, y_data_HSP, label='HSP')
    ax1.plot(x_data_HSP, y_data_SAT, label='SAT')
    ax2.plot(x_data_HSP, y_steps_HSP, label='HSP')
    ax2.plot(x_data_HSP, y_steps_SAT, label='SAT')
    ax1.set_xlabel("Problem number")
    ax1.set_ylabel("Time in seconds")
    ax1.set_title('Gripper, time')
    ax2.set_xlabel("Problem number")
    ax2.set_ylabel("Number of steps")
    ax2.set_title('Gripper, number of steps')
    ax1.legend()
    ax2.legend()

    plt.show()


def plotLogistics():
    # depot

    x_data_HSP = [12,14,15,11,13,4,7,9,10,3,2,1,5,8,6]
    y_data_HSP = [0,16.08,6.17,4.97,4.89,1.87,1.21,0.79,0.6,0.6,0.59,0.45,0.44,0.35,0.29]
    y_data_SAT = [0,0,0,0,18.28,4.24,2.02,4.40,0.79,0.21,1.86,0.22,0.21,0.09,0.03]
    y_steps_HSP = [0,44,36,36,31,27,26,25,24,15,19,20,17,14,8]
    y_steps_SAT = [0,0,0,0,31,27,25,25,24,15,19,20,17,14,8]
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.plot(x_data_HSP, y_data_HSP, label='HSP')
    ax1.plot(x_data_HSP, y_data_SAT, label='SAT')
    ax2.plot(x_data_HSP, y_steps_HSP, label='HSP')
    ax2.plot(x_data_HSP, y_steps_SAT, label='SAT')
    ax1.set_xlabel("Problem number")
    ax1.set_ylabel("Time in seconds")
    ax1.set_title('Logistics, time')
    ax2.set_xlabel("Problem number")
    ax2.set_ylabel("Number of steps")
    ax2.set_title('Logistics, number of steps')
    ax1.legend()
    ax2.legend()

    plt.show()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plotBlocksworld()
    plotDepot()
    plotGripper()
    plotLogistics()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
