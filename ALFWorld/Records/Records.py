# ['put', 'clean', 'heat', 'cool', 'examine', 'puttwo']

#%% SALA
# SALA - success

list1 = [0, 2, 1, 1, 0, 1]
list2 = [1, 2, 0, 2, 0, 0]
list3 = [0, 0, 0, 0, 1, 0]
list4 = [1, 1, 0, 1, 0, 1]
list5 = [1, 0, 1, 0, 0, 1]
list6 = [1, 0, 3, 2, 0, 0]
list7 = [1, 0, 0, 0, 0, 0]
list8 = [0, 1, 1, 0, 0, 0]
list9 = [2, 3, 2, 1, 2, 0]
list10 = [1, 0, 0, 1, 0, 1]
list11 = [1, 0, 1, 1, 0, 1]
list12 = [0, 1, 0, 0, 0, 0]
list13 = [1, 0, 0, 1, 0, 0]
list14 = [2, 1, 1, 0, 2, 1]
list15 = [0, 1, 1, 0, 0, 1]
list16 = [2, 0, 1, 0, 0, 1]
list17 = [2, 0, 0, 0, 1, 0]
list18 = [0, 3, 0, 2, 0, 0]
list19 = [0, 1, 0, 0, 0, 0]
list20 = [1, 1, 1, 0, 0, 0]
list21 = [0, 0, 0, 1, 0, 0]
list22 = [0, 0, 0, 0, 0, 0]
list23 = [0, 1, 0, 0, 0, 0]
list24 = [0, 0, 0, 0, 0, 0]
list25 = [1, 1, 0, 0, 0, 0]

# Using zip with unpacking
SALA_success = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7, list8,
    list9, list10, list11, list12, list13, list14, list15,
    list16, list17, list18, list19, list20, list21, list22,
    list23, list24, list25
)]
print(SALA_success)

# SALA - total

list1 = [0, 2, 1, 2, 0, 1]
list2 = [1, 3, 1, 3, 0, 0]
list3 = [1, 0, 0, 1, 1, 0]
list4 = [2, 2, 1, 1, 0, 1]
list5 = [1, 1, 3, 0, 0, 1]
list6 = [2, 1, 3, 3, 0, 0]
list7 = [1, 0, 0, 0, 0, 2]
list8 = [0, 2, 2, 0, 1, 0]
list9 = [3, 4, 2, 1, 2, 1]
list10 = [1, 0, 0, 1, 2, 1]
list11 = [1, 0, 1, 1, 1, 2]
list12 = [0, 1, 0, 0, 1, 1]
list13 = [1, 1, 0, 2, 0, 1]
list14 = [3, 2, 1, 0, 2, 1]
list15 = [0, 2, 1, 1, 0, 1]
list16 = [2, 0, 2, 0, 0, 2]
list17 = [2, 0, 0, 0, 3, 0]
list18 = [0, 4, 0, 2, 1, 0]
list19 = [0, 2, 0, 0, 0, 1]
list20 = [2, 1, 1, 1, 1, 0]
list21 = [0, 0, 1, 2, 1, 0]
list22 = [0, 0, 2, 0, 0, 0]
list23 = [0, 1, 0, 0, 2, 0]
list24 = [0, 1, 0, 0, 0, 1]
list25 = [1, 1, 1, 0, 0, 0]

# Using zip with unpacking
SALA_total = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7, list8,
    list9, list10, list11, list12, list13, list14, list15,
    list16, list17, list18, list19, list20, list21, list22,
    list23, list24, list25
)]
print(SALA_total)

# Elementwise division
SALA_ratio = [s / t if t != 0 else 0 for s, t in zip(SALA_success, SALA_total)]

print(SALA_ratio)

# SALA total success rate
SALA_success_rate_all = sum(SALA_success)/sum(SALA_total)
print(SALA_success_rate_all)

