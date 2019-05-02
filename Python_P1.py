#Freya Varez
#3/4/2019

import functools
import math
#########################__1. Dictionaries -  busStops(b)____######################################################################
def busStops(b):
    L = dict()
    for bus, stops in b.items():
        for stop in stops:
            if stop in L:
                L[stop].append(bus)
            else:
                L[stop] = [bus]
    for stop, buses in L.items():
        buses.sort()
    return L

def testbusStops():
    print("busStops Test:")
    TestbusStops1 = { "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
          "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
          "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
          "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
          "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"] }
    TestbusStops2 = {"bus1":["stop1", "stop2", "stop3"], "bus2":["stop1", "stop2", "stop3"]}
    TestbusStops3 = {1:[1,2], 2:[2], 3:[3]}
    TestbusStops4 = {"bus1":["stop1"], "bus2":["stop1"], "bus3":["stop1"]}
    
    print("Test 1: ", busStops(TestbusStops1) == {'Chinook': ['Blue', 'Lentil', 'Wheat'], 'Orchard': ['Lentil', 'Wheat'], 'Valley': ['Lentil', 'Wheat'],
                              'Emerald': ['Lentil'], 'Providence': ['Lentil'], 'Stadium': ['Gray', 'Lentil', 'Silver'], 'Main': ['Gray', 'Lentil'],
                              'Arbor': ['Lentil'], 'Sunnyside': ['Gray', 'Lentil'], 'Fountain': ['Lentil'], 'Crestview': ['Gray', 'Lentil'],
                              'Wheatland': ['Lentil'], 'Walmart': ['Lentil', 'Silver', 'Wheat'], 'Bishop': ['Lentil', 'Silver', 'Wheat'],
                              'Derby': ['Lentil'], 'Dilke': ['Lentil'], 'Maple': ['Wheat'], 'Aspen': ['Wheat'], 'TerreView': ['Blue', 'Wheat'],
                              'Clay': ['Wheat'], 'Dismores': ['Wheat'], 'Martin': ['Wheat'], 'PorchLight': ['Silver', 'Wheat'], 'Campus': ['Wheat'],
                              'TransferStation': ['Blue', 'Gray', 'Silver'], 'Shopco': ['Silver'], 'RockeyWay': ['Silver'], 'State': ['Blue'],
                              'Larry': ['Blue'], 'Grand': ['Blue'], 'TacoBell': ['Blue'], 'Library': ['Blue'], 'Wawawai': ['Gray'], 'CityHall': ['Gray'],
                              'Colorado': ['Gray']})
    print("Test 2: ", busStops(TestbusStops2) == {"stop1":["bus1", "bus2"], "stop2":["bus1", "bus2"], "stop3":["bus1", "bus2"]})
    print("Test 3: ", busStops(TestbusStops3) == {1:[1], 2:[1,2], 3:[3]})
    print("Test 4: ", busStops(TestbusStops4) == {"stop1":["bus1", "bus2", "bus3"]})

####################_______2. (Dictionaries)___________###################################################################################### 
####_____a) addDict(d)_____###
def addDict(d):
    if d == {} or d == None:#ignore if no studying was done during the week
        return {}
    L = dict()
    for day, courses in d.items():
        if courses == {}:   #ignore days with no studying
            continue
        for course, hours_studied in courses.items():
            if course in L:
                L[course] += hours_studied
            else:
                L[course] = hours_studied
    return L

def testaddDict():
    print("addDict Test:")
    TestaddDict1 = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3},'Thu':{'355':3,'451':2,'360':3},'Fri':{'355':2},'Sun':{'355':1,'451':3,'360':1}}
    TestaddDict2 = {'Mon':{},'Tue':{}, 'Thu':{}}
    TestaddDict3 = {'Mon':{},'Tue':{'451':2,'360':3}, 'Thu':{'355':3}, 'Fri':{'355':2}, 'Sun':{'360':1}}
    TestaddDict4 = {'Mon':{'355':2},'Tue':{'355':2}, 'Thu':{'355':3}, 'Fri':{'355':2}, 'Sun':{'355':1}}
         
    print("Test 1: ", addDict(TestaddDict1) == {'355': 8, '451': 8, '360': 9})
    print("Test 2: ", addDict(TestaddDict2) == {})
    print("Test 3: ", addDict(TestaddDict3) == {'355': 5, '451': 2, '360': 4})
    print("Test 4: ", addDict(TestaddDict4) == {'355': 10})

