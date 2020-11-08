age = int(input('请输入你的年龄'))    # input接受到的数据是str类型，如果需要比较记得转换数据类型

if age < 18:
    print('没成年隔着干啥呢，一边去..')

elif (age >= 18) and (age < 60):
    print('已经成年执行下一步')

else:                                    # else是如果条件不成力后执行的，不需要再把条件输入一次
    print('大爷别来了，遭罪不起')
