'''
本模块储存了蒙特卡洛模拟、遗传算法和模拟退火算法，用于简易模拟

This module stores Monte Carlo, Genetic Algorithm and Simulated Annealing Algorithm for simple simulation
'''
import random
import numpy as np


class MC():
    '''
    蒙特卡洛模拟
    
    参数
    ----
    loop：整型，可选，循环次数，默认为1000
    random_type：字符串类型或函数类型，可选，可以取'random'、'randint'或自定义函数(无参数，需输出length * dim的二维ndarray)，默认'random'
    random_state：整型，可选，随机种子
    begin：整型，可选，表示整数随机序列的开始数字，仅当random_type='randint'时起作用
    end：整型，可选，表示整数随机序列的结束数字，仅当random_type='randint'时起作用
    
    属性
    ----
    loop：整型，循环次数
    random_type：字符串类型，取随机的方法
    EX：数类型，select函数返回值的数学期望
    DX：数类型，select函数返回值的方差
    history：字典类型，历史EX和DX值
    
    
    Monte Carlo
    
    Parameters
    ----------
    loop: int, callable, loop count, default = 10000
    random_type: str or function, callable, 'random', 'randint' and function(no parameter, output a 2-D ndarray with size length * dim) are optional, default = 'random'
    random_state: int, callable, random seed
    begin: int, callable, beginning number of the random sequence, it's used only when random_type='randint'
    end: int, callable, end number of the random sequence, it's used only when random_type='randint'
    
    Atrributes
    ----------
    loop: int, loop count
    random_type: str, the method of generating random number
    EX: num, mathematical expectation of return value of select function
    DX: num, variance of return value of select function
    history: dict, historical EX and DX
    '''
    def __init__(self, loop=1000, random_type='random', random_state=None, begin=None, end=None):
        self.loop = loop
        self.random_type = random_type
        self.history = {'EX':[], 'DX':[]}
        self.__begin = begin
        self.__end = end
        np.random.seed(random_state)
    

    def sel_ind(self, condition):
        '''
        用于快速构建条件函数
        将condition函数作用于随机序列全部元素
        任意一个状态满足condition，则会输出1，否则输出0
        
        参数
        ----
        condition：函数，判断一个状态是否符合条件的函数，要求符合则输出True，不符合则输出False

        返回
        ----
        一个新函数


        for quick construction of condition function
        apply condition function to all elements of random sequence
        if any state is qualified, 1 will be reutrn, otherwise 0 will be return
        
        Parameters
        ----------
        condition: function, a function that determines if a state is qualified. If qualified, return True, otherwise reutrn False

        Return
        ------
        a new function
        '''
        def obj(x):
            for i in x:
                if condition(i):
                    return 1
            return 0
        return obj

    
    def sel_any(self, n, condition):
        '''
        用于快速构建条件函数
        将condition函数作用于随机序列全部元素
        至少任意n个状态满足condition，则会输出1，否则输出0
        
        参数
        ----
        n：int类型
        condition：函数，判断一个状态是否符合条件的函数，要求符合则输出True，不符合则输出False

        返回
        ----
        一个新函数


        for quick construction of condition function
        apply condition function to all elements of random sequence
        if at least any_n states are qualified, 1 will be reutrn, otherwise 0 will be return
        
        Parameters
        ----------
        n: int
        condition: function, a function that determines if a state is qualified. If qualified, return True, otherwise reutrn False

        Return
        ------
        a new function
        '''
        def obj(x):
            calcu_ = 0
            for i in x:
                if condition(i):
                    calcu_ += 1
                if calcu_ >= n:
                    break
            if calcu_ >= n:
                return 1
            else:
                return 0
        return obj
    
    
    def sel_con(self, n, condition):
        '''
        用于快速构建条件函数
        将condition函数作用于随机序列全部元素
        至少连续n个状态满足condition，则会输出1，否则输出0
        
        参数
        ----
        n：int类型
        condition：函数，判断一个状态是否符合条件的函数，要求符合则输出True，不符合则输出False

        返回
        ----
        一个新函数


        for quick construction of condition function
        apply condition function to all elements of random sequence
        if at least con_n consecutive states are qualified, 1 will be reutrn, otherwise 0 will be return
        
        Parameters
        ----------
        n: int
        condtition: function, a function that determines if a state is qualified. If qualified, return True, otherwise reutrn False
        
        Return
        ------
        a new function
        '''
        def obj(x):
            calcu_ = 0
            for i in x:
                if condition(i):
                    calcu_ += 1
                else:
                    calcu_ *= 0
                if calcu_ >= n:
                    break
            if calcu_ >= n:
                return 1
            else:
                return 0
        return obj
    
    
    def __one_experiment(self, length, dim, select):
        '''
        进行一次完整的实验
        '''
        if self.random_type == 'random':
            random_list_ = np.random.rand(length, dim)

        elif self.random_type == 'randint':
            random_list_ = np.random.randint(self.__begin, self.__end + 1, size=(length, dim))
        
        else:
            random_list_ = self.random_type()

        #如果随机序列满足select，就算实验成功输出1，否则算失败输出0
        if type(select).__name__ == 'function':
            return select(random_list_)
        else:
            judge_ = 1
            for li in select:
                if li(random_list_):
                    judge_ *= 1
                else:
                    judge_ *= 0
            return judge_


    def fit(self, length, dim, select):
        '''
        进行蒙特卡洛模拟
        
        参数
        ----
        length：整型，随机序列长度
        dim：整型，随机序列元素维度
        select：条件函数或函数列表，select函数应该以length * dim的二维ndarray为自变量
            select函数用于甄别某一个随机矩阵是否符合预期，符合输出1，不符合输出0
            select函数同时也可以输出其他值以满足实际需求
            select若为函数列表，则要求每个函数只能输出1或0

        
        Simulate
        
        Parameters
        ----------
        length: int, the length of random sequence
        dim: int, dimension of elements in random sequence
        select: function or function list, select function should take 2-dimension ndarray(length * dim) as independent variable
            select function used for Identifying whether the random matrix meets the expectation, if meets, output 1, otherwise output 0
            select function can also output other values to meet the actual demand
            if select is a list, every function in the list can only output 1 or 0
        '''
        final_propability_ = []
        for i in range(self.loop):
            freq_ = MC.__one_experiment(self, length=length,\
                dim=dim, select=select)
            final_propability_.append(freq_)
        
        self.EX = np.mean(final_propability_)
        self.DX = np.var(final_propability_)
        self.history['EX'].append(self.EX)
        self.history['DX'].append(self.DX)