####_____b) addDictN(L)_____###Note: Should use the Python map and reduce functions as well as addDict (part(a))
def addDictN(L):
    if L == {}:
        return {}
    L = list(map(addDict, L))
    def foldWeeks(A, B):
        for course, hours in A.items():
            if course in B:
                B[course] += hours
            else:
                B[course] = hours
        return B
    L = functools.reduce(foldWeeks, L)
    return L
 
def testaddDictN():
    print("addDictN Test:")
    TestaddDict1 = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1}},
                    {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},
                    {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}]
    TestaddDict2 = {}
    TestaddDict3 = [{'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2, '360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}]
    TestaddDict4 = [{'Mon':{'355':1},'Tue':{'355':1},'Thu':{'355':1}, 'Fri':{'355':1}, 'Sun':{'355':1}},
                    {'Tue':{'355':1},'Wed':{'355':1},'Fri':{'355':1}},
                    {'Mon':{'355':1},'Wed':{'355':1},'Thu':{'355':1},'Fri':{'355':1}, 'Sun':{'355':1}}]
         
    print("Test 1: ", addDictN(TestaddDict1) == {'355': 16, '360': 24, '451': 6})
    print("Test 2: ", addDictN(TestaddDict2) == {})
    print("Test 3: ", addDictN(TestaddDict3) == {'355': 8, '360': 9, '451': 8})
    print("Test 4: ", addDictN(TestaddDict4) == {'355': 13})
    
##############################_____________3. Dictionaries and lists________________###################################################################### 
####_____a) searchDicts(L,k)–________#####
def searchDicts(L,k):
    J = list(reversed(L))
    for dictionary in J:
        for L_key, L_value in dictionary.items():
            if L_key == k:
                return L_value
    return None
 
def testsearchDicts():
    print("searchDicts Test:")
    testsearchDicts1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
    testsearchDicts2 = [{"x":None,"y":True,"z":5},{"x":2},{2:False}]
    testsearchDicts3 = [{}]
         
    print("Test 1a: ", searchDicts(testsearchDicts1,"x") == 2)
    print("Test 1b: ", searchDicts(testsearchDicts1,"y") == False)
    print("Test 1c: ", searchDicts(testsearchDicts1,"z") == "found")
    print("Test 1d: ", searchDicts(testsearchDicts1,"t") == None)
    print("Test 2a: ", searchDicts(testsearchDicts2,"x") == 2)
    print("Test 2b: ", searchDicts(testsearchDicts2,"y") == True)
    print("Test 2c: ", searchDicts(testsearchDicts2,2) == False)
    print("Test 3a: ", searchDicts(testsearchDicts3,"a") == None)
    
####_______b) searchDicts2(tL,k)__####
def searchDicts2(L,k):
    if L == []:
        return None
    def getNext(tup, L):        #given current tuple, find next tuple
        return L[tup[0]]
    if k in L[-1][1]:           #check last index
        return L[-1][1][k]
    index = getNext(L[-1], L)   #get next tuple
    n = 0;
    while not(k in index[1]):   #search dictionary at current tuple, if key found - exit and return value
        index = getNext(index, L)#"increment" tuple
        if index == L[-1] or n > len(L):       #If loop found return None
            return None
        n+=1
    return index[1][k]          #if key found, return respective value

def testsearchDicts2():
    print("searchDicts2 Test:")
    TestsearchDict2_1 = [(0,{"x":0,"y":True,"z":"zero"}),
                      (0,{"x":1}),
                      (1,{"y":False}),
                      (1,{"x":3, "z":"three"}),
                      (2,{})]
    TestsearchDict2_2 = [(0,{"z":"zero"}),(1,{"y":False}), (1,{"y":False})]
    TestsearchDict2_3 = []
         
    print("Test 1a: ", searchDicts2(TestsearchDict2_1,"x") == 1)
    print("Test 1b: ", searchDicts2(TestsearchDict2_1,"y") == False)
    print("Test 1c: ", searchDicts2(TestsearchDict2_1,"z") == "zero")
    print("Test 1d: ", searchDicts2(TestsearchDict2_1,"t") == None)
    print("Test 2a: ", searchDicts2(TestsearchDict2_2,"x") == None)
    print("Test 2b: ", searchDicts2(TestsearchDict2_2,"y") == False)
    print("Test 3a: ", searchDicts2(TestsearchDict2_3,"a") == None)
    