#%% ESALA - success
print("ESALA")
list1 = [1, 3, 1, 4, 0, 1]
list2 = [0, 1, 0, 0, 0, 0]
list3 = [0, 0, 0, 0, 0, 0]
list4 = [1, 1, 0, 1, 0, 1]
list5 = [1, 0, 1, 0, 0, 1]
list6 = [0, 0, 3, 2, 0, 0]
list7 = [2, 0, 0, 0, 0, 1]
list8 = [0, 2, 2, 0, 0, 0]
list9 = [1, 1, 0, 1, 1, 0]
list10 = [3, 1, 2, 1, 0, 1]
list11 = [1, 0, 0, 1, 0, 1]
list12 = [0, 1, 0, 0, 0, 0]
list13 = [1, 0, 0, 0, 0, 1]
list14 = [3, 1, 0, 0, 0, 1]
list15 = [0, 0, 0, 1, 0, 0]
list16 = [0, 1, 0, 0, 0, 0]
list17 = [2, 0, 0, 0, 0, 1]
list18 = [0, 0, 0, 0, 0, 0]
list19 = [2, 0, 0, 0, 1, 0]
list20 = [0, 4, 0, 3, 0, 1]
list21 = [2, 1, 1, 0, 0, 0]
list22 = [0, 0, 1, 1, 0, 0]
list23 = [0, 1, 0, 0, 0, 0]
list24 = [0, 0, 0, 0, 0, 0]
list25 = [1, 1, 0, 0, 0, 0]

# Using zip with unpacking
second_success = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7, list8,
    list9, list10, list11, list12, list13, list14, list15,
    list16, list17, list18, list19, list20, list21, list22,
    list23, list24, list25
)]
print(second_success)

# ESALA - total

list1 = [1, 4, 2, 4, 0, 1]
list2 = [1, 1, 0, 1, 0, 0]
list3 = [1, 0, 0, 1, 1, 0]
list4 = [1, 2, 1, 1, 0, 1]
list5 = [1, 1, 2, 0, 0, 1]
list6 = [1, 1, 4, 2, 0, 0]
list7 = [2, 0, 0, 1, 0, 2]
list8 = [0, 3, 2, 0, 1, 0]
list9 = [1, 2, 0, 1, 1, 1]
list10 = [3, 1, 2, 1, 2, 1]
list11 = [1, 0, 1, 1, 1, 2]
list12 = [0, 1, 0, 0, 1, 1]
list13 = [1, 1, 0, 1, 1, 1]
list14 = [3, 1, 0, 1, 1, 1]
list15 = [0, 1, 1, 1, 1, 0]
list16 = [0, 2, 1, 0, 0, 1]
list17 = [2, 0, 2, 0, 0, 1]
list18 = [0, 0, 0, 0, 1, 1]
list19 = [2, 0, 0, 0, 3, 0]
list20 = [0, 6, 0, 3, 0, 1]
list21 = [2, 1, 1, 0, 2, 0]
list22 = [0, 0, 3, 2, 0, 0]
list23 = [0, 1, 0, 0, 2, 0]
list24 = [0, 1, 0, 0, 0, 1]
list25 = [1, 1, 1, 0, 0, 0]

# Using zip with unpacking
second_total = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7, list8,
    list9, list10, list11, list12, list13, list14, list15,
    list16, list17, list18, list19, list20, list21, list22,
    list23, list24, list25
)]
print(second_total)

# Elementwise division
second_ratio = [s / t if t != 0 else 0 for s, t in zip(second_success, second_total)]

print(second_ratio)

# ESALA total success rate
ESALA_success_rate_all = sum(second_success)/sum(second_total)
print(ESALA_success_rate_all)

#%% ReAct
# ReAct - success
print("ReAct")
list1 = [7, 7, 5, 7, 4, 4]
list2 = [9, 4, 4, 6, 6, 6]
list3 = [3, 3, 3, 2, 2, 0]

# Using zip with unpacking
ReAct_success = [sum(values) for values in zip(
    list1, list2, list3
)]
print(ReAct_success)

# ReAct - total

