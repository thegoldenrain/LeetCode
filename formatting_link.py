def github_link(address):
    link = address.split('. ', 1)
    filename = link[1].replace(" ", "_") + ".py"
    location = 'Algorithms/'+ filename[0:-3]+'/'+filename
    url = 'https://leetcode.com/problems/'+link[1].lower().replace(' ', '-')
    location_cpp = '), [C++](./{}.cpp'.format( location[0:-3])

    print('\n\n' + location +'\n')
    print(f'|{link[0]}|[{link[1]}]({url}/)|[Python](./{location})|Easy|') 
    print(f'\n|{link[0]}|[{link[1]}]({url}/)|[Python](./{location}{location_cpp})|Easy|')

github_link(input("Enter the description: "))

'''
Algorithms/Maximum_69_Number/Maximum_69_Number.py

|1323|[Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/)
|[Python](./Algorithms/Maximum_69_Number/Maximum_69_Number.py)|Easy|

|1323|[Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/)
|[Python](./Algorithms/Maximum_69_Number/Maximum_69_Number.py), 
[C++](./Algorithms/Maximum_69_Number/Maximum_69_Number.cpp)|Easy|
'''