##############################_____________4. (Lists)  subsets________________######################################################################
def subsets(L):
    if L == []:
        return [[]]
    subset = subsets(L[1:])
    pSet = []
    for s in subset:
        pSet.append([L[0]] + s)
    pSet += subset
    return sorted(pSet, key = len)

def testsubsets():
    print("subsets Test:")
    subsetsTest1 = [1,2,3]
    subsetsTest2 = [(1,"one"),(2,"two")]
    subsetsTest3 = ([])
    subsetsTest4 = (['a', 'b', 'c'])
    subsetsTest5 = (["Hello"])
         
    print("Test 1: ", subsets(subsetsTest1) == [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]])
    print("Test 2: ", subsets(subsetsTest2) == [[],[(1,"one")],[(2,"two")],[(1,"one"),(2,"two")]])
    print("Test 3: ", subsets(subsetsTest3) == [[]])
    print("Test 4: ", subsets(subsetsTest4) == [[],['a'],['b'],['c'],['a','b'],['a','c'],['b','c'],['a','b','c']])
    print("Test 5: ", subsets(subsetsTest5) == [[],["Hello"]])
    
##############################_____________5. (Recursion)   numPaths(m,n)_____######################################################################
def numPaths(m,n):
    if m <= 1 and n <= 1:
        return 0
    if m == 1:
        return 1
    if n == 1:
        return 1
    return numPaths(m - 1, n) + numPaths(m, n - 1)
 
def testnumPaths():
    print("numPaths Test:")
    print("Test 1: ", numPaths(2,2) == 2)
    print("Test 2: ", numPaths(3,3) == 6)
    print("Test 3: ", numPaths(4,5) == 35)
    print("Test 4: ", numPaths(0,0) == 0)
    print("Test 5: ", numPaths(-5, -2) == 0)
    
##############################_____________6. Iterators ____________________________######################################################################
####_____a) iterPrimes()_______________________#####
class iterPrimes():
    def __init__(self):
        self.cur = 1
    def isPrime(self):
        for n in range(2, int(math.sqrt(self.cur)) + 1):
            if self.cur % n == 0:
                return False
        return True
    def __next__(self):
        self.cur += 1
        while not self.isPrime():
            self.cur += 1
        return self.cur
    def __prev__(self):
        self.cur -= 1
        while not self.isPrime():
            self.cur -= 1
        return self.cur

####_____b) numbersToSum(iNumbers,sum)________#####
def numbersToSumActual(iNumbers,sum): #this function will work on an arbitrary iterator
    sequence = list()
    sum_count = 0
    index = 0
    while True:
        cur = iNumbers.__next__()
        sum_count += cur
        if sum_count >= sum:
            return sequence
        sequence.append(cur)
        
def numbersToSum(iNumbers,sum): #this function will work ONLY on iterators that have a __prev__() member 
    sequence = list()
    sum_count = 0
    index = 0
    while True:
        cur = iNumbers.__next__()
        sum_count += cur
        if sum_count >= sum:
            iNumbers.__prev__()
            return sequence
        sequence.append(cur)

def testnumbersToSum():
    print("numberToSum Test:")
    subsetsTest1 = iterPrimes()
    print("Test 1a: ", numbersToSum(subsetsTest1,58) == [2, 3, 5, 7, 11, 13])
    print("Test 1b: ", numbersToSum(subsetsTest1,100) == [17, 19, 23, 29])
    print("Test 1c: ", numbersToSum(subsetsTest1,0) == [])
    print("Test 1d: ", numbersToSum(subsetsTest1,-8) == [])
    
testFunctions = {"busStops":testbusStops,
                     "addDict": testaddDict,
                     "addDictN": testaddDictN,
                     "searchDicts": testsearchDicts,
                     "searchDicts2": testsearchDicts2,
                     "subsets":testsubsets,
                     "numPaths": testnumPaths,
                     "numbersToSum":testnumbersToSum}
if __name__ == '__main__':
    for testName,testFunc in testFunctions.items():
        print(testName,':  ',testFunc())
        print('---------------------')
