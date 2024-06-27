def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Access the Dictionary to see if member one follows member two
    follow_list=social_graph[from_member]["following"] 
    to_member
    if to_member in follow_list:
        from_fol_to=1
    else:
        from_fol_to=0
    #Access the Dictionary to see if member two follows member one
    follow_list2=social_graph[to_member]["following"] 
    from_member
    if from_member in follow_list2:
        to_fol_from=1
    else:
        to_fol_from=0
    #Compare your findings to the Given Criteria (Check Returns)
    #Check if fromMember follows toMember,
    if from_fol_to==1:
        if to_fol_from==0:
            return ("follower")
    #if fromMember is followed by toMember,
    if from_fol_to==0:
        if to_fol_from==1:
            return ("followed by")
    #if fromMember and toMember follow each other,
    if from_fol_to==1:
        if to_fol_from==1:
            return ("friends")
    #if neither fromMember nor toMember follow each other.
    if from_fol_to==0:
        if to_fol_from==0:
            return ("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #Horizontal Check for X
    places=len(board)-1
    while places>=0:
        x_count=board[places].count("X")
        if x_count==len(board):
            return("X")
        else:
            places=places-1

    #Horizontal Check for O
    places=len(board)-1
    while places>=0:
        x_count=board[places].count("O")
        if x_count==len(board):
            return("X")
        else:
            places=places-1

    #Vertical Check for X
    places=len(board)-1
    column=len(board[1])-1
    columnlist=[]
    while column>=0:
        while places>=0:
            columnlist.append(board[places][column])
            places=places-1
            y_count=columnlist.count("X")
            if y_count==len(board):
                return("X")
        column=column-1
        columnlist=[]

    #Vertical Check for O
    places=len(board)-1
    column=len(board[1])-1
    columnlist=[]
    while column>=0:
        while places>=0:
            columnlist.append(board[places][column])
            places=places-1
            y_count=columnlist.count("O")
            if y_count==len(board):
                return("O")
        column=column-1
        columnlist=[]

    #Diagonal Check 
    #Top-right to bottom-left of X 
    places=len(board)-1
    column=len(board[1])-1
    diagonalist=[]
    x=0
    while column>=0:
        diagonalist.append(board[x][column])
        x=x+1
        column=column-1
        d_count=diagonalist.count("X")
        if d_count==len(board):
            return("X")

    #Top-left to bottom-right of X
    places=len(board)-1
    column=len(board[1])-1
    diagonalist=[]
    while places>=0:
        diagonalist.append(board[places][column])
        places=places-1
        column=column-1
        d_count=diagonalist.count("X")
        if d_count==len(board):
            return("X")
        
    #Top-right to bottom-left of O
    places=len(board)-1
    column=len(board[1])-1
    diagonalist=[]
    x=0
    while column>=0:
        diagonalist.append(board[x][column])
        x=x+1
        column=column-1
        d_count=diagonalist.count("O")
        if d_count==len(board):
            return("O")

    #Top-left to bottom-right of O
    places=len(board)-1
    column=len(board[1])-1
    diagonalist=[]
    while places>=0:
        diagonalist.append(board[places][column])
        places=places-1
        column=column-1
        d_count=diagonalist.count("O")
        if d_count==len(board):
            return("O")
    
    #No winner
    return("NO WINNER")


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time=0
    current_stop=first_stop
    while True:
        for (from_stop, to_stop), data in route_map.items():
                if from_stop==current_stop:
                    time += data['travel_time_mins']
                    current_stop=to_stop
                    break
        if current_stop==second_stop:
            break
    return time