from PIL import Image
import os
import json
import shutil


SINGLE_X = 51
SINGLE_Y = 27

def get_one_block(pic, lx, ly):
    new_pic = Image.new("RGB",(SINGLE_X, SINGLE_Y))
    for i in range(lx, lx + SINGLE_X):
        for j in range(ly, ly+SINGLE_Y):
            try:
                pix = pic.getpixel((i,j))
                new_pic.putpixel((i-lx,j-ly), pix)
            except IndexError:
                print(lx, ly, j, i)
    return new_pic

def put_one_block(pic, lx, ly, new_pic):
    for i in range(lx, lx + SINGLE_X):
        for j in range(ly, ly+SINGLE_Y):
            try:
                pix = new_pic.getpixel((i-lx,j-ly))
                pic.putpixel((i,j), pix)
            except IndexError:
                print(lx, ly, j, i)


split_names = os.listdir("./222/")
split_names = [i for i in split_names if "png" in i]

origin_names = os.listdir("./111/")
origin_names = [i for i in origin_names if "png" in i]

def get_pic_datas(pattern, names):
    pic_data = []
    for i in names:
        im = Image.open(pattern.format(i))
        pic_data.append(list(im.getdata()))
        im.close()
    return pic_data

def get_pairs():
    origin_datas = get_pic_datas("./111/{}", origin_names)
    split_datas = get_pic_datas("./222/{}", split_names)
    pairs = dict()
    PIX_NUMBER = 5
    new_one = 0
    for i in split_datas:
        pair = [j for j in origin_datas if j == i]
        if len(pair) == 1:
            split_n = split_names[split_datas.index(i)]
            origin_n = origin_names[origin_datas.index(pair[0])]
            pairs[split_n] = origin_n
        else:
            pair = [j for j in origin_datas if j[-PIX_NUMBER:] == i[-PIX_NUMBER:]]
            if len(pair) == 1:
                new_one += 1
                split_n = split_names[split_datas.index(i)]
                origin_n = origin_names[origin_datas.index(pair[0])]
                pairs[split_n] = origin_n
            else:
                print(len(pair))
    print(new_one)
    return pairs

def combine_pic(pairs):
    new_demo = Image.new("RGB", (4096,2160))
    for split_n,origin_n in pairs.items():
        li, lj = split_n.split('.')[0].split('_')
        li, lj = int(li), int(lj)
        new_pic = Image.open("./111/{}".format(origin_n))
        put_one_block(new_demo, li * SINGLE_X, lj * SINGLE_Y, new_pic)
        new_pic.close()
    return new_demo


if __name__ == "__main__":
    #原图
    demo = Image.open("./demo.jpg")
    # im = get_one_block(demo, 0,0)
    # im.show()
    # for i in range(0, 80):
    #     for j in range(0, 80):
    #         im = get_one_block(demo, i * SINGLE_X, j * SINGLE_Y)
    #         im.save("222/{}_{}.png".format(i,j))

    pairs =get_pairs()
    print(len(pairs))
    with open("pairs.json", "w") as f:
        json.dump(pairs, f)

    with open("pairs.json", "r") as f:
        pairs = json.load(f)
    left = [i for i in origin_names if i not in pairs.values()]
    print(len(left))
    for i in left:
        shutil.copyfile("./111/{}".format(i), "./left/{}".format(i))
    print(left)

    new_demo = combine_pic(pairs)
    new_demo.show()
    new_demo.save("new_demo.png")