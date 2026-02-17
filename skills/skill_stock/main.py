def main(params):
    # 获取参数（如公司名称）
    company = params.get("company", "苹果公司")
    
    # 这里可以替换为真实的股价查询逻辑（如调用 API）
    # 示例：返回模拟数据（后续可替换为真实 API）
    return f"{company}的股价为：$150.00"
