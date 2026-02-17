def main(args, agent=None):
    """查询股票实时价格"""
    stock_code = args.get("code", "000001")
    # 这里添加实际的股票查询逻辑（如调用API）
    return f"股票 {stock_code} 的价格是：¥100.00"
