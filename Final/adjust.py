import json, sys
import os
import operator
from termcolor import colored

json_path = sys.argv[1]
jsobj = json.load(open(json_path))
BIAS = 1.2
tune_file = open(sys.argv[2], "w")
high_pro_error = []
max_int = 0

TUNE_PRINT = {"CB":"C大調\n",
              "DB":"D大調\n",
              "EB":"E大調\n",
              "FB":"F大調\n",
              "GB":"G大調\n",
              "AB":"A大調\n",
              "BB":"B大調\n",
              "JDB":"降D大調\n",
              "JEB":"降E大調\n",
              "JGB":"降G大調\n",
              "JAB":"降A大調\n",
              "JBB":"降B大調\n"}

TUNE_COUNT = {"CB":0,
             "DB":0,
             "EB":0,
             "FB":0,
             "GB":0,
             "AB":0,
             "BB":0,
             "JDB":0,
             "JEB":0,
             "JGB":0,
             "JAB":0,
             "JBB":0,
             }

TUNE_DICT = {"CB":[[40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84], [48, 60, 72, 84]],
             "DB":[[40, 42, 43, 45, 47, 49, 50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74, 76, 78, 79, 81, 83, 85], [50, 62, 74]],
             "EB":[[40, 42, 44, 45, 47, 49, 51, 52, 54, 56, 57, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85], [40, 52, 64, 76]],
             "FB":[[40, 41, 43, 45, 46, 48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 65, 67, 69, 70, 72, 74, 76, 77, 79, 81, 82, 84], [41, 53, 65, 77]],
             "GB":[[40, 42, 43, 45, 47, 48, 50, 52, 54, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 72, 74, 76, 78, 79, 81, 83, 84], [43, 55, 67]],
             "AB":[[40, 42, 44, 45, 47, 49, 50, 52, 54, 56, 57, 59, 61, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 80, 81, 83, 85], [45, 57, 69]],
             "BB":[[40, 42, 44, 46, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63, 64, 66, 68, 70, 71, 73, 75, 76, 78, 80, 82, 83, 85], [47, 59, 71]],
             "JDB":[[41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 63, 65, 66, 68, 70, 72, 73, 75, 77, 78, 80, 82, 84, 85], [49, 61, 73, 85]],
             "JEB":[[41, 43, 44, 46, 48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 72, 74, 75, 77, 79, 80, 82, 84], [51, 63, 75]],
             "JGB":[[41, 42, 44, 46, 47, 49, 51, 53, 54, 56, 58, 59, 61, 63, 65, 66, 68, 70, 71, 73, 75, 77, 78, 80, 82, 83, 85], [54, 66, 78]],
             "JAB":[[41, 43, 44, 46, 48, 49, 51, 53, 55, 56, 58, 60, 61, 63, 65, 67, 68, 70, 72, 73, 75, 77, 79, 80, 82, 84], [56, 68, 80]],
             "JBB":[[41, 43, 45, 46, 48, 50, 51, 53, 55, 57, 58, 60, 62, 63, 65, 67, 69, 70, 72, 74, 75, 77, 79, 81, 82, 84], [58, 70, 82]]
             }

TONE_CHANGE_DICT = {"DB":[[48, 53, 60, 65, 72, 77, 84],[49, 54, 61, 66, 73, 78, 85]],
                    "EB":[[41, 43, 48, 50, 53, 55, 60, 62, 65, 67, 72, 74, 77, 79, 84], [42, 44, 49, 51, 54, 56 ,61, 63, 66, 68, 73, 75, 78, 80, 85]],
                    "FB":[[47, 59, 71, 83],[46, 58, 70, 82]],
                    "GB":[[41, 53, 65, 77],[42, 54, 66, 78]],
                    "AB":[[41, 43, 48, 53, 55, 60, 65, 67, 72, 77, 79, 84],[42, 44, 49, 54, 56, 61, 66, 68, 73, 78, 80, 85]],
                    "BB":[[41, 43, 45, 48, 50, 53, 55, 57, 60, 62, 65, 67, 69, 72, 74, 77, 79, 81, 84],[42, 44, 46, 49, 51, 54, 56, 58, 61, 63, 66, 68, 70, 73, 75, 78, 80, 82, 85]]
                   }

count = 0
change = 0
for i in range(1500):
    # i = 1
    index = str(i+1)
    print("__ " , index, " __")
    TUNE = int(jsobj[index][len(jsobj[index])-1][2])
    data_list = jsobj[index]
    pitch_list = [int(x[2]) for x in data_list]
    TUNE_RATIO = dict(TUNE_DICT)
    ACC_TUNE = ""
    # Calculate 1s
    for TUNE_CHOICE in TUNE_DICT:
        new_int = 0
        for pitch in pitch_list:
            if pitch in TUNE_DICT[TUNE_CHOICE][0]:
                new_int += 1
        TUNE_RATIO[TUNE_CHOICE] = new_int/len(pitch_list)
    TUNE_RATIO = dict((k, v) for k, v in TUNE_RATIO.items() if v >= 0.7)
    
    if len(TUNE_RATIO) != 0:
        if len(TUNE_RATIO) > 1:
            LAST_PITCH = "None"
            for TUNE in TUNE_RATIO:
                if pitch_list[len(pitch_list)-1] in TUNE_DICT[TUNE][1]:
                    LAST_PITCH = TUNE
            MAX_TUNE_RATIO = max(TUNE_RATIO.items(), key=operator.itemgetter(1))[0]
            print(MAX_TUNE_RATIO, LAST_PITCH)

            if LAST_PITCH == "None":
                ACC_TUNE = "NONE"
            else:
                if MAX_TUNE_RATIO == LAST_PITCH:
                    ACC_TUNE = MAX_TUNE_RATIO
                elif MAX_TUNE_RATIO != LAST_PITCH and TUNE_RATIO[MAX_TUNE_RATIO]-TUNE_RATIO[LAST_PITCH] < 0.03:
                    ACC_TUNE = LAST_PITCH
                else:
                    ACC_TUNE = "NONE"

        else:
            ACC_TUNE = max(TUNE_RATIO.items(), key=operator.itemgetter(1))[0]
            TUNE_COUNT[ACC_TUNE] += 1
    # change pitch value
        if ACC_TUNE in TONE_CHANGE_DICT:
            print(colored("* "+ index+ " : "+TUNE_PRINT[ACC_TUNE], 'yellow'))
            tune_file.write(index+" : "+TUNE_PRINT[ACC_TUNE])
            change+=1
            for i in range(len(pitch_list)):
                if pitch_list[i] in TONE_CHANGE_DICT[ACC_TUNE][0]:
                    ind = TONE_CHANGE_DICT[ACC_TUNE][0].index(pitch_list[i])
                    jsobj[index][i][2] = TONE_CHANGE_DICT[ACC_TUNE][1][ind]
        elif ACC_TUNE == "NONE":
            tune_file.write(index+" : None\n")
    else:
        tune_file.write(index+" : None\n")

    # os._exit()
print(change)
with open(sys.argv[3], 'w') as outfile:
    json.dump(jsobj, outfile)   

print(colored("TOTAL HIGH_PRO_ERROR = "+str(len(high_pro_error)), 'red'))
print(colored(high_pro_error, "red"))

for i in TUNE_COUNT:
    print(i, " : ", TUNE_COUNT[i])
print(max_int)
    
        

    
    


        
    
        
