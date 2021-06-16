from urllib.request import urlretrieve as get
for i in range(0,350):
    name = 'student_id.png' % (i)
    link = 'https://link_to_my_uni/images/profile_pictures/%s' % (name)
    print(name)
    try:
        get(link, 'images/%s' % (name))
    except:
        print("Not Found!!")
        continue
    print('*'*15)
    
