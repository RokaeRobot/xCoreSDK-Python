def print_log(func_name,ec,detail_info=""):
    """打印错误信息"""
    print(f"{func_name}:{ec['message']}")
    if detail_info != "":
        print(detail_info)
        
def print_separator(title:str,separator:str = "-",length:int = 90):
    """打印分隔符"""
    total_len = length
    title_len = len(title)
    pre_len = (total_len - title_len) // 2
    suf_len = total_len - title_len - pre_len
    print(separator*pre_len + title + separator*suf_len)