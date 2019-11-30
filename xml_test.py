import xml.etree.ElementTree as eltree

if __name__ == '__main__':
    tree = eltree.parse(r'l-2698.xml')
    root_iter = tree.iter('object')
    res = []
    for i in root_iter:
        tem = i.getchildren()
        tem_res = []
        for jj in tem:
            if jj.tag == 'name':
                tem_res.append(jj.text)
                # print(type(jj.text))
            if jj.tag == 'bndbox':
                # print(type(jj[0].text))
                # 直接读取输出的均为字符串格式
                tem_res.extend(map(eval, [jj[0].text, jj[1].text, jj[2].text, jj[3].text]))
                pass

        res.append(tem_res.copy())
        tem_res.clear()
    print(len(res))
    print(res)


def back(root):
    tem = root.getchildren()
    while len(tem) != 0:
        if tem[0].tag == 'BFOV':
            print(tem[0].tag, tem[0].text)
        temm = tem[0].getchildren()
        tem.pop(0)
        tem.extend(temm)

# findall 函数只能返回子节点中找到的目标节点，切记。并不能找到整棵树中目标tag的节点
# AAA = tree.findall('xmin')
# print(len(AAA))
# root = tree.getroot()
# tem = root.findall('name')
# print(len(tem))
# # print(dir(root))
# print(root.tag, root.attrib, root.text, root.tail)
# # back(root)
