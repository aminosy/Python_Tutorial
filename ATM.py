name = input('请输入姓名')
money = 5000000

def atm_sys():
    global money
    while True:
        print('----------主菜单----------')
        print('您好，欢迎使用ATM')
        print('查询余额\t输入【1】')
        print('存款\t输入【2】')
        print('取款\t输入【3】')
        print('退出\t输入【4】')
        try:
            n = int(input('请输入选项'))
        except ValueError:
            print('invalid value')
            continue    
        if n == 1:
            print(f'{name},您好，您的余额剩余：{money}')
        if n == 2:
            while True:
                try:
                    amount = float(input("请输入存款金额"))
                except ValueError:
                    print('请输入正确格式的金额')
                    continue
                if amount >= 0:
                    money += amount
                    print(f'{name}，您好，您存款{amount}元成功')
                    print(f'{name},您好，您的余额剩余：{money}')
                    break
                else:
                    print('请输入正确的金额')
                    continue

        if n == 3:
            while True:
                try:
                    amount = float(input("请输入取款金额"))
                except ValueError:
                    print('请输入正确格式的金额')
                    continue
                if amount >= 0 and amount <= money:
                    money -= amount
                    print(f'{name}，您好，您取款{amount}元成功')
                    print(f'{name},您好，您的余额剩余：{money}')
                    break
                else:
                    print('请输入正确的金额')
                    continue
        if n == 4:
            print('已退出')
            break

