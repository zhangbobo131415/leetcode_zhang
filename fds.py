
# # n = int(input())
# # nums = [int(i) // 500 for i in input().split()]
# n = 5
# nums = [8,8,6,6,4]
# nums.sort()
# zonghe = sum(nums)

# tem = [False for i in range(sum(nums))]
# tem[0] = True
# tem.append(True)
# length = zonghe
# for k in nums:
#     if k<=length:
#         tem[k] = True
# for index, num in enumerate(nums):
#     if index == 0:
#         continue
#     for j in range(length, num, -1):
#         tem[j] = tem[j] or tem[j - num]
# min_ss = sum(nums)
# out_index = 0
# for index, num in enumerate(tem):
#     if num == True:
#         if min_ss > abs(zonghe - 2 * index):
#             min_ss = abs(zonghe - 2 * index)
#             out_index = index
# print(max(out_index,zonghe-out_index))

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Test_26 {
public static void main (String[] args)
{
    Scanner in = new Scanner(System.in);
    //获取输入的个数
    int num = in.nextInt();
    List<Integer> number = new ArrayList<>();
    //将输入的数字装入number列表里面去
    for(int i = 0;i<num;i++){
        number.add(in.nextInt());
    }
    //初始化一个key，这个key将指向头或者尾部的元素
    int flagNum = 0;
    //首先获取投或者尾部中最小的一个值设为起始的key的位置
    int j = number.get(0) > number.get(number.size()-1)?number.size()-1: 0;
    //用来计算最少次数
    int count = 0;
    //一直循环，直到数组有序则结束
    while(true){
        //首先获取key位置对应的值，不是第一个就是最后一个
        flagNum = number.get(j);
        //记录 数组中某个离当前key最近的元素，也就是他们两个挨得比较近。比如1 5 3
        int index = -1;
        //初始化两个元素之间的差值，因为我们需要寻找数组中的任意一个元素与key所指向的值的最小值
        int min = 1;
        //如果j = 0，表示当前的key是第一个元素。初始化一个值，作为一个基准值，然后更新。寻找最接近他的值
        if(j == 0){
            //第一个元素作为基准的话，需要寻找跟她比较贴近的值
            int tempmin =number.get(0) - number.get(1);
            //判断是否大于等于0，因为所有的元素都不相同，所有不可能存在等于0 。但是我们需要找比他小的，也就是差值最小都为1的，
            //如果两者的差值不大于0，我们将置min为1，大于0则设置为他们的差值
            min = tempmin>=0?tempmin:1;
        }
        //j = 1表示在尾部，在尾部的话我们需要拿第一个元素与当前的key对应位置的值相减，也就是最后一个是key所在的位置了
        else{
            //
            int tempmin = number.get(0) - number.get(number.size() - 1);
            min = tempmin>=0?tempmin:1;
        }
        //循环交换
        for(int i=0;i< number.size();i++){
            //定义一个temp作为两个元素的差值，然后与min对比，谁最小就取谁
            int temp ;
            if(j == 0 ){
                //j =0表示key在第一个，我们需要用key值减去下一个作为基准开始比较
                temp  = flagNum - number.get(i);
            }else{
                //key的位置在最后，需要前面的元素值减去 key的值
                temp  = number.get(i) - flagNum;
            }
            //比较当前的差值与上一步计算得到的min值谁最小，谁小就取谁，然后记录他的index，因为等会我们需要将它放到key的前面或者后面。
            if(temp <= min && temp > 0){
                min = temp;
                index = i ;
            }
        }
        //index 不等于-1表示能找到与key最接近的数字，不然index = -1表示没找到比他小的，并且跟她比较接近的，那么key所在的位置就是这个数组中最小的数值了。
        if(index != -1){
            //j =0表示当前的key在头，我们需要将比他小的，最接近的那个值放到他的前面去。
            if( j == 0 )
            {
                    Integer t = number.get(index);
                    number.remove(index);
                    number.add(0,t);
                //继续将key设置为最后一个，如果当前的key找不到一个元素与他相近，说明该key是最小的了，需要换一下key的位置继续找
                    j = 0;

            }
            //当前的key所在的位置是在最后，因为我们需要将比他大的元素放到他的后面，直接add即可，然后把原来他所在的位置上的元素删除。
            else if(j == number.size() -1){
                number.add(number.get(index));
                number.remove(index);
                //继续将key设置为最后一个，如果
                j = number.size()-1;
            }
            //记录一下移动的次数
            count++;
            index = -1;
        }
        //判断一下该序列是否已经有序了，有序就结束了。
        if(isSort(number)){
            break;
        }
    }
    System.out.println(count);
}
public static  Boolean isSort(List<Integer> num){

    for(int i = 0;i< num.size() - 1;i++){
        if( num.get(i) > num.get(i+1)){
            return false;
        }
    }
    return true;
}
}



