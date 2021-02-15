"""清理 DNSCrypt public-resolvers.md 文件.

排除来源自中国或者与匿名性不相容的服务提供者
"""


def clean_provider():
    """清理函数.

    读取当前目录下 public-resolvers.md, 筛选之后按原格式写入新的md文件
    """
    section_title = ""
    section_content = []
    provider_section = {}

    with open("public-resolvers.md", "r") as fr, open(
        "cleaned_public_resolvers.md", "a"
    ) as fw:
        for line in fr:
            if "##" in line:
                section_title = line
                section_content.clear()
            else:
                section_content.append(line)

            provider_section[section_title] = section_content.copy()

        for k, v in provider_section.items():
            elstr = ""
            for el in v:
                elstr += str(el)

            if all(["china" not in elstr.lower(), "warning" not in elstr.lower()]):
                fw.write(k+str(elstr))


if __name__ == "__main__":

    clean_provider()
