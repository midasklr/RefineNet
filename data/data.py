import os
for i in range(1000,2355):
    with open("train.parking","a+") as f:
        f.writelines("train_images/{}.png".format(i)+"\t"+"train_labels/{}.png".format(i)+"\n")
        
