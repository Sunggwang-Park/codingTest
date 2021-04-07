# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




def solution(board, moves):
    answer = 0
    stack = []  #뽑은 인형 저장
    for crane in moves:
        for depth in range(len(board)):
            if board[depth][crane-1] != 0:
                stack.append(board[depth][crane-1])
                board[depth][crane-1] = 0

                if len(stack) > 1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break





    return answer




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    # print(len(board))

    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
