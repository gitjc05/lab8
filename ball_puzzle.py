import ball_puzzle_animation
import cs_stack as stack
import string


def move_ball(can1, can2, can_list):
    ball_puzzle_animation.animate_move(stack_list=can_list, from_can=can1, to_can=can2)
    ball = stack.pop(can1)
    return can1, stack.push(can2, ball)


def sort_cans(cans):
    
    while stack.size(cans[0]) > 0:
        if stack.top(cans[0]) == "G":
            cans[0], cans[1] = move_ball(cans, cans[0], cans[1])
        else:
            cans[0], cans[2] = move_ball(cans, cans[0], cans[2])
    while stack.size(cans[2]) > 0:
        if stack.top(cans[0]) == "R":
            cans[2], cans[0] = move_ball(cans, cans[2], cans[0])
        else:
            cans[2], cans[1] = move_ball(cans, cans[2], cans[1])
    while stack.top(cans[1]) != "G":
        cans[1], cans[2] = move_ball(cans, cans[1], cans[2])

    return cans
            

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
    
    n_cans = sort_cans(cans_list)
    
    ball_puzzle_animation.animate_finish()


if __name__ == "__main__":
    main()