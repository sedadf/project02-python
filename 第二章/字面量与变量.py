# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} X {i}={i*j}",end=" \t")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f"{j}",end=" ")
#     print()

# for i in range(1,9):
#     for j in range(1,9):
#         if (i%2==1 and j%2==1) :
#             print("*",end=" ")
#         elif (i%2==0 and j%2==0):
#             print("*",end=" ")
#         else:
#             print("+",end=" ")
#     print()
# 解包
# num_list1=[]
# num_list2=[]
# num_list=[*num_list1,*num_list2]
# num_list=[i**2 for i in range(1,21)]
# print(num_list)
# num_list=[i**2 for i in range(1,21) if i%2==0]
# print(num_list)
# mail=input()
# if mail.count('@')==1 and '.'in mail:
#     print(f"{mail}")
# else:
#     print(f"no")
# t1=(1,2,3,4,5,6,7,8)
# a ,*b=t1

# *a,b=t1

# a,*b,c=t1
# print(a)
# print(b)
# print(c)

# a=10
# b=20
#
# a,b=b,a
# t=b,a
# a,b=t
# print(a,b)

# student=(
# ()
# ()
# )
# for id,name,chinese,math,english in student:
#
# dic1={}
# dic1['zs']=130
# print(dic1)

shopping_cart={"Meta80":{'price':6999,'num':2}}
menu="""

      购物车菜单
      1添加
      2修改
      3删除
      4查询
      5退出
"""
print("欢迎使用")
while True:
    print(menu)
    choice = input("请选择")
    match choice:
        case '1':
            goods_name = input("请输入商品名称")
            goods_price = float(input("请输入商品价格"))
            goods_num = int(input("请输入商品数量"))
            #       如果商品存在不添加
            if goods_name in shopping_cart:
                print("已存在")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
        case '2':
            goods_name = input("请输入最新商品名称")
            if goods_name not in shopping_cart:
                print("不存在")
                continue
            goods_price = float(input("请输入最新商品价格"))
            goods_num = int(input("请输入最新商品数量"))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("已修改")
        case '3':
            goods_name = input("请输入要删除商品名称")
            if goods_name not in shopping_cart:
                print("不存在")
            else:
                del shopping_cart[goods_name]
                print("删除完毕")
        case '4':
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
            print(f"{goods_name},{goods_info['price']},{goods_info['num']}")
        case '5':
            print("拜拜")
            break
        case _:
            print("非法操作")







































