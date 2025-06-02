print('''
      Welcome to Treasure Island.
Your mission is to find the treasure.
Left
Right or
anything else
left or right? Fall into a hole.
Game Over.
Wait
Swim or
anything else
swim or wait Attacked by trout.
Game Over.
Which door? Eaten by beasts.
Game Over.
Burned by fire.
Game Over.
You Win!
Blue
Yellow
Red
Game Over
      ''')
print('''
         T\ T\
                  | \| \
                  |  |  :
             _____I__I  |
           .'            '.
         .'                '
         |   ..             '
         |  /__.            |
         :.' -'             |
        /__.                |
       /__, \               |
          |__\        _|    |
          :  '\     .'|     |
          |___|_,,,/  |     |    _..--.
       ,--_-   |     /'      \../ /  /\\
      ,'|_ I---|    7    ,,,_/ / ,  / _\\
    ,-- 7 \|  / ___..,,/   /  ,  ,_/   '-----.
   /   ,   \  |/  ,____,,,__,,__/            '\
  ,   ,     \__,,/                             |
  | '.       _..---.._                         !.
  ! |      .' z_M__s. '.                        |
  .:'      | (-_ _--')  :          L            !
  .'.       '.  Y    _.'             \,         :
   .          '-----'                 !          .
   .           /  \                   .          .
ARV
      ''')

print('''Welcome to Treasure Island.\n
Your mission is to find the treasure.''')
Gate=input("You are at the cross road,which gate will you choose: Right or Left").lower()
if Gate=='left':
    print('''you have come across a lake, want to wait or swim across''')
    act=input('type "wait" to wait and "swim" to swim across').lower()
    if act=='wait':
        print("you have reached the door, which door you want to go ahead with")
        gates=input("Red, white or yellow").lower()
        if gates=='yellow':
            print("congratulations, you have passed the game")
        elif gates=='red' or gates=='white':
            print("you have failed the game")
        else:
            print("wrong door")
    else:
        print("you could not cross")
else:
    print("You have fallen into hole")