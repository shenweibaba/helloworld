package june;

/**
 * 求1+2 + 。。。 + n
 * 要求不能使用乘除法，for while if else switch case 以及条件判断语句
 * @author shenwei1
 *
 */
public class Progression
{
    // 方法一 直接使用递归
    public int Sum_Solution(int n) {
        if (n == 1)
        {
            return 1;
        }
        else
        {
            return n + Sum_Solution(n -1);
        }
    }
    
    /**
     * 方法二 使用短路求值原理
     * @param n
     * @return
     */
    public int sum_solution2(int n)
    {
        int sum = n;
        boolean falg = (sum > 0) && ((sum += sum_solution2(sum - 1)) > 0);
        return sum;
    }
    
    
    
}
