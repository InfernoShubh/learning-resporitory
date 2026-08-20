try:
    num=int ( input( "value="))
    num2=int( input ( "value="))
    res=num/num2
    print ( "the result =",res)
except ValueError:
    print ("IVALID VALUE ERROR!")
except TypeError:
    print ( "INVALID TYPE OF THE VALUE ERROR!")
except Exception as e :
    print(f"an unexpected error occurred {e}")
else:
    print("devision performed successfully")
finally:
    print("the execution of try- except block complete")