from detecting.detec import get_face
import os

dir = os.getcwd().replace('\\', '/')  # get current directory and replace \ to /
in_path = '/video/'
vid_list = os.listdir('.' + in_path)
for i in vid_list:
   if i.endswith('.mp4'):
    vid_list.remove(i)
for vid_name in vid_list:
    out_path = '/Output/' + str(vid_name.split('.mp4')[0])
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    # print('in:{} and out:{} '.format(dir + in_path + vid_name, dir + out_path))
    get_face(input_path=(dir + in_path + vid_name),
             output_path=(dir + out_path))

if __name__ == "__main__":
    pass
