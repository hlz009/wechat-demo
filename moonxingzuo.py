#coding=utf-8
import datetime
import ephem
def main():
    with MoApp(appid='wxed511f58abdf607b', name='月亮星座'):
        with Page(name='page1', onReady=getGMT):

            with Box(size=[750,60],background='white',borderBottom='1rpx solid #eeeeee'):
                Text(text='日期选择',pos=[20,0])
                with DatePickerBox(id='picker1',
                    onChange=onDatePickerChange):
                    Text(text='点击选择日期',pos=[500,10],color='black',id='date',fontSize='26rpx')

            with Box(top= 80, size=[750,60],background='white',borderBottom='1rpx solid #eeeeee'):
                Text(text='时间选择',pos=[20,0])
                with TimePickerBox(id='picker2',#range=[str(x)+'时' for x in range(24)],
                    onChange=onTimePickerChange):
                    Text(text='点击选择小时',pos=[500,10],color='black',id='hour',fontSize='26rpx')

            with Box(top= 160, size=[750,60],background='white',borderBottom='1rpx solid #eeeeee'):
                Text(text='时区选择',pos=[20,0])
                with SelectorPicker(id='picker3',range=['(GMT-12.00)国际日期变更线西','(GMT-11.00)中途岛，萨摩亚群岛','(GMT-10.00)夏威夷','(GMT-9.00)阿拉\
                    斯加','(GMT-8.00)太平洋时间（美国和加拿大）；蒂华纳','(GMT-7.00)山地时间（美国和加拿大）','(GMT-6.00)中部时间（美国和加拿大），萨斯喀彻温','(GMT-5.00)\
                    东部时间（美国和加拿大）','(GMT-4.00)大西洋时间（加拿大）','(GMT-3.00)纽芬兰，巴西利亚','(GMT-2.00)中大西洋','(GMT-1.00)佛得角群岛，亚速尔群岛','(GMT)\
                    格林威治标准时间，都柏林，爱丁堡，伦敦','(GMT+1.00)阿姆斯特丹，柏林，马德里，巴黎,罗马，维也纳','(GMT+2.00)开罗，雅典，贝鲁特，明斯克,耶路撒冷','(GMT+3.00)\
                    巴格达，科威特，利雅得，德黑兰,莫斯科,圣彼得堡','(GMT+4.00)阿布扎比，马斯喀特','(GMT+5.00)叶卡捷琳堡，伊斯兰堡，卡拉奇，塔什干','(GMT+6.00)阿拉木图，新西伯\
                    利亚，阿斯塔纳，达卡','(GMT+7.00)曼谷，河内，雅加达，克拉斯诺亚尔斯克','(GMT+8.00)北京，重庆，香港特别行政区，乌鲁木齐','(GMT+9.00)首尔，大坂，东京，札幌，\
                    雅库茨克','(GMT+10.00)布里斯班，符拉迪沃斯托克（海参崴）'],
                    onChange=onGMTPickerChange, value=8):
                    Text(text='点击选择时区',pos=[500,10],color='black',id='GMT',fontSize='26rpx') 


            Text(pos=[500,500], id='constellation')

async def getGMT(user, app, page, mo):
    page.picker3.value = 8+12
    page.GMT.text = 'GMT %d:00' %range(-12, 11)[int(page.picker3.value)]
async def onDatePickerChange(user, app, page, mo):
    page.date.text = page.picker1.value
    page.constellation.text = showSign(page.picker1.value, page.picker2.value, page.picker3.value)

async def onTimePickerChange(user, app, page, mo):
    page.hour.text = page.picker2.value 
    page.constellation.text = showSign(page.picker1.value, page.picker2.value, page.picker3.value)

async def onGMTPickerChange(user, app, page, mo):
    page.GMT.text = 'GMT %d:00' %range(-12, 11)[int(page.picker3.value)]
    page.constellation.text = showSign(page.picker1.value, page.picker2.value, page.picker3.value)


def showSign(datevalue, hourvalue, GMTvalue):
    if datevalue and hourvalue:
        datelist = [int(x) for x in datevalue.split('-')]
        datetimelist = datelist + [int(x) for x in hourvalue.split(':')]
        return SignCalculatiton(*datetimelist, GMT=range(-12, 11)[int(GMTvalue)])
    else:
        return ''

# 计算月亮星座的代码
Moon = ephem.Moon()

Constellations = [
    ['Aries', '白羊座'],
    ['Taurus', '金牛座'],
    ['Gemini', '双子座'],
    ['Cacer', '巨蟹座'],
    ['Leo', '狮子座'],
    ['Virgo', '处女座'],
    ['Libra', '天秤座'],
    ['Scorpio', '天蝎座'],
    ['Sagittarius', '射手座'],
    ['Capricom', '摩羯座'],
    ['Aquarius', '水瓶座'],
    ['Pisces', '双鱼座']
]


def SignCalculatiton(year, month, day, hour, minute=0, second=0, GMT=8):
    date = datetime.datetime(year, month, day, hour, minute, second)
    date -= datetime.timedelta(hours=GMT)
    Moon.compute(date)
    longitude = ephem.Ecliptic(Moon, epoch=str(date.year)).lon
    index = int(longitude//(math.pi/6))
    return Constellations[index][1]