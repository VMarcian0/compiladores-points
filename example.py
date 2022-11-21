from points_compiler.first_follow_grammar import get_first_and_follow_from_grammar_file
from points_compiler.token_extractor import token_extractor


file_path = f'points_compiler\gammar.example.txt'
print('========FIRST AND FOLLOW=======')
get_first_and_follow_from_grammar_file(file_path)
print('================================')
print('=====POINTS TOKEN EXTRACTOR=====')
with open('demofile.dots','r') as file:  
    lines = file.readlines()
    tokens = token_extractor(lines)
    print(tokens)
print('=================================')