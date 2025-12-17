



# Question No : 1
image_list_a = [f"img{i}.png" for i in range(1, 124)]
print(image_list_a)


# Question No : 2
for i in range(len(image_list_a)):
    temp_seg = image_list_a[i].split('.')[0]
    num = int(temp_seg.split('g')[1])
    image_list_a[i] = f"img{num:04d}.png"
print(image_list_a)