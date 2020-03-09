# Exception 

def div(x, y):
    try:
        result = x / y
    except Exception as e:
        print('Exception ', e)
        return None
    '''
    except ZeroDivisionError:
        print('can not divide by zero')
        return None
    except TypeError:
        print('String type can not accepted')
        return None
    '''
    return result

print(div('2', '4'))
print(div(5, 0))