class GA():
    '''
    遗传算法
    
    参数
    ----
    population：整型，种群数
    iteration: 整型，迭代次数（自然选择次数）
    random_type：字符串类型，可选，可以取'random'和'randint'，默认'random'
    select：字符串类型或函数类型，可选，选择个体的方法，可以取'rw'、'st'或者自定义函数，默认'rw'
        'rw'：基于随机接受的轮盘赌选择
        'st'：随机竞争选择
    crossover：字符串类型或函数类型，可选，交叉互换的方法，可以取'uniform'、'point'或者自定义函数，默认'uniform'
        'uniform'：均匀交叉
        'point'：单点及多点交叉
    begin：整型，可选，表示整数随机序列的开始数字，仅当random_type='randint'时起作用
    end：整型，可选，表示整数随机序列的结束数字，仅当random_type='randint'时起作用
    random_state：整型，可选，随机种子
    select_rate：浮点数类型，可选，选择率（存活率），默认0.3
    mutate_rate：浮点数类型，可选，变异率，默认0.05
    crossover_rate：浮点数类型，可选，基因交叉概率，默认0.5
    repeat：布尔类型，可选，是否允许序列元素重复，默认为True，仅在random_type='randint'时起作用
    
    属性
    ----
    population：整型，种群数
    iteration：整型，迭代次数（自然选择次数）
    random_type：字符串类型，取随机的方法
    select：字符串类型，选择个体的方法
    crossover：字符串类型，交叉互换的方法
    dom：二维ndarray，优势种群
    dom_fitness：一维ndarray，优势种群的适应度
    

    
    Genetic Algorithm
    
    Parameters
    ----------
    population: int, the population size
    iteration: int, the times of iterations( the times of natural selection)
    random_type: str, callable, 'random' and 'randint' are optional, default = 'random'
    select: string or function, callable, the method of selecting individuals, 'rw', 'st' or custom function, default = 'rw'
        'rw': Roulette Wheel Selection
        'st': Stochastic Tournament Selection
    crossover: string or function, callable, the method of crossing over, 'uniform', 'point' or custom function, default = 'uniform'
        'uniform': Uniform Crossover
        'point': Multi-point Crossover
    begin: int, callable, beginning number of the random sequence, it's used only when random_type='randint'
    end: int, callable, end number of the random sequence, it's used only when random_type='randint'
    random_state: int, callable, random seed
    select_rate: float, callable, selection rate( survival rate), default=0.3
    mutate_rate: float, callable, variation rate, default=0.05
    crossover_rate: float, callable, gene crossover probability, default=0.5
    repeat: bool, callable, whether sequence elements are allowed to repeat, default=True, only works when random_type='randint'
    
    Atrributes
    ----------
    population: int, the population size
    iteration: int, the times of iterations( the times of natural selection)
    random_type: str, the method of generating random number
    select: str, the method of selecting individuals
    crossover: str, the method of crossing over
    dom: 2-D ndarray, the dominance
    dom_fitness: 1-D ndarray, the fitness of the dominance
    '''
    def __init__(self, population=1000, iteration=100, random_type='random', select='rw', crossover='uniform', begin=None,
                 end=None, random_state=None, select_rate=0.3, mutate_rate=0.05, crossover_rate=0.5, repeat=True):
        self.population = population
        self.iteration = iteration
        self.random_type = random_type
        self.select = select
        self.crossover = crossover
        self.__begin = begin
        self.__end = end
        self.__select_rate = select_rate
        self.__mutate_rate = mutate_rate
        self.__crossover_rate = crossover_rate
        self.__repeat = repeat
        np.random.seed(random_state)
    
    
    def __mutate_func(self, length, populations_matrix):
        '''
        完成对新一代的变异
        '''
        mutate_matrix = np.random.rand(self.population, length) - self.__mutate_rate
        mutate_matrix = np.argwhere(mutate_matrix <= 0)

        if self.random_type == 'random':
            for i in mutate_matrix:
                populations_matrix[i[0], i[1]] = random.random()
        
        elif self.random_type == 'randint':
            if self.__repeat:
                for i in mutate_matrix:
                    populations_matrix[i[0], i[1]] = random.randint(self.__begin, self.__end)
                
            else:
                for i in mutate_matrix:
                    random_value = random.randint(self.__begin, self.__end)
                    index = np.where(populations_matrix[i[0]]==random_value)[0]
                    if len(index) == 0:
                        populations_matrix[i[0], i[1]] = random_value
                    else:
                        populations_matrix[i[0], index[0]] = populations_matrix[i[0], i[1]]
                        populations_matrix[i[0], i[1]] = random_value
        
        return populations_matrix
    
    
    def __repeat_adjust(self, child_individual_1, child_individual_2, random_loc_list):
        '''
        调整序列使得序列不存在重复元素
        '''
        mask = np.ones(child_individual_1.shape[0], bool)
        mask[random_loc_list] = False
        d_loc_list = np.where(mask)[0]
        child_11 = child_individual_1[random_loc_list].copy()    # 被交叉互换的片段
        child_12 = child_individual_1[d_loc_list].copy()         # 未被交叉互换的片段
        child_21 = child_individual_2[random_loc_list].copy()    # 被交叉互换的片段
        child_22 = child_individual_2[d_loc_list].copy()         # 未被交叉互换的片段

        for i in range(len(child_12)):
            while child_12[i] in child_11:
                index = np.where(child_11 == child_12[i])[0][0]
                child_12[i] = child_21[index]
            child_individual_1[d_loc_list] = child_12
        
        for i in range(len(child_22)):
            while child_22[i] in child_21:
                index = np.where(child_21 == child_22[i])[0][0]
                child_22[i] = child_11[index]
            child_individual_2[d_loc_list] = child_22
        
        return child_individual_1, child_individual_2
    
    
    def __crossover(self, num_point, length, parent_matrix, func_type):
        '''
        交叉
        '''
        #begin
        if num_point:
            if num_point > length:
                raise Exception("'num_point' should be less than 'length'.")
        #end
        
        num_of_parents = len(parent_matrix)
        child_matrix = []
        child_population = self.population - num_of_parents
        
        while len(child_matrix) < child_population:
            while True:
                random_num_1 = random.randint(0, num_of_parents - 1)
                random_num_2 = random.randint(0, num_of_parents - 1)
                if random_num_1 != random_num_2:
                    break
            child_individual_1 = parent_matrix[random_num_1]
            child_individual_2 = parent_matrix[random_num_2]
            #begin
            child_individual_1, child_individual_2, random_loc_list = func_type(self, num_point, length, child_individual_1, child_individual_2)
            if not self.__repeat:
                child_individual_1, child_individual_2 = GA.__repeat_adjust(self, child_individual_1, child_individual_2, random_loc_list)
            #end
            child_matrix.append(child_individual_1)
            child_matrix.append(child_individual_2)
        child_matrix = np.array(child_matrix)
        child_matrix = np.concatenate([parent_matrix, child_matrix])
        return child_matrix
    

    def __point_crossover(self, num_point, length, child_individual_1, child_individual_2):
        '''
        多点交叉
        
        
        Multi-point Crossover
        '''
        random_loc_list = []
        for j in range(num_point):
            while True:
                random_loc = random.randint(0, length - 1)
                if random_loc not in random_loc_list:
                    random_loc_list.append(random_loc)
                    break
            medium_gene = child_individual_1[random_loc]
            child_individual_1[random_loc] = child_individual_2[random_loc]
            child_individual_2[random_loc] = medium_gene
        return child_individual_1, child_individual_2, random_loc_list
    
    
    def __uniform_crossover(self, num_point, length, child_individual_1, child_individual_2):
        '''
        均匀交叉
        
        
        Uniform Crossover
        '''
        random_loc_list = []
        for j in range(length):
            crossover_possibility = random.random()
            if crossover_possibility <= self.__crossover_rate:
                medium_gene = child_individual_1[j]
                child_individual_1[j] = child_individual_2[j]
                child_individual_2[j] = medium_gene
                random_loc_list.append(j)
        return child_individual_1, child_individual_2, random_loc_list
    
    
    def __st(self, parent_matrix, fitness, num_dead):
        '''
        随机竞争选择
        num_dead: 整型，死亡的数量
        
        
        Stochastic Tournament
        num_dead: int, the number of dead individual
        '''
        num_of_parents = len(parent_matrix)
        
        for i in range(num_dead):
            while True:
                random_num_1 = random.randint(0, num_of_parents - i - 1)
                random_num_2 = random.randint(0, num_of_parents - i - 1)
                if random_num_1 != random_num_2:
                    break
            if fitness(parent_matrix[random_num_1]) <= fitness(parent_matrix[random_num_2]):
                parent_matrix = np.delete(parent_matrix, random_num_1, axis=0)
            else:
                parent_matrix = np.delete(parent_matrix, random_num_2, axis=0)
        return parent_matrix
    
    
    def __rw(self, parent_matrix, fitness, num_alive):
        '''
        轮盘赌选择
        
        
        Roulette Wheel Selection
        '''
        fitness_list = []
        child_matrix = []
        
        for parent_individual in parent_matrix:
            fitness_list.append(fitness(parent_individual))
        max_fitness = max(fitness_list)
        
        while len(child_matrix) < num_alive:
            ind = np.random.randint(0, len(parent_matrix))
            a = np.random.rand()
            if np.random.rand() > fitness_list[ind] / max_fitness or\
                parent_matrix[ind].tolist() in np.array(child_matrix).tolist():
                pass
            else:
                child_matrix.append(parent_matrix[ind])
        parent_matrix = np.array(child_matrix)
        return parent_matrix
    
    
    def fit(self, length, fitness):
        '''
        进行遗传算法模拟
        
        参数
        ----
        length：整型，染色体长度
        fitness：函数类型，适应度函数
        
        
        Simulate
        
        Parameters
        ----------
        length: int, the length of chromosome
        fitness: funtion, fitness function
        '''
        self.__fitness = fitness
        if self.random_type == 'random':
            parent_matrix = np.random.rand(self.population, length)
        elif self.random_type == 'randint':
            if not self.__repeat:
                parent_matrix = []
                for i in range(self.population):
                    parent_matrix.append(random.sample(range(self.__begin, self.__end+1), length))
                parent_matrix = np.array(parent_matrix)
            
            else:
                parent_matrix = np.random.randint(self.__begin, self.__end, size=(self.population, length))
        else:
            raise Exception("'random_type' must be one of 'random' and 'randint'.")
        
        num_alive = self.population * self.__select_rate
        num_dead = int(self.population - num_alive)
        num_point = int(length * self.__crossover_rate)
        
        for i in range(self.iteration - 1):
            if self.select == 'rw':
                parent_matrix = GA.__rw(self, parent_matrix=parent_matrix, fitness=fitness, num_alive=num_alive)
            elif self.select == 'st':
                parent_matrix = GA.__st(self, parent_matrix=parent_matrix, fitness=fitness, num_dead=num_dead)
            elif type(self.select).__name__ == 'function':
                parent_matrix == self.select(parent_matrix, fitness)
            
            if self.crossover == 'uniform':
                parent_matrix = GA.__crossover(self, num_point=None, length=length,
                                               parent_matrix=parent_matrix, func_type=GA.__uniform_crossover)
            elif self.crossover == 'point':
                parent_matrix = GA.__crossover(self, num_point=num_point, length=length,
                                               parent_matrix=parent_matrix, func_type=GA.__point_crossover)
            
            parent_matrix = GA.__mutate_func(self, length, parent_matrix)
        
        if self.select == 'rw':
            parent_matrix = GA.__rw(self, parent_matrix=parent_matrix, fitness=fitness, num_alive=num_alive)
        elif self.select == 'st':
            parent_matrix = GA.__st(self, parent_matrix=parent_matrix, fitness=fitness, num_dead=num_dead)
        elif type(self.select).__name__ == 'function':
            parent_matrix == self.select(parent_matrix, fitness)
        
        self.dom = parent_matrix
        
        dominance_fitness = []
        for individual in parent_matrix:
            dominance_fitness.append(fitness(individual))
        self.dom_fitness = np.array(dominance_fitness)


