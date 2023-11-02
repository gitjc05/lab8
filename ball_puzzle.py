import ball_puzzle_animation
import cs_stack as stack
import string


def move_ball(cans, can1, can2):
    ball = stack.pop(cans[can1])
    stack.push(cans[can2], ball)
    ball_puzzle_animation.animate_move(stack_list=cans, from_can=can1, to_can=can2)
    return cans


def sort_cans(cans):
    moves = 0
    
    while stack.size(cans[0]) > 0:
        if stack.top(cans[0]) == "G":
            cans = move_ball(cans, 0, 1)
        else:
            cans = move_ball(cans, 0, 2)
        moves += 1
    while stack.size(cans[2]) > 0:
        if stack.top(cans[2]) == "R":
            cans = move_ball(cans, 2, 0)
        else:
            cans = move_ball(cans, 2, 1)
        moves += 1
    while stack.top(cans[1]) != "G":
        cans = move_ball(cans, 1, 2)
        moves += 1

    return cans, moves
            

def main():
    can1 = list(input("Enter left can balls: ").upper())
    s_can1 = stack.make_empty_stack()
    for x in can1:
        stack.push(s_can1, x)
        
    cans_list = []
    cans_list.append(s_can1)
    for i in range(2):
        cans_list.append(stack.make_empty_stack())
        
    ball_puzzle_animation.animate_init(can1)
    
    n_cans, moves = sort_cans(cans_list)
    print(moves)
    
    ball_puzzle_animation.animate_finish()


if __name__ == "__main__":
    main()