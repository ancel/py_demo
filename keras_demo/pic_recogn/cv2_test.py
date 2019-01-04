import matplotlib.pyplot as plt 
import cv2

img_BGR = cv2.imread('101_ObjectCategories/anchor/image_0019.jpg') # BGR 
plt.subplot(3,3,1); plt.imshow(img_BGR);plt.axis('off');plt.title('BGR')

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
print(img_RGB.shape)
plt.subplot(3,3,2); plt.imshow(img_RGB);plt.axis('off');plt.title('RGB')

img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
plt.subplot(3,3,3); plt.imshow(img_GRAY);plt.axis('off');plt.title('GRAY')

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
plt.subplot(3,3,4); plt.imshow(img_HSV);plt.axis('off');plt.title('HSV')

img_YcrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)
plt.subplot(3,3,5); plt.imshow(img_YcrCb);plt.axis('off');plt.title('YcrCb')

img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)
plt.subplot(3,3,6); plt.imshow(img_HLS);plt.axis('off');plt.title('HLS')

img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)
plt.subplot(3,3,7); plt.imshow(img_XYZ);plt.axis('off');plt.title('XYZ')

img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)
plt.subplot(3,3,8); plt.imshow(img_LAB);plt.axis('off');plt.title('LAB')

img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)
plt.subplot(3,3,9); plt.imshow(img_YUV);plt.axis('off');plt.title('YUV')
plt.show()

