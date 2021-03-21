input_file =open("input.txt","r")
output_file = open("output.txt","w+")
goodies={}
output_list=[]
for f in input_file:
    toRead_index_price=f.index(":")
    print(f[toRead_index_price+1:].strip())
    print(f[:toRead_index_price])
    goodies[f[:toRead_index_price]]=f[toRead_index_price+1:].strip()
print(goodies) 
prices_goodie=list(goodies.values())
prices_goodie=[int(i)for i in prices_goodie]
prices_goodie.sort(reverse=True)
print(prices_goodie)
num_of_employees=int(input("Enter number of employees: "))
len_considered=(len(prices_goodie)-num_of_employees)
print(len_considered)

for i in range(len_considered):
    max_price=prices_goodie[i]
    min_price=prices_goodie[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        index_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        index_choosen=i

choosen_prices=prices_goodie[index_choosen:num_of_employees+index_choosen]
diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

cnt=0
for key,value in goodies.items():
    prices_goodie[cnt]
    print(value)
    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+" : "+value
        output_list.append(str1)
        cnt+=1
        print(str1)
output_file.write("The goodies selected for distribution are: \n")
output_file.write("\n")
for i in output_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("\n And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))
input_file.close()
output_file.close()