list1 = [9, 14, 11, 11, 4, 6]
list2 = [12, 11, 7, 6, 10, 9]
list3 = [3, 6, 5, 4, 4, 2]

# Using zip with unpacking
ReAct_total = [sum(values) for values in zip(
    list1, list2, list3
)]
print(ReAct_total)

# Elementwise division
ReAct_ratio = [s / t if t != 0 else 0 for s, t in zip(ReAct_success, ReAct_total)]

print(ReAct_ratio) # [0.7916666666666666, 0.45161290322580644, 0.5217391304347826, 0.7142857142857143, 0.6666666666666666, 0.5882352941176471]

# ReAct total success rate
ReAct_success_rate_all = sum(ReAct_success)/sum(ReAct_total)
print(ReAct_success_rate_all) # 0.6119402985074627

#%% Rate of fail and adapt
fail_total = 33 # Count of fail in ReAct and SALA and fail in ReAct and adapt in SALA
adapt_total = 2 # Count of fail in ReAct and adapt in SALA
Adaptation_rate = adapt_total / fail_total
print("Adaptation Rate")
print(Adaptation_rate) # 0.06060606060606061

#%% Rate of improve 
nonoptimal_total = 50 # Count of success in ReAct and ESALA
improve_total = 22
Improve_rate = improve_total / nonoptimal_total
print("Improve Rate")
print(Improve_rate) # 0.44

#%% SALA_rmvRflx0
print("SALA_rmvRflx0")
list1 = [6, 8, 5, 4, 3, 3] # 1-58 success
list2 = [10, 8, 2, 3, 2, 1] # 70-134 success
list3 = [2, 1, 1, 2, 0, 2] # 59-69 success
list4 = [2, 0, 0, 1, 2, 0] # 77-117 fail
list5 = [3, 0, 0, 2, 0, 2] # 3-42 fail
list6 = [0, 1, 2, 0, 0, 0] # 121-132 fail
list7 = [1, 0, 0, 0, 3, 1] # 43-76 fail

# Using zip with unpacking
SALA_rmvRflx0_success = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7
)]
print(SALA_rmvRflx0_success)

# SALA_rmvRflx0 - total

list1 = [6, 8, 8, 7, 3, 3] # 1-58 success
list2 = [10, 10, 4, 4, 3, 3] # 70-134 success
list3 = [2, 1, 1, 2, 0, 2] # 59-69 success
list4 = [2, 4, 1, 2, 4, 3] # 77-117 fail
list5 = [3, 4, 4, 4, 0, 2] # 3-42 fail
list6 = [0, 1, 4, 1, 3, 1] # 121-132 fail
list7 = [1, 3, 1, 1, 5, 3] # 43-76 fail

# Using zip with unpacking
SALA_rmvRflx0_total = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7
)]
print(SALA_rmvRflx0_total)

# Elementwise division
SALA_rmvRflx0_ratio = [s / t if t != 0 else 0 for s, t in zip(SALA_rmvRflx0_success, SALA_rmvRflx0_total)]

print(SALA_rmvRflx0_ratio) # [1.0, 0.5806451612903226, 0.43478260869565216, 0.5714285714285714, 0.5555555555555556, 0.5294117647058824]

# SALA_rmvRflx0 total success rate
SALA_rmvRflx0_success_rate_all = sum(SALA_rmvRflx0_success)/sum(SALA_rmvRflx0_total)
print(SALA_rmvRflx0_success_rate_all) # 0.6194029850746269

#%% SALA_rmvRflx1
print("SALA_rmvRflx1")
list1 = [4, 5, 5, 6, 2, 2] # 1-55 success
list2 = [10, 10, 3, 4, 2, 3] # 70-134 success
list3 = [3, 1, 3, 2, 0, 2] # 56-69 success
list4 = [1, 1, 1, 2, 1, 3] # 71-112 fail
list5 = [1, 4, 1, 2, 5, 4] # 3-49 fail
list6 = [1, 1, 2, 1, 0, 0] # 113-132 fail
list7 = [1, 0, 0, 0, 0, 0] # 52-66 fail

