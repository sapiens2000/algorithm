def solution(players, callings):
    d = {player: i for i, player in enumerate(players)}
    for who in callings:
        idx = d[who]
        d[who] -= 1
        d[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players