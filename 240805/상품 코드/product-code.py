#클래스 선언
class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

#제품1 선언 및 초기화
product1 = product('codetree', 50)

#제품2 선언 및 입력
product_name, product_code = tuple(input().split())
product2 = product(product_name, int(product_code))

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")