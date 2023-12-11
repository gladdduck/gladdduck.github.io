import os

start_='''
<div class="outer">
'''
end_='''
</div>
'''
image_='<img src="./wallimages/{}">'

def get_image_path():
    result=[]
    image_list=os.listdir(r'D:\BaiduSyncdisk\Blog\source\picturewall\wallimages')
    for i in range(len(image_list)):
        result.append(image_.format(image_list[i]))
    return start_+''.join(result)+end_

print(get_image_path())