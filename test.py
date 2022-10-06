
def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    return lambda x:f(x)


def two(f):
    return lambda x:f(f(x))

three = successor(two)


def church_to_int(n):
    f = lambda x : x+1
    return n(f)(0)

def add_church(m, n):
    return lambda f:lambda x:m(f)(0)+n(f)(0)

def funny(joke):
    hoax = joke + 1
    return funny(hoax)

def sad(joke):
    hoax = joke - 1
    return hoax + hoax

def double(x):
    return double(x + x)

first = double

def double(y):
    return y + y

def add(n):
    return n+100000
def sub(n):
    return n-n%100000
def mod(n):
    return n%100000
def div(n):
    return n//100000

def hailstone(n):
    print(mod(n))
    # cnt+=1
    add(n)
    if mod(n)==1:
        return div(n)+1
    if n%2==0:
        return hailstone(sub(n)+(mod(n)//2))+1
    else:
        return hailstone(sub(n)+mod(n)*3+1)+1

def solve(n1,n2):#合并两个有序的
    n1 = str(n1)
    n2 = str(n2)
    i,j=0,0
    ans=""
    while i<len(n1) and j<len(n2):
        if n1[i]>=n2[j]:
            ans+=n1[i]
            i+=1
        else:
            ans+=n2[j]
            j+=1
    while i<len(n1):
        ans+=n1[i]
        i+=1
    while j<len(n2):
        ans+=n2[j]
        j+=1
    return ans

def merge(n1, n2):
    #Error: merge(0,0)
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1<10 and n2<10:
        return solve(n1,n2)
    n1 = merge(n1//10,n1%10)
    n2 = merge(n2 // 10, n2 % 10)
    x = int(solve(n1,n2))
    while x%10==0:
        x=x//10
    return x

def num_eights(pos):
    if pos==0:
        return 0
    if pos%10==8:
        return 1+num_eights(pos//10)
    else:
        return num_eights(pos//10)

def pingpong(n):

    def cal(x,dif,val):
        if x==n:
            return val
        if x%8==0 or num_eights(x):
            return cal(x+1,-dif,val-dif)
        else :
            return cal(x+1,dif,val+dif)
    return cal(1,1,1)

def next_larger_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def count_coins(change):


    def get(change,pre):
        if change==0:
            return 1
        ans=0
        now=pre
        while now!=None and now<=change:
            ans += get(change-now,now)
            now = next_larger_coin(now)
        return ans

    return get(change,1)
def uuu():
    yield 5
    yield 6
    yield 7

def cal(baoji,baoshang,dagongji,xiaogongji,dashengming,xiaoshengming,jingtong):
    return baoji*2+baoshang+dagongji*1.33*0.5+xiaogongji*0.398*0.5*0.5+dashengming*1.33*0.8+xiaoshengming*0.026*0.66*0.8+jingtong*0.33*0.75
if __name__=='__main__':
    bei = cal(0,12.4,0,33,15.2,0,0)
    sha = cal(6.2,14,0,0,0,747,0)
    tou = cal(0,6.2,0,0,14,0,0)
    mao = cal(11.7,13.2,9,9,0,0,0)
    hua = cal(13.2,5.4,0,0,8.7,0,0)
    touplus = cal(0,15.5,0,0,20.4,0,0)
    huaplus = cal(7,10.9,0,0,5.8,0,63)
    shaplus = cal(11.7,6.2,0,0,16.3,0,0)
    # print(touplus)
    # print(tou)
    #散件头比追忆头高16  57-41
    #追忆花41,散件花46
    #追忆火伤杯32分,最好的火伤杯
    #追忆毛43分，散件55分
    #追忆精通沙36分，散件精通沙（36双爆），散件攻击沙 47分+一个词条
    print(57+41+32+43+36)

# for i in range(1,101):
    #     print(count_coins(i))
