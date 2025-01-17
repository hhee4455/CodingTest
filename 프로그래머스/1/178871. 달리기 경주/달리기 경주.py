def solution(players, callings):
    player_indices = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        call_index = player_indices[call]
        player = call_index-1
        players[player], players[call_index] = players[call_index], players[player]
        
        player_indices[players[call_index]] = call_index
        player_indices[players[player]] = player
    
    return players