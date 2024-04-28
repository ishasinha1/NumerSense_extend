import json

filepath = "/Users/isha/Desktop/COS484/NumerSense/results_484/places_roberta.output.jsonl"
truth_file = "/Users/isha/Desktop/COS484/NumerSense/data_484/places.masked.withlabels.txt"

#----------------------------------------------------
# SizeSense code
#----------------------------------------------------
# true_larger = 0
# true_smaller = 0
#----------------------------------------------------

#----------------------------------------------------
# ColorSense code
#----------------------------------------------------
# color_freq_true = {
#       'red': 0,
#       'blue': 0,
#       'yellow': 0,
#       'pink': 0,
#       'white': 0,
#       'black': 0,
#       'green': 0,
#       'orange': 0,
#       'purple': 0,
#       'brown': 0
# }
#----------------------------------------------------

#----------------------------------------------------
# LocationSense code
#----------------------------------------------------
places = ['united states', 'france', 'australia', 'united kingdom', 'china',
 'canada', 'argentina', 'brazil', 'portugal', 'germany', 'italy', 'nepal',
 'pakistan', 'india', 'ireland', 'poland', 'finland', 'netherlands', 'saudi arabia',
 'south africa', 'mexico', 'niger', 'spain', 'panama', 'iran', 'japan', 'sierra leone',
 'switzerland', 'jordan', 'iraq', 'belgium', 'georgia', 'chile', 'greece', 'russia',
 'egypt', 'guinea', 'turkey', 'afghanistan', 'israel', 'oman', 'austria', 'norway',
 'cuba', 'new zealand', 'philippines', 'denmark', 'syria', 'vietnam',
 'mali', 'sweden', 'vatican city', 'zimbabwe', 'albania', 'andorra',
 'armenia', 'azerbaijan', 'bangladesh', 'bolivia', 'bulgaria',
 'colombia', 'hungary', 'liberia', 'north macedonia',
 'papua new guinea', 'peru', 'senegal', 'slovenia']

place_freq_true = {}
place_freq_pred = {}
for place in places:
    place_freq_true[place] = 0
    place_freq_pred[place] = 0
#----------------------------------------------------
    
truth_dict = {}
with open(truth_file, encoding="utf-8") as f:
    for line in f.read().splitlines():
        ls = line.split("\t")
        truth_dict[ls[0].strip().lower()] = ls[1]
        
        #----------------------------------------------------
        # SizeSense code
        #----------------------------------------------------
        # if ls[1] == "larger":
        #     true_larger += 1
        # else:
        #     true_smaller +=1
        #----------------------------------------------------
        
        #----------------------------------------------------
        # ColorSense code
        #----------------------------------------------------
        # color_freq_true[ls[1]] += 1
        #----------------------------------------------------
        
        #----------------------------------------------------
        # LocationSense code
        #----------------------------------------------------
        place_freq_true[ls[1]] += 1
        #----------------------------------------------------
        

correct_cnt = 0
correct_top2_cnt = 0
correct_top3_cnt = 0
num_probes = 0

#----------------------------------------------------
# SizeSense code
#----------------------------------------------------
# count_larger = 0
# count_smaller = 0
#----------------------------------------------------

#----------------------------------------------------
# ColorSense code
#----------------------------------------------------
# color_freq_pred = {
#       'red': 0,
#       'blue': 0,
#       'yellow': 0,
#       'pink': 0,
#       'white': 0,
#       'black': 0,
#       'green': 0,
#       'orange': 0,
#       'purple': 0,
#       'brown': 0
# }
#----------------------------------------------------
with open(filepath) as f:
    for line in f.read().splitlines():
        # print(line)
        if not line:
            continue
        data = json.loads(line)
        # print(data)
        data["probe"] = data["probe"].strip().lower()
        assert data["probe"] in truth_dict, data["probe"]
        num_probes += 1
        assert len(data["result_list"]) >= 1
        truth = truth_dict[data["probe"]]
        
        #----------------------------------------------------
        # NumerSense code that we commented out
        #----------------------------------------------------
        # deal with the ambiguitiy of no/zero
        # if truth == "no":
        #     truth = "zero"  # always use zero
        # result_list = ["zero" if item["word"] == "no" else item["word"]
        #               for item in data["result_list"]]
        #----------------------------------------------------
        
        result_list = [item["word"] for item in data["result_list"]]
        
        #----------------------------------------------------
        # SizeSense code
        #----------------------------------------------------
        # if result_list[0] == "larger":
        #     count_larger += 1
        # else:
        #     count_smaller +=1
        #----------------------------------------------------
        
        #----------------------------------------------------
        # ColorSense code
        #----------------------------------------------------
        # color_freq_pred[result_list[0]] += 1
        #----------------------------------------------------
        
        #----------------------------------------------------
        # LocationSense code
        #----------------------------------------------------
        place_freq_pred[result_list[0]] += 1
        #----------------------------------------------------
            
        if truth == result_list[0]:
            correct_cnt += 1
        if truth in result_list[:2]:
            correct_top2_cnt += 1
        if truth in result_list[:3]:
            correct_top3_cnt += 1

print(filepath)
print("num_probes:", num_probes)
print("top1-acc:", correct_cnt/num_probes)
print("top2-acc:", correct_top2_cnt/num_probes)
print("top3-acc:", correct_top3_cnt/num_probes)
# print(truth_dict)

#----------------------------------------------------
# SizeSense code
#----------------------------------------------------
# print("num-larger-pred:", count_larger)
# print("num-smaller-pred:", count_smaller)
# print("num-larger-true:", true_larger)
# print("num-smaller-true:", true_smaller)
#----------------------------------------------------

#----------------------------------------------------
# ColorSense code
#----------------------------------------------------
# print("true-dist-colors:", color_freq_true)
# print("pred-dist-colors:", color_freq_pred)
#----------------------------------------------------

#----------------------------------------------------
# LocationSense code
#----------------------------------------------------
print("true-dist-colors:", place_freq_true)
print("pred-dist-colors:", place_freq_pred)
#----------------------------------------------------