from models import Order, OrderStatus, User

# ✅ 1. 函数签名必须带类型提示
# 参数 order 必须是 Order 类型，返回值必须是 bool
def process_order(order: Order) -> bool:
    print(f"📦 Processing order: {order.order_id}")
    
    # 模拟业务逻辑
    if order.total_price == 0:
        print("❌ Order rejected: Price cannot be zero.")
        return False
        
    if not order.items:
        print("❌ Order rejected: Empty items.")
        return False

    # 模拟改变状态
    # 在 Python 里直接修改属性，不需要 setter
    print(f"   Current status: {order.status.value}")
    order.status = OrderStatus.DELIVERED
    print(f"   New status: {order.status.value}")
    
    print(f"✅ Order processed successfully. Total: ${order.total_price}")
    return True

if __name__ == "__main__":
    # 1. 创建一个合法的 User (虽然这个 demo 还没用到，但作为上下文很重要)
    user = User(user_id=1, name="Gemini", email="gemini@google.com")
    # 2. 创建一个合法的 Order
    # 注意：这里我们故意用 total_price=100.0，这会通过 models.py 里的校验
    my_order = Order(
        order_id="ORD-2024",
        items=["RTX 4090", "Intel i9"],
        total_price=2000.0,
        status=OrderStatus.PENDING
    )
    # 3. 调用函数
    result = process_order(my_order)
    print(f"\nResult: {result}")