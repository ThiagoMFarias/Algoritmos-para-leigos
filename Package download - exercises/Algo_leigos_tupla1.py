MyTuple = (1,2,3,(4,5,6,(7,8,9)))
print(MyTuple)

for Value1 in MyTuple:
    if type (Value1)==int:
        print(Value1)
    else:
        for Value2 in Value1:
            if type (Value2)==int:
                print('\t', Value2)
            else:
                for Value3 in Value2:
                    if type (Value3)==int:
                        print('\t\t', Value3)
