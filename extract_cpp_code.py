import re

input_file = 'sourcecode.md'
output_file = 'output.cpp'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Regex pour extraire les blocs de code C++
cpp_blocks = re.findall(r'```(?:cpp|c\+\+)\s([\s\S]*?)```', content, re.MULTILINE)

with open(output_file, 'w', encoding='utf-8') as f:
    for block in cpp_blocks:
        f.write(block.strip() + '\n\n')

print(f"{len(cpp_blocks)} bloc(s) C++ extrait(s) dans {output_file}") 