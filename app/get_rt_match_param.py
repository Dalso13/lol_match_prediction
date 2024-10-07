def getMatchParam(json: dict):
    blue_gold = []
    red_gold = []
    for data in json['info']['participants']:
        if data['teamId'] == 100:
            blue_gold.append(data['goldEarned'])
        if data['teamId'] == 200:
            red_gold.append(data['goldEarned'])

    blue_dragon = json['info']['teams'][0]['objectives']['dragon']['kills']
    red_dragon = json['info']['teams'][1]['objectives']['dragon']['kills']

    blue_tower = json['info']['teams'][0]['objectives']['tower']['kills']
    red_tower = json['info']['teams'][1]['objectives']['tower']['kills']

    blue_kill = json['info']['teams'][0]['objectives']['champion']['kills']
    red_kill = json['info']['teams'][1]['objectives']['champion']['kills']

    return [[sum(blue_gold), blue_dragon, blue_tower, blue_kill],
            [sum(red_gold), red_dragon, red_tower, red_kill]]
