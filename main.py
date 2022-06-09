from vidstab import VidStab
import matplotlib.pyplot as plt

stabilizer = VidStab()
stabilizer.stabilize(input_path='video.mp4', output_path='stable_video.avi')

stabilizer.plot_trajectory()
plt.savefig('img1.png')

stabilizer.plot_transforms()
plt.savefig('img2.png')