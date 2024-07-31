s = 'You must\tremove\nextra\bcharacters'

remove_map = {
        ord('\n') : ' ',
        ord('\t') : ' ',
        ord('\b') : ' '
}

print(s.translate(remove_map))