# Using zip with unpacking
SALA_rmvRflx1_success = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7
)]
print(SALA_rmvRflx1_success)

# SALA_rmvRflx1 - total

list1 = [5, 8, 6, 7, 3, 3] # 1-55 success
list2 = [10, 10, 4, 4, 3, 3] # 70-134 success
list3 = [3, 1, 3, 2, 0, 2] # 56-69 success
list4 = [1, 4, 1, 2, 5, 4] # 71-112 fail
list5 = [3, 5, 5, 4, 1, 3] # 3-49 fail
list6 = [1, 2, 4, 2, 4, 1] # 113-132 fail
list7 = [1, 1, 0, 0, 2, 1] # 52-66 fail

# Using zip with unpacking
SALA_rmvRflx1_total = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7
)]
print(SALA_rmvRflx1_total)

# Elementwise division
SALA_rmvRflx1_ratio = [s / t if t != 0 else 0 for s, t in zip(SALA_rmvRflx1_success, SALA_rmvRflx1_total)]

print(SALA_rmvRflx1_ratio) # [0.875, 0.7096774193548387, 0.6521739130434783, 0.8095238095238095, 0.5555555555555556, 0.8235294117647058]

# SALA_rmvRflx1 total success rate
SALA_rmvRflx1_success_rate_all = sum(SALA_rmvRflx1_success)/sum(SALA_rmvRflx1_total)
print(SALA_rmvRflx1_success_rate_all) # 0.7388059701492538

#%% ESALA_rmvRflx1
print("ESALA_rmvRflx1")
list1 = [4, 3, 1, 3, 2, 0] # 102-121
list2 = [1, 6, 2, 5, 0, 1] # 1-23
list3 = [2, 2, 3, 0, 0, 1] # 35-49
list4 = [3, 2, 0, 1, 0, 3] # 70-85
list5 = [1, 3, 3, 1, 0, 0] # 122-134
list6 = [1, 1, 5, 2, 0, 1] # 24-34
list7 = [4, 3, 3, 2, 2, 2] # 50-69
list8 = [2, 1, 3, 1, 1, 2] # 86-101

# Using zip with unpacking
ESALA_rmvRflx1_success = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7
)]
print(ESALA_rmvRflx1_success) # [21, 22, 15, 17, 10, 14]

# ESALA_rmvRflx1 - total

list1 = [4, 7, 1, 3, 4, 1] # 102-121
list2 = [4, 7, 2, 7, 1, 2] # 1-23
list3 = [3, 3, 4, 1, 1, 3] # 35-49
list4 = [5, 3, 0, 2, 3, 3] # 70-85
list5 = [1, 3, 4, 2, 2, 1] # 122-134
list6 = [1, 2, 5, 2, 0, 1] # 24-34
list7 = [4, 3, 3, 3, 4, 3] # 50-69
list8 = [2, 3, 4, 1, 3, 3] # 86-101

# Using zip with unpacking
ESALA_rmvRflx1_total = [sum(values) for values in zip(
    list1, list2, list3, list4, list5, list6, list7
)]
print(ESALA_rmvRflx1_total) # [22, 28, 19, 20, 15, 14]

# Elementwise division
ESALA_rmvRflx1_ratio = [s / t if t != 0 else 0 for s, t in zip(ESALA_rmvRflx1_success, ESALA_rmvRflx1_total)]

print(ESALA_rmvRflx1_ratio) # [0.7272727272727273, 0.7142857142857143, 0.8947368421052632, 0.7, 0.26666666666666666, 0.5714285714285714]

# SALA_rmvRflx0 total success rate
ESALA_rmvRflx1_success_rate_all = sum(ESALA_rmvRflx1_success)/sum(ESALA_rmvRflx1_total)
print(ESALA_rmvRflx1_success_rate_all) # 0.6694915254237288
