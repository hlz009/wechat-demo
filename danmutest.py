def main():
    with MoApp(name='testdanmu',appid='wx02207e6022e44158'):
        with Page(name='index', background='http://material.motimaster.com/yuyuan/Duudle/create/2150e545ed230f5f8314a855fd9f8fad.jpg'):
            this.onReady = indexReady
            TextNickName(pos=['center',50], color='red', fontSize=40)
            Text(text='你有什么要对我说的',pos=['center',100], color='red', fontSize=40)
            ImageAvatar(pos=['center',300], borderRadius='50%', size=[300,300])
            with Box(size=[750,600], pos=[0,200]):
                Barrage(name='danmu')
            Input(name='inputDanmu',color='white',placeholder='请输入弹幕',borderBottom='1rpx solid red',pos=[100,850],size=[400,80])
            with Button(size=[200,80], text='评论', type='primary',pos=[550,850],lineHeight=80,openType='getUserInfo'):
                this.onTap = sendBarrage
            with List(name='recommands',pos=[50,950]):
                with Button(text='{item.text}',border='1px dotted red',color='white',
                      paddingRight='30rpx',paddingLeft='30rpx',background='none',float='left', 
                      marginRight=20,marginBottom=20):
                      this.onTap = moui.request(onRecommandTap,id='{item.id}')

            with Button(text='评论管理',size=[100,60],lineHeight=60,fontSize=20,padding=0,pos=[550,100]):
                this.onTap=moui.goto('second')

        with Page(name='second',onReady=managerReady):
            with List(name='pinglun',pos=[25,0]):
                with Box(size=[700,200], border='1px solid black', marginBottom=20):
                      Image(src='{item.avatar}', size=[80,80], borderRadius='50%', pos=[50,50])
                      Text(text='{item.nick}', pos=[200,80])
                      Text(text='{item.pinglun}', pos=[400,80], color='red')

async def indexReady(user, app, page, mo):
    page.danmu.data = [{'id':1,'text':'我喜欢你萨达达大厦萨就是垃圾焚烧收到反馈数据反馈时间到发生了大空间','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':2,'text':'弹幕一','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"},
        {'id':3,'text':'弹幕二','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':4,'text':'弹幕三','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':5,'text':'弹幕四','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':6,'text':'弹幕五','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':7,'text':'弹幕六','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':8,'text':'弹幕七 ','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':9,'text':'弹幕八','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"},  ]
    page.danmu.danmuStyle = 'color:red'
    page.danmu.tailImage = "http://material.motimaster.com/harvey///0d3f664b4a65c9f4dc21c3d60903a99f.png"
    page.recommands.data = [{'id':0,'text':'我喜欢你'},{'id':1,'text':'我喜欢讨厌你'},{'id':2,'text':'你赶紧滚吧'}]

    page.data.danmuLength= 9
      
async def onRecommandTap(user, app, page, mo, params):
    mid = params.id
    text = page.recommands.data[mid]['text']
    page.inputDanmu.value = text

async def sendBarrage(user, app, page, mo):

    page.danmu.data.append({'id':page.data.danmuLength+1,'text':page.inputDanmu.value,'avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"})
    page.data.danmuLength+=1

async def managerReady(user, app, page, mo):
    page.pinglun.data=[{'id':0,'nick':'harvey','pinglun':'测试','avatar':'http://material.motimaster.com/appmaker/lijiong/2315.png'},
    {'id':1,'nick':'harvey','pinglun':'测试','avatar':'http://material.motimaster.com/appmaker/lijiong/2315.png'},
    {'id':2,'nick':'harvey','pinglun':'测试','avatar':'http://material.motimaster.com/appmaker/lijiong/2315.png'}]
