import os
#r'C:\Users\pc_zhangbo\Desktop\luru'
# .\PanoramaImage rearrange e:/123/pano_aaosywgmkxekgt.jpg 10 0 e:/123/143.bmp 0
image_folder=r'C:\Users\pc_zhangbo\Desktop\luru'
daichuli_list=os.listdir(image_folder)

for i in daichuli_list:
    if i[-1]=='g' and i[-2]=='p':

        tem=os.path.abspath(image_folder+'\\'+i)
        hehe=tem.replace("\\","/")
        print(hehe)
        print('PanoramaImage rearrange '+hehe+' 10 0 '+'e:/123/'+i[0:-4]+'.bmp 0')
        guocheng=os.popen('PanoramaImage rearrange '+hehe+' 10 0 '+'e:/123/'+i[0:-4]+'.bmp 0')
        print(guocheng.read())
   