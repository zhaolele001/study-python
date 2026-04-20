#异常处理


try:
    print("=" * 100)
    # print(my_name)
    print(1/0)
    print("-" * 100)
except NameError as e:
    print("错误信息:", e)
except ZeroDivisionError as e:
    print("0错误：", e)
except Exception as e:
    print("未知异常")
finally:
    print("彻底结束!")
