import time
from cache_decorator import cache



#1. Function with positional arguments and a time delay
@cache
def heavy_computation(a: int, b: int) -> int:
    time.sleep(2)  
    return a ** b



#2. Function with strings and a default keyword argument
@cache
def format_user_card(name: str, age: int, role: str = "user") -> str:
    return f"User: {name.capitalize()}, Age: {age}, Role: {role.upper()}"



#3. Function with arbitrary arguments (*args, **kwargs)
@cache
def calculate_total_price(*args: float, discount: float = 0.0) -> float:

    total = sum(args)

    return total - (total * discount)



if __name__ == "__main__":
    print("Test 1: Math Operations")
    #First call will take 2 seconds and print [heavy_computation] Executing function...
    print("Result 1:", heavy_computation(2, 10)) 
    
    #Second call will return instantly and print [heavy_computation] Returning result from cache!
    print("Result 2:", heavy_computation(2, 10)) 

    print("\nTest 2: String Processing")
    print("First call:", format_user_card("matvii", 20, role="admin"))
    print("Second call (cached):", format_user_card("matvii", 20, role="admin"))
    
    #Function will execute again because the parameters are different
    print("Third call (not cached):", format_user_card("alex", 25))

    print("\nTest 3: *args and **kwargs")
    print("First call:", calculate_total_price(100.0, 50.0, 200.0, discount=0.1))
    print("Second call (cached):", calculate_total_price(100.0, 50.0, 200.0, discount=0.1))