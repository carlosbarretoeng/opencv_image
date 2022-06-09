from vidstab import VidStab
import matplotlib.pyplot as plt

stabilizer = VidStab()
stabilizer.stabilize(input_path='video.mp4', output_path='stable_video.avi')

stabilizer.plot_trajectory()
plt.savefig('img1.png')

stabilizer.plot_transforms()
plt.savefig('img2.png')

stabilizer.stabilize(input_path='stable_video.avi', output_path='final_video.avi')

stabilizer.plot_trajectory()
plt.savefig('img3.png')

stabilizer.plot_transforms()
plt.savefig('img4.png')