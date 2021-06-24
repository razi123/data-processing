#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 22:44:52 2021

@author: khazi
"""

def Valid_Invalid_Buildings(df):
    
    foundX = [101, 103, 121, 122, 123, 124, 126, 131,141, 142, 144, 145, 151, 152, 210, 211, 213, 220, 221, 222, 223, 224, 225, 226, 227, 
              228, 230,231, 232, 234, 235, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 
              257, 258, 259, 272, 273, 274,276, 277, 300,301, 302, 303, 304, 305, 306,307, 308, 309, 310, 311, 313, 315, 316, 317, 320, 
              323, 321,322, 326, 327, 329, 330, 341,343, 345, 348, 351, 352, 348, 351, 352, 351, 349, 348, 347,343, 341, 348, 330, 329, 327, 
              326, 436, 423, 400, 402, 401,403, 404, 456, 405, 406, 407, 408, 409, 411, 449, 410, 411, 413, 414, 415, 416, 418, 419, 420, 
              421,422,423, 424, 425, 426, 427, 428, 429, 430, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 443, 444, 445, 448, 451, 452,
              453,454,449,456,460,450, 448, 446, 442, 417, 500, 510, 511, 512, 513, 516, 518, 515, 514, 519, 521, 522, 523, 526, 545, 547, 
              549, 551, 527, 532, 535, 536, 541, 544, 545, 546, 547, 548, 549, 551, 556,559, 560, 563, 570,571, 572, 573, 574, 575, 506, 601,
              602, 603, 604, 605, 606, 607, 608, 614, 615, 618, 620, 629, 630, 631, 650, 670, 630, 640, 660,686, 681, 686,688, 691,695, 696,
              689, 622, 611, 693,701, 705, 706, 707, 708, 711, 712, 713, 714, 717, 723, 725, 721, 724, 725, 727,732,733,741, 769, 768, 760,
              757, 755, 754,758, 752, 745, 744, 742, 729,727, 725, 724, 723, 721,717,716, 715, 801,901,907,910,915,905,908, 911, 912, 913, 
              914, 915, 916, 917, 918, 920, 935, 9546, 9657,9608, 9670, 9637, 9651, 9675]
    
    notFoundX = [102, 104, 127, 9602, 132, 263, 319, 229, 4691, 711, 9910, 9660, 9661, 323,342, 612, 687,668,437, 531, 
             540, 543, 557, 610, 616, 4614, 685,1500, 1507, 1600, 5131, 5253, 5311, 5523, 9100, 9546, 9605, 9639, 9900,
             5523, 1501, 1600, 5813, 9220, 9520, 229, 6907,5812, 9100, 9646, 529, 5523, 5415, 5414, 5404, 5402, 530, 
             5131, 1600, 1582, 1552, 1551,1533, 1531, 1527, 1501, 1524, 1518, 1517, 1513, 1512, 1511, 1500, 1508, 1507,
             1506, 1505, 1504, 1502, 728,684, 612,557,539, 229, 1502, 554, 342, 1531, 748, 6255, 6523, 9420, 9400, 
             6523, 6713, 6631, 6660, 9658, 9641, 5435, 738, 6611, 264, 720, 195, 5252, 9606, 9634, 9680, 4668, 673, 672,
             530, 9687, 267, 664, 6701, 675, 9410, 194,199,393, 566, 266, 214, 677,4319, 463]
    
    foundX.sort()
    notFoundX.sort()
    validBuildings = list(set(foundX))
    invalidBuildings = list(set(notFoundX))
    
    # pads zero prior to 3 digt numbers
    newinvalidBuildings = []
    for i in invalidBuildings:
        xyz = str(i).zfill(4)
        newinvalidBuildings.append(xyz)
    
    # segrigate the invalid buildings, valid and num numeric building numbers

    buildingNameWithStringIndex = []
    buildingNameWithValidIndex = []
    buildingNameWithInvalidIndex = []

    for idx, build in enumerate(df['Anlage']):
        if build.isnumeric():
            if build not in newinvalidBuildings:
                buildingNameWithValidIndex.append(idx)
            else:
                buildingNameWithInvalidIndex.append(idx)
        else:
            buildingNameWithStringIndex.append(idx)
    
    
    df_InvalidBuildings = df.iloc[buildingNameWithInvalidIndex,:]
    df_ValidBuildings = df.iloc[buildingNameWithValidIndex,:]
    df_NonNumericBuildings = df.iloc[buildingNameWithStringIndex,:]
    
    
    
    return df_ValidBuildings , df_InvalidBuildings, df_NonNumericBuildings
    

    
    

