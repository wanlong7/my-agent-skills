def main(params):
    command = params.get("command", "get_stock_price")
    if command == "get_stock_price":
        company = params.get("company", "苹果公司")
        return f"{company}的股价为：$150.00"
    else:
        return "未知命令"
