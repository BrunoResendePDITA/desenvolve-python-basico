import emoji

print('Emojis disponíveis: ')
print('\U0001F600 - :grinning_face:')
print('\U0001F602 - :face_with_tears_of_joy:')
print('\U0001F914 - :thinking_face:')
print('\U0001F605 - :grinning_face_with_sweat:')
print('\U0001FAE1 - :saluting_face:')

frase = input('Digite uma frase e ela será emojizada: ')

print(emoji.emojize(frase))