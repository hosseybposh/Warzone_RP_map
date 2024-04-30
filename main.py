import numpy as np
import matplotlib.pyplot as plt
import time

def in_valid(c, valid_areas):
    return c[0] >= -valid_areas[0] and c[0] <= valid_areas[0] and c[1] >= -valid_areas[1] and c[1] < valid_areas[1]

def get_centers(n, shape):
    centers = []
    radii = []    # the first three centers need to be somewhat at the center of the map
    centered_coord_system = np.array([shape[0] - shape[0] // 2, shape[1] - shape[1] // 2])
    radii.append(0.7 * np.min(centered_coord_system))
    radii += [radii[0] * 0.7**n for n in range(9)]

    # First determine the valid area. In COD it's the map, where the players can play, here I'm just gonna limit it to the central area.
    valid_areas = (0.5 * centered_coord_system).astype(np.int32)


    first_three_lmt = (0.2 * centered_coord_system).astype(np.int32)

    xs = np.random.randint(-first_three_lmt[0], first_three_lmt[0], 3)
    ys = np.random.randint(-first_three_lmt[1], first_three_lmt[1], 3)
    centers += list(np.stack([xs, ys], axis=1))

    # Now we want to expand the limit of the new centers and determine them:
    new_lmt = (0.3 * centered_coord_system).astype(np.int32)
    centers += [np.array([np.random.randint(-new_lmt[0], new_lmt[0]),
                        np.random.randint(-new_lmt[1], new_lmt[1])])]
    
    # Now the next point needs to be within certain distance from the last center
    for i in range(n - 4):
        last_center = centers[-1]
        while True:
            new_center = last_center + np.array([np.random.randint(-new_lmt[0], new_lmt[0]),
                                            np.random.randint(-new_lmt[1], new_lmt[1])])
            if in_valid(new_center, valid_areas):
                centers.append(new_center)
                break

    decenter = np.array([shape[0] // 2, shape[1] // 2])
    centers = [c + decenter for c in centers]

    return centers, radii

def get_transition(centers, radii, resolution=100):
    n = len(centers)
    transition_centers = []
    transition_radii = []
    for i in range(n -1):
        old_center = centers[i]
        new_center = centers[i+1]
        old_radius = radii[i]
        new_radius = radii[i+1]
        transition_centers.append(np.array(([np.linspace(old_center[0], new_center[0], resolution),
                                np.linspace(old_center[1], new_center[1], resolution)])))

        transition_radii.append(np.linspace(old_radius, new_radius, resolution))
    return transition_centers, transition_radii

if __name__ == "__main__":
    shape = (200, 200)
    centers, radii = get_centers(10, shape)
    trans_centers, trans_radii = get_transition(centers, radii, resolution=100)
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the limits of the plot
    ax.set_xlim(0, shape[1])
    ax.set_ylim(0, shape[0])

    for center_ls, radius_ls in zip(trans_centers, trans_radii):
        for center, radius in zip(np.stack(center_ls, axis=1), radius_ls):
            # Clear the previous circle
            ax.cla()
            ax.set_xlim(0, shape[1])
            ax.set_ylim(0, shape[0])

            # Create a circle
            circle = plt.Circle(center, radius, color='blue', fill=False)
            ax.add_patch(circle)

            # Display the plot
            plt.draw()
            plt.pause(0.01)  # Display each disk for 10 seconds

    plt.close()