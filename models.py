from enum import Enum
from pydantic import BaseModel, field_validator, ValidationError
from typing import Optional

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    
class User(BaseModel):
    user_id: int
    name: str
    email: Optional[str] = None

class Order(BaseModel):
    order_id: str
    items: list[str]
    total_price: float
    status: OrderStatus = OrderStatus.PENDING

    @field_validator('total_price')
    @classmethod
    def check_price_positive(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Total price must be positive")
        return v
    
if __name__ == "__main__":
    try:
        print("Creating invalid order...")
        invalid_order = Order(
            order_id="ORD-001",
            items=["Apple", "Banana"],
            total_price=-50.0,  # ❌ 故意传入负数
            status=OrderStatus.PENDING
        )
    except ValidationError as e:
        print(f"Pydantic Validation Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")
    else:
        print("Order created successfully:", invalid_order)

        
