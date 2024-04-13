
################################
# Your Name: Bhim Raj Rai
# Your Section: B.E First Electrical Engineering
# Your Student ID Number: 02230056
################################

# REFERENCES
# https://github.com/golergka/advent-of-code-2022-with-chat-gpt/blob/master/day_2/README.md
# https://discuss.python.org/t/rock-paper-scissors-game-help/8823
# https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/
# https://youtu.be/Qcefu1jVPds?si=bvLwN1CcXLgqaK52
# https://youtu.be/fn68QNcatfo?si=TKth5J2ZhWQedhzL
################################

# SOLUTION
# Your Solution Score: 50223
################################

# Reading of input file
def read_input(input_file_path):
    with open(input_file_path, 'r') as file:
        return [line.strip() for line in file]

def calculate_score(lines):
    # Mapping of opponent's choice to the corresponding shape
    opponent = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissor'}
    
    # Mapping of the Required outcome to the shape you need to play
    outcome = {'X': {'A': 'Scissor', 'B': 'Rock', 'C': 'Paper'},  # To lose
                   'Y': {'A': 'Rock', 'B': 'Paper', 'C': 'Scissor'},   # To draw
                   'Z': {'A': 'Paper', 'B': 'Scissor', 'C': 'Rock'}}   # To win
    
    # Scores for Shape and Outcome
    shape_score = {'Rock': 1, 'Paper': 2, 'Scissor': 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}

    total_score = 0
    for line in lines:
        opponent_play, desired_outcome = line.split()
        your_shape = outcome[desired_outcome][opponent_play]
        # Calculate the score for the shape and the outcome
        round_score = shape_score[your_shape] + outcome_score[desired_outcome]
        total_score += round_score

    return total_score

# Inserting the input file
input_file_path = 'input_6_cap1.txt'
lines = read_input(input_file_path)
total_score = calculate_score(lines)
print(f"the total score is: {total_score}")