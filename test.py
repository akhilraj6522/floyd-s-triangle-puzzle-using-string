import sys

height = int(input("Enter pyramid height: "))
stringg  = str(input("Enter the string: "))

if not stringg.isupper():
   sys.exit('Error : String must be uppercase...')
   
no_of_queries = int(input("Enter no:of queries: "))

row = []
char = []

for i in range(no_of_queries):
    row_no, character =input().split()
    row.append(row_no)
	
    if not character.isupper():
        sys.exit('Error : Letter must be uppercase...')
		
    char.append(character)
	
if height >= 1 and height <= 10**18 and no_of_queries >= 1 and no_of_queries <= 5000 :
    
   
    pyramid = []
    char_count = 0
    temp_string = ''
    for i in range(1, height + 1):
	
        if i % 3 == 0 :
		
            for j in range(i):
			
                if char_count < len(stringg) :
               
                    temp_string += stringg[char_count]
                    char_count += 1

                else :
                    char_count = 0
                    temp_string += stringg[char_count]
                    char_count += 1
					
        else :
		
            for j in range(i):
			
                if char_count < len(stringg) :
				
                    temp_string += stringg[char_count]
                    char_count += 1

                else :
				
                    char_count = 0
                    temp_string += stringg[char_count]
                    char_count += 1
					
            temp_string = temp_string[::-1]
					
															
        pyramid.append(temp_string)
        
        temp_string = ''
#print(pyramid.shape)
for i in pyramid:
    print(i, "\n")
	
for q in range(no_of_queries) :
    print(pyramid[int(row[q]) - 1].count(str(char[q])))