class SA():
    '''
    模拟退火算法
    默认以评估函数select的最小值为最优值
    
    参数
    ----
    anneal：浮点数类型或函数类型，可选，退火方法，若为浮点数，则按T = anneal * T退火，默认为0.9
    step：浮点数类型，可选，步长倍率，每次生成的步长为step乘一个属于(-1, 1)的随机数，默认为1
    n：整型，可选，等温时迭代次数，默认为10
    random_state：整型，可选，随机种子
    
    属性
    ----
    anneal：浮点数类型或函数类型，退火方法
    step：浮点数类型，步长倍率
    n：整型，等温时迭代次数
    solution：浮点数类型，最优解
    value：浮点数类型，最优解的函数值
    
    
    Simulated Annealing Algorithm
    By default, the minimum value of the evaluation function 'select' is the optimal value
    
    Parameters
    ----------
    anneal: float or function, callable, annealing method, if type is float, it will be annealed with T = anneal * T, default=0.9
    step: float, callable, step, each generated step length = step * a random number belonging to (-1, 1), default=1
    n: int, callable, isothermal iterations, default=10
    random_state: int, callable, random seed
    
    Attributes
    ----------
    anneal: float or function, annealing method
    step: float, step
    n: int, isothermal iterations
    solution: float, optimal solution
    value: float, function value of optimal solution
    '''
    def __init__(self, anneal=0.9, step=0.1, n=10, random_state=None):
        self.anneal = anneal
        self.step = step
        self.n = n
        np.random.seed(random_state)
    
    
    def fit(self, initial, T, T0, select):
        '''
        参数
        ----
        initial：列表，初始解，select函数的输入值
        T：浮点数类型，初始温度
        T0：浮点数类型，退火温度
        select：函数，评估函数
        
        
        Parameters
        ----------
        initial: list, initial solution, the input value of select function
        T: float, initial temperature
        T0: float, annealing temperature
        select: function, evaluation function
        '''
        initial = np.array(initial, dtype=np.float)
        while T > T0:
            for i in range(self.n):
                random_x = 2 * self.step * (np.random.rand(*initial.shape) - 0.5)
                initial_copy = initial.copy()
                initial_copy += random_x
                if select(initial_copy) < select(initial):
                    initial = initial_copy
                else:
                    pro = random.random()
                    if pro < np.e**(-(select(initial_copy) - select(initial)) / T):
                        initial = initial_copy
            
            if type(self.anneal).__name__ == 'float':
                T *= self.anneal
            elif type(self.anneal).__name__ == 'function':
                T = self.anneal(T)
            else:
                raise Exception("Type of 'anneal' must be one of 'float' and 'function'.")
        
        self.solution = initial
        self.value = select(initial)


