pt1 = (0, 2)
pt2 = (2, 5)
pt3 = (5, 2)
pt4 = (6, 6)
pt5 = (8, 3)

way12 = ((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2) ** 0.5
way13 = ((pt3[0] - pt1[0]) ** 2 + (pt3[1] - pt1[1]) ** 2) ** 0.5
way14 = ((pt4[0] - pt1[0]) ** 2 + (pt4[1] - pt1[1]) ** 2) ** 0.5
way15 = ((pt5[0] - pt1[0]) ** 2 + (pt5[1] - pt1[1]) ** 2) ** 0.5

if way12 <= way13 and way12 <= way14 and way12 <= way15:
    min_way1 = way12
elif way13 <= way12 and way13 <= way14 and way13 <= way15:
    min_way1 = way13
elif way14 <= way12 and way14 <= way13 and way14 <= way15:
    min_way1 = way14
elif way15 <= way12 and way15 <= way13 and way15 <= way14:
    min_way1 = way15

way23 = ((pt3[0] - pt2[0]) ** 2 + (pt3[1] - pt2[1]) ** 2) ** 0.5
way24 = ((pt4[0] - pt2[0]) ** 2 + (pt4[1] - pt2[1]) ** 2) ** 0.5
way25 = ((pt5[0] - pt2[0]) ** 2 + (pt5[1] - pt2[1]) ** 2) ** 0.5

if way23 <= way24 and way23 <= way25:
    min_way2 = way23
elif way24 <= way23 and way24 <= way25:
    min_way2 = way24
elif way25 <= way23 and way25 <= way24:
    min_way2 = way25

way43 = ((pt3[0] - pt4[0]) ** 2 + (pt3[1] - pt4[1]) ** 2) ** 0.5
way45 = ((pt5[0] - pt4[0]) ** 2 + (pt5[1] - pt4[1]) ** 2) ** 0.5

if way43 <= way45:
    min_way3 = way43
else:
    min_way3 = way45

way53 = ((pt3[0] - pt5[0]) ** 2 + (pt3[1] - pt5[1]) ** 2) ** 0.5
min_way4 = way53

way31 = ((pt1[0] - pt3[0]) ** 2 + (pt1[1] - pt3[1]) ** 2) ** 0.5
min_way5 = way31

print(f"{pt1} -> {pt2}{[way12]} -> {pt4}{[way12 + way24]} -> {pt5}{[way12 + way24 + way45]} -> {pt3}{[way12 + way24 + way45 + way53]} -> {pt1}{[way12 + way24 + way45 + way53 + way31]} = {way12 + way24 + way45 + way53 + way31}")