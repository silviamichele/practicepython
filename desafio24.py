#h, v = '-', '|'
#print(complete_draw)
user_option = int(input('padrão do desenho: (ex.: 4 = 4 x 4)'))
horizontal_l, vertical_l = ' ', ''
for x in range(1, user_option+1):
    horizontal_l += user_option * '-' + ' '
    vertical_l += '|' + user_option * ' '

print(horizontal_l)

for x in range(1, user_option+1):
    print(vertical_l + '|')
    print(horizontal_l)
