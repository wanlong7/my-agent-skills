   def get_stock_info(args, agent=None):
       """获取股票信息"""
       stock_code = args.get("stock_code")
       return f"股票 {stock_code} 的当前价格为 $150.00"
   
