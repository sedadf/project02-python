# def test1(*args,**kwarge):
#     if kwarge.get("") is not None:
#         print(kwarge.get(""))
#     if kwarge.get("") :
#         print()
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def calc(a,b,oper):
#     return oper(a,b)

# def calc_order_cost(*args:tuple[str,int|float,int],coupon=0,score=0,express=0.0)->float|int :
#     """
#
#     :param args: 商品信息：（商品名，价格，数量），例：（“鼠标”，100，20）
#     :param score: 积分
#     :param express: 运费
#     :return: 总金额=商品总金额-优惠劵-积分抵用+运费
#     """
#     total_price=[goods[1]*goods[2] for goods in args]
#     total_cost=sum(total_price)
#
#     if total_cost>=5000 and coupon<=total_cost:
#         total_cost-=coupon
#
#     if total_cost>=5000 and score//100<=total_cost:
#         total_cost-=score//100
#
#     total_cost+=express
#
#     return total_cost

# if __name__ == '__main__':
#     print('1')

