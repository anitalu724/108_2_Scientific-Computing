def R_init(xi, yi, x_array, y_array):
    r_array = []
    for num in range(len(x_array)):
        r_tmp =((xi-x_array[num])**2+(yi-y_array[num])**2)**0.5
        r_array.append(r_tmp)
    return array_avg(r_array)

def array_avg(a):
    sum = 0
    for data in a:
        sum+=data
    return round(sum/len(a), 3)


def circleFitByDss(data):
    from scipy import optimize
    x_array, y_array = data[0], data[1]
    if len(x_array)!= len(y_array):
        print("Input error!!\n")
        return 0,0,0
    x_init, y_init = array_avg(x_array), array_avg(y_array)
    r_init = R_init(x_init, y_init, x_array, y_array)
    x0 = [x_init, y_init, r_init]
    # print(x_init, y_init, r_init)
    def objective_function(x0):
        a, b, r = x0[0], x0[1], x0[2]
        ans = 0
        for i in range(len(x_array)):
            ans += abs((((x_array[i]-a)**2+(y_array[i]-b)**2)**0.5)-r)
        return ans
    output = optimize.fmin(objective_function, x0, xtol = 0.00000001, disp = False)
    return round(output[0],4), round(output[1],4), round(output[2],4)
