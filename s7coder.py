import base64


class S7Coder:
    def __init__(self):
        # 标准码表
        self.std_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        # 变形后的码表
        self.trans_table = "Vg21WQ5KdRt0yNpcr9m4O3PoHaZvsLeCY8FjSwiTkUbuEBIJlAG7fqXM6xDnzh-;"

    def encode(self, text: str) -> str:
        text = text.encode()
        results = str(base64.b64encode(text), encoding="utf-8").translate(str.maketrans(self.std_table, self.trans_table))
        return results.replace("=", "_")

    def decode(self, text: str) -> str:
        text = text.replace("_", "=")
        map_table = str.maketrans(self.trans_table, self.std_table)
        trans_text = text.translate(map_table)
        result = str(base64.b64decode(trans_text), encoding="utf-8")
        return result


_inst = S7Coder()
encode = _inst.encode
decode = _inst.decode


def test():
    s7code = "HPNfcPLwLQhjawhUviaJRT9UvPOhy4HMN4r7y7yfNGaBa1OhHj3iaj3jp1SGN1ylHP9ia1w8N4HMpPdxp48FHX98y7Via53XZPNwoXwS" \
             "c3LR4jy7p13FHPWqajYfyjy6yj9Sy4Rwa5Wxy598Hj3iNjWfRT3UvjfAy7VAy4rlymaXaodhym6GyG6ARiQlZPwSc4WAy2aEHPxTc4Vi" \
             "HXhqvT9Ge4q14Fa7NXOhyr__"

    d = decode(s7code)
    e = encode("act=get_cf_info&time=1675433347&md5=b5ff5c892430adfd9a5679b998bcda30&device_id"
               "=WIN3385baa5f8423824d12eda90dab5f614&uin=13011401&ver=1.23.1&apiid=110&lang=0&country=CN&s7e=1") 

    print(d)
    print("-"*40)
    print(e)


if __name__ == '__main__':
    test()
