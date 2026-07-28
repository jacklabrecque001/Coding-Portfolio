import random
from multiprocessing import Pool
from multiprocessing import cpu_count
import time
from itertools import product

number_of_values = 4
values = ["a","b","c", "d"]
count = 0

#def generate_matrices():
#    matrices = []
 #   for x1 in values:
  #      for x2 in values:
   #         for x3 in values:
    #            for x4 in values:
     #               for x5 in values:
      #                  for x6 in values:
       #                     for x7 in values:
        #                        for x8 in values:
         #                           for x9 in values:
          #                              for x10 in values:
           #                                 for x11 in values:
            #                                    for x12 in values:
             #                                       for x13 in values:
              #                                          for x14 in values:
               #                                             for x15 in values:
                #                                                for x16 in values:
                 #                                                   matrices.append([[x1, x2, x3, x4],[x5, x6, x7, x8],[x9, x10, x11, x12], [x13, x14, x15, x16]])
    #return(matrices)


def generate_matrices():
    n = number_of_values
    for entries in product(values, repeat=n*n):
        matrix = []
        idx = 0
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(entries[idx])
                idx += 1
            matrix.append(row)
        yield matrix



class table_vars:
    def __init__(self,num,letter,matrix):
        self.matrix = matrix
        self.num = num
        self.letter = letter

    def __add__(self,other):
        return table_vars(
            values.index(self.matrix[self.num][other.num]),self.matrix[self.num][other.num],self.matrix)
    def __mul__(self, other):
        value = self.matrix[self.num][other.num]
        return table_vars(values.index(value), value, self.matrix)
    def __eq__(self, other):
        return self.letter == other.letter

    def __repr__(self):
        return self.letter


def commutative_check(matrix):
    truth = True
    for i in range(number_of_values):
        for j in range(number_of_values):
            upper = table_vars(i,values[i],matrix)
            lower = table_vars(j,values[j],matrix)
            if (upper + lower) != (lower + upper):
                truth = False
    return truth
def commutative_check_mult(matrix):
    for i in range(number_of_values):
        for j in range(number_of_values):
            a = table_vars(i, values[i], matrix)
            b = table_vars(j, values[j], matrix)
            if (a * b) != (b * a):
                return False
    return True


def associativity_check_stochastic(matrix, trials=1000):
    for _ in range(trials):
        i = random.randrange(number_of_values)
        j = random.randrange(number_of_values)
        k = random.randrange(number_of_values)

        a = table_vars(i, values[i], matrix)
        b = table_vars(j, values[j], matrix)
        c = table_vars(k, values[k], matrix)

        if (a + b) + c != a + (b + c):
            return False

    return True

def associativity_check(matrix):
    truth = True
    for i in range(number_of_values):
        for j in range(number_of_values):
            for k in range(number_of_values):
                first = table_vars(i, values[i], matrix)
                second = table_vars(j, values[j], matrix)
                third = table_vars(k, values[k], matrix)

                if (first + second) + third != first + (second + third):
                    truth = False
    return truth
def associativity_check_mult(matrix):
    for i in range(number_of_values):
        for j in range(number_of_values):
            for k in range(number_of_values):
                a = table_vars(i, values[i], matrix)
                b = table_vars(j, values[j], matrix)
                c = table_vars(k, values[k], matrix)
                if (a * b) * c != a * (b * c):
                    return False
    return True

def find_identity(matrix):
    for i in range(number_of_values):
        e = table_vars(i, values[i], matrix)
        is_identity = True

        for j in range(number_of_values):
            x = table_vars(j, values[j], matrix)
            if (e + x) != x or (x + e) != x:
                is_identity = False
                break

        if is_identity:
            return e

def find_identity_mult(matrix):
    for i in range(number_of_values):
        e = table_vars(i, values[i], matrix)
        identity = True
        for j in range(number_of_values):
            x = table_vars(j, values[j], matrix)
            if (e * x) != x or (x * e) != x:
                is_id = False
                break
        if identity:
            return e
    return None

def check_inverses(matrix):
    identity = find_identity(matrix)
    for i in range(number_of_values):
        found_inverse = False
        a = table_vars(i, values[i], matrix)
        for j in range(number_of_values):
            b = table_vars(j, values[j], matrix)
            if a + b == identity:
                found_inverse = True
                break
        if not found_inverse:
            return False
    return True

def check_inverses_mult(matrix):
    identity = find_identity(matrix)
    if identity is None:
        return False

    for i in range(number_of_values):
        a = table_vars(i, values[i], matrix)
        has_inverse = False
        for j in range(number_of_values):
            b = table_vars(j, values[j], matrix)
            if (a * b) == identity:
                has_inverse = True
                break
        if not has_inverse:
            return False
    return True

def check_cycle(matrix):
    identity = find_identity(matrix)
    generator = None

    for num in range(number_of_values):
        candidate = table_vars(num, values[num], matrix)
        if candidate != identity:
            generator = candidate
            break

    if generator is None:
        return False

    step = identity
    visited = set()

    for i in range(number_of_values):
        step = step + generator
        visited.add(step.letter)
        if step == identity and len(visited) != number_of_values:
            return False

    return len(visited) == number_of_values

def check_cycle_mult(matrix):
    identity = find_identity(matrix)
    for i in range(number_of_values):
        g = table_vars(i, values[i], matrix)
        if g == identity:
            continue

        visited = set()
        step = identity

        for _ in range(number_of_values):
            step = step * g
            visited.add(step.letter)

        if len(visited) == number_of_values:
            return True

    return False


def analyze_one_matrix_add(M):

    if not commutative_check(M):
        return(None)

    if not associativity_check(M):
        return(None)

    identity = find_identity(M)
    if identity is None:
        return(None)
    
    if not check_inverses(M):
        return(None)
    
    if not check_cycle(M):
        return(None)
    
    return(M)

def analyze_one_matrix_mult(M):
    if not commutative_check_mult(M):
        return(None)

    if not associativity_check_mult(M):
        return(None)

    identity = find_identity_mult(M)
    if identity is None:
        return(None)

    if not check_inverses_mult(M):
        return(None)

    if not check_cycle_mult(M):
        return(None)

    return(M)

def analyze_parallel(n):
    good_matrices = []

    with Pool(processes = n) as pool:
        for i in pool.imap_unordered(analyze_one_matrix_add, generate_matrices(),chunksize = 100):
            if i is not None:
                good_matrices.append(i)
    print(good_matrices)


start = time.time()
analyze_parallel(5)
end = time.time()
print(end-start)