class GD():
    '''
    梯度下降法
    沿函数负梯度方向逐步下降进而得到函数的最优解，最优解默认为最小值
    
    参数
    ----
    ytol：浮点数类型，可选，连续两次迭代的函数值小于ytol时即停止迭代，默认为0.1
    step：浮点数类型，可选，步长倍率，每次生成的步长为step * 负梯度，默认为0.1
    acc：浮点数类型，可选，求导精度，默认为0.05
    
    属性
    ----
    solution：浮点数类型，最优解
    value：浮点数类型，最优解的函数值
    
    
    Gradient Descent
    The optimal solution of the function is obtained by gradually decreasing along the negative gradient direction
    The optimal solution is the minimum value by default
    
    Parameters
    ----------
    ytol: float, callable, when △f of two successive iterations is less than ytol, the iteration will stop, default=0.1
    step: float, callable, step, each generated step length = - step * gradient, default=1
    acc: float, callable, accuracy of derivation, default=0.05
    
    Attributes
    ----------
    solution: float, optimal solution
    value: float, function value of optimal solution
    '''
    def __init__(self, ytol=0.1, step=0.1, acc=0.05):
        self.ytol = ytol
        self.step = step
        self.acc = acc
    
    
    def fit(self, initial, select):
        initial = np.array(initial, dtype=np.float)
        f_change = float('inf')
        
        while f_change > self.ytol:
            # 计算偏导矩阵
            dy = select(initial + self.acc) - select(initial - self.acc)
            dx = np.ones_like(initial) * self.acc
            dy_dx = dy / dx
            
            # 计算函数值变化量
            f_change = select(initial)
            initial = initial - dy_dx * self.step
            f_change = select(initial) - f_change
        
        self.solution = initial
        self.value = select(initial)